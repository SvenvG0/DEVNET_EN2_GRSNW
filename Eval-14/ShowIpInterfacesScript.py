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

SW01 = {
        'device_type': f"{deviceType}",
        'ip': f"{subnet}68",  # Last numbers depending on device
        'username': f"{user}", 
        'password': f"{password}",
        'secret': f"{secret}",
}


SW02 = {
        'device_type': f"{deviceType}",
        'ip': f"{subnet}69",  # Last numbers depending on device
        'username': f"{user}", 
        'password': f"{password}",
        'secret': f"{secret}",
}


SW03 = {
        'device_type': f"{deviceType}",
        'ip': f"{subnet}70",  # Last numbers depending on device
        'username': f"{user}", 
        'password': f"{password}",
        'secret': f"{secret}",
}

devices = R01, R02, SW01, SW02, SW03
for device in devices:
    # Initialize the connection to the device
    net_connect = ConnectHandler(**device)
    net_connect.enable()

    # Send a show command
    output = net_connect.send_command('show ip interface')
    print('------------------------------------------------')
    print(output)
    print('------------------------------------------------')

    # Close the connection
    net_connect.disconnect()