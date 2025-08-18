#!/srv/venv/bin/python3
"""
vifvmset_update.py - Utility page for updating CPUs or memory for a VM
"""
import cgi
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
import html

form = cgi.FieldStorage()
vm_name = form.getvalue('vm_name', '')
update_type = form.getvalue('update_type', '')  # 'cpus' or 'memory'
current_value = form.getvalue('current_value', '')

print('Content-Type: text/html')
print()
print('<!DOCTYPE html>')
print(f'<html><head><title>zlma vif vm set {update_type}</title>')
print('<link rel="icon" type="image/png" href="/zlma.ico">')
print('<link rel="stylesheet" href="/zlma.css">')
print('</head><body>')
zlma_buttons = Zlma_buttons("using-vif-vm")
print(f'<h2>Update {update_type} for VM: {html.escape(vm_name)}</h2>')

print('<form method="get" action="/zlmarw/vifcmd.py">')
print(f'<input type="hidden" name="cmd" value="vm">')
print(f'<input type="hidden" name="sub_cmd" value="set">')
print(f'<input type="hidden" name="arg1" value="{html.escape(vm_name)}">')
print(f'<input type="hidden" name="arg2" value="{html.escape(update_type)}">')
print(f'<input type="hidden" name="arg4" value="">')
print('<table>')
print('<tr><td>Current value:</td><td><strong>{}</strong></td></tr>'.format(html.escape(current_value)))
print('<tr><td>New value:</td><td>')
for val in ['1','2','3','4']:
    checked = 'checked' if val == current_value else ''
    disabled = 'disabled' if val == current_value else ''
    print(f'<label><input type="radio" name="arg3" value="{val}" {checked} {disabled}> {val}</label><br>')
print('</td></tr>')
print('<tr><td colspan="2"><button type="submit" class="button green-button">Update</button></td></tr>')
print('</table></form>')
print('</body></html>')
