# Thread Information
Title: Thread-213802
Section: RouterOS
Thread ID: 213802

# Discussion

## Initial Question
Dear all, Good afternoon.I am having trouble communicating with an RB750 Gr3.In my current scenario, I have an RB750Gr with two internet links on Ether 1 and Ether 2 ports.I need to connect an Asus router to the network that runs a specific streaming service for my client.This router has a fixed IP range and cannot be changed (IP 192.168.132.1).I connected this Asus router to the Mikrotik's Ether 3 port so that I can access it from a local machine, but I cannot access it from a local machine, but from the MK terminal I can ping the IP 192.168.132.1.My RB750 GR settings:Ether1 - dhcp clientEther 2 - dhcp ClientEther 3 - dhcp client Asus Router 192.168.132.190Ether 4 - disableEther 5 - LOCAL LAN - 192.168.10.1DHCP Local Network - 192.168.10.0/24Important information: the Asus Router has a specific and dedicated link just for it that is not connected to the RB750GR. I justneed to make the communication between this router and the RB through a specific machine on the local network. ---

## Response 1
Good Evening, It shouldn`t be a Problem to communicate with the Asus Router from the RB750-Router and/or from the Local Network on Ether5.If i had to guess the Issue, i would check if "Masquerade" is enabled for the Asus-NetworkIf that doesn`t help or need more help, please Post the Configuration of the Router, so we can check it. ---