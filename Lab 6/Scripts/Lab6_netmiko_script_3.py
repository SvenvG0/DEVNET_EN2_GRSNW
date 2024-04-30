from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '172.17.7.68',  # Replace with your device's IP address
    'username': 'cisco',  # Replace with your username
    'password': 'secret',  # Replace with your password
    'secret': 'secret'  # Replace with your enable secret if needed
}

# Initialize the connection to the device
net_connect = ConnectHandler(**device)
net_connect.enable()

# List of configuration commands
config_commands = [
    'interface GigabitEthernet 1/0/20',
    'description Connected to R01',
    'no shutdown'
]

# Send configuration commands to the device
output = net_connect.send_config_set(config_commands)
print("Configuration Output:")
print(output)

# Save the configuration
net_connect.save_config()

# Close the connection
net_connect.disconnect()