# Document Information
Title: Feature support based on architecture
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/146440194/Feature+support+based+on+architecture,

# Content
All devices support the same features, with a few exceptions, clarified in the below table:
Architecture | Not supported | Exclusively supported
ARM |  | Zerotier, Container, BTH
ARM64 |  | Zerotier, Container, BTH
MIPSBE | Zerotier, Dude server |
MMIPS | Zerotier |
SMIPS | Zerotier, DOT1X, BGP, MPLS, PIMSM, Dude server, User manager |
TILE | Zerotier | BTH
PPC | Zerotier, Dude server |
X86 PC | Zerotier, Cloud | Container
CHR VM |  |
Apart from features, there are also a few differences in hardware capabilities, based on the specific model of device. For these differences, please see the below articles:
Switch chip featureshttps://help.mikrotik.com/docs/display/ROS/Switch+Chip+Features