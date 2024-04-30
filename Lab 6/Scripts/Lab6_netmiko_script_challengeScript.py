import logging
from netmiko import ConnectHandler
from datetime import datetime

# Setup basic logging
logging.basicConfig(filename='network_health.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Device List and Credentials
devices = [
    {'device_type': 'cisco_ios', 'host': '192.168.1.1', 'username': 'admin', 'password': 'admin123', 'secret': 'secret123'},
    {'device_type': 'cisco_ios', 'host': '192.168.1.2', 'username': 'admin', 'password': 'admin123', 'secret': 'secret123'}
]

# Command to Check CPU and Memory Utilization
commands = ['show processes cpu', 'show memory']

def check_device_health(device):
    """ Function to check device health and log if any thresholds are exceeded """
    try:
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()
            for command in commands:
                output = net_connect.send_command(command)
                # Dummy check: Log if 'CPU' or 'memory' in output, this should be replaced with actual logic
                if 'CPU' in output or 'memory' in output:
                    logging.warning(f"High utilization detected on {device['host']}: {output[:100]}")  # log first 100 chars
    except Exception as e:
        logging.error(f"Failed to connect to {device['host']}: {e}")

# Main routine to check each device
def main():
    for device in devices:
        check_device_health(device)

if __name__ == "__main__":
    main()