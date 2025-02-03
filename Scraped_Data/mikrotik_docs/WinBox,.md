---
title: WinBox
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/328129/WinBox,
crawled_date: 2025-02-02T21:09:31.672410
section: mikrotik_docs
type: documentation
---

* 1Summary
* 2Starting WinBox2.1Simple mode2.1.1Buttons/check-boxes and Other Fields2.1.2Menu Items2.2Advanced mode2.2.1Buttons/check-boxes and Other Fields2.3Command Line2.4IPv6 connectivity2.5Run WinBox on macOS2.6Run WinBox on Linux
* 3Interface Overview
* 4Work Area and Child Windows4.1Child window menu bar4.2Sorting out displayed items4.3Customizing list of displayed columns4.3.1Detail mode4.3.2Category view4.4Drag & Drop4.5Traffic monitoring4.6Item copy
* 5Transferring Settings
* 6WinBox Keyboard Shortcuts
* 7Troubleshooting7.1WinBox cannot connect to the router's IP address, devices do not show up in the Neighbors list7.2I get an error '(port 20561) timed out' when connecting to routers mac address7.3I can't find my device in WinBox IPv4 Neighbors list or MAC connection fails with "ERROR could not connect to XX-XX-XX-XX-XX-XX"
* 2.1Simple mode2.1.1Buttons/check-boxes and Other Fields2.1.2Menu Items
* 2.2Advanced mode2.2.1Buttons/check-boxes and Other Fields
* 2.3Command Line
* 2.4IPv6 connectivity
* 2.5Run WinBox on macOS
* 2.6Run WinBox on Linux
* 2.1.1Buttons/check-boxes and Other Fields
* 2.1.2Menu Items
* 2.2.1Buttons/check-boxes and Other Fields
* 4.1Child window menu bar
* 4.2Sorting out displayed items
* 4.3Customizing list of displayed columns4.3.1Detail mode4.3.2Category view
* 4.4Drag & Drop
* 4.5Traffic monitoring
* 4.6Item copy
* 4.3.1Detail mode
* 4.3.2Category view
* 7.1WinBox cannot connect to the router's IP address, devices do not show up in the Neighbors list
* 7.2I get an error '(port 20561) timed out' when connecting to routers mac address
* 7.3I can't find my device in WinBox IPv4 Neighbors list or MAC connection fails with "ERROR could not connect to XX-XX-XX-XX-XX-XX"
# Summary
WinBox is a small utility that allows the administration of MikroTik RouterOS using a fast and simple GUI. It is a native Win32/Win64 binary but can be run onLinuxandmacOS (OSX)using Wine. All WinBox interface functions are as close as possible mirroring the console functions, that is why there are no WinBox sections in the manual. Some advanced and system critical configurations are not possible from the WinBox, like MAC address change on an interface.
From WinBox v3.14, the following security features are used:
* WinBox.exe is signed with an Extended Validation certificate, issued by SIA Mikrotīkls (MikroTik).
* WinBox uses ECSRP for key exchange and authentication (requires a new WinBox version).
* Both sides verify that the other side knows the password (no man in the middle attack is possible).
* WinBox in RoMON mode requires that the agent is the latest version to be able to connect to the latest version routers.
* WinBox uses AES128-CBC-SHA as an encryption algorithm (requires WinBox version 3.14 or above).
# Starting WinBox
WinBox loader can be downloaded from theMikroTik download page. When WinBox.exe is downloaded, double click on it, and the WinBox loader window will pop up. There are two WinBox loader modes: simple which is enabled by default and advanced.
## Simple mode
When you open WinBox loader for the first time simple mode layout will be used:
To connect to the router enter the IP or MAC address of the router, specify username and password (if any) and click on theConnectbutton. You can also enter the port number after the IP address, separating them with a colon, like this 192.168.88.1:9999. The port can be changed in the RouterOSservicesmenu.
You can also use neighbor discovery, to list available routers use theNeighborstab:
From the list of discovered routers, you can click on the IP or MAC address column to connect to that router. If you click on IP address then IP will be used to connect, but if you click on MAC Address then the MAC address will be used to connect to the router.
### Buttons/check-boxes and Other Fields
* Connect- Connect to the router
* Connect To RoMON- Connect toRoMONAgent
* Add/set- Save/Edit any of the saved router entries in theManagedtab.
* Open In New Window- Leaves loader open in the background and opens new windows for each device to which connection is made.
* Connect To:- destination IP or MAC address of the router
* Login- username used for authentication
* Password- password used for authentication
* Keep Password- if unchecked, the password is not saved to the list
### Menu Items
* FileNew- Create a new managed router list in a specified locationOpen- Open managed router list fileSave As- Save current managed router list to fileExit- Exit WinBox loader
* New- Create a new managed router list in a specified location
* Open- Open managed router list file
* Save As- Save current managed router list to file
* Exit- Exit WinBox loader
* ToolsAdvanced Mode- Enables/Disables advanced mode viewImport- Imports saved session fileExport- Exports saved session fileMove Session Folder- Change path where session files are storedClear cache- Clear WinBox cacheCheck For Updates- Check for updates for WinBox loader
* Advanced Mode- Enables/Disables advanced mode view
* Import- Imports saved session file
* Export- Exports saved session file
* Move Session Folder- Change path where session files are stored
* Clear cache- Clear WinBox cache
* Check For Updates- Check for updates for WinBox loader
## Advanced mode
Additional WinBox loader parameters are revealed when anadvanced modeis enabled withTools → Advanced Mode:
### Buttons/check-boxes and Other Fields
Buttons/check-boxes
* Browse- Browse file directory for some specific session
* Keep Password- if unchecked, the password is not saved to the list
* Secure mode- if checked, WinBox will use DH-1984 for key exchange and modified and hardened RC4-drop3072 encryption to secure the session.
* Autosave session- Saves sessions automatically for devices to which connections are made.
Fields:
* Session- Saved router session.
* Note- Note that is assigned to save router entry.
* Group- Group to which saved router entry is assigned.
* RoMON Agent- Select RoMON Agent from the available device list
## Command Line
It is possible to use the command line to pass connect to, user and password parameters automatically:
```
winbox.exe [<connect-to> [<login> [<password>]]]
```
For example (with no password):
```
winbox.exe 10.5.101.1 admin ""
```
Will connect to router 10.5.101.1 with user "admin" without a password.
It is possible to use the command line to pass connect to, user, and password parameters automatically to connect to the router through RoMON. In this case, RoMON Agent must be saved on the Managed routers list so WinBox would know the user and password for this device:
```
winbox.exe --romon [<romon-agent> [<connect-to> [<login> [<password>]]]]
```
For example (with no password):
```
winbox.exe --romon 10.5.101.1 D4:CA:6D:E1:B5:7D admin ""
```
Will connect to router D4:CA:6D:E1:B5:7D, through 10.5.101.1 via RoMON Agent with user "admin" without a password.
## IPv6 connectivity
WinBox supports IPv6 connectivity. To connect to the router's IPv6 address, it must be placed in square braces the same as in web browsers when connecting to the IPv6 server. Example:
[db8::1]
when connecting to the link-local address interface index must be entered after the %:
[0:a00:27ff:fe70::e88c%2]
Port number is set after the square brace when it is necessary to connect WinBox to other port than the default:
[0:a00:27ff:fe70::e88c]:8299
WinBox neighbor discovery is capable of discovering IPv6 enabled routers. There are two entries for each IPv6 enabled router, one entry is with IPv4 address and another one with IPv6 link-local address. You can easily choose which one you want to connect to.
## Run WinBox on macOS
Starting with macOS 10.15 Catalina, Apple has removed support for 32bit applications, meaning it is no longer possible to use regular Wine and regular WinBox in this OS. Wine has made available a 64bit version for macOS, and MikroTik has released a specialWinBox64.exeversion as well.
To run WinBox64 the following steps are required.
* Install latest Wine from theWine macOS builds page(wine-devel-7.X-osx64.tar.xz) and make sure you have downloaded theWinBox64.exe executablefrom the MikroTik download page.
* Launch WinBox64.exe with "open file with" > Wine64.app
## Run WinBox on Linux
It is possible to run WinBox on Linux by using Wine emulation software. Make sure that the Microsoft font pack is installed, otherwise, you may see distortions.
# Interface Overview
WinBox interface has been designed to be intuitive for most of the users. The interface consists of:
* The main toolbar at the top where users can add various info fields, like CPU and memory usage.
* The menu bar on the left - list of all available menus and sub-menus. This list changes depending on what packages are installed. For example, if the IPv6 package is disabled, then theIPv6menu and all its sub-menus will not be displayed.
* Work area - an area where all menu windows are opened.
The title bar shows information to identify with which router WinBox session is opened. Information is displayed in the following format:
```
[username]@[Router's IP or MAC] ( [RouterID] ) - WinBox [ROS version] on [RB model] ([platform])
```
From screenshot above we can see that userkrisjanisis logged into router with IPv4/IPv6 address[fe80::4e5e:cff:fef6:c0ab%3]. Router's ID is3C18-Krisjanis_GW, currently installed RouterOS version isv6.36rc6, RouterBoard isCCR1036-12G-4Sand platform istile.
On the Main toolbar's left side is located:
* undo
* redo
* Safe Mode
* Currently loaded session
More about Safe mode and undoing performed actions readin this article.
On the right side is located:
* an indicator that shows whether the WinBox session uses encryption
* WinBox traffic indicator displayed as a green bar,
* Custom info fields that can be added by the user by right-clicking on the toolbar and picking available info fields from the list
# Work Area and Child Windows
WinBox has an MDI interface meaning that all menu configuration (child) widows are attached to the main (parent) WinBox window and is showed in the work area.
Child windows can not be dragged out of the working area. Notice in the screenshot above that theInterfacewindow is dragged out of the visible working area and a horizontal scroll bar appeared at the bottom. If any window is outside visible work area boundaries the vertical or/and horizontal scrollbars will appear.
## Child window menu bar
Each child window has its own toolbar. Most of the windows have the same set of toolbar buttons:
* Add- add a new item to the list
* Remove- remove the selected item from the list
* Enable- enable selected item (the same asenablecommand from console)
* Disable- disable selected item (the same asdisablecommand from console)
* Comment- add or edit a comment
* Sort- allows to sort out items depending on various parameters.Read more >>
```
Read more >>
```
Almost all windows have a quick search input field on the right side of the toolbar. Any text entered in this field is searched through all the items and highlighted as illustrated in the screenshot below
Notice that on the right side next to the quick find input filed there is a drop-down box. For the currently opened (IP Route) window, this drop-down box allows to quickly sort out items by routing tables. For example, if themainis selected, then only routes from the main routing table will be listed.A similar drop-down box is also in all firewall windows to quickly sort out rules by chains.
## Sorting out displayed items
Almost every window has aSortbutton. When clicking on this button several options appear as illustrated in the screenshot below
The example shows how to quickly filter out routes that are in the 10.0.0.0/8 range
* PressSortbutton
* ChooseDst.Addressfrom the first drop-down box.
* Chooseinform the second drop-down box. "in" means that filter will check if DST address value is in range of the specified network.
* Enter the network against which values will be compared (in our example enter "10.0.0.0/8")
* These buttons are to add or remove another filter to the stack.
* Press theFilterbutton to apply our filter.
As you can see from the screenshot WinBox sorted out only routes that are within the 10.0.0.0/8 range.
Comparison operators (Number3in the screenshot) may be different for each window. For example "IP Route" window has only twoisandin. Other windows may have operators such as "is not", "contains", "contains not".
WinBox allows building a stack of filters. For example, if there is a need to filter by destination address and gateway, then
* set the first filter as described in the example above,
* press[+]button to add another filter bar in the stack.
* set up a second filter to filter by the gateway
* press theFilterbutton to apply filters.
You can also remove unnecessary filters from the stack by pressing the[-]button.
## Customizing list of displayed columns
By default, WinBox shows the most commonly used parameters. However sometimes it is needed to see other parameters, for example, "BGP AS Path" or other BGP attributes to monitor if routes are selected properly.
WinBox allows to customize displayed columns for each individual window. For example to add BGP AS path column:
* Click on the little arrow button (1) on the right side of the column titles or right mouse click on the route list.
* From popped up menu move toShow Columns(2) and from the sub-menu pick the desired column, in our case click onBGP AS Path(3)
Changes made to window layout are saved and next time when WinBox is opened the same column order and size are applied.
### Detail mode
It is also possible to enableDetail mode. In this mode all parameters are displayed in columns, the first column is the parameter name, the second column is the parameter's value.
To enable detail mode right mouse click on the item list and from the popup menu pickDetail mode
### Category view
It is possible to list items by categories. In this mode, all items will be grouped alphabetically or by another category. For example, items may be categorized alphabetically if sorted by name, items can also be categorized by type like in the screenshot below.
To enable Category view, right mouse click on the item list and from the popup menu pickShow Categories
## Drag & Drop
It is possible to upload and download files to/from the router using WinBox drag & drop functionality. You can also download the file by pressing the right mouse button on it and selecting "Download".
## Traffic monitoring
WinBox can be used as a tool to monitor the traffic of every interface, queue, or firewall rule in real-time. The screenshot below shows Ethernet traffic monitoring graphs.
## Item copy
This shows how easy it is to copy an item in WinBox. In this example, we will use the COPY button to make a Dynamic PPPoE server interface into a Static interface.
This image shows us the initial state, as you see DR indicates "D" which means Dynamic:
Double-Click on the interface and click on COPY:
A new interface window will appear, a new name will be created automatically (in this case pppoe-in1)
After this Down/Up event this interface will be Static:
# Transferring Settings
* Managed router transfer - In the File menu, use Save As and Open functions to save the managed router list to file and open it up again on a new workstation.
* Router sessions transfer - In the Tools menu, use Export and Import functions to save existing sessions to file and import them again on a new workstation.
# WinBox Keyboard Shortcuts
Shortcut | Description
----------------------
Ctrl+F | Find
Ctrl+G | Find Next
F3 | Find / Find next
Ctrl+M | Add or edit a comment
Ctrl+EorNum+ | Enables a selected setting
Ctrl+DorNum- | Disables a selected setting
Ctrl++ | Zoom in WinBox
Ctrl+- | Zoom out WinBox
Tab | Choose next control
Tab+Shift | Choose previous control
Space | Select focused control
F4orEsc | Close window
F6 | Focus previous window
F6+Shift | Focus next window
Insert | Add new entry into list
Delete | Delete entry from list
# Troubleshooting
#### WinBox cannot connect to the router's IP address, devices do not show up in the Neighbors list
Make sure that the Windows firewall is set to allow WinBox connections through Private and/or Public network interfaces in the Windows firewall, it can be changed inControl Panel\System and Security\Windows Defender Firewall\Allowed applicationsor disable the Windows firewall.
#### I get an error '(port 20561) timed out' when connecting to routers mac address
Windows (7/8) does not allow mac connection if file and print sharing is disabled.
#### I can't find my device in WinBox IPv4 Neighbors list or MAC connection fails with "ERROR could not connect to XX-XX-XX-XX-XX-XX"
Most of the network drivers will not enable IP stack unless your host device has an IP configuration. Set IPv4 configuration on your host device.
Sometimes the device will be discovered due to caching, but MAC connection will still fail with "ERROR: could not connect to XX:XX:XX:XX:XX:XX