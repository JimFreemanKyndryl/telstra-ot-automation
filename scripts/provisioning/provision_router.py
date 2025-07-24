#!/usr/bin/env python3
"""
Router Provisioning Script
Automates the configuration of new Cisco/Juniper routers
"""

import json
import logging
from netmiko import ConnectHandler
from jinja2 import Template
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RouterProvisioner:
    def __init__(self, device_info, template_path):
        self.device_info = device_info
        self.template_path = template_path
        
    def load_template(self):
        """Load Jinja2 template for router configuration"""
        with open(self.template_path, 'r') as f:
            return Template(f.read())
    
    def generate_config(self, parameters):
        """Generate configuration from template"""
        template = self.load_template()
        return template.render(**parameters)
    
    def connect_device(self):
        """Establish SSH connection to device"""
        device = {
            'device_type': self.device_info['vendor'],
            'ip': self.device_info['ip'],
            'username': self.device_info['username'],
            'password': self.device_info['password'],
            'port': self.device_info.get('port', 22)
        }
        return ConnectHandler(**device)
    
    def provision(self, config_params):
        """Main provisioning workflow"""
        try:
            # Generate configuration
            logger.info(f"Generating config for {self.device_info['hostname']}")
            config = self.generate_config(config_params)
            
            # Connect to device
            logger.info("Connecting to device...")
            connection = self.connect_device()
            
            # Backup current config
            logger.info("Backing up current configuration...")
            backup = connection.send_command("show running-config")
            
            # Apply new configuration
            logger.info("Applying configuration...")
            output = connection.send_config_set(config.split('\n'))
            
            # Save configuration
            logger.info("Saving configuration...")
            connection.save_config()
            
            # Verify
            logger.info("Verifying configuration...")
            # Add verification logic here
            
            connection.disconnect()
            logger.info("Provisioning completed successfully!")
            
            return True
            
        except Exception as e:
            logger.error(f"Provisioning failed: {str(e)}")
            return False

if __name__ == "__main__":
    # Example usage
    device = {
        'hostname': 'router-syd-001',
        'ip': '10.0.1.1',
        'vendor': 'cisco_xr',
        'username': 'admin',
        'password': 'secure_password'
    }
    
    params = {
        'hostname': 'router-syd-001',
        'management_ip': '10.0.1.1',
        'bgp_as': '64512',
        'snmp_community': 'telstra-ro'
    }
    
    provisioner = RouterProvisioner(device, 'templates/cisco_xr.j2')
    provisioner.provision(params)
