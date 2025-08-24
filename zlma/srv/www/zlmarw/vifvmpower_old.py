#!/srv/venv/bin/python3
"""
vifvmpower.py - VM power operations (start, stop, stopall)
"""
import cgi
import subprocess
import sys
import html
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf

class Vif_vm_power:
  def __init__(self):
    """
    get arguments to call the 'vif vm' power commands
    """
    self.form = cgi.FieldStorage()
    self.sub_cmd = self.form.getvalue('sub_cmd', '')
    self.title = f"zlma vif vm {self.sub_cmd}"
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')

  def create_page(self):                   # make the HTML page
    zlma_buttons = Zlma_buttons("using-vif-vm") # add navigation buttons
    print(f'<h2>{self.title}</h2>') 
    
    if self.sub_cmd == 'start':
      self.handle_start()
    elif self.sub_cmd == 'stop':
      self.handle_stop()
    elif self.sub_cmd == 'stopall':
      self.handle_stopall()
    else:
      html_code = '<table>'
      html_code += "<tr><td><pre>"
      html_code += f"TODO: implement vif vm {self.sub_cmd}\n"
      html_code += "</pre></td></tr></table>\n"
      html_code += "</body></html>"
      print(html_code)

  def handle_start(self):
    """Handle VM start - redirect to vifcmd """
    print('<form method="get" action="/zlmarw/vifcmd.py">')
    print('<input type="hidden" name="cmd" value="vm">')
    print('<input type="hidden" name="sub_cmd" value="start">')
    print('<input type="hidden" name="arg2" value="">')
    print('<input type="hidden" name="arg3" value="">')
    print('<input type="hidden" name="arg4" value="">')
    print('<table>')
    print('<tr><td><label for="vm_name">VM Name :</label></td>')
    print('<td><input type="text" id="vm_name" name="arg1" required placeholder="Enter VM name"></td></tr>')
    print('<tr><td colspan="2">')
    print('<button type="submit" class="button green-button">Start VM</button>')
    print('</td></tr>')
    print('</table></form>')
    print('</body></html>')

  def handle_stop(self):
    """Handle VM stop - redirect to vifcmd """
    print('<form method="get" action="/zlmarw/vifcmd.py">')
    print('<input type="hidden" name="cmd" value="vm">')
    print('<input type="hidden" name="sub_cmd" value="stop">')
    print('<input type="hidden" name="arg2" value="">')
    print('<input type="hidden" name="arg3" value="">')
    print('<input type="hidden" name="arg4" value="">')
    print('<table>')
    print('<tr><td><label for="vm_name">VM Name :</label></td>')
    print('<td><input type="text" id="vm_name" name="arg1" required placeholder="Enter VM name"></td></tr>')
    print('<tr><td colspan="2">')
    print('<button type="submit" class="button red-button" ')
    print('onclick="return confirm(\'Are you sure you want to stop this VM?\');">Stop VM</button>')
    print('</td></tr>')
    print('</table></form>')
    print('</body></html>')

  def handle_stopall(self):
    """Handle stopall - let the VIF backend handle getting VM list"""
    print('<h3>Stop All VMs</h3>')
    print('<p>This will stop all VMs in the current LPAR. The system will automatically retrieve the VM list from the database.</p>')
    
    # Create form to execute stopall - VIF backend will handle getting VM list
    print('<form method="get" action="/zlmarw/vifcmd.py">')
    print('<input type="hidden" name="cmd" value="vm">')
    print('<input type="hidden" name="sub_cmd" value="stopall">')
    print('<input type="hidden" name="arg1" value="">')
    print('<input type="hidden" name="arg2" value="">')
    print('<input type="hidden" name="arg3" value="">')
    print('<input type="hidden" name="arg4" value="">')
    print('<table>')
    print('<tr><td colspan="2">')
    print('<button type="submit" class="button red-button" ')
    print('onclick="return confirm(\'Are you sure you want to stop all VMs in this LPAR?\');">Stop All VMs</button>')
    print('</td></tr>')
    print('</table></form>')
    print('</body></html>')

# main()
vif_vm_power = Vif_vm_power()          # create a singleton
vif_vm_power.create_page()               # create a web page
