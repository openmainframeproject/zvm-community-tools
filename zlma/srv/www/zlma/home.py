#!/srv/venv/bin/python3
"""
home.py - The zlma home page 
"""
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class Zlma_home:
  def __init__(self):
    """
    Initialize globals, create page header, set background
    """
    self.title = "zlma home page"
    print('Content-Type: text/html')       # start the HTML page
    print()
    print('<!DOCTYPE html>')  
    print(f'<html><head><title>{self.title}</title>')
    print('<link rel="icon" type="image/png" href="/zlma.ico">')
    print('<link rel="stylesheet" href="/zlma.css">') # common CSS's
    print('</head><body>') 

  def create_page(self):                   # create body of page
    zlma_buttons = Zlma_buttons("using-zlma") # add navigation buttons
    print(f'<h2>{self.title}</h2>')
    html = "<table id='zlma-table'><tr><td>"  # start table then add headers
    html += '<p><b><span style="font-size: 1.2em;">z/VM and Linux Modern Administration</span></b> (<b>zlma</b>) enables Linux servers on z/VM to be managed in a more modern fashion.</p>\n'
    html += "<p>Navigation is simple - use the 5-button menu at the top of each page (see above):</p>\n" 
    html += '<ul><li><span style="color:green"><b>Commands</b></span> - run z/VM comands</li>\n' 
    html += '<li><span style="color:green"><b>Consoles</b></span> - View and manage z/VM console data</li>\n' 
    html += '<li><span style="color:green"><b>Finder</b></span> - search the configuration management database (CMDB)</li>\n' 
    html += '<li><span style="color:green"><b>VIF</b></span> - The Virtual Image Facility abstracts z/VM function</li>\n' 
    html += '<li><span style="color:#F6BE00"><b>Help</b></span> - Get topic-specific documentation in a new tab</li>\n' 
    html += "</ul></td></tr></table>\n"
    html += '<table><tr><td align="center"><figure><img src="/zlma256.ico" alt="zlma icon image"></figure></td></tr></table>\n'
    html += "</body></html>"               # end page
    print(html)

# main()
zlma_home = Zlma_home()                    # create a singleton
zlma_home.create_page()                    # create main page 
