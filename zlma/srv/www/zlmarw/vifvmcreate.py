#!/usr/bin/env python3
import cgi
import html
import subprocess
import sys
sys.path.append('/srv/www/zlma')
from zlma_buttons import Zlma_buttons

class VifVmCreate:
    def __init__(self):
        self.title = "zlma vif - Create VM"
        
    def create_form_page(self):
        """Create a form page to collect VM creation parameters"""
        print('Content-Type: text/html')
        print()
        print('<!DOCTYPE html>')  
        print(f'<html><head><title>{self.title}</title>')
        print('<link rel="icon" type="image/png" href="/zlma.ico">')
        print('<link rel="stylesheet" href="/zlma.css">')
        print('<script>')
        print('''
        function validateForm() {
            const vmName = document.getElementById('vm_name').value.trim();
            const arch = document.getElementById('architecture').value;
            
            if (!vmName) {
                alert('VM name is required');
                return false;
            }
            
            if (vmName.length > 8) {
                alert('VM name must be 8 characters or less (z/VM limitation)');
                return false;
            }
            
            if (!/^[A-Za-z0-9]+$/.test(vmName)) {
                alert('VM name can only contain letters and numbers');
                return false;
            }
            
            if (arch === 'intel') {
                alert('Intel architecture is not yet supported. Please select s390x.');
                return false;
            }
            
            return true;
        }
        ''')
        print('</script>')
        print('</head><body>')
        
        zlma_buttons = Zlma_buttons("using-vif")
        
        print(f'<h2>{self.title}</h2>')
        print('<form action="/zlmarw/vifvmcreate.py" method="post" accept-charset="utf-8" onsubmit="return validateForm()">')
        print('<input type="hidden" name="action" value="create">')
        
        print('<table id="zlma-table">')
        print('<thead><tr><th colspan="2">VM Creation Parameters</th></tr></thead>')
        print('<tbody>')
        
        # VM Name (required)
        print('<tr>')
        print('<td><label for="vm_name">VM Name:</label></td>')
        print('<td>')
        print('<input type="text" id="vm_name" name="vm_name" required placeholder="Enter VM name (max 8 chars)" maxlength="8" pattern="[A-Za-z0-9]+">')
        print('<br><small>Only letters and numbers, max 8 characters (z/VM limitation)</small>')
        print('</td>')
        print('</tr>')
        
        # Architecture Selector
        print('<tr>')
        print('<td><label for="architecture">Architecture:</label></td>')
        print('<td>')
        print('<select id="architecture" name="architecture" required>')
        print('<option value="s390x" selected>s390x (IBM Z)</option>')
        print('<option value="intel" disabled style="color: #999;">Intel x86_64 (Not supported yet)</option>')
        print('</select>')
        print('</td>')
        print('</tr>')
        
        # CPU Count
        print('<tr>')
        print('<td><label for="cpus">CPU Count:</label></td>')
        print('<td>')
        print('<select id="cpus" name="cpus" required>')
        print('<option value="1" selected>1 CPU</option>')
        print('<option value="2">2 CPUs</option>')
        print('<option value="3">3 CPUs</option>')
        print('<option value="4">4 CPUs</option>')
        print('</select>')
        print('</td>')
        print('</tr>')
        
        # Memory Size
        print('<tr>')
        print('<td><label for="memory">Memory:</label></td>')
        print('<td>')
        print('<select id="memory" name="memory" required>')
        print('<option value="512">512 MB</option>')
        print('<option value="1024" selected>1 GB (1024 MB)</option>')
        print('<option value="2048">2 GB (2048 MB)</option>')
        print('<option value="3072">3 GB (3072 MB)</option>')
        print('<option value="4096">4 GB (4096 MB)</option>')
        print('</select>')
        print('</td>')
        print('</tr>')
        
        # Image Selector (hardcoded for now)
        print('<tr>')
        print('<td><label for="image">Base Image:</label></td>')
        print('<td>')
        print('<select id="image" name="image" required>')
        print('<option value="sles15sp6-minimal" selected>SLES 15 SP6 Minimal</option>')
        print('</select>')
        print('<br><small>Currently only SLES 15 SP6 Minimal is available</small>')
        print('</td>')
        print('</tr>')
        
        # Action buttons
        print('<tr>')
        print('<td colspan="2" style="text-align: center; padding-top: 20px;">')
        print('<button type="submit" class="button green-button">Create VM</button>')
        print('&nbsp;&nbsp;')
        print('<button type="button" class="button red-button" onclick="window.close()">Cancel</button>')
        print('</td>')
        print('</tr>')
        
        print('</tbody></table>')
        print('</form>')
        print('</body></html>')
    
    def process_creation(self, form_data):
        """Process the VM creation request by calling VIF"""
        vm_name = form_data.getvalue('vm_name', '').strip().upper()
        cpus = form_data.getvalue('cpus', '1')
        memory = form_data.getvalue('memory', '1024')
        architecture = form_data.getvalue('architecture', 's390x')
        image = form_data.getvalue('image', 'sles15sp6-minimal')
        
        if not vm_name:
            self.show_error("VM name is required")
            return
            
        # Build the VIF command with parameters
        vif_cmd = [
            '/usr/local/sbin/vif',
            'vm', 'create', vm_name,
            '--cpus', cpus,
            '--memory', memory,
            '--architecture', architecture,
            '--image', image
        ]
        
        # Execute the VIF command and show results
        self.execute_vif_command(vif_cmd, vm_name, {
            'cpus': cpus,
            'memory': memory,
            'architecture': architecture,
            'image': image
        })
    
    def execute_vif_command(self, vif_cmd, vm_name, config):
        """Execute the VIF command and show results"""
        print('Content-Type: text/html')
        print()
        print('<!DOCTYPE html>')
        print(f'<html><head><title>{self.title} - Results</title>')
        print('<link rel="icon" type="image/png" href="/zlma.ico">')
        print('<link rel="stylesheet" href="/zlma.css">')
        print('</head><body>')
        
        zlma_buttons = Zlma_buttons("using-vif")
        
        print(f'<h2>Creating VM: {html.escape(vm_name)}</h2>')
        
        # Display configuration summary
        print('<div class="vm-config-summary">')
        print('<h3>VM Configuration:</h3>')
        print('<ul>')
        print(f'<li><strong>Name:</strong> {html.escape(vm_name)}</li>')
        print(f'<li><strong>Architecture:</strong> {html.escape(config["architecture"])}</li>')
        print(f'<li><strong>CPUs:</strong> {html.escape(config["cpus"])}</li>')
        print(f'<li><strong>Memory:</strong> {html.escape(config["memory"])}MB ({int(config["memory"])/1024:.1f}GB)</li>')
        print(f'<li><strong>Base Image:</strong> {html.escape(config["image"])}</li>')
        print('</ul>')
        print('</div>')
        
        print('<div class="command-output">')
        print(f'<p><strong>Executing:</strong> <code>{html.escape(" ".join(vif_cmd))}</code></p>')
        
        try:
            # Execute the VIF command
            result = subprocess.run(vif_cmd, capture_output=True, text=True, timeout=120)
            
            print('<pre class="output">')
            if result.stdout:
                print(html.escape(result.stdout))
            if result.stderr:
                print('<span class="error">')
                print(html.escape(result.stderr))
                print('</span>')
            print('</pre>')
            
            if result.returncode == 0:
                print('<p class="success">✓ VM creation completed successfully!</p>')
            else:
                print(f'<p class="error">✗ Command failed with return code: {result.returncode}</p>')
                
        except subprocess.TimeoutExpired:
            print('<p class="error">✗ Command timed out after 2 minutes</p>')
        except Exception as e:
            print(f'<p class="error">✗ Error executing command: {html.escape(str(e))}</p>')
        
        print('</div>')
        
        print('<div style="margin-top: 20px; text-align: center;">')
        print('<button onclick="window.close()" class="button">Close Window</button>')
        print('&nbsp;&nbsp;')
        print('<button onclick="window.opener.location.reload(); window.close()" class="button green-button">Refresh & Close</button>')
        print('</div>')
        
        print('</body></html>')
    
    def show_error(self, message):
        """Show an error message"""
        print('Content-Type: text/html')
        print()
        print('<!DOCTYPE html>')
        print(f'<html><head><title>{self.title} - Error</title>')
        print('<link rel="icon" type="image/png" href="/zlma.ico">')
        print('<link rel="stylesheet" href="/zlma.css">')
        print('</head><body>')
        
        zlma_buttons = Zlma_buttons("using-vif")
        
        print(f'<h2>Error</h2>')
        print(f'<p class="error">✗ {html.escape(message)}</p>')
        print('<p><button onclick="history.back()" class="button">Go Back</button></p>')
        print('</body></html>')

# Main execution
if __name__ == "__main__":
    vif_vm_create = VifVmCreate()
    
    # Check if this is a POST request (form submission)
    form = cgi.FieldStorage()
    action = form.getvalue('action', '')
    
    if action == 'create':
        vif_vm_create.process_creation(form)
    else:
        vif_vm_create.create_form_page()