#!/srv/venv/bin/python3
"""
consuifuncs.py - functions common to consolez Web UI interface

Python conversion of consuifuncs bash script
"""

import os
import sys
import urllib.parse
from pathlib import Path

# Add the sbin directory to path to import consfuncs
sys.path.insert(0, '/usr/local/sbin')
try:
    from consfuncs import _get_debug_info
except ImportError:
    def _get_debug_info():
        import inspect
        frame = inspect.currentframe()
        try:
            caller_frame = frame.f_back
            source_file = caller_frame.f_code.co_filename
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

# Global variables
cmdCalled = Path(sys.argv[0]).name
color1 = "#DAEAFF"  # first background color
headerColor = "#fff2e6"  # color of divider rows - a muted orange
adminGID = 0  # GID of full administrators (0 = all users are admins)
numCols = 14  # number of columns in main tables
webIcon = "consolez.ico"  # browser tab icon


def startPage(*title_parts):
    """
    Common Web page header
    Args: page title parts
    """
    source_file, stack = _get_debug_info()
    
    title = " ".join(str(part) for part in title_parts)
    
    print("Content-type: text/html")
    print("")
    print('<!DOCTYPE html><meta https-equiv="Content-Type" content="text/html; charset=iso-8859-1" />')
    print("<html><head>")
    print('<link rel="icon" href="/zlma.ico" type="image/x-icon"/>')
    print(f"<title>{title}</title>")
    print("</head><body>")


def startTable(table_id="consolezTable", table_class="consolezTable"):
    """
    Start an HTML table using the consolezTable CSS
    Args: 
        table_id: id of the table (default: "consolezTable")
        table_class: table class "basic", "consolezTable", "invisible" (default: "consolezTable")
    """
    source_file, stack = _get_debug_info()
    
    if table_class == "basic":
        table_class = "basicTable"
    elif table_class == "invisible":
        table_class = "invisibleTable"
    elif table_class != "consolezTable":
        table_class = "consolezTable"
    
    print(f'<table id="{table_id}" class="{table_class}">')


def startRow(color=""):
    """
    Start a table row
    Args: color for the row (optional)
    """
    source_file, stack = _get_debug_info()
    
    if color:
        print(f'<tr style="background-color:{color};">')
    else:
        print("<tr>")


def drawButtons(anchor=""):
    """
    Draw 5 buttons common to zlma
    Args: Anchor for location on help page
    NOTE: this code has to be kept in sync with zlma_buttons.py
    """
    source_file, stack = _get_debug_info()
    
    print('<br><table align=center border="0" cellpadding="0" cellspacing="0"><tr>')
    
    print("<td><form action='/zlmarw/cpcmds.py' accept-charset='utf-8'>")
    print("<button class='button green-button'>Commands</button>&nbsp;")
    print("</form></td>")
    
    print("<td><form action='/zlmarw/consolez.py' accept-charset='utf-8'>")
    print("<button class='button green-button'>Consoles</button>&nbsp;")
    print("</form></td>")
    
    print("<td><form action='/zlma/finder.py' accept-charset='utf-8'>")
    print("<button class='button green-button'>Finder</button>&nbsp;")
    print("</form></td>")
    
    print("<td><form action='/zlmarw/vif.py' accept-charset='utf-8'>")
    print("<button class='button green-button'>Vif</button>&nbsp;")
    print("</form></td>")
    
    print(f'<td><a href="https://github.com/mike99mac/zlma#{anchor}" target="_blank">')
    print("<button class='button yellow-button'>Help</button><br>")
    print("</a></td></tr></table><br>")


def consButtons(userID, systemID, script_name):
    """
    Draw buttons to:
    (1) Spool the current user ID's console
    (2) Search consoles
    Args:
        userID: user ID for spooling
        systemID: system ID for spooling
        script_name: current script name for form action
    """
    source_file, stack = _get_debug_info()
    
    print('<br><table align=center border="0" cellpadding="0" cellspacing="0"><tr>')
    
    spool_cmd = f"{script_name}?{userID}&amp;{systemID}&amp;spool"
    print(f'<td><form method=POST action="{spool_cmd}" accept-charset="utf-8">')
    print('<input class=button style="background-color:#8CFF66" type=submit value="Spool console">&nbsp;')
    print("</form></td>")
    
    print('<td><form action="/zlmarw/searchcons.py" accept-charset="utf-8">')
    print('<button class=button style="background-color:#FFDB4D">Search</button>')
    print("</form></td>")
    print("</tr></table>")


def startCell(color=""):
    """
    Start a table cell
    Args: optional color
    """
    source_file, stack = _get_debug_info()
    
    if color:
        print(f'<td style="background-color:{color};">')
    else:
        print("<td>")


def uudecode(encoded_string):
    """
    Decode special characters - URL decode functionality
    Args: the string to decode
    Returns: decoded string
    """
    source_file, stack = _get_debug_info()
    
    try:
        # Replace + with spaces and decode percent-encoded characters
        decoded = encoded_string.replace('+', ' ')
        decoded = urllib.parse.unquote(decoded)
        return decoded
    except Exception:
        return encoded_string


def checkUser():
    """
    Check that REMOTE_USER is set
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    remote_user = os.environ.get('REMOTE_USER', '')
    if not remote_user:
        startPage("ERROR")
        startTable()
        startRow("#FF6666")  # draw row in light red
        print("<td><h2>Unexpected!</h2><p>global REMOTE_USER is not set</p>")
        print("</td></tr></table>")
        sys.exit(3)  # internal server error


def addScrollButton():
    """
    Draw a button that scrolls to bottom of page
    Args: none
    """
    source_file, stack = _get_debug_info()
    
    # JavaScript to scroll to bottom of page
    print("<script>")
    print("scrollingElement = (document.scrollingElement || document.body)")
    print("function scrollToBottom () {")
    print("   scrollingElement.scrollTop = scrollingElement.scrollHeight;")
    print("}")
    print("</script>")
    
    # add 'Scroll to bottom' button
    print("<table align=center><tr><td>")
    print('<button class=button style="background-color:#8CFF66" onClick="scrollToBottom()">Scroll to Bottom</button>')
    print("</td></tr></table>")
    print("<br>")


def drawSearchBar(search_tool="", role=""):
    """
    Draw a search bar to find consoles by host name or user ID if such a tool
    exists, specified by the parameter 'search_tool'
    Args: 
        search_tool: name of search tool (optional)
        role: user role (optional)
    """
    source_file, stack = _get_debug_info()
    
    if not search_tool or role != "admin":
        return  # all done
    
    print('<table class="consolezTable">')
    print('<tr><form method=GET action=/zlmarw/searchforcons.py accept-charset="utf-8">')
    print("<td><b>Search for z/VM consoles by host name or user ID:</b></td>")
    print("<td><input type=text id=searchString name=searchString></td>")
    print("</form>")
    print("</tr></table><br>")


# Helper functions for common HTML patterns
def endRow():
    """End a table row"""
    print("</tr>")


def endCell():
    """End a table cell"""
    print("</td>")


def endTable():
    """End a table"""
    print("</table>")


def endPage():
    """End the HTML page"""
    print("</body></html>")


def headerRow(cols, *text_parts):
    """
    Create a table header row that spans columns and writes a title in large font
    Args:
        cols: number of columns to span
        text_parts: title text parts
    """
    source_file, stack = _get_debug_info()
    
    text = " ".join(str(part) for part in text_parts)
    
    if cols == 1:
        print(f'<tr><th style="background-color:{headerColor};"><font size="+1">')
    else:
        print(f'<tr><th style="background-color:{headerColor};" colspan="{cols}"><font size="+1">')
    
    print(f"{text}</font></th></tr>")


# Constants for button styles
GREEN_STYLE = 'style="background-color:#8CFF66"'
YELLOW_STYLE = 'style="background-color:#FFDB4D"'
