# Thread Information
Title: Thread-214053
Section: RouterOS
Thread ID: 214053

# Discussion

## Initial Question
Is there a way to encrypt file system (with something like LUKS or FSCrypt) on Chateau Pro AX? Intel now offers Total Memory Encryption. Is there something similar that can be enabled on this MikroTik device? ---

## Response 1
Intel TME doesn’t add much in a locked-down setup like Mikrotik ROS since the environment is already pretty tightly controlled, leaving little room for the kind of physical memory attacks TME is designed to prevent in servers using Intel processors etc. ---