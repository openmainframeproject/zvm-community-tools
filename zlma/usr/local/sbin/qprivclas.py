#!/usr/bin/env python3
"""
qprivclas.py - query the user's privilege class

Python conversion of qprivclas bash script
"""

import os
import sys
import subprocess
import re
from pathlib import Path

# Import debug function
try:
    from consfuncs import _get_debug_info
except ImportError:
    # Fallback if consfuncs.py is not in the same directory
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from consfuncs import _get_debug_info

# Global variables
classToCheck = ""
verbose = 1


def usage():
    """
    Give help
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    print("")
    print("Name:   qprivclass - query the user's privilege class")
    print("Usage:  qprivclass [OPTIONS] [CLASS]")
    print("Where:  CLASS is an optional privilege class A-G to check for")
    print("Return: 0: User does not have privilege class")
    print("        1: User has privilege class")
    print("        2: Could not obtain privilege classes")
    print("")
    print("OPTIONS:")
    print("  -h|--help             Give help")
    print("  -v|--verbose          Include additional output")
    print("  -x|--debug            Print commands and arguments as they are executed")
    print("")
    sys.exit(51)


def parseArgs(args):
    """
    Parse arguments passed into script
    """
    global classToCheck, verbose
    
    source_file, stack = _get_debug_info()
    
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg in ['-h', '--help']:
            usage()
        elif arg in ['-v', '--verbose']:
            verbose = 2
        elif arg in ['-x', '--debug']:
            # Note: Python equivalent of 'set -vx' would be logging/debugging
            # For now, we'll just note this flag was set
            pass
        else:
            # Non-flag args
            if arg.startswith('-'):
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            
            if classToCheck:  # too many args
                print(f"ERROR: unrecognized flag {arg}")
                usage()
            
            classToCheck = arg.upper()
            
            if len(classToCheck) != 1:  # too long
                print(f"ERROR: CLASS must be one character {arg}")
                usage()
            
            if not re.match(r'^[A-G]$', classToCheck):  # wrong letters
                print("ERROR: can only check privilege classes A-G")
                usage()
        
        i += 1


def checkPrivClass():
    """
    If a privilege class was passed in, check it, or show the user's current class(es)
    """
    source_file, stack = _get_debug_info()
    
    try:
        # Get user ID
        result_userid = subprocess.run(['sudo', 'vmcp', 'q', 'userid'], 
                                     capture_output=True, text=True, timeout=30)
        if result_userid.returncode != 0:
            print("ERROR: could not obtain user ID")
            sys.exit(2)
        
        userID = result_userid.stdout.strip()
        
        # Get privilege classes
        result_privclas = subprocess.run(['sudo', 'vmcp', 'Q', 'PRIVCLAS'], 
                                       capture_output=True, text=True, timeout=30)
        if result_privclas.returncode != 0:
            print("ERROR: could not obtain privilege classes")
            sys.exit(2)
        
        # Extract privilege classes from output
        match = re.search(r'Currently:\s+(\S+)', result_privclas.stdout)
        if not match:
            print("ERROR: could not obtain privilege classes")
            sys.exit(2)
        
        privClasses = match.group(1)
        
        if not classToCheck:  # no class passed in
            print(f"User {userID} current privilege classes: {privClasses}")
            sys.exit(0)
        else:
            # Check if user has the specified privilege class
            if classToCheck in privClasses:
                print(f"user {userID} has {classToCheck} privilege class")
                sys.exit(1)  # success - user has privilege class
            else:
                print(f"user {userID} does not have {classToCheck} privilege class")
                sys.exit(0)  # user does not have privilege class
                
    except subprocess.TimeoutExpired:
        print("ERROR: command timed out")
        sys.exit(2)
    except Exception as e:
        print(f"ERROR: could not obtain privilege classes: {e}")
        sys.exit(2)


def main():
    """Main function"""
    global classToCheck, verbose
    
    # Initialize variables
    classToCheck = ""
    verbose = 1
    
    # Parse arguments (skip script name)
    parseArgs(sys.argv[1:])
    
    # Do the work
    checkPrivClass()


if __name__ == "__main__":
    main()
