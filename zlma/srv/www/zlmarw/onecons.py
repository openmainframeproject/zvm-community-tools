#!/srv/venv/bin/python3
"""
onecons.py - show console data for one user ID

Python conversion of onecons bash script
Sample URL: zlnx1.example.com/zlmarw/onecons?TCPIP&LPAR1
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
    from consuifuncs import (startPage, startCell, drawButtons, GREEN_STYLE, YELLOW_STYLE)
except ImportError as e:
    print(f"Content-type: text/html\n\nERROR: Could not import required modules: {e}")
    sys.exit(1)

# Global variables
userID = ""
systemID = ""
option = ""
title = ""


def showOneConsole(user_id, system_id, option_param):
    """
    Draw a page showing one saved console file
    Args:
        user_id: user ID
        system_id: system ID 
        option_param: option - 'spool' means spool new console
    """
    source_file, stack = _get_debug_info()
    
    # Add page title
    print(f"<h3>{title}</h3>")  # add a heading
    
    if option_param == "spool":  # user asked to have console spooled
        cmd = ['/usr/local/sbin/spoolcons', '-s', user_id, system_id]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            # Output is handled by the spoolcons command itself
        except subprocess.TimeoutExpired:
            print("<p>Warning: Spool command timed out</p>")
        except Exception as e:
            print(f"<p>Warning: Spool command failed: {e}</p>")
    
    # Draw the main table
    print('<table class="greenScreenTable" align="center">')
    print("<tr>")
    startCell()
    print("<pre>")  # preformatted text
    
    # Run catcons to show console data
    cmd = ['/usr/local/sbin/catcons', user_id, system_id]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        output = result.stdout
        if result.stderr:
            output += result.stderr
        
        # HTML escape the output to prevent XSS
        output = output.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        print(output, end='')
        
    except subprocess.TimeoutExpired:
        print("Error: catcons command timed out")
    except Exception as e:
        print(f"Error: catcons command failed: {e}")
    
    print("</pre></td></tr></table>")  # end preformatted, cell
    print("</body></html>")  # end the page


def selfButtons():
    """
    Draw buttons to:
    (1) Spool the current user ID's console
    (2) Search consoles
    """
    source_file, stack = _get_debug_info()
    
    # JavaScript to scroll to bottom of page
    print("<script>")
    print("scrollingElement = (document.scrollingElement || document.body)")
    print("function scrollToBottom () {")
    print("   scrollingElement.scrollTop = scrollingElement.scrollHeight;")
    print("}")
    print("</script>")
    
    print('<br><table align=center border="0" cellpadding="0" cellspacing="0"><tr>')  # start table and row
    
    script_name = os.environ.get('SCRIPT_NAME', '/zlmarw/onecons')
    spool_cmd = f"{script_name}?{userID}&amp;{systemID}&amp;spool"
    
    print(f'<td><form method=POST action="{spool_cmd}" accept-charset="utf-8">')
    print(f'<input class=button {GREEN_STYLE} type=submit value="Spool console">&nbsp;')
    print("</form></td>")  # end form and cell
    
    print('<td><form action="/zlmarw/searchcons.py" accept-charset="utf-8">')
    print(f'<button class=button {GREEN_STYLE}>Search consoles</button>&nbsp;')
    print("</form></td>")  # end form and cell
    
    print('<td><button class=button style="background-color:#8CFF66" onClick="scrollToBottom()">Scroll to Bottom</button>')
    print("</td></tr></table>")  # end row and table


def parseQueryString():
    """Parse query string parameters"""
    global userID, systemID, option, title
    
    query_string = os.environ.get('QUERY_STRING', '')
    if query_string:
        parts = query_string.split('&')
        
        if len(parts) > 0:
            userID = urllib.parse.unquote_plus(parts[0])
        if len(parts) > 1:
            systemID = urllib.parse.unquote_plus(parts[1])
        if len(parts) > 2:
            option = urllib.parse.unquote_plus(parts[2])
    
    title = f"Console of {userID} at {systemID}"


def main():
    """Main function"""
    try:
        parseQueryString()  # Parse query parameters
        
        startPage()  # start the Web page
        print('<link rel="stylesheet" href="/zlma.css">')  # CSS
        drawButtons("using-consoles")  # common menu buttons
        selfButtons()  # menu buttons for this page
        # checkUser()  # Uncomment when authentication is needed
        showOneConsole(userID, systemID, option)  # do the work
        
    except Exception as e:
        print("Content-type: text/html\n\n")
        print(f"<html><body><h1>Error</h1><p>An error occurred: {e}</p></body></html>")
        sys.exit(1)


if __name__ == "__main__":
    main()
