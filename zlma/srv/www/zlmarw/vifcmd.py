#!/srv/venv/bin/python3
#import html
import os
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif_cmd:
  def __init__(self):
    """
    Initialize globals, create page header, set background
    """
    self.title = "zlma vif run command"
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')
    zlma_buttons = Zlma_buttons("using-vif")     # add navigation buttons
    print(f'<h2>{self.title}</h2>')

  def run_vif_cmd(self, cmd: str, sub_cmd: str, arg1: str, arg2: str, arg3: str, arg4: str) -> str:
    """
    Run a vif command showing command and output in preformatted text
    All commands have a sub-command, which can have 0 - 4 args
    """
    output = f"Running command: vif {cmd} {sub_cmd} {arg1} {arg2} {arg3} {arg4}\n"
    the_cmd = f"/srv/venv/bin/python3 /usr/local/sbin/vif {cmd} {sub_cmd} {arg1} {arg2} {arg3} {arg4}"
    proc = subprocess.run(the_cmd, shell=True, capture_output=True, text=True)
    rc = proc.returncode
    if rc != 0:
      output += f"Vif_cmd.run_cmd(): subprocess.run({the_cmd}) returned {rc}"
    else:
      output += f"{proc.stdout}"
    return output

  def create_page(self):
    """
    Create an HTML page with four tables: hypervisor, image, disk, and query.
    Handle dynamically based on vif commands and subcommands.
    """
    query_string = os.environ.get('QUERY_STRING', '')
    query_params = parse_qs(query_string)  # Parse the query string
    cmd = query_params.get('cmd', [''])[0] # Get 'cmd', default to '' if not found
    sub_cmd = query_params.get('sub_cmd', [''])[0].rstrip()
    arg1 = query_params.get('arg1', [''])[0].rstrip() # vif sub-commands have up to four arguments
    arg2 = query_params.get('arg2', [''])[0].rstrip()
    arg3 = query_params.get('arg3', [''])[0].rstrip()
    arg4 = query_params.get('arg4', [''])[0].rstrip()

    html_code = '<table class="greenScreenTable">' # start a 'green screen' table
    html_code += "<tr><td><pre>"                   # start row, cell, preformatted text
    html_code += self.run_vif_cmd(cmd, sub_cmd, arg1, arg2, arg3, arg4)  
    html_code += "</pre></td></tr></table>\n"       # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

# main()
vif_cmd = Vif_cmd()                        # create a singleton
vif_cmd.create_page()                      # create a web page

