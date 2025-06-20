#!/srv/venv/bin/python3
import urllib.parse
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif_hyp_disk:
  def __init__(self):
    """
    get arguments to call the 'vif hypervisor disk' command 
    """
    self.title = "zlma vif hypervisor disk"
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')

  def create_page(self):                   # make the page body
    zlma_buttons = Zlma_buttons("using-vif-hypervisor") # show navigation buttons
    print(f'<h2>{self.title}</h2>')        # show title
    html_code = '<table>'
    html_code += "<tr><td><pre>"           # start row, cell, preformatted text
    html_code += "TODO: gather args to call 'vif hypervisor disk'\n"
    html_code += "Vif syntax: ADD IMAGE|PAGING device volid\n"
    html_code += "            DELete IMAGE|PAGING device|volid"
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_hyp_disk = Vif_hyp_disk()              # create a singleton
vif_hyp_disk.create_page()                 # create a web page

