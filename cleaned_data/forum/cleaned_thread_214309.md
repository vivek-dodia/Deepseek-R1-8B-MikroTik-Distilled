# Thread Information
Title: Thread-214309
Section: RouterOS
Thread ID: 214309

# Discussion

## Initial Question
Hello, Can you please help me with a strange situation?I have a CCR2116 CCR, and since I upgraded to ROS 7.17 it is incorrectly displaying the download on the vlan of an interface. On SFP+1 interface there are 2 vlan whose traffic is wrong. The traffic value per port is correct, the one displayed on the vlan is strange. I attach 2 pictures with the graph on that port , and also with the traffic rendering in Winbox.Thank you in advance ---

## Response 1
VLAN traffic is traffic between device's IP stack and that device. If device is used as a switch, then traffic shown for VLAN interfaces will be low.Or is sfp-sfpplus1 being used in a "router on a stick" manner? ---

## Response 2
Hi, Do you have an ip addressing on the sfp+1 physical interface?Without the configuration we can only guess... possible problems.Regards, ---