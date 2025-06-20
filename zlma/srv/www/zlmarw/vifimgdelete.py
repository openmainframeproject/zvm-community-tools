#!/srv/venv/bin/python3
import urllib.parse
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif_img_delete:
  def __init__(self):
    """
    get arguments to call the 'vif image delete' command 
    """
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print('<html><head><title>Run vif image delete</title>')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')
    zlma_buttons = Zlma_buttons("using-vif-image") # add navigation buttons

  def create_page(self):                   # make the HTML page
    html_code = '<table>'
    html_code += "<tr><td><pre>"           # start row, cell, preformatted text
    html_code += "TODO: gather args to call 'vif image delete' - just host name\n"
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_img_create = Vif_img_create()          # create a singleton
vif_img_delete.create_page()               # create a web page

