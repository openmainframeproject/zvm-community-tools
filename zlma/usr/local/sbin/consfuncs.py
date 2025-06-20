#!/usr/bin/env python3
"""
consfuncs.py - consolez functions 

Python conversion of consfuncs bash script
"""

import inspect
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Global variables that will be set by readConfFile()
lpars = []
zlmaSrvrs = []
numLPARs = 0
logLevel = "info"
thisUserID = ""
thisSysID = ""
verbose = 1
logFile = ""
confFile = ""
vmcpCmd = ""
CPverbose = "yes"


def _get_debug_info():
    """Get source file and function stack info similar to bash ${BASH_SOURCE} and ${FUNCNAME[@]}"""
    frame = inspect.currentframe()
    try:
        # Get calling function info
        caller_frame = frame.f_back
        source_file = caller_frame.f_code.co_filename
        
        # Build function stack
        stack = []
        current_frame = caller_frame
        while current_frame:
            func_name = current_frame.f_code.co_name
            if func_name != '<module>':
                stack.append(func_name)
            current_frame = current_frame.f_back
            
        return source_file, stack
    finally:
        del frame


def regMsg(*args):
    """
    Write a regular message to stdout and log file unless in silent mode
    Args: the message
    """
    source_file, stack = _get_debug_info()
    
    if verbose > 0:  # not in silent mode
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]  # milliseconds
        script_name = Path(sys.argv[0]).name if sys.argv else Path(source_file).name
        caller_func = stack[0] if stack else "main"
        user = os.environ.get('USER', 'unknown')
        
        message = f"{timestamp} {script_name}/{caller_func}()/{user}: {' '.join(map(str, args))}"
        print(message)
        
        if logFile:
            try:
                with open(logFile, 'a') as f:
                    f.write(message + '\n')
            except (IOError, OSError) as e:
                print(f"Warning: Could not write to log file {logFile}: {e}")


def verboseMsg(*args):
    """
    Write a message to stdout and log file when verbose is 2 or 3
    Args: the message
    """
    source_file, stack = _get_debug_info()
    
    if verbose > 1:  # verbose or very verbose
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]  # milliseconds
        script_name = Path(sys.argv[0]).name if sys.argv else Path(source_file).name
        caller_func = stack[0] if stack else "main"
        user = os.environ.get('USER', 'unknown')
        
        message = f"{timestamp} {script_name}/{caller_func}()/{user}: {' '.join(map(str, args))}"
        print(message)
        
        if logFile:
            try:
                with open(logFile, 'a') as f:
                    f.write(message + '\n')
            except (IOError, OSError) as e:
                print(f"Warning: Could not write to log file {logFile}: {e}")


def readConfFile():
    """
    Read configuration file /etc/zlma.conf
    Also set thisUserID and thisSysID - user ID and system ID we are on
    """
    global lpars, zlmaSrvrs, numLPARs, logLevel, thisUserID, thisSysID, verbose
    
    source_file, stack = _get_debug_info()
    
    if not os.path.isfile(confFile):
        print(f"ERROR: configuration file {confFile} not found")
        sys.exit(1)
    
    try:
        with open(confFile, 'r') as f:
            confFileData = f.read()
        
        # Parse JSON configuration
        config = json.loads(confFileData)
        
        # Extract LPARs and zlma servers
        lpars = [server.get('lpar', '') for server in config.get('zlma_srvrs', [])]
        lpars = [lpar for lpar in lpars if lpar]  # filter empty values
        
        if not lpars:
            regMsg(f"ERROR: did not find .lpar values in {confFile}")
            sys.exit(1)
        
        zlmaSrvrs = [server.get('zlma_srvr', '') for server in config.get('zlma_srvrs', [])]
        zlmaSrvrs = [server for server in zlmaSrvrs if server]  # filter empty values
        
        if not zlmaSrvrs:
            regMsg(f"ERROR: did not find .zlma_srvrs values in {confFile}")
            sys.exit(1)
        
        numLPARs = len(lpars)
        
        # Get log level
        logLevel = config.get('log_level', 'info')
        if logLevel == 'debug':
            verbose = 2  # increase verbosity
        
        # Get system information
        try:
            with open('/proc/sysinfo', 'r') as f:
                sysinfo = f.read()
            
            # Extract user ID and system ID
            vm_name_match = re.search(r'VM00 Name:\s+(\S+)', sysinfo)
            lpar_name_match = re.search(r'LPAR Name:\s+(\S+)', sysinfo)
            
            thisUserID = vm_name_match.group(1) if vm_name_match else ""
            thisSysID = lpar_name_match.group(1) if lpar_name_match else ""
            
        except (IOError, OSError) as e:
            print(f"Warning: Could not read /proc/sysinfo: {e}")
            thisUserID = ""
            thisSysID = ""
            
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse JSON in {confFile}: {e}")
        sys.exit(1)
    except (IOError, OSError) as e:
        print(f"ERROR: Failed to read {confFile}: {e}")
        sys.exit(1)


def CPcmd(*args):
    """
    Invoke a CP command with the vmcp module/command
    Args: the command to issue
    Return: the CP return code (not the vmcp rc)
    
    Sets global variable CPout with the command output
    """
    global CPout
    
    source_file, stack = _get_debug_info()
    
    CPrc = 0  # assume CP command succeeds
    thisServer = os.environ.get('HOSTNAME', 'localhost')
    
    cmd_args = list(args)
    verboseMsg(f"on {thisServer} invoking CP command: {vmcpCmd} {' '.join(cmd_args)}")
    
    try:
        # Run the CP command
        result = subprocess.run([vmcpCmd] + cmd_args, 
                              capture_output=True, text=True, timeout=60)
        CPout = result.stdout + result.stderr
        rc = result.returncode
        
        if rc == 2:  # output buffer overflow
            # Try to extract buffer size from error message
            bytes_match = re.search(r'\((\d+)\s+bytes', CPout)
            if bytes_match:
                bytes_needed = int(bytes_match.group(1))
                if bytes_needed > 1048576:  # larger than 1 MB
                    print(f"WARNING: Unable to get CP output of {bytes_needed} bytes - larger than 1 MB")
                    return 11
                
                verboseMsg(f"increasing vmcp buffer size to {bytes_needed} bytes and trying again")
                
                # Retry with larger buffer
                vmcp_with_buffer = vmcpCmd.replace('--buffer=1M', f'--buffer={bytes_needed}')
                result2 = subprocess.run([vmcp_with_buffer] + cmd_args,
                                       capture_output=True, text=True, timeout=60)
                CPout = result2.stdout + result2.stderr
                rc2 = result2.returncode
                
                if rc2 != 0:
                    # Extract CP return code from error message
                    cp_rc_match = re.search(r'Error: non-zero CP.*#(\d+)', CPout)
                    if cp_rc_match:
                        CPrc = int(cp_rc_match.group(1))
        
        elif rc != 0:
            # Extract CP return code from error message
            cp_rc_match = re.search(r'Error: non-zero CP.*#(\d+)', CPout)
            if cp_rc_match:
                CPrc = int(cp_rc_match.group(1))
        
        # Show CP output in verbose mode
        if CPout and CPverbose != "no":
            print(CPout)
            
    except subprocess.TimeoutExpired:
        print("ERROR: CP command timed out")
        CPout = ""
        CPrc = 99
    except (subprocess.SubprocessError, OSError) as e:
        print(f"ERROR: Failed to execute CP command: {e}")
        CPout = ""
        CPrc = 98
    
    return CPrc


def getZlmaServer(theLPAR):
    """
    Given a z/VM system ID, return the engineering server
    Arg: LPAR being queried
    Return: engineering server host name, or None if not found
    """
    source_file, stack = _get_debug_info()
    
    if not theLPAR:
        print("INTERNAL ERROR: no args passed to getZlmaServer")
        if logFile:
            try:
                with open(logFile, 'a') as f:
                    f.write("INTERNAL ERROR: no args passed to getZlmaServer\n")
            except:
                pass
        sys.exit(3)  # internal server error
    
    for i in range(numLPARs):
        if lpars[i] == theLPAR:
            return zlmaSrvrs[i]
    
    return None  # object not found


def getPrivClass():
    """
    Get the current user's z/VM privilege class
    Sets global variable privClass
    """
    global privClass
    
    source_file, stack = _get_debug_info()
    
    try:
        result = subprocess.run(['sudo', 'vmcp', 'q', 'privclas'], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            # Extract privilege class from output
            match = re.search(r'Currently\s+(\S+)', result.stdout)
            privClass = match.group(1) if match else ""
        else:
            privClass = ""
            
    except (subprocess.SubprocessError, OSError, subprocess.TimeoutExpired):
        privClass = ""


# Initialize CPout as global variable
CPout = ""
privClass = ""
