# Thread Information
Title: Thread-1116079
Section: RouterOS
Thread ID: 1116079

# Discussion

## Initial Question
hiI have two route tables - main and custom. internal lan (bridge) writing in both tables.[admin@H] > ip address/printFlags: D - DYNAMICColumns: ADDRESS, NETWORK, INTERFACE# ADDRESS NETWORK INTERFACE0 10.0.3.1/24 10.0.3.0 bridge1[admin@H] > /ip route/ printFlags: D - DYNAMIC; X - DISABLED, I - INACTIVE, A - ACTIVE; c - CONNECT, s - STATIC; H - HW-O>Columns: DST-ADDRESS, GATEWAY, DISTANCE# DST-ADDRESS GATEWAY DISTANCEDAc 10.0.3.0/24 bridge1 0[admin@H] > /ip route/ print where routing-table=b1Flags: A - ACTIVE; s - STATICColumns: DST-ADDRESS, GATEWAY, DISTANCE# DST-ADDRESS GATEWAY DISTANCE22 As 10.0.3.0/24 bridge1 1Via mangle I forwarded traffic from 10.0.3.252 via route-table b1. I check, that another client 10.0.3.253 is accessible, but router 10.0.3.1 not.When traffic from 10.0.3.252 going via main route-table - router accessible via sshWhy router not accessible through manual table? ---

## Response 1
Found solution - available only vi VRF (ip-services ) ---