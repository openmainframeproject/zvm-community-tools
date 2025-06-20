#!/srv/venv/bin/python3
"""
searchforcons.py - Search for consoles by user ID or host name

Python conversion of searchforcons bash script
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
    from consuifuncs import (startPage, headerRow, drawButtons, checkUser, 
                           drawSearchBar)
except ImportError as e:
    print(f"Content-type: text/html\n\nERROR: Could not import required modules: {e}")
    sys.exit(1)

# Global variables
numHits = 0  # number of servers matching pattern
searchString = ""  # search string from query
title = "Search for z/VM console"  # page title
color1 = "#DAEAFF"  # button color
color3 = "#fff2e6"  # header color
userIDflt = ""
systemIDflt = ""
pattern = ""


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


def showOneRow(header_drawn, lpar, *user_ids):
    """
    Show one row of hits
    Args:
        header_drawn: has the header been drawn?
        lpar: LPAR name
        user_ids: User IDs
    """
    global numHits
    
    source_file, stack = _get_debug_info()
    
    if header_drawn == "no":  # this is the first row
        print('<table class="consolezTable">')  # start table
        print("<tr><th>LPAR</th>")  # start header row
        print("<th>User ID 1 ... </th>")
        print("</tr>")  # end header row
    
    print(f"<tr><td>{lpar}</td>")  # start row, show LPAR column
    
    for next_user_id in user_ids:
        numHits += 1  # increment counter
        print('<td bgcolor="black">')
        print(f'<a style="color:#40ff00; text-decoration:none;" href=onecons.py?{next_user_id}&amp;{lpar}>{next_user_id}</a></td>')
    
    print("</tr>")  # end row


def showSavedConsoles():
    """
    Search and show saved consoles matching the search string
    Args: none
    """
    global numHits
    
    source_file, stack = _get_debug_info()
    
    found_one = "no"  # has there been one hit?
    hits = ""  # user IDs that match
    
    if searchString:
        # Search through console data to find matches
        try:
            # Use lscons to get all console data
            result = subprocess.run(['/usr/local/sbin/lscons'], 
                                  capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                console_data = result.stdout.strip()
                header_drawn = "no"
                
                # Process each line to find matches
                for line in console_data.split('\n'):
                    if line.strip():
                        parts = line.strip().split()
                        if parts:
                            lpar = parts[0]
                            user_ids = parts[1:] if len(parts) > 1 else []
                            
                            # Check if any user ID matches the search string
                            matching_users = []
                            for user_id in user_ids:
                                if searchString.upper() in user_id.upper():
                                    matching_users.append(user_id)
                            
                            # Also check if LPAR name matches
                            if searchString.upper() in lpar.upper():
                                matching_users.extend([uid for uid in user_ids if uid not in matching_users])
                            
                            if matching_users:
                                showOneRow(header_drawn, lpar, *matching_users)
                                header_drawn = "yes"
                                found_one = "yes"
                
                if header_drawn == "yes":
                    print("</table>")  # end table if we started one
                    
        except Exception as e:
            print(f"<p>Error searching consoles: {e}</p>")
    
    if found_one == "no":  # no hits
        print(f"<h4>No consoles found matching '{searchString}'</h4>")
    else:  # at least one hit
        print(f"<h4>Found {numHits} consoles matching '{searchString}'</h4>")


def drawMainTable():
    """
    Draw a table with search criteria for user ID, system ID/environment
    the text pattern to search form and a 'Search consoles' button
    """
    source_file, stack = _get_debug_info()
    
    page_title = title
    if searchString:  # a search string passed in
        page_title = f"{title} with pattern '{searchString}'"  # append pattern searched on
    
    startPage(page_title)  # start the Web page
    print('<link rel="stylesheet" href="/zlma.css">')  # CSS
    
    drawSearchBar()  # Draw search interface
    
    if not searchString:  # no search string passed in
        return  # all done
    
    # Perform the search
    showSavedConsoles()
    
    if numHits > 1:  # multiple servers found
        print("</table><br>")  # end table, leave some room


def parseQueryString():
    """Parse query string parameters"""
    global searchString
    
    query_string = os.environ.get('QUERY_STRING', '')
    if query_string:
        parsed = urllib.parse.parse_qs(query_string)
        searchString = parsed.get('searchString', [''])[0]
        searchString = urllib.parse.unquote_plus(searchString)


def main():
    """Main function"""
    try:
        parseQueryString()  # Parse query parameters
        checkUser()  # Check authentication
        drawMainTable()  # show table with search interface
        drawButtons("using-consoles")  # add custom navigation buttons
        
    except Exception as e:
        print("Content-type: text/html\n\n")
        print(f"<html><body><h1>Error</h1><p>An error occurred: {e}</p></body></html>")
        sys.exit(1)


if __name__ == "__main__":
    main()
