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

# Send a show command
output = net_connect.send_command('show version')
print(output)

# Close the connection
net_connect.disconnect()