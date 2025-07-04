#!/srv/venv/bin/python3
"""
vifvmcreate.py - create a new Linux VM
"""
#import urllib.parse
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf

class Vif_vm_create:
  def __init__(self):
    """
    get arguments to call the 'vif vm create' command 
    """
    self.title = "zlma vif vm create"
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
    html_code += "TODO: gather args to call 'vif vm create' - VM name, template image?\n"
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_vm_create = Vif_vm_create()          # create a singleton
vif_vm_create.create_page()               # create a web page
