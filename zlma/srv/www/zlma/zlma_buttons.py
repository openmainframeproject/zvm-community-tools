#!/srv/venv/bin/python3
#
# zlmabuttons.py - action buttons common to all zlma pages:
#                'commands', 'consoles', 'finder', 'vif', 'help'
#
class Zlma_buttons:
  def __init__(self, page: str):
    """
    draw buttons common to zlma pages in a table
    """
    self.green="style=\"background-color:#8CFF66\""
    self.yellow="style=\"background-color:#FFDB4D\""

    self.html = '<br><table align=center border="0" cellpadding="0" cellspacing="0"><tr>\n' # start a table
    self.html += "<td><form action='/zlmarw/cpcmds.py' accept-charset=utf-8>"
    self.html += f"<button class=button {self.green}>Commands</button>&nbsp; "
    self.html += "</form></td>\n"

    self.html += "<td><form action='/zlmarw/consolez.py' accept-charset=utf-8>"
    self.html += f"<button class=button {self.green}>Consoles</button>&nbsp; "
    self.html += "</form></td>\n" 

    self.html += "<td><form action='/zlma/finder.py' accept-charset=utf-8>"
    self.html += f"<button class=button {self.green}>Finder</button>&nbsp; "
    self.html += "</form></td>\n" 

    self.html += "<td><form action='/zlmarw/vif.py' accept-charset=utf-8>"
    self.html += f"<button class=button {self.green}>Vif</button>&nbsp; "
    self.html += "</form></td>\n"

    self.html += f"<td><a href='https://github.com/mike99mac/zlma#{page}' target='_blank'> "
    self.html += f"<button class=button {self.yellow}>Help</button><br>"
    self.html += "</a></td></tr></table><br>\n" 

    print(self.html)

# main()
# nothing to do?

