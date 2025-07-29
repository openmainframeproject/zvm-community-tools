#!/srv/venv/bin/python3
"""
vifimgset.py - handle VM operations (delete, set, network) and image delete
"""
import os
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_srvrs import Zlma_srvrs

class Vif_img_set:                         # handle VM and image operations
  def __init__(self):
    query_string = os.environ.get('QUERY_STRING', '') # get env var
    query_params = parse_qs(query_string)  # parse query string
    self.sub_cmd = query_params.get('sub_cmd', ['set'])[0] # get first element of 'sub_cmd' value
    self.cmd = query_params.get('cmd', ['vm'])[0]   # get command type (vm or image)
    
    if self.cmd == 'vm':
      self.title = f"zlma vif vm {self.sub_cmd}"
      self.nav_context = "using-vif-vm"
    else:
      self.title = f"zlma vif image {self.sub_cmd}"
      self.nav_context = "using-vif-image"
      
    self.srvrs = Zlma_srvrs()              # get s390x servers in the CMDB
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">') # common CSS's
    print('</head><body>')

  def create_page(self):                   # make the page body
    zlma_buttons = Zlma_buttons(self.nav_context) # add navigation buttons
    print(f'<h2>{self.title}</h2>')
    
    # Handle different sub-commands
    if self.sub_cmd == 'delete':
      self.handle_delete()
    # both network and set are moved to vm grammar
    # elif self.sub_cmd == 'network':
    #   self.handle_network()
    # else:  # 'set' command
    #   self.handle_set()

  def handle_delete(self):
    html = "<table><tr><td><pre>"           # start table, row, cell and preformatted text
    if self.cmd == 'vm':
      html += "TODO: gather args to call 'vif vm delete' - VM name?\n"
    else:
      html += "TODO: gather args to call 'vif image delete' - image name?\n"
    html += "</pre></td></tr></table></body></html>"
    print(html)

  # def handle_network(self):
  #   html = "<table><tr><td><pre>"           # start table, row, cell and preformatted text
  #   html += "TODO: gather args to call 'vif vm network' - VM name, device, VSWITCH name?\n"
  #   html += "</pre></td></tr></table></body></html>"
  #   print(html)

  # def handle_set(self):
  #   html = "<table id='zlma-table'><tr>\n" # start table then add headers
  #   html += "<th>Host name</th><th>LPAR</th><th>User ID</th><th>IP address</th><th>CPUs</th>\n"
  #   html += "<th>Set</th><th>GB memory</th><th>Set</th>"
  #   cmd = "/usr/local/sbin/zlma webdata"   # get all s390x servers
  #   try:
  #     proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  #   except Exception as e:
  #     print(f"search_cmdb(): Exception calling zlma: {e}")
  #     exit(3)
  #   row_list = proc.stdout.splitlines()
  #   for next_row in row_list:
  #     list_row = next_row.split(",")
  #     html += "<tr>\n"                     # start row
  #     cell_num = 0                         # keep track of cell nums
  #     for cell in list_row:
  #       cell_num += 1
  #       match cell_num:
  #         case 1:                          # host name 
  #           host_name = cell
  #           html += f"<td>{cell}</td>\n"
  #         case 2:                          # LPAR
  #           lpar = cell
  #           html += f"<td>{cell}</td>\n"
  #         case 3:                          # user ID
  #           user_id = cell
  #           html += f"<td>{cell}</td>\n"
  #         case 5:                          # CPUs - add button to modify them
  #           html += f"<td>&nbsp;{cell}</td>\n"
  #           html += "<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
  #           html += f"<input type='hidden' name='cmd' value='{self.cmd}'>\n"
  #           html += f"<input type='hidden' name='sub_cmd' value='set'>\n"
  #           html += f"<input type='hidden' name='arg1' value='{user_id}'>\n"
  #           html += f"<input type='hidden' name='arg2' value='cpus'>\n"
  #           html += f"<input type='hidden' name='arg3' value='{cell}'>\n"
  #           html += "<button class='button green-button'>CPUs</button></form></td>\n"
  #         case 6:                          # memory - add button to modify it
  #           html += f"<td>&nbsp;{cell} GB</td>\n"
  #           html += "<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
  #           html += f"<input type='hidden' name='cmd' value='{self.cmd}'>\n"
  #           html += f"<input type='hidden' name='sub_cmd' value='set'>\n"
  #           html += f"<input type='hidden' name='arg1' value='{user_id}'>\n"
  #           html += f"<input type='hidden' name='arg2' value='memory'>\n"
  #           html += f"<input type='hidden' name='arg3' value='{cell}'>\n"
  #           html += "<button class='button green-button'>memory</button></form></td>\n"
  #         case _:                         
  #           html += f"<td>{cell}</td>\n"
  #     html += "</tr>\n"                    # end row
  #   html += "</table></body></html>"
  #   print(html)

# main()
vif_img_set = Vif_img_set()                # create a singleton
vif_img_set.create_page()                  # create a web page

