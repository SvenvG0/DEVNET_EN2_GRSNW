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

# Read configuration commands from a file
with open('config_commands.txt', 'r') as file:
    config_commands = file.read().splitlines()

for device in devices:
    # Initialize the connection to the device
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    # Send configuration commands to the device
    output = net_connect.send_config_set(config_commands)
    print("Configuration Output:")
    print(output)

    # Sending the show command
    show_command = 'show running-config'
    output = net_connect.send_command(show_command)
    
    # Saving the output to a file
    filename = f"{device['ip']}-running-config.txt"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"The output has been saved to {filename}")

    # Save the configuration
    net_connect.save_config()

    # Close the connection
    net_connect.disconnect()