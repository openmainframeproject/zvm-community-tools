#!/usr/bin/env python3
"""
cpcommand.py - issue a CP command on a specified z/VM LPAR

Python conversion of cpcommand bash script
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path

# Import the converted console functions
try:
    from consfuncs import (regMsg, verboseMsg, readConfFile, getZlmaServer, 
                          CPcmd, _get_debug_info)
except ImportError:
    # Fallback if consfuncs.py is not in the same directory
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from consfuncs import (regMsg, verboseMsg, readConfFile, getZlmaServer, 
                          CPcmd, _get_debug_info)

# Global variables
cmdCalled = ""
confFile = "/etc/zlma.conf"
cpCmd = ""
flags = ""
logFile = "/var/log/zlma/consolez.log"
logLevel = "info"
sshCmd = "/usr/bin/ssh -q"
tgtSysID = ""
tgtUserID = ""
thisServer = ""
thisSysID = ""
thisUserID = ""
verbose = 1
vmcpCmd = "sudo vmcp --buffer=1M"


def usage():
    """
    Give help
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    print("")
    print("Name:   cpcommand - issue a CP command on a specified z/VM LPAR")
    print("Usage:  cpcommand [OPTIONS] CP-COMMAND")
    print("Where:  SYSTEM-ID  is the z/VM system to run the CP command on")
    print("Where:  CP-COMMAND is CP command to invoke")
    print("")
    print("OPTIONS:")
    print("  -h|--help             Give help")
    print("  -l|--lpar [LPAR]      LPAR system identifier to run command on (default: this LPAR)")
    print("  -s|--silent           Minimal output")
    print("  -v|--verbose          Include additional output")
    print("  -V|--veryverbose      Include even more output")
    print("  -x|--debug            Print commands and arguments as they are executed")
    print("")
    sys.exit(51)


def parseArgs(args):
    """
    Parse arguments
    Args: all arguments passed into script
    """
    global tgtSysID, verbose, flags, cpCmd
    
    source_file, stack = _get_debug_info()
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ['-h', '--help']:
            usage()
        elif arg in ['-l', '--lpar']:
            i += 1
            if i >= len(args):
                print("ERROR: not enough arguments")
                usage()
            tgtSysID = args[i].upper()  # fold to upper case
        elif arg in ['-s', '--silent']:
            verbose = 0
            flags += " -s"
        elif arg in ['-v', '--verbose']:
            verbose = 2
            flags += " -v"
        elif arg in ['-V', '--veryverbose']:
            verbose = 3
            flags += " -V"
        elif arg in ['-x', '--debug']:
            flags += " -x"
            # Note: Python equivalent of 'set -vx' would be logging/debugging
            # For now, we'll just note this flag was set
        else:
            # Non-flag args
            if arg.startswith('-'):
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            # All remaining args = CP command
            cpCmd = ' '.join(args[i:])
            break
        i += 1
    
    if not cpCmd:
        print("ERROR: CP-COMMAND not specified")
        usage()
    
    readConfFile()
    verboseMsg(f"cpCmd = {cpCmd} logLevel = {logLevel}")


def checkEnv():
    """
    Verify the environment
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    user = os.environ.get('USER')
    if not user:
        # Get current user if USER env var not set
        try:
            import pwd
            user = pwd.getpwuid(os.getuid()).pw_name
        except:
            user = 'unknown'
    
    if user == 'root':
        print("ERROR: Sorry, cpcommand cannot run as root")
        sys.exit(2)  # not authorized


def sendCPcommand():
    """
    Send CP command on this local LPAR or a remote one
    NOTE: if remote, this function will be called and will become local
    Args: none
    """
    global thisServer
    
    source_file, stack = _get_debug_info()
    
    thisServer = subprocess.run(['hostname', '-f'], capture_output=True, text=True).stdout.strip()
    
    verboseMsg(f"thisServer: {thisServer} tgtSysID: {tgtSysID} cpCmd: {cpCmd}")
    
    if not tgtSysID:
        # Run locally
        cmd_parts = cpCmd.split()
        try:
            result = subprocess.run(['sudo', 'vmcp'] + cmd_parts, 
                                  capture_output=True, text=True, timeout=60)
            print(result.stdout, end='')
            if result.stderr:
                print(result.stderr, end='')
            rc = result.returncode
        except subprocess.TimeoutExpired:
            print("ERROR: Command timed out")
            rc = 99
        except Exception as e:
            print(f"ERROR: Command failed: {e}")
            rc = 98
    else:
        verboseMsg(f"trying to get engineering server with: getZlmaServer {tgtSysID}")
        tgtServer = getZlmaServer(tgtSysID)
        if tgtServer is None:
            print(f"ERROR: did not find LPAR {tgtSysID} in {confFile}")
            regMsg(f"ERROR: did not find LPAR {tgtSysID} in {confFile}")
            sys.exit(1)  # object not found
        
        if tgtServer == thisServer:
            # Run locally
            cmd_parts = cpCmd.split()
            try:
                result = subprocess.run(['sudo', 'vmcp'] + cmd_parts, 
                                      capture_output=True, text=True, timeout=60)
                print(result.stdout, end='')
                if result.stderr:
                    print(result.stderr, end='')
                rc = result.returncode
            except subprocess.TimeoutExpired:
                print("ERROR: Command timed out")
                rc = 99
            except Exception as e:
                print(f"ERROR: Command failed: {e}")
                rc = 98
        else:
            # Run remotely
            ssh_cmd = f"{sshCmd} {tgtServer} sudo vmcp {cpCmd}"
            verboseMsg(f"Executing remote CP command: {ssh_cmd}")
            try:
                # Use shell=True for complex remote command
                result = subprocess.run(ssh_cmd, shell=True, 
                                      capture_output=True, text=True, timeout=60)
                print(result.stdout, end='')
                if result.stderr:
                    print(result.stderr, end='')
                rc = result.returncode
            except subprocess.TimeoutExpired:
                print("ERROR: Remote command timed out")
                rc = 99
            except Exception as e:
                print(f"ERROR: Remote command failed: {e}")
                rc = 98
    
    if rc != 0:
        verboseMsg(f"WARNING: command returned {rc}")
    
    return rc


def main():
    """Main function"""
    global cmdCalled, thisServer, logFile, verbose
    
    # Initialize global variables
    cmdCalled = Path(sys.argv[0]).name
    confFile_global = "/etc/zlma.conf"
    logFile = "/var/log/zlma/consolez.log"
    thisServer = subprocess.run(['hostname', '-f'], capture_output=True, text=True).stdout.strip()
    
    # Set global variables in consfuncs module
    import consfuncs
    consfuncs.confFile = confFile_global
    consfuncs.logFile = logFile
    consfuncs.verbose = verbose
    consfuncs.vmcpCmd = vmcpCmd
    
    # Parse arguments (skip script name)
    parseArgs(sys.argv[1:])
    
    # Verify environment
    checkEnv()
    
    # Issue requested CP command
    rc = sendCPcommand()
    
    sys.exit(rc)


if __name__ == "__main__":
    main()
