# Document Information
Title: Interface Lists
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/47579180/Interface+Lists,

# Content
# Summary
Allows defining a set of interfaces for easier interface management in the different interface-based configuration sections such as Neighbor Discovery, Firewall, Bridge, and Internet Detect.
# Lists
Sub-menu:/interface list
```
/interface list
```
This menu contains information about all interface lists available on the router. There are four predefined lists -all(contains all interfaces),none(contains no interfaces),dynamic(contains dynamic interfaces), andstatic(contains static interfaces). It is also possible to create additional interface lists.
```
all
```
```
none
```
```
dynamic
```
```
static
```
Property | Description
----------------------
name(string) | Name of the interface list
include(string) | Defines interface list which members are included in the list. It is possible to add multiple lists separated by commas
exclude(string) | Defines interface list which members are excluded from the list. It is possible to add multiple lists separated by commas
Members are added to the interface list in the following order:
# Members
Sub-menu:/interface list member
```
/interface list member
```
This sub-menu contains information about statically configured interface members to each interface list. Note that dynamically added interfaces by include and exclude statements are not represented in this sub-menu.
Property | Description
----------------------
interface(string) | Name of the interface
list(string) | Name of the interface list