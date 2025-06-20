#!/srv/venv/bin/python3
"""
vifimgpower.py - create a web page to allow users to start or stop Linux images. It is called for:
                 - vif image start:   8 columns with action button
                 - vif image stop     8 columns with action button
                 - vif image stopall  7 columns
"""
import os
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif_img_set:
  def __init__(self):
    """
    get arguments to call the 'vif image set' command 
    """
    query_string = os.environ.get('QUERY_STRING', '') # get env var
    query_params = parse_qs(query_string)  # parse query string
    self.sub_cmd = query_params.get('sub_cmd', [''])[0] # get first element of 'sub_cmd' value
    self.title = f"zlma vif image {self.sub_cmd} command"
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print('</head><body>')

  def ping_server(self, ip_addr: str):     # ping IP addr of a server as efficiently as possible
    ping_cmd = f"ping -c1 -W 0.5 {ip_addr}" # send 1 packet, timeout after 500ms
    proc = subprocess.run(ping_cmd, shell=True, capture_output=True, text=True)
    return proc.returncode                 # 0 = server pings

  def create_page(self):                   # make the HTML page
    zlma_buttons = Zlma_buttons("using-vif-image") # add navigation buttons
    print(f'<h2>{self.title}</h2>')
    html = "<table id='zlma-table'>\n<tr>" # start table then add headers
    html += "<th>Host name</th><th>LPAR</th><th>User ID</th><th>IP address</th><th>CPUs</th><th>GB memory</th><th>Status</th>"
    if self.sub_cmd != "stopall":          # need an 8th column
      html += "<th>Manage</th>"
    html += "</tr>\n"
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
      html += "<tr>\n"                     # start row
      cell_num = 0                         # keep track of cell nums
      for cell in list_row:
        cell_num += 1
        match cell_num:
          case 2:                          # LPAR
            lpar = cell
            html += f"<td>{cell}</td>\n"
          case 3:                          # user ID
            user_id = cell
            html += f"<td>{cell}</td>\n"
          case 4:                          # IP address 
            ip_addr = cell
            html += f"<td>{cell}</td>\n"
          case _:
            html += f"<td>{cell}</td>\n"

      # add 7th column "Status"
      if self.ping_server(ip_addr):        # server does not ping
        html += '<td style="color:red;">down</td>'
        status = "down"
      else:
        html += '<td style="color:green;">up</td>'
        status = "up"
 
      # for 'start' and 'stop' add 8th colunm "Manage" and determine if an action is needed
      if self.sub_cmd != 'stopall':        # extra column needed
        if self.sub_cmd == "start" and status == "down":
          html += f"<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
          html += f"<input type='hidden' name='cmd' value='image'>\n"
          html += f"<input type='hidden' name='sub_cmd' value='{self.sub_cmd}'>\n"
          html += f"<input type='hidden' name='arg1' value='{user_id}'>\n"
          html += f"<input type='hidden' name='arg2' value='{lpar}'>\n"
          html += f"<button class='button green-button'>Start</button></form></td>\n"
        elif self.sub_cmd == "stop" and status == "up":
          html += f"<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
          html += f"<input type='hidden' name='cmd' value='image'>\n"
          html += f"<input type='hidden' name='sub_cmd' value='{self.sub_cmd}'>\n"
          html += f"<input type='hidden' name='arg1' value='{user_id}'>\n"
          html += f"<input type='hidden' name='arg2' value='{lpar}'>\n"
          html += f"<button class='button green-button'>Stop</button></form></td>\n"
        else:                              # no action needed
          html += f"<td></td>\n"
      html += "</tr>\n"                    # end row
    html += "</table>"
    if self.sub_cmd == 'stopall':          # ask "are you sure"
      html = "<h2>Are you sure?</h2>"
      html += "<table><tr><td>"            # start table, row and cell
      html += f"<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
      html += f"<input type='hidden' name='cmd' value='image'>\n"
      html += f"<input type='hidden' name='sub_cmd' value='stopall'>\n"
      html += f"<input type='hidden' name='arg1' value='{lpar}'>\n"
      html += f"<button class='button green-button'>Stop all</button></form></td>\n"
      html += "</pre></td></tr></table>\n" # end cell, row and table
    html += "</body></html>"
    print(html)

# main()
vif_img_set = Vif_img_set()                # create a singleton
vif_img_set.create_page()                  # create a web page

