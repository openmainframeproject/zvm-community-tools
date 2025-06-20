#!/srv/venv/bin/python3
"""
Note the above "shebang" - this must be run from virtual environment /srv/venv/

restapi.py - the zlma RESTful API - accesses the table 'servers' in the mariadb database 'zlma'.
Format: http://<hostname>/restapi.py?<operation>&param1&param2 ...

Input:
Operation   Return                              Parameters
---------   ------                              ----------
- active    Number of servers that ping         <col>=<value>&...
- count     Number of servers                   <col>=<value>&...
- hostname  Host names of servers               <col>=<value>&...
- ping      Servers pinged out of total         <col>=<value>&...
- query     All server data                     <col>=<value>&...
- update    Update server's env/app/grp/owner   hostname&app&env&grp&owner
- webdata   host_name, lpar, userid, ip_addr, cpus, mem_gb          

Output: JSON

Examples: 
http://<server>/restapi.py?update&model1000&myApp&myGroup&myOwner => update metadata in "servers" table
http://<server>/restapi.py?count => { "num_servers": 4 }
http://<server>/restapi.py?count&cpus=4&mem_gb=4 => number of servers with 4 CPUs and 4 GB of memory
http://<server>/restapi.py?hostname => {"servers": ["model1000", "model1500", "model2000", "model800"]}
http://<server>/restapi.py?hostname&cpus<4 => host names of servers with fewer than 4 CPUs
http://<server>/restapi.py?linuxip => {"servers": ["z-graf1", "10.1.1.1"], ["z-graf2", "10.1.1.2"]]}
http://<server>/restapi.py?ping => { "up_servers": 3, "num_servers": 4 }
"""
import base64
import json
import logging
import mariadb
import os
import re
import subprocess
from urllib.parse import urlparse, parse_qs

class ZlmaAPI():
  def __init__(self):
    logging.basicConfig(filename='/var/log/zlma/restapi.log', format='%(asctime)s %(levelname)s %(message)s')
    self.log = logging.getLogger(__name__)
    self.conn = None 
    self.cursor = None 
    self.db_user = "none"
    self.db_pw = "none"  
    self.db_host = "none"
    self.db_name = "none"
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

  def print_env(self):
    """
    Show all environment variables with the 'env' command
    """
    proc = subprocess.run("env", shell=True, capture_output=True, text=True)
    rc = proc.returncode
    env_vars = []
    env_vars = proc.stdout
    print("<pre>")
    for line in env_vars.split("\n"):
      print(str(line))
    print("</pre>")
    print("")

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
    self.log_level = confJSON['log_level'].upper()

  def connect_to_cmdb(self):
    """
    Connect to mariadb, use datase cmdb and establish a cursor
    """
    try:
      self.conn = mariadb.connect(user=self.db_user, password=self.db_pw, host=self.db_host, database=self.db_name)
      self.cursor = self.conn.cursor(dictionary=True) # open cursor returning dictionary
    except mariadb.Error as e:
      self.log.error(f"initialize(): Exception creating database: {e}")
      exit(3)

  def run_sql_query(self, cmd: str) -> str:
    """
    run the SQL command passed in
    """
    self.log.info(f"ZlmaAPI.run_sql_query(): using database: {self.db_name}")
    self.connect_to_cmdb()                 # connect to DB
    try:   
      self.cursor.execute(f"use {self.db_name}")
    except mariadb.Error as e:
      print(f"ERROR changing database to {self.db_name}: {e}")
      print("</body></html>")
      self.conn.close()                    # cannot contiue
      exit(1)
    rows = "" 
    json_out = ""
    self.log.info(f"ZlmaAPI.run_sql_query(): running cmd: {cmd}") 
    try:   
      self.cursor.execute(cmd)             # query the cmdb
      rows = self.cursor.fetchall()
    except mariadb.Error as e:
      self.log.error(f"ZlmaAPI.run_sql_query(): ERROR! e: {e}")  
    # print(f"rows: {rows}")
    json_out = json.dumps(rows, indent=2)
    return json_out  

  def close_conn(self):
    """
    Close the SQL cursor, then the connection 
    """
    self.cursor.close()
    self.conn.close()

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

  def ping_servers(self, where_clause: str) -> str:
    """
    ping specified servers and return how many servers ping out of how many found 
    """
    sql_cmd = f"SELECT host_name FROM servers {where_clause}"
    sql_out = self.run_sql_query(sql_cmd)  # list of server host names
    sql_json = json.loads(sql_out)
    self.log.debug(f"ping_servers() sql_json: {sql_json}")
    self.close_conn()
    self.log.info(f"ZlmaAPI.ping_servers(): sql_out:  {sql_out} type(sql_out) = {type(sql_out)}")
    up_servers = 0
    num_servers = 0
    if sql_out == "":                      # no records found
      self.log.debug(f"ZlmaAPI.ping_servers(): no records found")
    else:                                  # ping servers
      for entry in sql_json:
        next_server = entry["host_name"]
        self.log.debug(f"ZlmaAPI.ping_servers(): next_server = {next_server}")
        num_servers += 1 
        proc = subprocess.run(f"ping -c1 -w1 {next_server}", shell=True, capture_output=True, text=True)     
        if proc.returncode == 0:                            # server pings
          up_servers += 1
    self.log.debug(f"ZlmaAPI.ping_servers(): up_servers: {up_servers} num_servers: {num_servers}")
    return ('{"up_servers": '+str(up_servers)+', "num_servers": '+str(num_servers)+'}') # return JSON

  def uu_decode(self, url):
    """ 
    Decode a uu-encoded URL (have absolutely no idea how this works, but it does :))
    """
    return re.compile('%([0-9a-fA-F]{2})',re.M).sub(lambda m: chr(int(m.group(1),16)), url)

  def mk_where_clause(self, query_parms: list) -> str:
    """ 
    Construct an SQL WHERE clause from search parameters passed in 
    Return: constructed WHERE clause
    """
    where_clause = "WHERE arch=\"s390x\"" # search only zLinux
    for next_word in query_parms:       # add search criteria to the WHERE clause
      self.log.debug(f"ZlmaAPI.mk_where_clause() next_word: {next_word}")
      next_list = next_word.split("=")
      if len(next_list) == 2:            # '=' found
        attr = next_list[0]
        # if column is a string, escape with double quotes
        if attr != "cpus" and attr != "mem_gb": 
          value = next_list[1]
          next_word = f"{attr} LIKE \"%{value}%\""
      where_clause = f"{where_clause} AND {next_word}"
    self.log.debug(f"ZlmaAPI.mk_where_clause(): where_clause: {where_clause}")
    return where_clause

  def count_servers(self, where_clause: str) -> str:
    """ 
    Send SQL command to count servers  
    Return: JSON output
    """
    sql_cmd = f"SELECT COUNT(host_name) FROM servers {where_clause}"
    self.log.debug(f"ZlmaAPI.count_servers(): sql_cmd: {sql_cmd}")
    sql_out = self.run_sql_query(sql_cmd)
    self.log.debug(f"count_servers() sql_out: {sql_out}")
    self.close_conn()
    return sql_out

  def get_host_names(self, where_clause: str) -> str:
    """
    Send SQL command to return hostnames of specified search
    Return: list of servers
    """
    sql_cmd = f"SELECT host_name FROM servers {where_clause}"
    self.log.debug(f"ZlmaAPI.get_host_names(): hostname sql_cmd: {sql_cmd}")
    sql_out = self.run_sql_query(sql_cmd)
    self.close_conn()
    self.log.debug(f"ZlmaAPI.get_host_names(): sql_out: {sql_out}")
    return sql_out

  def get_webdata(self, where_clause: str) -> str:
    """
    Send SQL command to return host_name, lpar, userid, ip_addr, cpus, mem_gb of specified servers
    Return: list of servers
    """
    sql_cmd = f"SELECT host_name, lpar, userid, ip_addr, cpus, mem_gb FROM servers {where_clause}"
    self.log.debug(f"ZlmaAPI.get_webdata(): sql_cmd: {sql_cmd}")
    sql_out = self.run_sql_query(sql_cmd)
    self.close_conn()
    self.log.debug(f"ZlmaAPI.get_webdata(): sql_out: {sql_out}")
    
    # Convert tuples to a list of dictionaries
    keys = ["host_name", "lpar", "userid", "ip_addr", "cpus", "mem_gb"]
    sql_json = [dict(zip(keys, row)) for row in sql_out]  # Build list of dictionaries
    #try:
    #  sql_json = json.loads(sql_out)          # convert to list of dictionaries
    #except json.JSONDecodeError as e:
    #  self.log.error("Failed to decode JSON: ", e)
    #  sql_json = []
    #return sql_json 
    return json.dumps(sql_json)  # Convert list of dictionaries to JSON string

  def get_linux_ips(self, where_clause: str) -> str:
    """
    Send SQL command to return host names and IP addresses 
    Return: list of servers
    """
    sql_cmd = f"SELECT host_name, ip_addr FROM servers {where_clause}"
    self.log.debug(f"ZlmaAPI.get_linux_ips(): hostname sql_cmd: {sql_cmd}")
    sql_out = self.run_sql_query(sql_cmd) 
    self.close_conn()
    self.log.debug(f"ZlmaAPI.get_linux_ips(): sql_out: {sql_out}")
    return sql_out

  def get_records(self, where_clause: str) -> str:
    """
    Send SQL command to return hostnames of specified search
    Return: JSON output
    """
    sql_cmd = f"SELECT * FROM servers {where_clause}"
    self.log.debug(f"ZlmaAPI.get_records(): query sql_cmd: {sql_cmd}")
    sql_out = self.run_sql_query(sql_cmd) 
    self.close_conn()
    return sql_out  

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
      case "count":                        # number of servers in table
        json_out = self.count_servers(where_clause)
        print(json_out)
      case "hostname":                     # all host names in table
        json_out = self.get_host_names(where_clause)
        print(json_out)
      case "linuxips":                     # all host names in table
        json_out = self.get_linux_ips(where_clause)
        print(json_out)
      case "ping":
        json_out = self.ping_servers(where_clause)
        print(json_out)
      case "query":                        # all rows in table
        json_out = self.get_records(where_clause)
        print(json_out)
      case "update":
        self.update_record(query_parms)    # parms are hostname&newEnv&newApp&newGroup&newOwner
      case _:  
        print(f"unexpected: operation = {operation}")
        exit(1)    

# main()
zlmaAPI = ZlmaAPI()          # create a singleton
# zlmaAPI.print_env()             # show env vars when debugging
zlmaAPI.process_uri()             # process the request
