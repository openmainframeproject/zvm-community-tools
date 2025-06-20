#!/srv/venv/bin/python3
"""
vifdiskcmd.py - get arguments to call the 'vif disk copy|create|delete|share' command 
"""
import os 
import subprocess
import sys
from urllib.parse import parse_qs
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf

class Vif_disk_cmd:
  def __init__(self):
    query_string = os.environ.get('QUERY_STRING', '') # get env var
    query_params = parse_qs(query_string)  # parse query string
    self.sub_cmd = query_params.get('sub_cmd', [''])[0]
    self.user_id = query_params.get('user_id', [''])[0]
    self.lpar = query_params.get('lpar', [''])[0]
    self.title = f"zlma vif disk {self.sub_cmd}"
    print("Content-Type: text/html")       # start HTML page
    print()
    print("<!DOCTYPE html>")
    print(f"<html><head><title>{self.title}</title>")
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">')
    print("</head><body>")

  def copy_disk(self):                     # create table body to copy disk
    html = "<table id='zlma-table'><tr>\n"                                   # start table and row
    html += "<th></th><th>User ID</th><th>Address</th><th></th>\n"           # table header
    html += f"<tr><td>&nbsp;From&nbsp;</td>"                                 # start first row
    html += f"<td>{self.user_id}</td>\n"
    html += "<td><input type='text' name='arg2'></td>\n"                     # text box for source vaddr
    html += "<td><input value='Copy disk' class='button green-button' type='submit'></td>\n" 
    html += "</tr><tr><td>&nbsp;To&nbsp;</td>"                               # start second row
    html += "<td><input type='text' name='arg3'>\n"                          # text box for target user ID
    html += "<td><input type='text' name='arg4'>\n"                          # text box for target vaddr
    html += "<td></td>\n"                                                    # empty cell
    html += "</tr></table>\n"                                                # end row and table
    print(html)

  def create_disk(self):                       # create table body to create disk
    html = "<table id='zlma-table'><tr>\n"                                   # start table and row
    html += "<th>User ID</th><th>Address</th><th>Size GB</th><th></th>\n"    # table header
    html += f"<tr><td>{self.user_id}</td>\n"                                 # start first row
    html += "<td><input type='text' name='arg2'></td>\n"                     # text box for source vaddr
    html += "<td><input type='text' name='arg3'></td>\n"                     # text box for disk size 
    html += "<td><input value='Create disk' class='button green-button' type='submit'></td>\n"
    html += "<td></td>\n"                                                    # empty cell
    html += "</tr></table>\n"                                                # end row table
    print(html)

  def delete_disk(self):                   # create table to delete disk
    html = "<table id='zlma-table'><tr>\n"                                   # start table and row
    html += "<th>User ID</th><th>Address</th><th></th>\n"                    # table header
    html += f"<tr><td>{self.user_id}</td>\n"                                 # start first row
    html += "<td><input type='text' name='arg2'></td>\n"                     # text box for vaddr to delete
    html += "<td><input value='Delete disk' class='button green-button' type='submit'></td>\n"
    html += "<td></td>\n"                                                    # empty cell
    html += "</tr></table>\n"                                                # end row table
    print(html)

  def share_disk(self):                    # create table to share disk
    html = "<table id='zlma-table'><tr>\n"                                   # start table and row
    html += "<th></th><th>User ID</th><th>Address</th><th></th>\n"           # table header
    html += f"<tr><td>&nbsp;From&nbsp;</td>"                                 # start first row
    html += f"<td>{self.user_id}</td>\n"
    html += "<td><input type='text' name='arg2'></td>\n"                     # text box for source vaddr
    html += "<td><input value='Share disk' class='button green-button' type='submit'></td>\n"
    html += "</tr><tr><td>&nbsp;To&nbsp;</td>"                               # start second row
    html += "<td><input type='text' name='arg3'>\n"                          # text box for target user ID
    html += "<td><input type='text' name='arg4'>\n"                          # text box for target vaddr
    html += "<td></td>\n"                                                    # empty cell
    html += "</tr></table>\n"                                                # end row and table
    print(html)

  def create_page(self):                   # make page body
    zlma_buttons = Zlma_buttons("using-vif-disk") # add navigation buttons
    print(f'<h2>{self.title}</h2>')        # add page title
    html = "<form action='/zlmarw/vifcmd.py' accept-charset='utf-8'>\n"      # start form
    html += f"<input type='hidden' name='cmd' value='disk'>\n"               # pass cmd
    html += f"<input type='hidden' name='sub_cmd' value='{self.sub_cmd}'>\n" # pass sub_cmd
    html += f"<input type='hidden' name='arg1' value='{self.user_id}'>\n"    # pass source user ID
    print(html)
    match self.sub_cmd:
      case "copy":
        self.copy_disk()
      case "create":
        self.create_disk()
      case "delete":
        self.delete_disk()
      case "share":
        self.share_disk()
      case _: 
        print(f'<h2>INTERNAL ERROR: unexpected sub_cmd: {self.sub_cmd}</h2>') 
    html = "</form>\n"                     
    html += "</body></html>\n"             # end page    
    print(html)

# main()
vif_disk_cmd = Vif_disk_cmd()              # create a singleton
vif_disk_cmd.create_page()                 # create a web page

