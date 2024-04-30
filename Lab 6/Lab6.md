# Lab 6: Python Network automation with netmiko
## Part 1: Connecting to a single iOS device

During this exercise we'll build on a single script to test multiple functionalities.
The scripts are provided with extra commentary to clarify each step and the additions we made.

### Requirements

```Powershell
pip install netmiko
```

### Sending single show command

```python
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
```

Save this script as `Lab6_netmiko_script_1.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_1.py
```

### Sending multiple show commands

Now do the same again by using an extended version of the previous script.
>[!Note]
> Notice the addition with the comment `Send multiple show commands and print outputs`

```python
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

# List of show commands
commands = ['show version', 'show interfaces', 'show ip interface brief']

# Send multiple show commands and print outputs
for command in commands:
    output = net_connect.send_command(command)
    print(f"Output of {command}:")
    print(output)
    print("-" * 40)  # Just a separator for better readability

# Close the connection
net_connect.disconnect()
```
Save this script as `Lab6_netmiko_script_2.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_2.py
```

### Send multiple configuration commands to a single device

Let's do it again with another extended version.

>[!Note]
> Notice the addition with the comment `Send configuration commands to the device`

```python
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
```
Save this script as `Lab6_netmiko_script_3.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_3.py
```

## Part 2 & 3: Connect to multiple IOS devices

Now that we have learned to connect to a single device and run show commands and configuration commands, we can easily begin to transmit the same information to multiple devices.

How are we going to do this?
- Define the devices in a dictionary per device
- Set variables for common values
- Create functions to call upon

### Send show commands to multiple devices

```python
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

    # Send a show command
    output = net_connect.send_command('show version')
    print(output)

    # Close the connection
    net_connect.disconnect()
```

Save this script as `Lab6_netmiko_script_4.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_4.py
```

### Send configuration commands to multiple devices

```python
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
```

Save this script as `Lab6_netmiko_script_5.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_5.py
```


### Run show commands and save the output & Backup the device configurations

We combine the next exercises because we can create a back-up by showing the running configuration.
For both exercises we would save the output.

```python
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

    # Sending the show command
    show_command = 'show running-config'
    output = net_connect.send_command(show_command)
    # Saving the output to a file
    filename = "running-config.txt"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"The output has been saved to {filename}")

    # Save the configuration
    net_connect.save_config()

    # Close the connection
    net_connect.disconnect()
```

Save this script as `Lab6_netmiko_script_6.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_6.py
```

### Configure a subset of Interfaces

As we configured a interface in script 5, we now target multiple interfaces.
We can do this by using a range or configuring multiple interfaces after eachother.
In this script we'll use the second option, but feel free to try the range.

```python
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
        'no shutdown',
        'interface GigabitEthernet 0/0/1',
        'description Connected to external switch',
        'no shutdown'
    ]

    # Send configuration commands to the device
    output = net_connect.send_config_set(config_commands)
    print("Configuration Output:")
    print(output)

    # Sending the show command
    show_command = 'show running-config'
    output = net_connect.send_command(show_command)
    # Saving the output to a file
    filename = "running-config.txt"
    with open(filename, 'w') as file:
        file.write(output)
    print(f"The output has been saved to {filename}")

    # Save the configuration
    net_connect.save_config()

    # Close the connection
    net_connect.disconnect()
```

Save this script as `Lab6_netmiko_script_7.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_7.py
```

### Send device configuration using an external file

Instead of hardcoding the configuration, we can make a configuration file that contains all the configuration commands.
We alter the script to read the commands out of this file.

- First create a `configuration_commands.txt` file with the following content:

```
interface GigabitEthernet0/0/0
description Connected to Internal switch
no shutdown
interface GigabitEthernet0/0/1
description Connected to External switch
no shutdown
```
- Next alter the script:
```python
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
```
>[!Note]
>Notice we also changed the part where we save the output to a file. Otherwise the usage on multiple device would overide the file because of the static name.

Save this script as `Lab6_netmiko_script_8.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_8.py
```

### Connect using a Python Dictionary

We are not going to make a separate script for this exercise, cause we have already used a dictionary in the previous scripts.
If you really want, you can still try to optimize the dictionary for multiple devices.

### Execute a script with a Function or classes

```python
from netmiko import ConnectHandler
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

for device in devices:
    ConfigureRouters(device, configRouters)

```

>[!Note]
> We just put the whole part of the connection and configuration into a function and call upon the function per device. We also made some extra variables so we can be more flexible.

Save this script as `Lab6_netmiko_script_9.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_9.py
```

### Execute a script with a statements (if, ifelse, else)

```python
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

```

>[!Note]
> We'll check if the configuratin file exists before using the function. Otherwise a text will appear on the screen asking to create the configuration file.

Save this script as `Lab6_netmiko_script_Final.py` and run it.

```powershell
python.exe .\Lab6_netmiko_script_Final.py
```

This will be the final version of the script based on Part 2 and 3.

## Part 4: Create an challenging excited script as a network 

We will make a standarized script that can be altered based on different situations.

```Python
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
```

>[!Important]
>This script can still be made more flexible by putting the values for the dictionaries in variables. These variables can be lists that it needs to go through.