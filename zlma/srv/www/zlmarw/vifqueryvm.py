#!/srv/venv/bin/python3
"""
vifqueryvm.py - Simple form to get VM name for query vm command
"""
import cgi
import sys
import html
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

form = cgi.FieldStorage()
vm_name = form.getvalue('vm_name', '')

print('Content-Type: text/html')
print()
print('<!DOCTYPE html>')
print('<html><head><title>zlma vif query vm</title>')
print('<link rel="icon" type="image/png" href="/zlma.ico">')
print('<link rel="stylesheet" href="/zlma.css">')
print('</head><body>')
zlma_buttons = Zlma_buttons("using-vif-query")
print('<h2>Query VM Configuration</h2>')

print('<form method="get" action="/zlmarw/vifcmd.py">')
print('<input type="hidden" name="cmd" value="query">')
print('<input type="hidden" name="sub_cmd" value="vm">')
print('<input type="hidden" name="arg2" value="">')
print('<input type="hidden" name="arg3" value="">')
print('<input type="hidden" name="arg4" value="">')
print('<table>')
print('<tr><td><label for="vm_name">VM Name :</label></td>')
print('<td><input type="text" id="vm_name" name="arg1" required placeholder="Enter VM name"></td></tr>')
print('<tr><td colspan="2"><button type="submit" class="button green-button">Query VM Configuration</button></td></tr>')
print('</table></form>')
print('</body></html>')
