#!/srv/venv/bin/python3
"""
consolez.py - draw one Web page for console management

Python conversion of consolez bash script
"""

import os
import sys
import subprocess
from pathlib import Path

# Add necessary paths
sys.path.insert(0, '/usr/local/sbin')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from consfuncs import _get_debug_info
    from consuifuncs import (startPage, startTable, startRow, drawButtons, 
                           drawSearchBar, endTable, endPage, numCols)
except ImportError as e:
    print(f"Content-type: text/html\n\nERROR: Could not import required modules: {e}")
    sys.exit(1)

# Global variables
consolezUser = "none"  # user this script is running as
curCEC = "none"  # the current CEC being processed
flags = "-s"  # default is succinct output
role = "none"
title = "zlma Console data"  # page title
color = "green"  # default link color


def drawUserIDcell(systemID, userID):
    """
    Draw a userID with hot link or an empty cell
    Args:
        systemID: system ID it runs on
        userID: user ID to draw
    """
    source_file, stack = _get_debug_info()
    
    if not userID:  # no more saved consoles
        print("<td>&nbsp;</td>")  # empty cell
    else:  # show user ID as a hot link
        print(f'<td><a style="color:{color};" href=onecons.py?{userID}&amp;{systemID}>{userID}</a></td>')


def drawOneRow(systemID, *userIDs):
    """
    Draw one table row for one z/VM LPAR - each row gets max of numCols user IDs
    Args:
        systemID: System ID (LPAR)
        userIDs: User IDs that have console data saved
    """
    source_file, stack = _get_debug_info()
    
    # Draw LPAR column and up to numCols more user IDs
    print(f'<tr><td><a style="color:{color};" href=onelpar.py?{systemID}>{systemID}</a></td>')  # column 1 - the LPAR
    
    colNum = 2  # current column
    userID_list = list(userIDs)
    
    for i, nextUserID in enumerate(userID_list):
        colNum += 1
        if colNum == numCols:  # this is the last column
            print(f'<td><a style="color:{color};" href=onelpar.py?{systemID}>More</a></td>')
            break
        print(f'<td bgcolor="black"><a style="color:#40ff00; text-decoration:none;" href=onecons.py?{nextUserID}&amp;{systemID}>{nextUserID}</a></td>')
    
    # Draw empty cells, if needed
    while colNum < numCols:
        print("<td>&nbsp;</td>")  # empty cell
        colNum += 1
    
    print("</tr>")  # end row


def drawMainTable():
    """
    Produce a table with console data
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    startPage(title)  # start the Web page
    print('<link rel="stylesheet" href="/zlma.css">')
    drawButtons("using-consoles")
    
    # Get console data
    try:
        result = subprocess.run(['/usr/local/sbin/lscons'], 
                              capture_output=True, text=True, timeout=30)
        rc = result.returncode
        console_data = result.stdout.strip()
        
        if rc != 0:  # not expected
            startTable()
            startRow("#FF6666")  # draw row in light red
            if rc == 1:
                print("<td><h3>ERROR!</h3><p>No data found by lscons</p>")
            else:
                print(f"<td><h3>Unexpected!</h3><p>/usr/local/sbin/lscons returned {rc}</p>")
            
            print(f"<p>{console_data}</p>")  # error message is the data
            print("</td></tr></table>")  # end cell, row and table
            sys.exit(3)  # internal server error
            
    except subprocess.TimeoutExpired:
        startTable()
        startRow("#FF6666")
        print("<td><h3>ERROR!</h3><p>lscons command timed out</p>")
        print("</td></tr></table>")
        sys.exit(3)
    except Exception as e:
        startTable()
        startRow("#FF6666")
        print(f"<td><h3>ERROR!</h3><p>Failed to run lscons: {e}</p>")
        print("</td></tr></table>")
        sys.exit(3)
    
    # Draw the table
    print(f"<h3 align='center'>{title}</h3>")
    drawSearchBar()  # enable searching for consoles
    print('<table class="consolezTable">')  # start a consolez table
    
    # Process each row from console data
    if console_data:
        for next_row in console_data.split('\n'):
            if next_row.strip():  # skip empty lines
                row_parts = next_row.strip().split()
                if row_parts:  # ensure we have data
                    system_id = row_parts[0]
                    user_ids = row_parts[1:] if len(row_parts) > 1 else []
                    drawOneRow(system_id, *user_ids)
    
    print("</table>")


def main():
    """Main function"""
    global consolezUser, curCEC, flags, role, title
    
    # Import common functions and variables
    try:
        # checkUser()  # Uncomment when authentication is needed
        drawMainTable()  # show table with all LPARs and tests
    except Exception as e:
        print("Content-type: text/html\n\n")
        print(f"<html><body><h1>Error</h1><p>An error occurred: {e}</p></body></html>")
        sys.exit(1)


if __name__ == "__main__":
    main()
