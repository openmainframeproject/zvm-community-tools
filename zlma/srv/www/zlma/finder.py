#!/srv/venv/bin/python3
import os 
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Finder:
  def __init__(self):
    """
    Initialize globals, create page header, set background
    """
    self.pattern = ""                      # search pattern
    self.rows = []                         # resulting rows
    self.headers = ['Host name', 'LPAR', 'User ID', 'IP address', 'CPUs', 'GB Mem', 'Arch', 'Common arch', 'OS', 'OS ver', 'Kernel ver', 'Kernel rel', 'RootFS % full', 'Last ping', 'Created', 'App', 'Env', 'Group', 'Owner']
    self.title = "zlma finder search"

    # start the HTML page
    print('Content-Type: text/html')
    print()
    print('<!DOCTYPE html>')  
    print(f'<html><head><title>{self.title}</title>')

    # include javascript libraries to make table editable
    print('<script type="text/javascript" src="/jquery-3.7.1.slim.min.js"></script>')
    print('<script type="text/javascript" src="/bootstable.js"></script>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">') # common CSS's
    print('<link rel="stylesheet" href="/glyphicons-free.css">')   
    print('</head><body>') 
    zlma_buttons = Zlma_buttons("using-finder")  # add navigation buttons

  def print_env(self):
    """
    Show all environment variables with the 'env' command
    """
    proc = subprocess.run("env", shell=True, capture_output=True, text=True)
    rc = proc.returncode
    env_vars = []
    env_vars = proc.stdout
    print('<pre>')
    for line in env_vars.split("\n"):
      print(str(line))
    print('</pre>')
    print()

  def search_cmdb(self):
    """
    Search zlma for pattern if included, else get all records
    """
    cmd = "/usr/local/sbin/zlma query"
    if len(self.pattern) > 1:              # search pattern specified
      cmd = f"{cmd} -p {self.pattern}"     # add -p <pattern> flag
    # print(f"search_cmdb() cmd: {cmd}<br>")
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

  def create_table(self, headers, data):
    """
    Given a list of table headers, and table data, produce an HTML table
    """
    html = "<table id='zlma-table'>\n" 
    html += "<tr>\n"
    for aHeader in headers:
      html += "  <th>"+aHeader+"</th>\n"
    html += "</tr>\n"
    for row in data:
      html += "<tr>\n"
      for cell in row:
        html += f"  <td>{cell}</td>\n"
      html += "</tr>\n"
    html += "</table>"
    return html

  def update_all(self):
    """
    Update all zlma records 
    """
    cmd = "/usr/local/sbin/zlma update"
    try:
      proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    except Exception as e: 
      print(f"update_all(): Exception calling zlma: {e}")
      exit(3)

  def process_query(self):
    """
    Perform operation specified in env var QUERY_STRING.  There are two formats:
    - pattern=<pattern>
    - action=update
    """
    print(f'<h2>{self.title}</h2>')
    proc = subprocess.run("echo $QUERY_STRING", shell=True, capture_output=True, text=True)
    rc = proc.returncode
    if rc != 0:
      print(f"Finder.process_query(): subprocess.run('echo $REQUEST_URI' returned {rc}")
      return 1
    query = []
    query = proc.stdout                    # get value
    query = query.split("=")
    verb = query[0]
    if verb == "action":                   # "update all" is only action
      self.update_all()
    else:                                  # assume pattern
      query_len = len(query)
      if query_len < 2:                    # no search pattern supplied
        self.pattern = ""                  # search for all
      else: 
        self.pattern = str(query[1])
    self.search_cmdb()                     # do search
    
    # print(f'<p> query: {query}<br>')
    # show the search pattern text box and submit button
    print('<form action="/finder.py" method="get" enctype="multipart/form-data">')
    print('  Search pattern: <input maxlength="60" size="60" value="" name="pattern">')
    print('  <input value="Submit" class="button green-button" type="submit">')
    print('</form><br>')

    # show the current search pattern if one exists
    if len(self.pattern) > 1:              # there is a current search pattern
      print(f"Current search pattern: {self.pattern}<br><br>") 
    print(self.create_table(self.headers, self.rows))

    # make the table editable
    print('<script>')
    print('$("#zlma-table").SetEditable({columnsEd: "15,16,17,18", onEdit:function(){}})')
    print('</script>')
    print('</body></html>')                # end page

# main()
finder = Finder()                          # create a singleton
# finder.print_env() 
finder.process_query()                     # process the request
