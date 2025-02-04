# Thread Information
Title: Thread-1118459
Section: RouterOS
Thread ID: 1118459

# Discussion

## Initial Question
Hi, I have CHR of version 7.16.2 in the datacenter. It has 8 p2p connections with the remote offices.Between the office and datacenter there are BGP tunnels with BFD flag enabled.Everything had been working so far, but at some day it could be the situation when all BGP tunnels are down because of BFD.When I log into CHR via winbox, I cannot even overview the BFD configuration neither via Winbox nor the Terminal.Знімок екрана 2025-01-08 о 23.42.21.pngOnly the reboot helps. After reboot is done the situation looks like this:Знімок екрана 2025-01-08 о 23.42.21.png ---

## Response 1
Since you didn’t provide an export or details about the virtual environment, here’s a guess: try increasing the RAM for the ROS virtual guest and monitor memory usage after the next restart. ---

## Response 2
Since you didn’t provide an export or details about the virtual environment, here’s a guess: try increasing the RAM for the ROS virtual guest and monitor memory usage after the next restart.I wish I would, but how you can see that was timed out. We do not have any bgp full views or so on, just each location announces 1-3 /24 subnets into the datacenter and that's it. Inside the DC we have up to 5 virtual machines which use that CHR as NAT gateway. ---

## Response 3
Since you didn’t provide an export or details about the virtual environment, here’s a guess: try increasing the RAM for the ROS virtual guest and monitor memory usage after the next restart.The CHR runs as the VM at the hypervisor, uses qemu 8.3.0. We enrolled 4vCPU and 4.0GiB of RAM. From the hypervisor's chart I can see that the usage was not more than 500 +/- MiB of the RAM.Знімок екрана 2025-01-10 о 03.05.09.png ---