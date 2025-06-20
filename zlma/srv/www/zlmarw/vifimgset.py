#!/srv/venv/bin/python3
"""
vifimgset.py - allow user to modify number of CPUs or amount of memory
"""
import os
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_srvrs import Zlma_srvrs

class Vif_img_set:                         # get arguments to call the 'vif image set' command 
  def __init__(self):
    self.srvrs = Zlma_srvrs()              # get s390x servers in the CMDB
    self.title = "zlma vif image set"
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">') # common CSS's
    print('</head><body>')

  def create_page(self):                   # make the page body
    zlma_buttons = Zlma_buttons("using-vif-image") # add navigation buttons
    print(f'<h2>{self.title}</h2>')
    html = "<table id='zlma-table'><tr>\n" # start table then add headers
    html += "<th>Host name</th><th>LPAR</th><th>User ID</th><th>IP address</th><th>CPUs</th>\n"
    html += "<th>Set</th><th>GB memory</th><th>Set</th>"
    cmd = "/usr/local/sbin/zlma webdata"   # get all s390x servers
    try:
      proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    except Exception as e:
      print(f"search_cmdb(): Exception calling zlma: {e}")
      exit(3)
    row_list = proc.stdout.splitlines()
    for next_row in row_list:
      list_row = next_row.split(",")
      html += "<tr>\n"                     # start row
      cell_num = 0                         # keep track of cell nums
      for cell in list_row:
        cell_num += 1
        match cell_num:
          case 1:                          # host name 
            host_name = cell
            html += f"<td>{cell}</td>\n"
          case 2:                          # LPAR
            lpar = cell
            html += f"<td>{cell}</td>\n"
          case 3:                          # user ID
            user_id = cell
            html += f"<td>{cell}</td>\n"
          case 5:                          # CPUs - add button to modify them
            html += f"<td>&nbsp;{cell}</td>\n"
            html += "<td><form action='/zlmarw/vifdoset.py' accept-charset='utf-8'>\n"
            html += f"<input type='hidden' name='host_name' value='{host_name}'>\n"
            html += f"<input type='hidden' name='lpar' value='{lpar}'>\n"
            html += f"<input type='hidden' name='user_id' value='{user_id}'>\n"
            html += f"<input type='hidden' name='cpus' value='{cell}'>\n"
            html += "<button class='button green-button'>CPUs</button></form></td>\n"
          case 6:                          # memory - add button to modify it
            html += f"<td>&nbsp;{cell} GB</td>\n"
            html += "<td><form action='/zlmarw/vifdoset.py' accept-charset='utf-8'>\n"
            html += f"<input type='hidden' name='host_name' value='{host_name}'>\n"
            html += f"<input type='hidden' name='lpar' value='{lpar}'>\n"
            html += f"<input type='hidden' name='user_id' value='{user_id}'>\n"
            html += f"<input type='hidden' name='memory' value='{cell}'>\n"
            html += "<button class='button green-button'>memory</button></form></td>\n"
          case _:                         
            html += f"<td>{cell}</td>\n"
      html += "</tr>\n"                    # end row
    html += "</table>"
    print(html)

# main()
vif_img_set = Vif_img_set()                # create a singleton
vif_img_set.create_page()                  # create a web page

