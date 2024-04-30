from netmiko import ConnectHandler
import os

# Declare variables
deviceType = "cisco_ios"
subnet = "172.17.7." # Replace with your subnet
user = "cisco" # Replace with your username
password = "secret" # Replace with your password
secret = "secret" # Replace with your secret

configRouters = ".\configRouters.txt"
configSwitches = ".\configSwitches.txt"

def ConfigureRouters(device, configRouters):
    try:
        # Initialize the connection to the device
        net_connect = ConnectHandler(**device)
        net_connect.enable()

    # Read configuration commands from a file
        with open(configRouters, 'r') as file:
            config_commands = file.read().splitlines()
            
            # Send configuration commands to the device
            output = net_connect.send_config_set(config_commands)
            print("Configuration Output for device", device['host'], ":\n", output)

            # Sending the show command
            show_command = 'show running-config'
            output = net_connect.send_command(show_command)
            
            # Saving the output to a file
            filename = f"{device['host']}-running-config.txt"
            with open(filename, 'w') as file:
                file.write(output)
            print(f"The running configuration has been saved to {filename}")

            # Save the configuration
            net_connect.save_config()

            # Close the connection
            net_connect.disconnect()
    except Exception as e:
        print(f"Failed to process device {device['host']}: {e}")

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

if os.path.exists(configRouters): 
    for device in devices:
        ConfigureRouters(device, configRouters)

else: print(f"First make a configuration file named configRouters!")