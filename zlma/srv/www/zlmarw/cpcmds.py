#!/srv/venv/bin/python3
"""
cpcmds.py - For admins run any CP command specified

Python conversion of cpcmds bash script
"""

import os
import sys
import subprocess
import urllib.parse
from pathlib import Path

# Add necessary paths
sys.path.insert(0, '/usr/local/sbin')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from consfuncs import _get_debug_info
    from consuifuncs import (startPage, startTable, startRow, drawButtons, 
                           checkUser, uudecode, GREEN_STYLE, YELLOW_STYLE)
except ImportError as e:
    print(f"Content-type: text/html\n\nERROR: Could not import required modules: {e}")
    sys.exit(1)

# Global variables
adminCmd = ""
systemID = ""
verbose = ""
allLPARs = []  # all z/VM LPARs in org
colors = ["#F6D9ED", "#FBF5E6", "#FEF0C9", "#F1EDC2", "#FEE0C9", "#DED0C6", "#FFEECA", "#EEF3E2"]  # to color-code CECs
LPARlist = []  # all z/VM LPARs chosen
title = "zlma z/VM commands"


def drawLPARchooser():
    """
    Draw a table that enables the user to choose which LPARs to run the CP commands on
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    startTable()
    
    # Get list of LPARs
    try:
        result = subprocess.run(['/usr/local/sbin/lscons', '-L'], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            all_lpars = result.stdout.strip().split()
        else:
            all_lpars = []
    except Exception:
        all_lpars = []
    
    for next_lpar in all_lpars:
        print("<tr>")  # start new row
        print(f"<td>&nbsp;&nbsp;<input type='checkbox' name='l' value='{next_lpar}'>{next_lpar}")
        print("</td>")  # end cell
        print("</tr>")
    
    print("</table><br>")  # end table, leave room


def addOneLPAR(lpar_to_add):
    """
    Add an LPAR to LPARlist if not already there
    Args:
        lpar_to_add: LPAR to add
    """
    global LPARlist
    
    source_file, stack = _get_debug_info()
    
    if not lpar_to_add:  # arg not passed
        print("INTERNAL ERROR - no LPAR passed to addOneLPAR<br>")
        sys.exit(3)
    
    if lpar_to_add not in LPARlist:  # not already in list
        LPARlist.append(lpar_to_add)  # add to list


def addToLPARlist(lpar_to_add):
    """
    Add an LPARs to LPARlist
    Args:
        lpar_to_add: LPAR to add
    """
    source_file, stack = _get_debug_info()
    
    if not lpar_to_add:
        print("INTERNAL ERROR - nothing passed to addToLPARlist<br>")
        sys.exit(3)
    
    # This function would need more context from the original system
    # For now, just add the LPAR directly
    addOneLPAR(lpar_to_add)


def setLPARlist():
    """
    Set the global variable LPARlist based on the query parameters
    Args: none
    """
    global LPARlist, adminCmd
    
    source_file, stack = _get_debug_info()
    
    query_string = os.environ.get('QUERY_STRING', '')
    
    # Parse LPAR selections from query string
    LPARlist = []
    if query_string:
        pairs = query_string.split('&')
        for pair in pairs:
            if pair.startswith('l='):
                lpar = pair[2:]  # remove 'l='
                lpar = urllib.parse.unquote_plus(lpar)
                if lpar and lpar not in LPARlist:
                    LPARlist.append(lpar)
    
    # Check if command exists but no LPARs selected
    if adminCmd and not LPARlist:
        print("<h2>Whoops! Select at least one LPAR</h2>")
        return


def drawCPcmdButtons():
    """
    Draw navigation buttons specifically for this page
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    print("<table align=center><tr><td>")  # leave room, start table, row and cell
    print("<p><b>z/VM command:</b></p>")
    print("</td></tr>")
    print("<tr><td>")
    print('<input type=text style="width: 300px;" id=adminCmd name=adminCmd>')
    print('&nbsp;&nbsp;<input type="checkbox" name="verbose" value="-v">verbose')
    print("</td></tr>")
    
    print("<tr><td><br>")
    print(f'<input class=button {GREEN_STYLE} type=submit value="Run Command">&nbsp;')
    print("</td></tr></table>")  # end cell, row, table
    print("<br><br>")  # leave some room


def runCommand():
    """
    Run CP command on selected LPARs and show output
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    if not adminCmd:  # no command yet
        return  # wait for a command
    
    cp_cmd = uudecode(adminCmd)  # UU-decode the command
    
    print('<table class="greenScreenTable">')  # start a 'green screen' table
    print("<tr><td><pre>")  # start row, cell, preformatted text
    
    # Run CP commands on each LPAR selected
    for next_lpar in LPARlist:
        cmd = ['/usr/local/sbin/cpcommand']
        if verbose:
            cmd.append(verbose)
        cmd.extend(['-l', next_lpar])
        cmd.extend(cp_cmd.split())  # Add command parts
        
        cmd_str = ' '.join(cmd)
        print(f"calling: {cmd_str}<br>")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            output = result.stdout + result.stderr
            
            # Prefix each line with LPAR name
            for line in output.split('\n'):
                if line.strip():  # skip empty lines
                    print(f"{next_lpar}: {line}<br>")
                    
        except subprocess.TimeoutExpired:
            print(f"{next_lpar}: Command timed out<br>")
        except Exception as e:
            print(f"{next_lpar}: Error running command: {e}<br>")
    
    print("</pre></td></tr></table>")  # end preformatted, cell, row, table


def doTheWork():
    """
    Draw the entire page
    """
    source_file, stack = _get_debug_info()
    
    print('Content-Type: text/html')  # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f"<html><head><title>{title}</title>")
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')
    
    drawButtons("using-consoles")  # add navigation buttons
    print(f"<h2>{title}</h2>")
    print("<h3>Choose LPARs</h3>")
    print('<form action="/zlmarw/cpcmds.py" method="GET">')  # rerun this script
    
    drawLPARchooser()  # allow choosing of LPARs
    setLPARlist()  # set which LPARs have been set
    drawCPcmdButtons()  # add custom navigation buttons
    runCommand()  # run CP command and show output
    
    print("</body></html>")  # end the page


def parseQueryString():
    """Parse query string parameters"""
    global adminCmd, systemID, verbose
    
    query_string = os.environ.get('QUERY_STRING', '')
    if not query_string:
        return
    
    # Parse parameters
    pairs = query_string.split('&')
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            value = urllib.parse.unquote_plus(value)
            
            if key == 'adminCmd':
                adminCmd = value
            elif key == 'systemID':
                systemID = value
            elif key == 'verbose':
                verbose = value


def main():
    """Main function"""
    try:
        parseQueryString()  # Parse query parameters
        checkUser()  # Check authentication
        doTheWork()  # draw the page
    except Exception as e:
        print("Content-type: text/html\n\n")
        print(f"<html><body><h1>Error</h1><p>An error occurred: {e}</p></body></html>")
        sys.exit(1)


if __name__ == "__main__":
    main()
