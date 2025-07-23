#!/srv/venv/bin/python3
"""
vifimgcreate.py - create a new Linux VM or golden image
"""
#import urllib.parse
import os
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf

class Vif_img_create:
  def __init__(self):
    """
    get arguments to call VM or image create commands 
    """
    query_string = os.environ.get('QUERY_STRING', '') # get env var
    query_params = parse_qs(query_string)  # parse query string
    self.sub_cmd = query_params.get('sub_cmd', [''])[0] # get first element of 'sub_cmd' value
    self.cmd = query_params.get('cmd', ['image'])[0]   # get command type (vm or image)
    
    if self.cmd == 'vm':
      self.title = "zlma vif vm create"
      self.nav_context = "using-vif-vm"
    else:
      self.title = "zlma vif image create"
      self.nav_context = "using-vif-image"
      
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')

  def create_page(self):                   # make the HTML page
    zlma_buttons = Zlma_buttons(self.nav_context) # add navigation buttons
    print(f'<h2>{self.title}</h2>') 
    html_code = '<table>'
    html_code += "<tr><td><pre>"           # start row, cell, preformatted text
    
    if self.cmd == 'vm':
      html_code += "TODO: gather args to call 'vif vm create' - VM name, template image?\n"
    else:
      html_code += "TODO: gather args to call 'vif image create' - host name, distro and T-shirt size?\n"
    
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_img_create = Vif_img_create()          # create a singleton
vif_img_create.create_page()               # create a web page

from flask import Flask, request, render_template_string

app = Flask(__name__)
vif_vm_create = VifVmCreate()

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        action = request.form.get('action', '')
        if action == 'create':
            return vif_vm_create.process_creation(request.form)
    return vif_vm_create.create_form_page()

if __name__ == "__main__":
    app.run(port=8000)

