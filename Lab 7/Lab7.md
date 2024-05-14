# LAB 7 – YANG, NETCONFIG and RESTCONFIG 
## Part 1: Install the CSR1000v VM
### Prerequisits
- Lab 1.1.2 Lab - Install the Virtual Machine Environment
- Virtualbox (& basic knowledge about virtualbox settings)
- Files in Lab 7

### Install the CSR1000v VM.
#### Ad the VM
- Open Oracle VirtualBox Manager and import the VM as shown below:

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/VirtualBoxImport.png?raw=true)
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/VirtualBoxImport_Location.png?raw=true)

#### Configure the VM
- Update the installation ISO location as shown below:

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CRS1000v_Settings.png?raw=true)
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CRS1000v_Settings_iso.png?raw=true)
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CRS1000v_Settings_iso_select.png?raw=true)

>[!Warning] 
>Do **NOT** change the Second CD Drive settings. That is used for the initial configuration of the router.

#### Check the adapter
Make sure it is on a Host-only adapter!

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CRS1000v_Settings_Adapter.png?raw=true)

>[!Tip]
>If you need to change the adapter, make sure the adapter is using the 192.168.56.1/24 IPv4-address.


#### Start CSR1000v VM

Except for pressing `any key` when the os is booting, you don't have to do anything.
Just wait till the VM is completely installed then press `Enter`.
You should see the the prompt.

>[!Note]
>There is no enable password, so you can switch to the privileged EXEC prompt and configure terminal prompt.

Switch to the privileged EXEC prompt and show the ip address.
```
Enable
Show ip interface brief
```
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowIPInterfaceBrief.png?raw=true)

>[!Important]
>Take note of the ip address shown, we will use it in the next steps!

### Launch the DEVASC VM
Start the DEVASC VM in virtualbox
### Ping the CSR1000v VM from the DEVASC VM VM.
- Open a Terminal window.
- Ping the CSR1000v VM at its IPv4 address.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/PingCSR1000v.png?raw=true)

### Establish a secure shell (SSH) session with the CSR1000v.
Some of the tasks you will complete in later labs will require an SSH session with the CSR1000v.

```
ssh cisco@192.168.56.101
```

>[!Note]
>Replace the ip address with the one you received in the previous steps. (if needed)

>[!Tip] 
>Use the password cisco123! to authenticate.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/SSHCSR1000v.png?raw=true)

>[!Note]
>Notice that you are automatically in privileged EXEC mode. Enter exit to end the SSH session.

Close the connection.

### From the DEVASC VM, access the CSR1000v WebUI (Web User Interface)
- Open a web browser on the DEVASC VM
- Follow the steps as shown below:

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/WebUICSR1000v.png?raw=true)
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/WebUICSR1000v_2.png?raw=true)
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/WebUICSR1000v_3.png?raw=true)

>[!Tip] 
>Use the password cisco123! to authenticate.

You will now see the Dashboard for the CSR1000v. You are now accessing the CSR1000v's WebUI from the DEVASC virtual machine.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/DEVASCWebDashboard.png?raw=true)

### From your local computer, access the CSR1000v WebUI (Web User Interface)
- Follow the same steps but on your local computer.

You will now see the Dashboard for the CSR1000v. You are now accessing the CSR1000v's WebUI from your local computer.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/LocalWebDashboard.png?raw=true)

## Part 2: Explore YANG Models

We'll explore yang files by making them more readable with the pyang module.

### Explore Cisco IOS XE YANG models in the GitHub repository

- Start the DEVASC VM and open chromium
- Navigate to https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1693/ietf-interfaces.yang

>[!Tip]
>If you are familiar with the output of IOS show commands, you will recognize some nodes like on line 221. Leaf is enabled. \
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/Leaf_enabled.png?raw=true)

### Copy the ietf-interfaces.yang model to a folder on your VM

- Open VS code and open devnet-src
  
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/VSCode_Devnet.png?raw=true)

- Open a terminal window in VS Code
  
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/TerminalVSCode.png?raw=true)

- Create a subdirectory called pyang in the /devnet-src directory.
  
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/SubDirPyang.png?raw=true))

- Display the YANG model of the previous task in Raw format
  
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/RawYangModel.png?raw=true)

- Copy the URL
  
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CopyURL.png?raw=true)


- In the terminal navigate to the new pyang folder and use wget to get the file.

```bash
cd labs/devasc-src/pyang
wget https://raw.githubusercontent.com/YangModels/yang/main/vendor/cisco/xe/1693/ietf-interfaces.yang
ls
```
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/TerminalCommands.png?raw=true)

### Verify pyang is installed and up to date

- Open the terminal in VSCode as seen in the previous exercise
- Use the following command:

```bash
pyang -v
```

>[!Note]
>The version you see is 2.2.1, this version is outdated.

To upgrade pyang to the latest version use:

```bash
pip3 install pyang --upgrade
```

 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/InstallPyang.png?raw=true)

- Navigate to the pyang directory and use pyang to transform the YANG model

```bash
cd pyang
pyang -f tree ietf-interfaces.yang
```

 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/EndOfPyang.png?raw=true)

>[!Tip]
>If you do not know how to use pyang, use `pyang -h | more`.


## Part 3: Use NETCONF to Access an IOS XE Device

>[!Important]
>Make sure both DEVASC VM and the CSR1000v VM are running and are connected, as we established in part 1.

- CSR1000v

```
enable
show ip interface brief
```
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowInterfaceBrief.png?raw=true)

>[!Note]
>Notice the ip address and use it in the next command on the DEVASC

- DEVASC

```bash
ping 192.168.56.101
```
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/pingCSR.png?raw=true)

>[!Note]
>Your CSR1000v VM can have a different ip-address.

- SSH from DEVASC to CSR1000v
  
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/SSHCSR.png?raw=true)

>[!Warning]
> If you get an error like this:
>  ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/SSH_Error.png?raw=true)
> It is because our previous exercise but don't worry use the command below to reset the ssh verification:
> ```bash
> ssh-keygen -f "/home/devasc/.ssh/known_hosts" -R "192.168.56.101"
> ```
>![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/Correct_Error.png?raw=true)
> now try again

- With the SSH connection active, verify if a NETCONF is already running:
```
show platform software yang-management process
```
>[!Note]
>Looks like the deamon is running (`ncsshd`)

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowServices.png?raw=true)

>[!Warning]
>If it is not running use the following commands:
>```
>configure terminal
>netconf-yang
>```

- Close the connection

```
exit
```
###  Access the NETCONF process through an SSH terminal.

- Reopen the connection with port 830 and subsystem netconf

```
ssh cisco@192.168.56.101 -p 830 -s netconf
```

The output will look like this:

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/XML_Results.png?raw=true)

>[!Note]
>Notice the construct of the message by opening with `<hello` because it is an hello message. And NETCONFIG messages end with `]]>]]>`

- Create your own message by pasting the following command in the terminal:
```
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
 <capability>urn:ietf:params:netconf:base:1.0</capability>
</capabilities>
</hello>
]]>]]>
```

- Verify the session:
    - Go to the CSR1000v VM and use the following commands:
    ```
    enable
    show netconf-yang sessions
    ```  
    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowYangSessions.png?raw=true)

- Now make an RPC message. It will give a respons back:
    ```
    <rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <get>
    <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    </get>
    </rpc>
    ]]>]]>
    ```
    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/RPCResponse.png?raw=true)

>[!Tip]
>Common RPC commands:

 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CommonRPCCommands.png?raw=true)

- Take the respons and use a prettifyer to make the respons more readable:
    ```
    <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="103"><data><interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"><interface><name>GigabitEthernet1</name><description>VBox</description><type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type><enabled>true</enabled><ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"></ipv4><ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"></ipv6></interface></interfaces></data></rpc-reply>]]>]]>
    ```
- https://jsonformatter.org/xml-pretty-print

    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/OnlineFormatter.png?raw=true)

- Close the NETCONF session
    ```
    <rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <close-session />
    </rpc>
    ```
    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CloseRPC.png?raw=true)

- Go to CSR1000v again and check if the session is closed
    ```
    show netconf-yang sessions
    ```
    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowYangSessions_2.png?raw=true)

### Use ncclient to Connect to NETCONF

- Use the following command to validate the installation of the ncclient module:
    ```bash
    pip3 list --format=columns | grep ncclient
    ```

    >[!Important]
    >If `ncclient` is not installed use:
    > ```bash
    > pip3 install ncclient
    > ```

    >[!Tip]
    >If you want to see all the modules currently installed use:
    > ```bash
    > pip3 list --format=columns | more
    > ```

- Create a script to use ncclient to connect to the NETCONF service
    - Like you created the pyang folder, now create a folder `netconf`
    - Ad a file named `ncclient-netconf.py` to the folder
    
        ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/CreateNetconfScript.png?raw=true)
    - Paste this script in the file:
        ```python
        from ncclient import manager

        m = manager.connect(
            host="192.168.56.101",
            port=830,
            username="cisco",
            password="cisco123!",
            hostkey_verify=False
        )
        ```
    - Verify by activating the script. There should not be any errors
        ```bash
        cd netconf/
        python3 ncclient-netconf.py
        ```
    >[!Note]
    >We can see the respons of CSR1000v:
    >
    > ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/SessionConfirmation.png?raw=true)

    >[!Tip]
    >Feel free to test every part we are adding but i won't mention it again

    -  Ad a for loop to the script that prints the capabilities of the device.
        ```python
        print("#Supported Capabilities (YANG models):")
        for capability in m.server_capabilities:
            print(capability)
        ```
    >[!Tip]
    >If you do not want to get 400+ lines during each test, comment out the print statement

    - Ad the following to your script:
        ```python
        netconf_reply = m.get_config(source="running")
        print(netconf_reply)
        ```
        This should give you the configuration. verify it by running the command on CSR1000v:
        ```
        show netconf-yang datastores
        ```
    >[!Note]
    >If you are testing the results, you will see you need the prettifyer of the previous exercise to make the result easier to read. In the next part we will make our own with python.

    -   Prettify results by adding the following line to the beginning of the script:
        ```python
        import xml.dom.minidom
        ```
        and altering `print(netconf_reply)` to:
        ```python
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
        ```
    - Ad an filter above `netconf_reply`:
    ```python
    netconf_filter = """
    <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    </filter>
    """
    ```
    - The end result should look like this:
    ```python
    from ncclient import manager
    import xml.dom.minidom

    m = manager.connect(
        host="192.168.56.101",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    )

    print("#Supported Capabilities (YANG models):")
    for capability in m.server_capabilities:
        print(capability)

    netconf_filter = """
    <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    </filter>
    """

    netconf_reply = m.get_config(source="running")
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    ```
### Use ncclient to Configure a Device
- Ad a configuration variable under the filter we just made, the example is altering the hostname to `NEWHOSTNAME`:
    ```python
    netconf_hostname = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>NEWHOSTNAME</hostname>
    </native>
    </config>
    """
    ```
- To make this configuration happen we need to use the variable in a function, the function is `edit_config` and we will save it by using netconf_reply again:
    ```python
    netconf_reply = m.edit_config(target="running", config=netconf_hostname)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    ```
    copy this under the existing code of `get_config`

- Use ncclient to create a new loopback interface on R1 by adding:
    ```python
    netconf_loopback = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <Loopback>
    <name>1</name>
    <description>My first NETCONF loopback</description>
    <ip>
    <address>
    <primary>
    <address>10.1.1.1</address>
    <mask>255.255.255.0</mask>
    </primary>
    </address>
    </ip>
    </Loopback>
    </interface>
    </native>
    </config>
    """
    ```
    and

    ```python
    netconf_reply = m.edit_config(target="running", config=netconf_loopback)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    ```
>[!Tip]
>You can verify by using these commands on NEWHOSTNAME (CSR1000v):
>   ```
>   enable
>   show ip interface brief
>   ```
>   ```
>   show run | section interface Loopback1
>   ```
>   

If you try this again with a new loopback with the same ip address, it will not work and give an error.

### Modify the Program Used in This Lab (Challenge)

Now you should have this script or something simular:

```python
from ncclient import manager 
import xml.dom.minidom 
 
m = manager.connect( 
    host="192.168.56.101", 
    port=830, 
    username="cisco", 
    password="cisco123!", 
    hostkey_verify=False 
    ) 
 
print("#Supported Capabilities (YANG models):") 
for capability in m.server_capabilities: 
    print(capability)  
 
netconf_reply = m.get_config(source="running") 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 
 
netconf_filter = """ 
<filter> 
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" /> 
</filter> 
""" 
netconf_reply = m.get_config(source="running", filter=netconf_filter) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 
 
netconf_hostname = """ 
<config> 
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
     <hostname>CSR1kv</hostname> 
  </native> 
</config> 
""" 
netconf_reply = m.edit_config(target="running", config=netconf_hostname) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 
 
netconf_loopback = """ 
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <interface> 
   <Loopback> 
    <name>1</name> 
    <description>My NETCONF loopback</description> 
    <ip> 
     <address> 
      <primary> 
       <address>10.1.1.1</address> 
       <mask>255.255.255.0</mask> 
      </primary> 
     </address> 
    </ip> 
   </Loopback> 
  </interface> 
 </native> 
</config> 
""" 
netconf_reply = m.edit_config(target="running", config=netconf_loopback) 
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 
 
netconf_newloop = """
<config> 
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
  <interface> 
   <Loopback> 
    <name>2</name> 
    <description>My second NETCONF loopback</description> 
    <ip> 
     <address> 
      <primary> 
       <address>10.1.1.1</address> 
       <mask>255.255.255.0</mask> 
      </primary> 
     </address> 
    </ip> 
   </Loopback> 
  </interface> 
 </native> 
</config> 
""" 
netconf_reply = m.edit_config(target="running", config=netconf_newloop) 
```
Try to add some extra verification and configuration commands.
In the following script you will see an example of a modified version where we add error handling, logging, extra verification and VLAN configuration.

```python
from ncclient import manager, NCClientError
import xml.dom.minidom
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Connect to the NETCONF server
    with manager.connect(
        host="192.168.56.101",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    ) as m:
        logging.info("Connected successfully to the device.")

        # Print supported capabilities
        logging.info("Supported Capabilities (YANG models):")
        for capability in m.server_capabilities:
            logging.info(capability)

        # Retrieve the running configuration
        netconf_reply = m.get_config(source="running")
        logging.info("Current running configuration:")
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

        # VLAN configuration example
        netconf_vlan = """
        <config>
          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <vlan>
              <vlan-list>
                <id>100</id>
                <name>DATA</name>
              </vlan-list>
            </vlan>
          </native>
        </config>
        """
        # Apply VLAN configuration
        vlan_reply = m.edit_config(target="running", config=netconf_vlan)
        logging.info("VLAN configuration applied:")
        print(xml.dom.minidom.parseString(vlan_reply.xml).toprettyxml())

        # Retrieve and verify the updated configuration
        netconf_filter = """
        <filter>
          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
        </filter>
        """
        verification_reply = m.get_config(source="running", filter=netconf_filter)
        logging.info("Verification of running configuration after changes:")
        print(xml.dom.minidom.parseString(verification_reply.xml).toprettyxml())

except NCClientError as e:
    logging.error(f"Encountered an error: {e}")

```

## Part 4: Use RESTCONF to Access an IOS XE Device

Make sure you are connected as in `Part 3`. Make sure a SSH connection is made.

### Configure an IOS XE Device for RESTCONF Access
With the SSH connection open, check if RESTCONF is already running.
```
show platform software yang-management process
```
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowYangProcess.png?raw=true)

It is not running in this case, so we will activate it.
```
configure terminal
restconf
exit
show platform software yang-management process
```
 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/ShowYangProcess_2.png?raw=true)

>[!Note]
>Notice that ncsshd is now added with a `Running` status. This is the NETCONF service as we have seen in `Part 3`, but we do not need it in this lab. But we do need an https server (nginx).

```
configure terminal
no netconf-yang
```

>[!Tip]
>If nginx is not running, use the following commands:
>```
>configure terminal
>ip http secure-server
>ip http authentication local 
>exit
>show platform software yang-management process
>```

### Open and Configure Postman
Devasc:
- Open postman

    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/OpenPostman.png?raw=true)

    >[!Note]
    >If this is the first time you have opened Postman, it may ask you to create an account or sign in. At the 
    bottom of the window, you can also click the “Skip” message to skip signing in. Signing in is not required 
    to use this application.

- Disable SSL certification verification

    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/OpenSettings.png?raw=true)
    ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/DisableSSLCertVer.png?raw=true)

### Use Postman to Send GET Requests 
Start a GET request on the URL.

>[!Important]
>Make sure you use `https`!

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETRequest.png?raw=true)

As you can see we are not getting a respons. We need to authenticate ourselves. We know the local user and password, so lets configure postman further.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/Authentication.png?raw=true)

Now try sending the GET request again.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETRequestRespons.png?raw=true)

Notice we get an respons in XML format by default. We will change this to JSON.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/AlterHeader.png?raw=true)

Key 1
```
Content-Type
```
Value 1
```
application/yang-data+json
```
Key 2
```
Accept
```
Value 2
```
application/yang-data+json
```
Now we are going to use what we prepared. First lets duplicate our tab.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/DuplicateTab.png?raw=true)

Let use the ietf-interfaces YANG model by using the following URL:
```
https://192.168.56.101/restconf/data/ietf-interfaces:interfaces
```
You should get the following respons or something close to it:

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETResponse_2.png?raw=true)

Try again but clarify further that you just want information about interface `GigabitEthernet1` with the following URL:
```
https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1
```
![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETRespons_3.png?raw=true)

>[!Tip]
>If you request interface information from a different Cisco device with names that use forward slashes, such as GigabitEthernet0/0/1, use the HTML code `%2F` for the forward slashes in the interface 
name. So, `0/0/1` becomes `0%2F0%2F1`

>[!Note]
>Notice that the IPv4 address is missing. This is because it is not configured on the device. The VM gets its IP-address by the DHCP of Virtualbox. Try setting the address manually and send the request again.
>```
>configure terminal
>interface g1
>ip address 192.168.56.101 255.255.255.0
>end
>show ip interface brief
>```

### Use Postman to Send a PUT Request
Change the type of the request to `PUT`. And use the following URL:
```
https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback1 
```

As we have not filled the Body yet a `error 400 'Bad request'` will appear.
Past the following in the body `raw` format to resolve:

```
{ 
  "ietf-interfaces:interface": { 
    "name": "Loopback1", 
    "description": "My first RESTCONF loopback", 
    "type": "iana-if-type:softwareLoopback", 
    "enabled": true, 
    "ietf-ip:ipv4": { 
      "address": [ 
        { 
          "ip": "10.1.1.1", 
          "netmask": "255.255.255.0" 
        } 
      ] 
    }, 
    "ietf-ip:ipv6": {} 
  }
}
```

Now we get an `201 Created` message.

![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/PUTResponse.png?raw=true)

>[!Tip]
>You can check this by using the following command:
>```
>show ip interface brief
>```

### Use a Python script to Send GET Requests 
>[!Note]
>As we already have seen the following steps in the other exercises in `Lab 7`, I will just sum the needed steps. Not how to execute them.

- Open the devnet-src folder in VSCode
- Open a terminal in VSCode
- Create a subfolder `restconf`
- Create a new file named `restconf-get.py`
- Paste the following in the file:
    ```python
    import json 
    import requests 
    requests.packages.urllib3.disable_warnings()
    ```
>[!Note]
>This basicly imports the required modules and disables SSL certificate warnings.

- Append a variable with the URL to `GET` information.
```python
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
```

- Now append the variables for the headers we filled out manually in postman.
```python
headers = { "Accept": "application/yang-data+json",  
            "Content-type":"application/yang-data+json" 
           }
```

- Append another variable for the authentication.
```python
basicauth = ("cisco", "cisco123!")
```

- The final variable will be one to hold the respons to our `GET` request.
```python
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
```

- Lastly, we want to get the respons as a printed message, append this code:
```python
print(resp) 
```

- Run the script.
```bash
python3 restconf-get.py
```

The response should be:

 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETScriptResponse.png?raw=true)

- To get the actual JSON reponse, create a new variable and print it.
```python
response_json = resp.json()
```

```python
print(response_json)
```

- Save and run the script again. You should get the following respons:

 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETScriptResponse_2.png?raw=true)

- Prettify the output by changing `print(response_json)`
```python
print(json.dumps(response_json, indent=4))
```

 ![alt text](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/blob/main/Lab%207/Images/GETScriptResponse_3.png?raw=true)

Your script should now look like:
```python
import json 
import requests 
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces" 

headers = { "Accept": "application/yang-data+json",  
            "Content-type":"application/yang-data+json" 
           }

basicauth = ("cisco", "cisco123!")

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

response_json = resp.json()

print(resp)

print(json.dumps(response_json, indent=4))
```
### Use a Python Script to Send a PUT Request

Now for this exercise I am not going to repeat all the reasons why we use the variables, dictionaries and print commands.

Try to figure out why we are using each part of this script based on the `Postman` exercise and the previous script.

- Create new file named `restconf-put.py`
- Paste following script:

```python
import json 
import requests 
requests.packages.urllib3.disable_warnings() 
 
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback2" 
 
headers = { "Accept": "application/yang-data+json",  
            "Content-type":"application/yang-data+json" 
           } 
 
basicauth = ("cisco", "cisco123!") 
 
yangConfig = { 
    "ietf-interfaces:interface": { 
        "name": "Loopback2", 
        "description": "My second RESTCONF loopback", 
        "type": "iana-if-type:softwareLoopback", 
        "enabled": True, 
        "ietf-ip:ipv4": { 
            "address": [ 
                { 
                    "ip": "10.2.1.1", 
                    "netmask": "255.255.255.0" 
                } 
            ] 
        }, 
        "ietf-ip:ipv6": {} 
    } 
} 
 
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, 
headers=headers, verify=False) 
 
if(resp.status_code >= 200 and resp.status_code <= 299): 
    print("STATUS OK: {}".format(resp.status_code)) 
else: 
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
```

