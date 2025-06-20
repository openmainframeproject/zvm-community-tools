#
# zlma_conf - load the zlma configuration file
#
import json
import os

class Zlma_conf:
  def __init__(self):
    self.db_user = "root"                   # default database user
    self.db_pw = "pi"                       # default database password
    self.db_host = "127.0.0.1"              # default database host
    self.db_name = "zlma"                   # default database name
    self.home_dir = "/home/someuser"        # default home directory
    self.log_level = "INFO"                 # default log level
    self.user = os.getenv('USER')           # get USER env var

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
    self.db_user = confJSON['db_user']
    self.db_pw = confJSON['db_pw']
    self.db_host = confJSON['db_host']
    self.db_name = confJSON['db_name']
    self.home_dir = confJSON['home_dir']
    self.log_level = confJSON['log_level'].upper()

