#!/srv/venv/bin/python3
"""
onelpar.py - draw a Web page showing user IDs that have saved console data and
             for admins user IDs that are logged on but don't have any saved data

Python conversion of onelpar bash script
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
    from consfuncs import _get_debug_info, readConfFile
    from consuifuncs import (startPage, startTable, startRow, drawButtons, 
                           checkUser, numCols)
except ImportError as e:
    print(f"Content-type: text/html\n\nERROR: Could not import required modules: {e}")
    sys.exit(1)

# Global variables
confFile = "/etc/consolez.conf"  # configuration file
consolezUser = "none"  # user this script is running as
flags = "-s"  # default is succinct output
systemID = ""  # arg 1
title = ""  # page title
userIDs = ""  # user IDs with saved console data
vmcpCmd = "sudo /sbin/vmcp"  # how to issue vmcp commands
role = "none"
redColor = "#FF6666"
netadminIDs = ""


def drawRows(data_type, lpar_spec, *user_ids):
    """
    Draw table row where each row gets max of numCols user IDs
    Args:
        data_type: 'consdata' or 'nodata'
        lpar_spec: LPAR specification
        user_ids: User IDs that have console data saved
    """
    source_file, stack = _get_debug_info()
    
    # Extract systemID from LPAR spec
    if ':' in lpar_spec:
        system_id = lpar_spec.split(':')[-1]
    else:
        system_id = lpar_spec
    
    # Convert user_ids to list with padding blanks
    user_id_list = [uid for uid in user_ids if uid.strip()]
    
    color = "green"
    col_num = 1
    
    for next_user_id in user_id_list:
        if role == "netadmin":  # user is a network admin
            if next_user_id not in netadminIDs:  # not a user ID network admins can see
                continue  # iterate loop
        
        if col_num == 1:  # first column
            print("<tr>")  # start row
        
        if data_type == "consdata":  # draw with black background and green text
            print('<td bgcolor="black">')
            print(f'<a style="color:#40ff00; text-decoration:none;" href=onecons.py?{next_user_id}&amp;{system_id}>{next_user_id}</a></td>')
        else:  # draw in normal text
            print("<td>")
            print(f'<a style="text-decoration:none;" href=onecons.py?{next_user_id}&amp;{system_id}&amp;spool>{next_user_id}</a></td>')
        
        if col_num == numCols:  # row is full
            print("</tr>")  # end row
            col_num = 1
        else:  # row is not full
            col_num += 1  # increment counter
    
    # Draw empty cells, if any
    if col_num <= numCols:  # there will be some empty cells
        num_empty_cells = numCols - col_num + 1  # number empty cells to draw
        for i in range(num_empty_cells):
            print("<td>&nbsp;</td>")  # empty cell


def drawMainTable():
    """
    Draw a table with all guests that have saved console data - numCols per row
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    startPage(title)  # start the Web page
    
    # Read and output CSS
    try:
        css_path = os.path.join(os.path.dirname(__file__), '..', 'zlma', 'zlma.css')
        if os.path.exists(css_path):
            with open(css_path, 'r') as f:
                print('<style>')
                print(f.read())
                print('</style>')
        else:
            print('<link rel="stylesheet" href="/zlma.css">')
    except:
        print('<link rel="stylesheet" href="/zlma.css">')
    
    # Get console data for this LPAR
    cmd = ['/usr/local/sbin/lscons', ':', systemID]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        console_data = result.stdout.strip()
        rc = result.returncode
        
        if rc != 0:  # not expected
            startTable()
            startRow(redColor)  # turn the row to red
            print(f"<td><h2>Unexpected!</h2><p>{' '.join(cmd)} returned {rc}</p>")
            print(f"<p>consoleData = {console_data}</p>")
            print("</td></tr></table>")  # end cell, row and table
            sys.exit(3)  # internal server error
            
    except subprocess.TimeoutExpired:
        startTable()
        startRow(redColor)
        print("<td><h2>Error!</h2><p>lscons command timed out</p>")
        print("</td></tr></table>")
        sys.exit(3)
    except Exception as e:
        startTable()
        startRow(redColor)
        print(f"<td><h2>Error!</h2><p>Failed to run lscons: {e}</p>")
        print("</td></tr></table>")
        sys.exit(3)
    
    # Draw the table
    print(f"<h2>{title}</h2>")
    print('<table class="consolezTable" align="center">')  # start consolez table aligned in center
    
    # Process console data and draw rows
    if console_data:
        lines = console_data.split('\n')
        for line in lines:
            if line.strip():
                parts = line.strip().split()
                if parts:
                    drawRows("consdata", parts[0], *parts[1:])
    
    print("</table>")  # end table


def getEngServer(system_id):
    """
    Get engineering server for a given system ID
    Args:
        system_id: System ID to look up
    Returns:
        0 on success, 1 on error
    Sets global variable engServer
    """
    global engServer
    
    # This would normally read from config file
    # For now, assume local server
    try:
        result = subprocess.run(['hostname', '-f'], capture_output=True, text=True)
        engServer = result.stdout.strip()
        return 0
    except:
        return 1


def drawNoDataTable():
    """
    Draw a table of users logged on for which there is no saved console data
    Args: none
    """
    global title, userIDs
    
    source_file, stack = _get_debug_info()
    
    title = "Guests without console data"  # title above table
    ssh_cmd = "/usr/bin/ssh -q -o StrictHostKeyChecking=no"  # command to SSH to other node
    
    if getEngServer(systemID) != 0:  # error
        print(f"ERROR: Unexpected - did not find LPAR {systemID} in {confFile}")
        sys.exit(1)  # object not found
    
    # Get all users logged on
    cmd = f"{ssh_cmd} {engServer} sudo vmcp QUERY NAMES"
    try:
        result = subprocess.run(cmd.split(), capture_output=True, text=True, timeout=30)
        logged_user_ids = result.stdout
        rc = result.returncode
        
        if rc != 0:  # not expected
            startTable()
            startRow(redColor)  # turn the row to red
            print(f"<td><h2>Unexpected!</h2><p>{cmd} returned {rc}</p>")
            print(f"<p>loggedUserIDs = {logged_user_ids}</p>")
            print("</td></tr></table>")  # end cell, row and table
            sys.exit(3)  # internal server error
            
    except subprocess.TimeoutExpired:
        startTable()
        startRow(redColor)
        print("<td><h2>Error!</h2><p>QUERY NAMES command timed out</p>")
        print("</td></tr></table>")
        sys.exit(3)
    except Exception as e:
        startTable()
        startRow(redColor)
        print(f"<td><h2>Error!</h2><p>Failed to run QUERY NAMES: {e}</p>")
        print("</td></tr></table>")
        sys.exit(3)
    
    # Process logged user IDs
    # Remove VSM entries, hyphens, commas, and filter out LOGN/LOGL/LOGV
    lines = logged_user_ids.split('\n')
    filtered_ids = []
    
    for line in lines:
        if 'VSM  ' not in line:
            # Remove hyphens and split by commas
            cleaned = line.replace('-', '').replace(',', ' ')
            words = cleaned.split()
            for word in words:
                if word and not word.startswith('LOG') and word not in ['LOGN', 'LOGL', 'LOGV']:
                    if word not in filtered_ids:
                        filtered_ids.append(word)
    
    filtered_ids.sort()
    
    # Draw the table
    no_data_ids = [systemID]  # user IDs that do not have saved consoles
    print(f"<h2>{title}</h2>")
    print('<table class="consolezTable">')  # start consolez table
    
    for next_user_id in filtered_ids:
        if f" {next_user_id} " not in f" {userIDs} ":  # no console data for this ID
            no_data_ids.append(next_user_id)  # add to list with no data
    
    drawRows("nodata", systemID, *no_data_ids[1:])  # skip systemID from the list
    print("</tr></table>")  # end row and table


def parseQueryString():
    """Parse query string parameters"""
    global systemID, title
    
    query_string = os.environ.get('QUERY_STRING', '')
    if query_string:
        parts = query_string.split('&')
        if len(parts) > 0:
            systemID = urllib.parse.unquote_plus(parts[0]).upper()
    
    title = f"{systemID} guests with console data"


def main():
    """Main function"""
    global userIDs, role, engServer
    
    try:
        parseQueryString()  # Parse query parameters
        
        readConfFile()  # read the /etc/consolez.conf file
        checkUser()
        
        drawMainTable()  # show table with all user IDs that have data
        
        if role == "admin":  # admins can add new spool files
            drawNoDataTable()  # show table with logged on users that don't have data
        
        drawButtons("using-consoles")  # add navigation buttons
        
    except Exception as e:
        print("Content-type: text/html\n\n")
        print(f"<html><body><h1>Error</h1><p>An error occurred: {e}</p></body></html>")
        sys.exit(1)


if __name__ == "__main__":
    main()
