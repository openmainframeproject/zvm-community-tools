#!/srv/venv/bin/python3
"""
vifvmpower.py - VM power operations (start, stop, stopall)
"""
import cgi
import subprocess
import sys
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
    html_code = '<table>'
    html_code += "<tr><td><pre>"           # start row, cell, preformatted text
    
    if self.sub_cmd == 'start':
      html_code += "TODO: gather args to call 'vif vm start' - VM name?\n"
    elif self.sub_cmd == 'stop':
      html_code += "TODO: gather args to call 'vif vm stop' - VM name?\n"
    elif self.sub_cmd == 'stopall':
      html_code += "TODO: implement 'vif vm stopall' - stop all VMs on LPAR\n"
    else:
      html_code += f"TODO: implement vif vm {self.sub_cmd}\n"
    
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_vm_power = Vif_vm_power()          # create a singleton
vif_vm_power.create_page()               # create a web page
