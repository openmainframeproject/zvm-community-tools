#!/usr/bin/env python3
import html
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Vif:
  def __init__(self):
    """
    Initialize globals, create page header, set background
    """
    self.pattern = ""                      # search pattern
    self.rows = []                         # resulting rows
    self.title = "zlma vif - Virtual Image Facility"

    # start the HTML page
    print('Content-Type: text/html')
    print()
    print('<!DOCTYPE html>')  
    print(f'<html><head><title>{self.title}</title>\n')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">') # common CSS's`
    print('</head>')
    print('<body>')
    zlma_buttons = Zlma_buttons("using-vif")  # add navigation buttons

  def create_table(self, vif_cmd, data): # create one of four vif tables
    """
    Create an HTML table 
    Args:
      vif_cmd: vif command/table name 
      data   : list of lists of table data
    """
    html_code = "&nbsp;<table id='zlma-table'>\n"
    html_code += f"<thead><tr><th colspan='2'>{vif_cmd}</th></tr></thead>\n<tbody>\n"
    script = ""                            # next script to perform operation
    for row in data:
      html_code += "<tr>"
      cell1 = "yes"
      for cell in row:
        if cell1 == "yes":                 # get args if needed else call call vif 
          # if vif_cmd == "hypervisor" and cell == "disk":
          if vif_cmd == "hyp" and cell == "disk":
            script = "vifhypdisk.py"
          elif vif_cmd == "vm" and cell == "create":
            script = "vifvmcreate.py"      
          elif vif_cmd == "vm" and (cell == "delete" or cell == "set" or cell == "network"):
            script = f"vifimgset.py?sub_cmd={cell}"      
          elif vif_cmd == "vm" and (cell == "start" or cell == "stop" or cell == "stopall"):
            script = f"vifimgpower.py?sub_cmd={cell}"      
          elif vif_cmd == "image" and cell == "create":
            script = "vifimgcreate.py"      
          elif vif_cmd == "image" and cell == "delete":
            script = f"vifimgset.py?sub_cmd={cell}"      
          elif vif_cmd == "query" and cell == "vm":
            script = f"vifimgset.py?sub_cmd={cell}"      
          elif vif_cmd == "disk":
            script = f"vifdisk.py?sub_cmd={cell}"      
          else:                            # no arguments needed
            script = "vifcmd.py" 
          html_code += f"<td><form action='/zlmarw/{script}' target='_blank' accept-charset='utf-8'>\n"
          html_code += f"<input type='hidden' name='cmd' value='{vif_cmd}'>\n"
          html_code += f"<input type='hidden' name='sub_cmd' value='{cell}'>\n"
          html_code += f"<button class='button green-button'>{cell}</button></form></td>\n"
          cell1 = "no"
        else:                              # second cell
          html_code += f"<td>{cell}</td>"  # add description
      html_code += "</tr>\n"
    html_code += "</tbody></table>&nbsp;\n"
    return html_code
  
  def create_page(self):                   # Create page body with 4 tables: hypervisor, vm, disk, and query
    hyper_data = [["collect", "Gather problem determination info"], 
                  ["disk", "Add paging or Linux disk space"],
                  ["errors", "Report on hardware errors"], 
                  ["restart", "SHUTDOWN REIPL z/VM"],
                  ["service", "Install latest z/VM service"],
                  ["shutdown", "SHUTDOWN z/VM"],
                  ["verify", "Perform consistency checks"]
                 ]
    vm_data = [["create", "Clone a Linux VM"], 
               ["delete", "Delete Linux VM"],
               ["list", "List all VMs and their status"],
               ["network", "Add OSA triplet"],
               ["set", "Change memory or number of CPUs"],
               ["start", "Start a VM"],
               ["stop", "Stop a VM"],
               ["stopall", "Stop all VMs on LPAR"]
              ]
    image_data = [["create", "Create a new Linux golden image"], 
                  ["delete", "Delete a Linux golden image"]
                 ]
    disk_data =  [["copy", "Copy source disk to newly added target disk"], 
                  ["create", "Add a new minidisk"], 
                  ["delete", "Delete an existing minidisk"],
                  # ["share", "Give R/O access to a disk of another image"]
                 ]
    query_data = [["active", "Report which VMs are running"],
                  # ["all", "Invoke all other query subcommands"],
                  ["configuration", "Display current vif settings"],
                  ["disks", "Display Linux and z/VM disks"],
                  # ["errors", "Report on hardware errors"],
                  ["version", "Show vif version"],
                  ["network", "Display network configuration"],
                  # ["paging", "Report on page space"],
                  ["performance", "Display current CPU, paging and I/O utilization"],
                  # ["shared", "Display VMs that share disks"],
                  ["vm", "Display configuration of a VM"],
                  # ["volumes", "Display image and paging DASD volumes"]
                 ]
  
    html_code = f"<h2>{self.title}</h2>\n"
    html_code += "<table id='surroundingTable'><tr><td>\n" 
    # html_code += self.create_table("hypervisor", hyper_data)
    html_code += self.create_table("hyp", hyper_data)
    html_code += "</td><td>\n"             # start new cell
    html_code += self.create_table("query", query_data)
    html_code += "</td></tr><tr><td>"      # end cell and row, start new row
    html_code += self.create_table("vm", vm_data)
    html_code += "</td><td>\n"             # start new cell
    html_code += self.create_table("image", image_data)
    html_code += "</td></tr><tr><td colspan='2'>"      # end cell and row, start new row spanning both columns
    html_code += self.create_table("disk", disk_data)
    html_code += "</td></tr></table>\n"    # end cell, row and table
    html_code += "</body>\n</html>"
    print(html_code)
  
# main()
vif = Vif()                                # create a singleton
vif.create_page()                          # create a web page
