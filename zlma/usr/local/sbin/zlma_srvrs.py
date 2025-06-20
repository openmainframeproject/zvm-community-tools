#
# zlma_srvrs - get s390x server data from "zlma webdata" 
#
import logging
import os
import sys
import requests
sys.path.append('/usr/local/sbin')
from zlma_conf import Zlma_conf            # to read /etc/zlma.conf

class Zlma_srvrs:
  def __init__(self):
    self.conf = Zlma_conf()                # configuration variables
    self.conf.load_config_file()           # read the config file
    logging.basicConfig(filename='/var/log/zlma/zlma_srvrs.log', format='%(asctime)s %(levelname)s %(message)s')
    self.log = logging.getLogger(__name__)
    self.log.setLevel(self.conf.log_level)

  def get_srvrs(self):                     # get s390x server data
    """
    Get data from zlma, not restapi.py

    """
    cmd = "/usr/local/sbin/zlma webdata"
    try:
      proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    except Exception as e:
      print(f"search_cmdb(): Exception calling zlma: {e}")
      exit(3)
    rc = proc.returncode
    self.rows = []
    row_list = proc.stdout.splitlines()
    for next_row in row_list:
      list_row = next_row.split(",")
      self.rows.append(list_row)           # add list to list of rows
 
