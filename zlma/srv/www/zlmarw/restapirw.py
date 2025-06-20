#!/srv/venv/bin/python3
"""
Note the above "shebang" - this must be run from virtual environment /srv/venv/

restapirw.py - the zlma RESTful API in the R/W directory 
Format: http://<hostname>/zlmarw/restapirw.py?<operation>&param1&param2 ...

Operations:
- updateimg: update the number of CPUs and/or the GB of memory of an image
"""
import base64
import json
import logging
import mariadb
import os
import re
import subprocess
from urllib.parse import urlparse, parse_qs

class Zlma_rw_api():
  def __init__(self):
    logging.basicConfig(filename='/var/log/zlma/restapirw.log', format='%(asctime)s %(levelname)s %(message)s')
    self.log = logging.getLogger(__name__)
    self.log_level = "DEBUG"
    logging.basicConfig(filename='/var/log/zlma/restapi.log',
                        format='%(asctime)s %(levelname)s %(message)s',
                        level=self.log_level)
    self.log = logging.getLogger(__name__)
    self.load_config_file()                # read the config file
    self.log.setLevel(self.log_level) # set log level from config file

    # start the web page
    print("Content-Type: text/html")       # print MIME type
    print()                                # required empty line

  def load_config_file(self):
    """
    read the JSON config file /etc/zlma.conf
    """
    try:
      conf_file = open("/etc/zlma.conf", 'r')
    except Exception as e:
      self.log.error("load_config_file(): could not open configuration file /etc/zlma.conf - using defaults")
      return
    confJSON = json.loads(conf_file.read())
    self.log_level = confJSON['log_level'].upper()

  def parse_query_string(self) -> tuple[str, str]:
    """
    Get the env var QUERY_STRING and return operation and remaining parameters 
    """
    proc = subprocess.run("echo $QUERY_STRING", shell=True, capture_output=True, text=True)
    rc = proc.returncode
    if rc != 0:
      self.log.error(f"ZlmaAPI.parse_query_string(): subprocess.run('echo $QUERY_STRING' returned {rc}")
      return 1
    query_str = proc.stdout.strip('\n')    # get value removing newline
    self.log.debug(f"ZlmaAPI.parse_query_string(): query_str: {query_str}")
    query_parms = query_str.split('&')
    operation = query_parms[0]             # get operation
    query_parms = query_parms[1:]          # chop off operation
    return operation, query_parms

  def uu_decode(self, url):
    """ 
    Decode a uu-encoded URL (have absolutely no idea how this works, but it does :))
    """
    return re.compile('%([0-9a-fA-F]{2})',re.M).sub(lambda m: chr(int(m.group(1),16)), url)

  def update_record(self, query_str: str):
    """
    query_str contains the host name to be updated and three pieces of metadata
    Send SQL command to update a record's metadata:
    - App
    - Group
    - Owner
    """
    self.log.debug(f"ZlmaAPI.update_record(): query_str: {query_str}") 
    list_len = len(query_str)
    if list_len != 5:                       # error
      self.log.error(f"ZlmaAPI.update_record(): len(query_str): {list_len}, expected 5") 
      return
    cmd = f"""UPDATE servers SET app = '{query_str[1]}', env = '{query_str[2]}', 
      grp = '{query_str[3]}', owner = '{query_str[4]}' 
      WHERE host_name = '{query_str[0]}'
    """
    self.connect_to_cmdb()                 # connect to DB
    try:   
      self.cursor.execute(cmd)             # run SQL command 
    except mariadb.Error as e:
      self.log.error(f"ZlmaAPI.update_record(): e: {e}")  
    self.conn.commit()                     # commit changes
    self.close_conn()                      # close connection
   
  def process_uri(self):
    """
    Perform operation specified in env var QUERY_STRING 
    """
    operation, query_parms = self.parse_query_string()
    self.log.debug(f"ZlmaAPI.process_uri() operation: {operation} query_parms: {query_parms}")
    for i in range(len(query_parms)):      # uu-decode each element
      query_parms[i] = self.uu_decode(query_parms[i]) 
    if operation != "update" and query_parms != "": # query parameters => WHERE clause 
      where_clause = self.mk_where_clause(query_parms)
      self.log.debug(f"ZlmaAPI.process_uri() where_clause: {where_clause}")
    else:
      where_clause = "WHERE arch=\"s390x\"" # search only zLinux
    match operation:
      case "updateimg":
        self.update_image(query_parms)    # parms are hostname&newcpus&newmem
      case _:  
        print(f"unexpected: operation = {operation}")
        exit(1)    

# main()
zlma_rw_api = Zlma_rw_api()                # create a singleton
zlma_rw_api.process_uri()                  # process the request
