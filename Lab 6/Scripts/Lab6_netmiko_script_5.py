from netmiko import ConnectHandler
# Declare variables
deviceType = "cisco_ios"
subnet = "172.17.7." # Replace with your subnet
user = "cisco" # Replace with your username
password = "secret" # Replace with your password
secret = "secret" # Replace with your secret

# Define the device parameters
R01 = {
    'device_type': f"{deviceType}",
    'ip': f"{subnet}66",  # Last numbers depending on device
    'username': f"{user}", 
    'password': f"{password}",
    'secret': f"{secret}",
}

R02 = {
        'device_type': f"{deviceType}",
        'ip': f"{subnet}67",  # Last numbers depending on device
        'username': f"{user}", 
        'password': f"{password}",
        'secret': f"{secret}",
}

devices = R01, R02
for device in devices:
    # Initialize the connection to the device
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    # List of configuration commands
    config_commands = [
        'interface GigabitEthernet 0/0/0',
        'description Connected to Internal switch',
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