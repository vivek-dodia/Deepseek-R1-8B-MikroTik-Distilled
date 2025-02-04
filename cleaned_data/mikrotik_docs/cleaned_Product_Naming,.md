# Document Information
Title: Product Naming
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/17498146/Product+Naming,

# Content
# Introduction
MikroTik product naming can be confusing at first glance, but all the product codes have a logical explanation and follow a code.
# RouterBOARD productsnaming details
RouterBOARD (short version RB)
<board name> <board features>-<built-in wireless> <wireless card features>-<connector type>-<enclosure type>
# Board Name
Currently, there can be three types of board names:
# Board Features
Board features follow immediately after board name section (no spaces or dashes), except when board name is a word, then board features are separated by space.
Currently used features (listed in the order they are used):
# Built-in wireless details
If the board has built-in wireless, then all its features are represented in the following format:
<band><power_per_chain><protocol><number_of_chains>
```
<band><power_per_chain><protocol><number_of_chains>
```
# Enclosuretype
More Specific types OUT enclosures are:
# Example
# 1 decodeRB912UAG-5HPnDnaming:
# 2 decodeRBD52G-5HacD2HnD-TCnaming:
# 3 decodeC52iG-5HaxD2HaxD-TCnaming:
i - single port power injector without controller
# CloudCoreRouter naming details
CloudCoreRouter (short version CCR) naming consists of:
<4 digit number>-<list of ports>-<enclosure type>
```
<4 digit number>-<list of ports>-<enclosure type>
```
# CloudRouterSwitch and CloudSmartSwitch naming details
CloudRouterSwitch (short version CRS, RouterOS device) CloudSmartSwitch (short version CSS, SwOS device) naming consists of:
<3 digit number>-<list of ports>-<built-in wireless card>-<enclosure type>
```
<3 digit number>-<list of ports>-<built-in wireless card>-<enclosure type>
```
* enclosure type- same as forRouterBOARD products.