# Lab4: NETWORK INFRASTRUCTURE AND TROUBLESHOOTING
## Part 1: Network Infrastructure
### Prep
#### Document
Open the Visio provided \
Create an IP Table:

![IPTable](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/assets/104322584/5c40409b-10da-43c8-be95-19f9d0d2708b)

#### Physical

>[!Tip]
>Make sure all devices are plugged in and have power!

Turn on the switches

Connect the switches:

![Switches](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/assets/104322584/d30fb6fd-bff4-4a27-9c71-7a0b945bb671)

![SwitchesC](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/assets/104322584/18466fdf-921a-4a7a-8134-069730269d62)

Turn on the routers

Connect the switches:

![Routers](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/assets/104322584/c5fe5e16-d227-4a48-a448-5a7a7a750e80)

![RoutersC](https://github.com/SvenvG0/DEVNET_EN2_GRSNW/assets/104322584/5014839c-66f9-4b12-b1d3-925c962c5eac)

>[!Important]
>Notice Gig 0/0/1 on both routers, they're connected to another switch and router.
>These devices are already configured in the lab. You only need to patch the cables correctly.

### Configure
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
switchport access vlan 75
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
Interface gigabitEthernet 1/0/20
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/21 - 22
Channel-group 1 mode active
exit
interface port-channel 1
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/23 - 24
Channel-group 2 mode active
exit
interface port-channel 2
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75
no shutdown
exit
interface vlan 75
ip address 172.17.7.68 255.255.255.240
no shutdown
exit
spanning-tree VLAN 75 priority 4096
spanning-tree mode rapid-pvst
ip default-gateway 172.17.7.65
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
switchport access vlan 75
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
Interface gigabitEthernet 1/0/20
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/21 - 22
Channel-group 1 mode active
exit
interface port-channel 1
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range gigabitEthernet 1/0/23 - 24
Channel-group 3 mode active
exit
interface port-channel 3
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
interface vlan 75
ip address 172.17.7.69 255.255.255.240
no shutdown
exit
spanning-tree VLAN 75 priority 8192
spanning-tree mode rapid-pvst
ip default-gateway 172.17.7.65

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
switchport access vlan 75
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
interface gigabitEthernet 0/1
switchport mode access
switchport access vlan 75
spanning-tree portfast
spanning-tree bpduguard enable
no shutdown
exit
interface gigabitEthernet 0/2
switchport mode access
switchport access vlan 75
spanning-tree portfast
spanning-tree bpduguard enable
shutdown
exit
Interface range fastEthernet 0/21 - 22
Channel-group 2 mode active
exit
interface port-channel 2
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
Interface range fastEthernet 0/23 - 24
Channel-group 3 mode active
exit
interface port-channel 3
switchport mode trunk
switchport trunk native vlan 99
switchport trunk allowed vlan 75,76,77,78,99
no shutdown
exit
interface vlan 75
ip address 172.17.7.70 255.255.255.240
no shutdown
exit
spanning-tree VLAN 75 priority 32768
spanning-tree mode rapid-pvst
ip default-gateway 172.17.7.65

```

##### LAB-RA0X-C02-R01

```
Enable
configure terminal
hostname LAB-RA0X-C02-R01
interface gigabitEthernet 0/0/0.75
description vlan 75
encapsulation dot1Q 75
ip address 172.17.7.66 255.255.255.240
standby 1 ip 172.17.7.65
standby 1 priority 110
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0.76
description vlan 76
encapsulation dot1Q 76
ip address 172.17.7.82 255.255.255.240
standby 1 ip 172.17.7.81
standby 1 priority 110
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0.77
description vlan 77
encapsulation dot1Q 77
ip address 172.17.7.98 255.255.255.240
standby 1 ip 172.17.7.97
standby 1 priority 110
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0.78
description vlan 78
encapsulation dot1Q 78
ip address 172.17.7.114 255.255.255.240
standby 1 ip 172.17.7.113
standby 1 priority 110
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0
no shutdown
interface gigabitEthernet 0/0/1
ip address 10.199.65.114 255.255.255.224
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 10.199.65.100

```

##### LAB-RA0X-C02-R02

```
Enable
configure terminal
hostname LAB-RA0X-C02-R02
interface gigabitEthernet 0/0/0.75
description vlan 75
encapsulation dot1Q 75
ip address 172.17.7.67 255.255.255.240
standby 1 ip 172.17.7.65
standby 1 priority 100
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0.76
description vlan 76
encapsulation dot1Q 76
ip address 172.17.7.83 255.255.255.240
standby 1 ip 172.17.7.81
standby 1 priority 100
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0.77
description vlan 77
encapsulation dot1Q 77
ip address 172.17.7.99 255.255.255.240
standby 1 ip 172.17.7.97
standby 1 priority 100
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0.78
description vlan 78
encapsulation dot1Q 78
ip address 172.17.7.115 255.255.255.240
standby 1 ip 172.17.7.113
standby 1 priority 100
standby 1 preempt
no shutdown
interface gigabitEthernet 0/0/0
no shutdown
interface gigabitEthernet 0/0/1
ip address 10.199.65.214 255.255.255.224
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 10.199.65.200
```

##### Client

Configure the clients IPV4 address.
- IPV4: 172.17.7.71
- SUBNETMASK: 255.255.255.240
- DEFAULT-GATEWAY: 172.17.7.65
- DNS: 10.199.64.66

You should be able to ping to the other devices and to devices outside your LAN.

### Troubleshooting

#### Can't ping
- Make sure your IPV4 address is filled in correctly?
- Is the default gateway filled correctly?
- Is the default static route configured correctly?

#### Can't be pinged
- Is the firewall on your PC off?

#### Switches can not reach router
- did you only activate the subnet interfaces? (Check the main one)
