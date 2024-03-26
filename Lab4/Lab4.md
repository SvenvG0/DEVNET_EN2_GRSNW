# Lab4: NETWORK INFRASTRUCTURE AND TROUBLESHOOTING
## Part 1: Network Infrastructure
### Prep
Open the Visio provided
We begin by setting up the switches:
- LAB-RA0X-A02-SW01
- LAB-RA0X-A02-SW02
- LAB-RA0X-A02-SW03

Create an IP Table:

![alt text](image-3.png)

#### Physical

Turn on the switches (make sure they have power!)

Connect the switches:

![alt text](image-1.png)

![alt text](image-2.png)

Now connect to the switches to configure.

#### Configure
##### LAB-RA0X-A02-SW01
```
Enable
configure terminal
hostname LAB-RA0X-A02-SW01
vlan 75
name Management
vlan 76
name Data_Users
vlan 77
name Voice_Users
vlan 78
name Reserved
vlan 99
name Native
exit
interface range gigabitEthernet 1/0/1 - 19
switchport mode access
switchport access vlan 75,76,77,78,99
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
Interface gigabitEthernet 1/0/20
switchport mode trunk
switchport trunk encapsulation dot1q
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/21 - 22
Channel-group 1 mode active
exit
interface port-channel 1
switchport mode trunk
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/23 - 24
Channel-group 2 mode active
exit
interface port-channel 2
switchport mode trunk
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
interface vlan 75
ip address 172.17.7.68 255.255.255.240
no shutdown
exit
spanning-tree VLAN 75 priority 4096
spanning-tree mode rapid-pvst
```
##### LAB-RA0X-A02-SW02
```
Enable
configure terminal
hostname LAB-RA0X-A02-SW02
vlan 75
name Management
vlan 76
name Data_Users
vlan 77
name Voice_Users
vlan 78
name Reserved
vlan 99
name Native
exit
interface range gigabitEthernet 1/0/1 - 19
switchport mode access
switchport access vlan 75,76,77,78,99
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
Interface gigabitEthernet 1/0/20
switchport mode trunk
switchport trunk encapsulation dot1q
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/21 - 22
Channel-group 1 mode active
exit
interface port-channel 1
switchport mode trunk
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/23 - 24
Channel-group 3 mode active
exit
interface port-channel 3
switchport mode trunk
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
interface vlan 75
ip address 172.17.7.69 255.255.255.240
no shutdown
exit
spanning-tree VLAN 75 priority 8192
spanning-tree mode rapid-pvst

```
##### LAB-RA0X-A02-SW03

```
Enable
configure terminal
hostname LAB-RA0X-A02-SW03
vlan 75
name Management
vlan 76
name Data_Users
vlan 77
name Voice_Users
vlan 78
name Reserved
vlan 99
name Native
exit
interface range fastEthernet 0/1 - 20
switchport mode access
switchport access vlan 75,76,77,78,99
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
interface gigabitEthernet 0/1
switchport mode access
switchport access vlan 75,76,77,78,99
spanning-tree portfast
spanning-tree bpduguard enable
no shutdown
exit
interface gigabitEthernet 0/2
switchport mode access
switchport access vlan 75,76,77,78,99
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
Interface range fastEthernet 0/21 - 22
Channel-group 2 mode active
exit
interface port-channel 2
switchport mode trunk
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range fastEthernet 0/23 - 24
Channel-group 3 mode active
exit
interface port-channel 3
switchport mode trunk
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
interface vlan 75
ip address 172.17.7.70 255.255.255.240
no shutdown
exit
spanning-tree VLAN 75 priority 32768
spanning-tree mode rapid-pvst

```