#!/srv/venv/bin/python3
"""
searchcons.py - Draw a page that enables the searching of saved console data
                on the Linux side

Python conversion of searchcons bash script
"""

import os
import sys
import subprocess
import urllib.parse
from pathlib import Path

# Add necessary paths
sys.path.insert(0, '/usr/local/sbin')
sys.path.insert(0, '/home/elliot/Desktop/zlma/usr/local/sbin')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from consfuncs import _get_debug_info
    from consuifuncs import (startPage, headerRow, drawButtons, checkUser, 
                           uudecode, addScrollButton)
except ImportError as e:
    print(f"Content-type: text/html\n\nERROR: Could not import required modules: {e}")
    sys.exit(1)

# Global variables
userIDflt = ""  # user ID filter
systemIDflt = ""  # env:CEC:LPAR filter
pattern = ""  # search pattern
nocase = ""  # case insensitive flag
title = "Search z/VM console data"  # page title
verbose = ""  # verbosity flag
color1 = "#DAEAFF"  # button color
color3 = "#fff2e6"  # header color


def drawClearButton():
    """
    Draw a button to clear all search filters
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    print("<tr>")
    print('<td style="text-align:center"; colspan="3">')
    print('<form method=GET action="/zlmarw/searchcons.py" accept-charset="utf-8">')
    print(f'<input class=button type=submit style="background-color:{color1}"; value="Clear filters">&nbsp;')
    
    if userIDflt:
        print('<input type=hidden name=hostFlt value="">')
    if systemIDflt:
        print('<input type=hidden name=systemIDflt value="">')
    if pattern:
        print('<input type=hidden name=pattern value="">')
    
    print("</form></td></tr>")


def getArgs():
    """
    Get search arguments passed in on URL
    Args: none
    """
    global userIDflt, systemIDflt, pattern, nocase, verbose
    
    source_file, stack = _get_debug_info()
    
    query_string = os.environ.get('QUERY_STRING', '')
    if not query_string:
        return
    
    # Parse query string parameters
    parsed = urllib.parse.parse_qs(query_string)
    
    userIDflt = parsed.get('userIDflt', [''])[0]
    userIDflt = uudecode(userIDflt) if userIDflt else ""
    
    systemIDflt = parsed.get('systemIDflt', [''])[0]
    systemIDflt = uudecode(systemIDflt) if systemIDflt else ""
    
    pattern = parsed.get('pattern', [''])[0]
    pattern = uudecode(pattern) if pattern else ""
    
    nocase = parsed.get('nocase', [''])[0]
    verbose = parsed.get('verbose', [''])[0]


def drawMainTable():
    """
    Draw a table with search criteria for user ID, system ID/environment
    the text pattern to search form and a 'Search consoles' button
    """
    source_file, stack = _get_debug_info()
    
    startPage(title)  # start the Web page
    print('<link rel="stylesheet" href="/zlma.css">')  # CSS
    
    if pattern:
        decoded_pattern = uudecode(pattern)  # uu-decode the string
    else:
        decoded_pattern = pattern
    
    # Draw table with the search criteria
    print(f"<h2>{title}</h2>")
    print("<h3 align=center>Enter a search pattern</h3>")
    print('<table class="consolezTable" align=center>')  # start table
    
    headerRow(3, "Search filters")  # first header row
    
    # row 1 - clear button
    drawClearButton()  # draw a button to clear filters
    
    # row 2 - start the form to run searchcons again with filters
    print('<tr><form method=GET action=/zlmarw/searchcons.py accept-charset="utf-8">')
    print("<td>User ID</td>")
    print(f'<td><input type=text id=userIDflt name=userIDflt value="{userIDflt}"></td>')
    print("<td></td>")  # empty cell
    print("</tr><tr>")  # end row, start row
    
    # row 3
    print("<td>LPAR</td>")
    print(f'<td><input type=text id=systemIDflt name=systemIDflt value="{systemIDflt}"></td>')
    print("<td></td>")  # empty cell
    print("</tr><tr>")  # end row, start row
    
    # row 4
    print("<td>Search pattern</td>")
    print(f'<td><input type=text id=pattern name=pattern value="{decoded_pattern}"></td>')
    print('<td><input type="radio" name="nocase" id="nocase" value="yes">Case insensitive')
    print('<input type="radio" name="verbose" id="verbose" value="yes">Verbose</td>')
    print("</tr><tr>")  # end row, start row
    
    # row 5
    print('<td align=center colspan="3">')
    print('<input class=button type=submit style="background-color:#8CFF66; font:bold 16px" value="Search consoles">&nbsp;')
    print("</form>")  # end form
    print("</td></tr></table><br>")  # end cell, row, table, leave some room
    
    # Perform the search
    if not decoded_pattern:  # no pattern found
        print("<h4>A search pattern must be supplied</h4>")
    else:  # there is a search pattern
        user_filter = userIDflt if userIDflt else ":"  # default is all
        system_filter = systemIDflt if systemIDflt else ":"  # default is all
        
        # Build command arguments
        cmd_args = ['/usr/local/sbin/grepcons']
        
        if nocase == "yes":  # case insensitive search
            cmd_args.append('-i')
        if verbose == "yes":  # add verbosity
            cmd_args.append('-v')
        
        cmd_args.extend([user_filter, system_filter, decoded_pattern])
        
        # Run the search command
        try:
            result = subprocess.run(cmd_args, capture_output=True, text=True, timeout=60)
            cmd_out = result.stdout
            rc = result.returncode
            
            print('<pre align="center">')  # preformatted text
            
            # Show first line (grep command info)
            if cmd_out:
                lines = cmd_out.split('\n')
                if lines:
                    print(lines[0])  # first line shows grep command run
            
            if rc == 0:  # search was successful
                print("</pre>")  # end preformatted text
                num_lines = len([line for line in cmd_out.split('\n') if line.strip()]) - 1
                print(f"<h4>Pattern '{decoded_pattern}' matched {num_lines} lines</h4>")
                
                addScrollButton()  # add a 'Scroll to bottom' button
                print('<table class="greenScreenTable">')  # start a 'green screen' table
                print("<tr><td><pre>")  # start row, cell, preformatted text
                
                # HTML escape the output to prevent XSS
                escaped_output = cmd_out.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                print(escaped_output)  # display the output
                
                print("</pre>")  # end preformatted text
            else:  # no lines found
                print("</pre>")  # end preformatted text
                print(f"<h4>Pattern '{decoded_pattern}' did not match any lines</h4>")
                
        except subprocess.TimeoutExpired:
            print('<pre align="center">')
            print("Error: Search command timed out")
            print("</pre>")
        except Exception as e:
            print('<pre align="center">')
            print(f"Error: Search command failed: {e}")
            print("</pre>")
    
    print("</td></tr></table><br>")  # end cell, row, table, leave some room


def main():
    """Main function"""
    try:
        checkUser()  # Check authentication
        getArgs()  # get arguments passed in
        drawMainTable()  # show table with search interface
        drawButtons("using-consoles")  # add custom navigation buttons
        
    except Exception as e:
        print("Content-type: text/html\n\n")
        print(f"<html><body><h1>Error</h1><p>An error occurred: {e}</p></body></html>")
        sys.exit(1)


if __name__ == "__main__":
    main()
