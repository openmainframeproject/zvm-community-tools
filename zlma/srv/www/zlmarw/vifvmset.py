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
    
    if self.sub_cmd == 'delete':
      self.handle_delete()
      return
    elif self.sub_cmd == 'set':
      self.handle_set()
      return
    elif self.sub_cmd == 'network':
      html_code = '<table>'
      html_code += "<tr><td><pre>"
      html_code += "TODO: gather args to call 'vif vm network' - VM name, device, VSWITCH name?\n"
      html_code += "</pre></td></tr></table>\n"
      html_code += "</body></html>"
      print(html_code)
    else:
      html_code = '<table>'
      html_code += "<tr><td><pre>"
      html_code += f"TODO: implement vif vm {self.sub_cmd}\n"
      html_code += "</pre></td></tr></table>\n"
      html_code += "</body></html>"
      print(html_code)

  def handle_delete(self):

    print('<form method="get" action="/zlmarw/vifcmd.py">')
    print('<input type="hidden" name="cmd" value="vm">')
    print('<input type="hidden" name="sub_cmd" value="delete">')
    print('<input type="hidden" name="arg2" value="">')
    print('<input type="hidden" name="arg3" value="">')
    print('<input type="hidden" name="arg4" value="">')
    print('<table>')
    print('<tr><td><label for="vm_name">VM Name :</label></td>')
    print('<td><input type="text" id="vm_name" name="arg1" required placeholder="Enter VM name/userid"></td></tr>')
    print('<tr><td colspan="2">')
    print('<button type="submit" class="button red-button" ')
    print('onclick="return confirm(\'Are you sure you want to delete this VM?\');">Delete VM</button>')
    print('</td></tr>')
    print('</table></form>')
    print('</body></html>')

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
              html += f"<td><form action='/zlmarw/vifvmset_update.py' method='get' accept-charset='utf-8'>\n"
              html += f"<input type='hidden' name='vm_name' value='{user_id}'>\n"
              html += f"<input type='hidden' name='update_type' value='cpus'>\n"
              html += f"<input type='hidden' name='current_value' value='{cell}'>\n"
              html += "<button class='button green-button'>CPUs</button></form></td>\n"
            case 6:                          # memory - add button to modify it
              html += f"<td>&nbsp;{cell} GB</td>\n"
              html += f"<td><form action='/zlmarw/vifvmset_update.py' method='get' accept-charset='utf-8'>\n"
              html += f"<input type='hidden' name='vm_name' value='{user_id}'>\n"
              html += f"<input type='hidden' name='update_type' value='memory'>\n"
              html += f"<input type='hidden' name='current_value' value='{cell}'>\n"
              html += "<button class='button green-button'>memory</button></form></td>\n"
            case _:                         
              html += f"<td>{cell}</td>\n"
        html += "</tr>\n"                    # end row
      html += "</table></body></html>"
      print(html)
# main()
vif_vm_set = Vif_vm_set()          # create a singleton
vif_vm_set.create_page()               # create a web page
