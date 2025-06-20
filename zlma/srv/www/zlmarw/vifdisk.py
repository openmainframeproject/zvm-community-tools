#!/srv/venv/bin/python3
"""
vifdisk.py: perform 'vif image disk' commands
'sub_cmd' passed with QUERY_STRING can be 'copy', 'create', 'delete' or 'share'
"""
import os 
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif_disk:
  def __init__(self):
    """
    get arguments to call the 'vif disk <sub_cmd>' command 
    """
    query_string = os.environ.get('QUERY_STRING', '') # get env var
    query_params = parse_qs(query_string)  # parse query string
    self.sub_cmd = query_params.get('sub_cmd', [''])[0]
    self.title = f"zlma vif disk {self.sub_cmd}"

    print("Content-Type: text/html")       # start the HTML page
    print()
    print("<!DOCTYPE html>")
    print(f"<html><head><title>{self.title}</title>")
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print("</head><body>")

  def create_page(self):                   # make the page body
    zlma_buttons = Zlma_buttons("using-vif-disk") # add navigation buttons
    print(f"<h2>{self.title}</h2>")
    html = "<table id='zlma-table'><tr>"   # start table then add headers
    html += "<th>Host name</th><th>LPAR</th><th>User ID</th><th>IP address</th>"
    html += "<th>CPUs</th><th>GB memory</th><th>&nbsp;</th>"
  
    cmd = "/usr/local/sbin/zlma webdata"   # get all s390x servers
    try:
      proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    except Exception as e:
      print(f"search_cmdb(): Exception calling zlma: {e}")
      exit(3)
    rc = proc.returncode
    row_list = proc.stdout.splitlines()
    for next_row in row_list:
      list_row = next_row.split(",")
      html += "<tr>\n"
      cell_num = 0
      for cell in list_row:
        html += f"  <td>{cell}</td>\n"
        cell_num += 1
        if cell_num == 2:                  # LPAR column
          lpar = cell
        if cell_num == 3:                  # user ID column
          user_id = cell

      # add a "Do it" button in the last column
      html += f"<td><form action='/zlmarw/vifdiskcmd.py' accept-charset='utf-8'>\n"
      html += f"<input type='hidden' name='sub_cmd' value='{self.sub_cmd}'>\n"
      html += f"<input type='hidden' name='lpar' value='{lpar}'>\n"
      html += f"<input type='hidden' name='user_id' value='{user_id}'>\n"
      html += f"<button class='button green-button'>{self.sub_cmd.capitalize()} disk</button></form></td>\n"
      html += "</tr>\n"
    html += "</table>"
    html += "</body></html>"               # end page
    print(html)

# main()
vif_disk = Vif_disk()                      # create a singleton
vif_disk.create_page()                     # create a web page

