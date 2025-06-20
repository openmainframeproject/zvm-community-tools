#!/usr/bin/env python3
"""
spoolcons.py - z/VM console management utilities

Python conversion of spoolcons bash script
Supports multiple command modes: spoolcons, catcons, grepcons, lscons, rmcons
"""

import os
import sys
import subprocess
import time
import re
import glob
from pathlib import Path
from datetime import datetime

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
consFile = ""
consDir = "/srv/consolez"
dashes = "-" * 80
equals = "=" * 80
flags = ""
fromServer = ""
grepFlags = ["-H", "-n"]  # always include file name and line numbers
logFile = "/var/log/zlma/consolez.log"
logLevel = "info"
lpars = []
numLPARs = 0
outputType = "short"
pattern = ""
privClass = ""
sshCmd = "/usr/bin/ssh -q"
tgtServer = ""
tgtSysID = ""
tgtUserID = ""
tmpConsFile = ""
thisServer = ""
thisUser = ""
tgtCEC = "none"
userID = ""
verb = ""
verbose = 1
vmcpCmd = "sudo vmcp --buffer=1M"
webUI = "no"
yes = 0
zlmaSrvrs = []


def usage():
    """
    Give help
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    print("")
    if cmdCalled == "grepcons":
        print("Name:    grepcons - search through saved console data")
        print("Usage:   grepcons  [OPTIONS] USERID SYSTEMID PATTERN...")
        print("Where:   USERID    is a pattern of user IDs to search or ':' for all user IDs")
        print("Where:   SYSTEMID  is a z/VM system ID ':' for all z/VM systems")
        print("Where:   PATTERN   is a pattern to search consoles for")
    elif cmdCalled == "lscons":
        print("Name:    lscons - list user IDs with saved console data")
        print("Usage:   lscons   [OPTIONS] [USERID] [SYSTEMID]")
        print("Where:   USERID   is a specific user ID or ':' to list all user IDs (default)")
        print("Where:   SYSTEMID is a specific z/VM system ID or ':' to list all (default)")
    else:
        print(f"Name:  {cmdCalled} - {verb} z/VM console data for a virtual machine")
        print(f"Usage: {cmdCalled} [OPTIONS] USERID [SYSTEMID]")
        print("Where: USERID   is the virtual machine whose console is to be spooled")
        print("       SYSTEMID is the z/VM System Identifier name (default: this LPAR)")
    
    print("")
    print("OPTIONS:")
    print("  -h|--help             Give help")
    
    if cmdCalled == "grepcons":
        print("  -i|--ignorecase       Ignore case")
    
    if cmdCalled in ["lscons", "catcons"]:
        print("  -l|--long             Long listing")
    
    if cmdCalled == "lscons":
        print("  -L|--lpars            List just LPARs with console data")
    
    print("  -s|--silent           Minimal output")
    print("  -v|--verbose          Include additional output")
    print("  -V|--veryverbose      Include even more output")
    print("  -x|--debug            Print commands and arguments as they are executed")
    
    if cmdCalled == "rmcons":
        print("  -y|--yes              Don't ask 'Are you sure?'")
    
    print("")
    sys.exit(51)


def parseArgs(args):
    """
    Parse arguments
    Args: all arguments passed into script
    """
    global tgtUserID, tgtSysID, verbose, flags, outputType, grepFlags
    global pattern, fromServer, webUI, yes, verb
    
    source_file, stack = _get_debug_info()
    
    # Set verb based on command called
    verb_map = {
        "catcons": "show",
        "grepcons": "search", 
        "lscons": "list",
        "rmcons": "remove",
        "spoolcons": "spool"
    }
    verb = verb_map.get(cmdCalled, "unknown")
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == "-F":  # "From server" - undocumented
            i += 1
            if i >= len(args):
                print("ERROR: -F requires server name")
                usage()
            fromServer = args[i]
            verboseMsg(f"on server {thisServer} fromServer = {fromServer}")
        elif arg in ["-h", "--help"]:
            usage()
        elif arg in ["-i", "--ignorecase"]:
            if cmdCalled != "grepcons":
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            grepFlags.append("-i")
        elif arg in ["-l", "--long"]:
            if cmdCalled not in ["lscons", "catcons"]:
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            outputType = "long"
        elif arg in ["-L", "--lpars"]:
            if cmdCalled != "lscons":
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            outputType = "lpars"
        elif arg in ["-s", "--silent"]:
            verbose = 0
            flags += " -s"
        elif arg in ["-v", "--verbose"]:
            verbose = 2
            flags += " -v"
        elif arg in ["-V", "--veryverbose"]:
            verbose = 3
            flags += " -V"
        elif arg == "-w":  # undocumented - called from Web UI
            webUI = "yes"
        elif arg in ["-x", "--debug"]:
            flags += " -x"
            # Note: Python equivalent of 'set -vx' would be logging/debugging
        elif arg in ["-y", "--yes"]:
            if cmdCalled != "rmcons":
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            yes = 1
        else:
            # Non-flag args
            if arg.startswith("-"):
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            
            if not tgtUserID:  # first arg
                tgtUserID = arg.upper()  # fold to upper case
            elif not tgtSysID:  # second arg
                tgtSysID = arg.upper()  # fold to upper case
            else:
                if cmdCalled != "grepcons":  # too many args
                    print("ERROR: Too many arguments")
                    usage()
                else:  # grepcons remaining args are search pattern
                    pattern = " ".join(args[i:])
                    break
        i += 1
    
    # Set defaults for spoolcons - import needed variables
    if cmdCalled == "spoolcons":
        if not tgtUserID:
            from consfuncs import thisUserID
            tgtUserID = thisUserID  # assume 'self'
        if not tgtSysID:
            from consfuncs import thisSysID
            tgtSysID = thisSysID  # assume 'self'
    
    if cmdCalled == "grepcons" and not pattern:
        print("ERROR: required argument PATTERN missing")
        regMsg("ERROR: required argument PATTERN missing")
        usage()


def checkEnv():
    """
    Verify the environment
    Args: none
    """
    global thisUser
    
    source_file, stack = _get_debug_info()
    
    try:
        import pwd
        thisUser = pwd.getpwuid(os.getuid()).pw_name
    except:
        thisUser = os.environ.get('USER', 'unknown')
    
    if not thisUser:
        print("ERROR: Unexpected: could not determine current user")
        sys.exit(3)  # internal server error
    
    if thisUser == "root" and cmdCalled == "spoolcons":
        print("ERROR: Sorry, spoolcons cannot run as root")
        sys.exit(2)  # not authorized


def makeConsoleFile():
    """
    Create the console file if it doesn't exist
    If this is the first console file for an LPAR, make a new directory
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    if not os.path.isfile(consFile):
        lpar_dir = os.path.dirname(consFile)
        if not os.path.isdir(lpar_dir):
            try:
                os.makedirs(lpar_dir)
                verboseMsg(f"created directory {lpar_dir}")
            except OSError as e:
                print(f"ERROR: failed to create directory {lpar_dir}: {e}")
                return 4
        
        # Create file with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        try:
            with open(consFile, 'w') as f:
                f.write(f"{timestamp}: Console file created\n{equals}\n")
            
            # Make file group readable/writable
            subprocess.run(["sudo", "chmod", "g+r,g+w", consFile], check=True)
            verboseMsg(f"created console file {consFile}")
            
        except (OSError, subprocess.SubprocessError) as e:
            print(f"ERROR: failed to create console file {consFile}: {e}")
            sys.exit(4)


def getRemoteConsole():
    """
    Get console data from a different z/VM LPAR by:
    1. Calling spoolcons on the remote zlma server
    2. Copying the temp spool file back
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    verboseMsg(f"remote server: {tgtServer}  local server: {thisServer}")
    
    cmd = f"{sshCmd} {tgtServer} /usr/local/sbin/spoolcons {flags} -F {thisServer} {tgtUserID}"
    verboseMsg(f"calling remote server with cmd: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, timeout=60)
        rc = result.returncode
        if rc != 0:
            regMsg(f"ERROR: {cmd} returned {rc}")
            return rc
        
        time.sleep(1)  # allow time for SPOOL
        
        # Copy temp console file back
        scp_cmd = f"/usr/bin/scp -q {tgtServer}:{tmpConsFile} {tmpConsFile}"
        verboseMsg(f"Copying temp console file back to calling server with: {scp_cmd}")
        
        # Wait for remote console file to be copied back
        for delay in [0.2, 0.3, 0.5, 1, 2, 3, 5]:
            result = subprocess.run(scp_cmd, shell=True)
            rc = result.returncode
            
            if os.path.isfile(tmpConsFile):
                # Append remote console data to local console file
                append_cmd = f"cat {tmpConsFile} >> {consDir}/{tgtSysID}/{tgtUserID}"
                verboseMsg(f"remote console {tmpConsFile} now local - appending with cmd: {append_cmd}")
                subprocess.run(append_cmd, shell=True)
                break
            
            verboseMsg(f"scp rc: {rc} - trying again in {delay} seconds")
            time.sleep(delay)
            
    except subprocess.TimeoutExpired:
        print("ERROR: Remote command timed out")
        return 99
    except Exception as e:
        print(f"ERROR: Remote command failed: {e}")
        return 98


def checkUserID():
    """
    Check the status of the user ID whose console is to be spooled
    This is only called on the local server
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    # Check if user ID exists using CPcmd function
    try:
        rc = CPcmd("QUERY", tgtUserID)  # Use CPcmd function like original bash
        
        if rc == 0:
            verboseMsg(f"user ID {tgtUserID} is logged on")
        elif rc == 3:
            print(f"ERROR: user ID {tgtUserID} does not exist on {tgtSysID}")
            sys.exit(4)
        elif rc == 45:
            print(f"ERROR: user ID {tgtUserID} at {tgtSysID} is logged off - cannot spool console")
            sys.exit(4)
        elif rc == 361:
            print(f"ERROR: user ID {tgtUserID} is pending log off - cannot spool console")
            sys.exit(4)
        else:
            print(f"ERROR: unexpected rc from QUERY USER {tgtUserID}: {rc}")
            sys.exit(4)
            
    except subprocess.TimeoutExpired:
        print(f"ERROR: QUERY USER {tgtUserID} timed out")
        sys.exit(4)
    except Exception as e:
        print(f"ERROR: failed to query user {tgtUserID}: {e}")
        sys.exit(4)


def getLocalConsole():
    """
    Get console data from this z/VM LPAR
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    # Check if reader is enabled
    if not os.path.exists("/dev/vmrdr-0.0.000c"):
        verboseMsg("enabling reader 000C")
        try:
            subprocess.run(["sudo", "/sbin/chccwdev", "-e", "000c"], check=True, timeout=30)
        except subprocess.SubprocessError as e:
            print(f"ERROR: failed to enable reader: {e}")
            print("Does this virtual machine have C privilege class?")
            sys.exit(4)
    
    # Get current reader files
    qrdr_cmd = f"{vmcpCmd} QUERY RDR"
    try:
        result = subprocess.run(qrdr_cmd.split(), capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            last_spool_id = result.stdout.strip().split('\n')[-1].split()[1]
        else:
            last_spool_id = ""
    except:
        last_spool_id = ""
    
    # Spool console to this user - use thisUserID from consfuncs
    from consfuncs import thisUserID
    spool_cmd = f"{vmcpCmd} FOR {tgtUserID} CMD SPOOL CONS TO {thisUserID} CLOSE"
    verboseMsg(f"getting console data on {tgtSysID} with: {spool_cmd}")
    
    try:
        subprocess.run(spool_cmd.split(), timeout=30)
        time.sleep(0.1)  # wait for console to arrive
        
        # Check for new reader file
        result = subprocess.run(qrdr_cmd.split(), capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            new_spool_id = result.stdout.strip().split('\n')[-1].split()[1]
        else:
            new_spool_id = ""
        
        verboseMsg(f"lastSpoolID = {last_spool_id} newSpoolID = {new_spool_id}")
        
        if last_spool_id == new_spool_id:
            verboseMsg(f"Did not find any console output from {tgtUserID}")
            time.sleep(2)  # wait a bit longer
            
            result = subprocess.run(qrdr_cmd.split(), capture_output=True, text=True, timeout=30)
            if result.returncode == 0 and result.stdout.strip():
                new_spool_id = result.stdout.strip().split('\n')[-1].split()[1]
            
            if last_spool_id == new_spool_id:
                timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
                with open(tmpConsFile, 'w') as f:
                    f.write(f"{timestamp}: No new console data found\n")
            
            # Reset console spooling
            reset_cmd = f"FOR {tgtUserID} CMD SPOOL CONS {tgtUserID} START"
            verboseMsg(f"Resetting console {reset_cmd}")
            CPcmd(*reset_cmd.split())
        else:
            # Receive reader file
            vmur_cmd = f"sudo /usr/sbin/vmur receive -f -t {new_spool_id} {tmpConsFile}"
            result = subprocess.run(vmur_cmd.split(), timeout=30)
            if result.returncode != 0:
                print(f"ERROR: {vmur_cmd} returned {result.returncode}")
                return 4
                
    except subprocess.TimeoutExpired:
        print("ERROR: Console operation timed out")
        return 4
    except Exception as e:
        print(f"ERROR: Console operation failed: {e}")
        return 4


def makeTempConsFile():
    """
    Make a temporary file in the user's home directory
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    if os.path.isfile(tmpConsFile):
        verboseMsg(f"removing old temporary console file {tmpConsFile}")
        try:
            subprocess.run(["sudo", "rm", tmpConsFile], check=True)
        except subprocess.SubprocessError as e:
            print(f"ERROR: failed to remove old temp file: {e}")
            sys.exit(4)
    
    verboseMsg(f"making temporary console file {tmpConsFile}")
    try:
        subprocess.run(["sudo", "touch", tmpConsFile], check=True)
        subprocess.run(["sudo", "chown", thisUser, tmpConsFile], check=True)
        verboseMsg(f"changed ownership of temp console file to {thisUser}")
    except subprocess.SubprocessError as e:
        print(f"ERROR: failed to create temp console file: {e}")
        sys.exit(4)


def spoolConsole():
    """
    Spool one z/VM console on this local LPAR or a remote one
    NOTE: if remote, this function will be called and will become local
    Args: none
    """
    global tgtServer, consFile
    
    source_file, stack = _get_debug_info()
    
    if fromServer:  # being called from main server
        tgtServer = thisServer  # console is local
    else:  # this is main server
        if verbose >= 1:
            verboseMsg(f"Spooling console of {tgtUserID} at {tgtSysID}")
        
        tgtServer = getZlmaServer(tgtSysID)
        if not tgtServer:
            regMsg(f"ERROR: did not find LPAR {tgtSysID} in {confFile}")
            sys.exit(1)
        
        consFile = f"{consDir}/{tgtSysID}/{tgtUserID}"
    
    verboseMsg(f"consFile = {consFile}")
    makeConsoleFile()  # make the console file if it doesn't exist
    verboseMsg(f"thisServer = {thisServer} tgtServer = {tgtServer}")
    
    if thisServer != tgtServer:  # target LPAR is remote
        if fromServer:  # not expected
            print(f"INTERNAL ERROR! thisServer = {thisServer} tgtServer = {tgtServer} but fromServer = {fromServer}")
            regMsg(f"INTERNAL ERROR! thisServer = {thisServer} tgtServer = {tgtServer} but fromServer = {fromServer}")
            sys.exit(3)
        
        verboseMsg(f"getting console on remote server {tgtServer}")
        getRemoteConsole()
    else:  # target LPAR is local
        checkUserID()
        makeTempConsFile()
        getLocalConsole()
    
    if not fromServer:  # on calling server
        if not os.path.isfile(tmpConsFile):
            print(f"ERROR: spoolConsole() Temporary console file {tmpConsFile} not found")
            regMsg(f"ERROR: spoolConsole() Temporary console file {tmpConsFile} not found")
            sys.exit(1)
        else:
            # Append console data
            timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            with open(consFile, 'a') as cf:
                cf.write(f"{timestamp}: Console data for {tgtUserID} at {tgtSysID}:\n")
                
            with open(tmpConsFile, 'r') as tf:
                with open(consFile, 'a') as cf:
                    cf.write(tf.read())
                    
            with open(consFile, 'a') as cf:
                cf.write(f"{equals}\n")
            
            # Remove temp file
            try:
                os.remove(tmpConsFile)
                verboseMsg(f"removed temp console file {tmpConsFile}")
            except OSError as e:
                verboseMsg(f"WARNING: failed to remove {tmpConsFile}: {e}")


def catConsole():
    """
    Print console file(s) for specified user ID
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    if not tgtSysID:  # no LPAR specified
        pattern = f"{consDir}/*/{tgtUserID}"
    else:  # an LPAR was specified
        pattern = f"{consDir}/{tgtSysID}/{tgtUserID}"
    
    verboseMsg(f"checking for consoles with pattern: {pattern}")
    files = glob.glob(pattern)
    
    if not files:
        if not tgtSysID:
            print(f"No consoles found for user ID {tgtUserID}")
        else:
            print(f"No consoles found for LPAR: {tgtSysID} user ID: {tgtUserID}")
        return 1
    
    for file_path in files:
        print(dashes)
        print(f"Console file: {file_path}:")
        print(dashes)
        try:
            with open(file_path, 'r') as f:
                print(f.read(), end='')
        except IOError as e:
            print(f"ERROR: Could not read {file_path}: {e}")
        print()


def searchConsoles():
    """
    Search through console data
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    system_search = "*" if tgtSysID == ':' else f"*{tgtSysID}*"
    user_search = "*" if tgtUserID == ':' else f"*{tgtUserID}*"
    
    search_pattern = f"{consDir}/{system_search}/{user_search}"
    verboseMsg(f"Searching with pattern: {search_pattern}")
    
    files = glob.glob(search_pattern)
    found = False
    
    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if re.search(pattern, line, re.IGNORECASE if '-i' in grepFlags else 0):
                        print(f"{file_path}:{line_num}:{line.rstrip()}")
                        found = True
        except IOError:
            continue
    
    if not found:
        print(f"Pattern '{pattern}' not found")
        regMsg(f"Pattern '{pattern}' not found")
        sys.exit(1)


def listConsoles():
    """
    List saved console files
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    if not os.path.isdir(consDir):
        verboseMsg(f"Base directory {consDir} not found")
        sys.exit(1)
    
    if not tgtSysID:  # not specified
        system_ids = [d for d in os.listdir(consDir) 
                     if os.path.isdir(os.path.join(consDir, d))]
    else:  # a system ID was passed in
        potential_dirs = glob.glob(f"{consDir}/*{tgtSysID}*")
        system_ids = [os.path.basename(d) for d in potential_dirs 
                     if os.path.isdir(d)]
        
        if not system_ids:
            print(f"No console data for LPAR {tgtSysID}")
            regMsg(f"No console data for LPAR {tgtSysID}")
            sys.exit(1)
    
    if outputType == "lpars":
        print(" ".join(system_ids))
        return
    
    found_one = False
    for system_id in system_ids:
        sys_dir = os.path.join(consDir, system_id)
        if not os.path.isdir(sys_dir):
            continue
            
        print(f"{system_id} ", end='')
        
        if outputType == "short":
            try:
                user_ids = os.listdir(sys_dir)
                print(" ".join(user_ids))
            except OSError:
                print("(error reading directory)")
        else:  # assume long
            try:
                result = subprocess.run(["ls", "-lth"], cwd=sys_dir, 
                                      capture_output=True, text=True)
                print(result.stdout, end='')
            except:
                print("(error listing files)")
        
        found_one = True
    
    if not found_one:
        verboseMsg(f"Did not find any consoles in {consDir}")
        sys.exit(1)


def removeConsole():
    """
    Remove a console file for specified userID/systemID
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    tgtServer = getZlmaServer(tgtSysID)
    if not tgtServer:
        print(f"ERROR: did not find LPAR {tgtSysID} in {confFile}")
        sys.exit(1)
    
    verboseMsg(f"Checking if {consFile} exists")
    if not os.path.isfile(consFile):
        print(f"WARNING: No console data found for user ID {tgtUserID} on LPAR {tgtSysID}")
        sys.exit(1)
    
    if yes != 1:  # if --yes is not set, ask "Are you sure?"
        answer = input(f"Are you sure you want to remove console data for {tgtUserID} at {tgtSysID} (y/n) ")
        if answer != "y":
            sys.exit(4)
    
    verboseMsg(f"Removing console file: {consFile}")
    try:
        os.remove(consFile)
    except OSError as e:
        print(f"WARNING: failed to remove {consFile}: {e}")


def doTheWork():
    """
    Perform the operation based on which script was called
    Args: None
    """
    source_file, stack = _get_debug_info()
    
    operation_map = {
        "catcons": catConsole,
        "grepcons": searchConsoles,
        "lscons": listConsoles,
        "rmcons": removeConsole,
        "spoolcons": spoolConsole
    }
    
    operation = operation_map.get(cmdCalled)
    if not operation:
        print(f"INTERNAL ERROR: cmdCalled = {cmdCalled}")
        sys.exit(3)
    
    return operation()


def main():
    """Main function"""
    global cmdCalled, thisServer, consFile, tmpConsFile, thisUser
    
    # Initialize global variables
    cmdCalled = Path(sys.argv[0]).name
    thisServer = subprocess.run(['hostname', '-f'], capture_output=True, text=True).stdout.strip()
    tmpConsFile = f"{consDir}/tmp-cons-file"
    
    # Set global variables in consfuncs module
    import consfuncs
    consfuncs.confFile = confFile
    consfuncs.logFile = logFile
    consfuncs.verbose = verbose
    consfuncs.vmcpCmd = vmcpCmd
    
    # Import common functions
    readConfFile()  # read /etc/zlma.conf
    
    # Parse arguments (skip script name)
    parseArgs(sys.argv[1:])
    
    # Set console file path after parsing args
    if tgtSysID and tgtUserID:
        consFile = f"{consDir}/{tgtSysID}/{tgtUserID}"
    
    # Verify environment
    checkEnv()
    
    # Perform requested function
    try:
        result = doTheWork()
        sys.exit(result if result is not None else 0)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(130)
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()
