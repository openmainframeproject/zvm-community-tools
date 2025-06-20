#!/srv/venv/bin/python3
"""
vifdoset.py: get arguments to call the 'vif image set' command to modify memory or CPUs 
Args passed with QUERY_STRING: 'host_name', 'lpar', 'user_id' and either 'cpus' or 'memory'
"""
import os 
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif_set_cpus:
  def __init__(self):
    query_string = os.environ.get('QUERY_STRING', '') # get env var
    query_params = parse_qs(query_string)  # parse query string
    self.host_name = query_params.get('host_name', [''])[0]
    self.lpar = query_params.get('lpar', [''])[0]
    self.user_id = query_params.get('user_id', [''])[0]
    self.cpus = query_params.get('cpus', [''])[0]
    self.memory = query_params.get('memory', [''])[0]
    self.title = "zlma image set cpus"

    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print('<html><head><title>Run vif image delete</title>')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')
    zlma_buttons = Zlma_buttons("using-vif-image") # add navigation buttons

  def create_page(self):                   # create the page body
    html_code = '<table>'
    html_code += "<tr><td><pre>"           # start row, cell, preformatted text
    html_code += f"lpar: {self.lpar} host_name: {self.host_name} user_id: {self.user_id} \n"
    html_code += f"cpus: {self.cpus} memory: {self.memory} \n"
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_set_cpus = Vif_set_cpus()              # create a singleton
vif_set_cpus.create_page()                 # create a web page

