---
title: Graphing
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/22773810/Graphing,
crawled_date: 2025-02-02T21:14:53.766970
section: mikrotik_docs
type: documentation
---

## 2Summary3Configuration3.1General3.2Interface graphing3.3Queue graphing3.4Resource graphing4Graphing in WinBox
* 2Summary
* 3Configuration3.1General3.2Interface graphing3.3Queue graphing3.4Resource graphing
* 4Graphing in WinBox
* 3.1General
* 3.2Interface graphing
* 3.3Queue graphing
* 3.4Resource graphing
# Summary
Graphing is a tool to monitor various RouterOS parameters over time and put collected data in graphs.Watch ourvideo about this feature.
The Graphing tool can display graphics for:
* Resource usage (CPU, Memory, and Disk usage)
* Traffic which is passed through an interface
* Traffic which is passed through a simple queue
Graphing consists of two parts - the first part collects information and the other part displays data on a Web page. To access the graphics, type http://[Router_IP_address]/graphs/ and choose a graphic to display in your Web browser.
Alternatively, look for the menu≡(triple bar sign) in the top right corner of the WebFig interface, allowing you to find "graphs":
Example of memory graphs:
# Configuration
## General
The configuration is done under "/tool graphing" menu, by default, graphing is disabled. You can configure graphing for interfaces, resources, and simple queues in their respective submenus.
Sub-menu:/tool graphing
```
/tool graphing
```
Property | Description
----------------------
store-every(24hours | 5min | hour; Default:5min) | How often to write collected data to system drive.
page-refresh(integer | never; Default:300) | How often graph page is refreshed
## Interface graphing
Sub-menu allows configuration for which interface graphing will collect bandwidth usage data.
Sub-menu:/tool graphing interface
```
/tool graphing interface
```
Property | Description
----------------------
allow-address(IP/IPv6 prefix; Default:0.0.0.0/0) | IP address range from which is allowed to access graphing information
comment(string; Default:) | Description of current entry
disabled(yes | no; Default:no) | Defines whether item is used
interface(all | interface name; Default:all) | Defines which interface will be monitored.allmeans that all interfaces on router will be monitored.
store-on-disk(yes | no; Default:yes) | Defines whether to store collected information on system drive.
## Queue graphing
Sub-menu allows configuration for which simple queue graphing will collect bandwidth usage data.
Sub-menu:/tool graphing queue
```
/tool graphing queue
```
Property | Description
----------------------
allow-address(IP/IPv6 prefix; Default:0.0.0.0/0) | IP address range from which is allowed to access graphing information
allow-target(yes | no; Default:yes) | Whether to allow access to graphs from queue's target-address
comment(string; Default:) | Description of current entry
disabled(yes | no; Default:no) | Defines whether item is used
simple-queue(all | queue name; Default:all) | Defines which queues will be monitored.allmeans that all queues on router will be monitored.
store-on-disk(yes | no; Default:yes) | Defines whether to store collected information on system drive.
## Resource graphing
Sub-menu allows to enable graphing of system resources. Graphing collects data of:
* CPU usage
* Memory usage
* Disk usage
Sub-menu:/tool graphing resource
```
/tool graphing resource
```
Property | Description
----------------------
allow-address(IP/IPv6 prefix; Default:0.0.0.0/0) | IP address range from which is allowed to access graphing information
comment(string; Default:) | Description of current entry
disabled(yes | no; Default:no) | Defines whether item is used
store-on-disk(yes | no; Default:yes) | Defines whether to store collected information on system drive
# Graphing in WinBox
Winbox allows viewing the same collected information as on the web page. OpenTools->Graphingwindow. Double click on the entry of which you want to see graphs.
The image below shows WinBox graphs of memory usage: