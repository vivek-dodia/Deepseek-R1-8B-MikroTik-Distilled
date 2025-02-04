# Thread Information
Title: Thread-1114504
Section: RouterOS
Thread ID: 1114504

# Discussion

## Initial Question
So, I'm in the midst of implementing monitoring solution, Security Onion OS. Now, my plan is to monitor specific Ethernet ports on Mikrotik via port mirroring.The Problem:The system is very tight and allows only few things (by design). Now, if I connect Security Onion OS and the 'seniors' into mirror sources, everything is OK.... BUT I would like to also connect Security Onion OS to the internet as then I'll have much more ability to analyze traffic, however my biggest concern is if Security Onion OS gets compromised, the sensors can be used to get access to the Mikrotik's and possibly compromised them.Question:If using port mirroring, the 'source mirror' is sending copy of packets to 'target mirror' Ethernet. Now, can 'target mirror' also send packets back to mikrotik? basically, does 'mirror traffics' do both way traffic or is it just sending copies of packets one way? ---

## Response 1
If using port mirroring, the 'source mirror' is sending copy of packets to 'target mirror' Ethernet. Now, can 'target mirror' also send packets back to mikrotik? basically, does 'mirror traffics' do both way traffic or is it just sending copies of packets one way?Did you find answer to that? I'm interested too if that mirror is bi-directional or just one way. ---