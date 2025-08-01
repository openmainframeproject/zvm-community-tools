#!/srv/venv/bin/python3
"""
vifvmset.py - set VM properties (delete, set, network)
"""
import cgi
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf

class Vif_vm_set:
  def __init__(self):
    """
    get arguments to call the 'vif vm' commands for delete, set, network
    """
    self.form = cgi.FieldStorage()
    self.sub_cmd = self.form.getvalue('sub_cmd', '')
    self.title = f"zlma vif vm {self.sub_cmd}"
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
    
    if self.sub_cmd == 'delete':
      html_code += "TODO: gather args to call 'vif vm delete' - VM name?\n"
    elif self.sub_cmd == 'set':
      handle_set()
      # html_code += "TODO: gather args to call 'vif vm set' - VM name, storage size or CPU count?\n"
    elif self.sub_cmd == 'network':
      html_code += "TODO: gather args to call 'vif vm network' - VM name, device, VSWITCH name?\n"
    else:
      html_code += f"TODO: implement vif vm {self.sub_cmd}\n"
    
    html_code += "</pre></td></tr></table>\n" # end cell, row and table
    html_code += "</body></html>"
    print(html_code)

    def handle_set(self):
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
              html += "<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
              html += f"<input type='hidden' name='cmd' value='{self.cmd}'>\n"
              html += f"<input type='hidden' name='sub_cmd' value='set'>\n"
              html += f"<input type='hidden' name='arg1' value='{user_id}'>\n"
              html += f"<input type='hidden' name='arg2' value='cpus'>\n"
              html += f"<input type='hidden' name='arg3' value='{cell}'>\n"
              html += "<button class='button green-button'>CPUs</button></form></td>\n"
            case 6:                          # memory - add button to modify it
              html += f"<td>&nbsp;{cell} GB</td>\n"
              html += "<td><form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"
              html += f"<input type='hidden' name='cmd' value='{self.cmd}'>\n"
              html += f"<input type='hidden' name='sub_cmd' value='set'>\n"
              html += f"<input type='hidden' name='arg1' value='{user_id}'>\n"
              html += f"<input type='hidden' name='arg2' value='memory'>\n"
              html += f"<input type='hidden' name='arg3' value='{cell}'>\n"
              html += "<button class='button green-button'>memory</button></form></td>\n"
            case _:                         
              html += f"<td>{cell}</td>\n"
        html += "</tr>\n"                    # end row
      html += "</table></body></html>"
      print(html)
# main()
vif_vm_set = Vif_vm_set()          # create a singleton
vif_vm_set.create_page()               # create a web page
