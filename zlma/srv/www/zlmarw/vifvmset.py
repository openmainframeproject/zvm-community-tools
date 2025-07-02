#!/srv/venv/bin/python3
"""
vifvmset.py - set VM properties (delete, set, network)
"""
import cgi
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf

class Vif_vm_set:
  def __init__(self):
    """
    get arguments to call the 'vif vm' commands for delete, set, network
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
    
    if self.sub_cmd == 'delete':
      html_code += "TODO: gather args to call 'vif vm delete' - VM name?\n"
    elif self.sub_cmd == 'set':
      html_code += "TODO: gather args to call 'vif vm set' - VM name, storage size or CPU count?\n"
    elif self.sub_cmd == 'network':
      html_code += "TODO: gather args to call 'vif vm network' - VM name, device, VSWITCH name?\n"
    else:
      html_code += f"TODO: implement vif vm {self.sub_cmd}\n"
    
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_vm_set = Vif_vm_set()          # create a singleton
vif_vm_set.create_page()               # create a web page
