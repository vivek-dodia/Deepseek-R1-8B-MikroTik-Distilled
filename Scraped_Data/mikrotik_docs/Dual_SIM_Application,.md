---
title: Dual SIM Application
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/240156741/Dual+SIM+Application,
crawled_date: 2025-02-02T21:11:30.919269
section: mikrotik_docs
type: documentation
---

## 2Summary3Initial settings4Roaming script example5Failover script example6Setting up scheduler
* 2Summary
* 3Initial settings
* 4Roaming script example
* 5Failover script example
* 6Setting up scheduler
## Summary
The first script example shows how to switch between SIM slots in case mobile roaming is detected for LtAP mini devices. This could be useful for mobile vehicle applications, where cars, buses or trains could drive abroad and should use two SIM cards (one for a home network, other for a roaming network). Since RouterOS has a roaming status in the LTE monitor (displayed only when roaming) we can use this in RouterOS scripts to change SIM cards accordingly.
The second script example shows how to switch between the SIM cards in case a mobile connection is lost on the currently selected one.
Note:Keep in mind that these are just examples of how to utilize dual SIM slots. For real-life production environments, proper testing should be carried out, so try to optimize them and add new features according to your needs.
## Initial settings
First, make sure you have correctly set up LTE network parameters (provided by the mobile network operator) for each SIM card. You can use the default APN profile or create two separate ones, follow this link -LTE#Quicksetupexample. This example uses the default APN profile.
After that, enable data roaming for connecting to other countries data-providers with the following command. This allows us to keep track of roaming status.
```
/interface lte set [find name=lte1] allow-roaming=yes
```
Then, choose which SIM slots will be used for home and roaming networks. In this example, we use slot "down" for home and slot "up" for roaming network. Use the following command to switch between active slots.Note:command for sim slot selection changes in v6.45.1. And some device models like SXT, have SIM slots named "a" and "b" instead of "up" and down"
Command for pre 6.45.1:
```
/system routerboard sim set sim-slot=down
```
Command after 6.45.1:
```
/system routerboard modem set sim-slot=down
```
Command in RouterOS v7 version:
```
/interface lte settings set sim-slot=down
```
After changing SIM slots, LTE modem will be restarted. It can take some time (depending on the modem and board around 30 seconds) to fully initialize it, so make sure you test your modem.
## Roaming script example
Now create a script that will run with a scheduler. This script will go through a few key points:
* Check if the LTE interface is initialized (shown in/interface lte), otherwise, try a power reset
* Check if an LTE connection is established (the interface is in a "running" state), otherwise create a log entry and simply wait for the next scheduler
* Read the currently used LTE slot and decide whether to change SIM slots based on roaming status
```
/interface lte
```
Let's call this script "roamingScript", and see below the source:
```
{
# Setup and read current values, "up" SIM slot will be used for roaming, "down" for home network
:global simSlot [/system routerboard sim get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60
# Wait for LTE to initialize for maximum "timeoutLTE" seconds
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface lte find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}
# Check if LTE is initialized, or try power-reset the modem
:if ($isLTEinit=true) do={
    # Wait for LTE interface to connect to mobile network for maximum "timeoutConnet" seconds
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface lte get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # Check if LTE is connected
    if ($isConnected=true) do={
        :local Info [/interface lte monitor lte1 once as-value]
        :local isRoaming ($Info->"roaming")
        # Check which SIM slot is used
        :if ($simSlot="down") do={
            # If "down" (home) slot, check roaming status
            :if ($isRoaming=true) do={
                :log info message="Roaming detected, switching to SIM UP (Roaming)"
                /system routerboard sim set sim-slot=up
            }
        } else={
            # Else "up" (roaming) slot, check roaming status
            :if (!$isRoaming=true) do={
                :log info message="Not roaming, switching to SIM DOWN (Home)"
                /interface lte settings set sim-slot=down
            }
        }
    } else={
        :log info message="LTE interface did not connect to network, wait for next scheduler"
    }
} else={
    :log info message="LTE modem did not appear, trying power-reset"
    /system routerboard usb power-reset duration=5s
}
}
```
## Failover script example
Now create a script that will run with a scheduler. This script will go through a few key points:
* Check if the LTE interface is initialized (shown in/interface lte), otherwise, try a power reset
* Check if an LTE connection is established (the interface is in a "running" state), otherwise, create a log entry and simply wait for the next scheduler
* Read the currently used LTE slot and make a decision whether to change SIM slots based on interface status
```
/interface lte
```
Note:Keep in mind that the SIM slot will only be changed if the current one is not able to connect to the network if you need to switch back to the main SIM card you need to schedule another action that does it at a certain time. It is not possible to know if the other SIM card is in service without switching back to it.
Let's call this script "failoverScript", and see below the source:
```
{
# Setup and read current values
:global simSlot [/system routerboard modem get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60
# Wait for LTE to initialize for maximum "timeoutLTE" seconds
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface lte find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}
# Check if LTE is initialized, or try power-reset the modem
:if ($isLTEinit=true) do={
    # Wait for LTE interface to connect to mobile network for maximum "timeoutConnet" seconds
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface lte get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # Check if LTE is connected
    if ($isConnected=false) do={
    # Check which SIM slot is used
        :if ($simSlot="down") do={
            # If "down" slot, switch to up
        :log info message="LTE down, switching slot to UP"
            /interface lte settings set sim-slot=up
    }
        :if ($simSlot="up") do={
            # If "up" slot, switch to down
        :log info message="LTE down, switching slot to DOWN"
            /interface lte settings set sim-slot=down
            }
        } else={
            # Else "running"
            :if ($isConnected=true) do={
                :log info message="LTE UP"
            } else={
        :log info message="LTE interface did not connect to network, wait for next scheduler"
        }
    } 
    } else={
    :log info message="LTE modem did not appear, trying power-reset"
    /system routerboard usb power-reset duration=5s
}
}
```
```
{
# Setup and read current values
:global simSlot [/system routerboard modem get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60
# Wait for LTE to initialize for maximum "timeoutLTE" seconds
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface lte find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}
# Check if LTE is initialized, or try power-reset the modem
:if ($isLTEinit=true) do={
    # Wait for LTE interface to connect to mobile network for maximum "timeoutConnet" seconds
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface lte get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # Check if LTE is connected
    if ($isConnected=false) do={
    # Check which SIM slot is used
        :if ($simSlot="down") do={
            # If "down" slot, switch to up
        :log info message="LTE down, switching slot to UP"
            /interface lte settings set sim-slot=up
    }
        :if ($simSlot="up") do={
            # If "up" slot, switch to down
        :log info message="LTE down, switching slot to DOWN"
            /interface lte settings set sim-slot=down
            }
        } else={
            # Else "running"
            :if ($isConnected=true) do={
                :log info message="LTE UP"
            } else={
        :log info message="LTE interface did not connect to network, wait for next scheduler"
        }
    } 
    } else={
    :log info message="LTE modem did not appear, trying power-reset"
    /system routerboard usb power-reset duration=5s
}
}
```
## Setting up scheduler
Last, create your scheduler that will run the previously created script. Choose a proper scheduler interval, so two or more events do not overlap with each other. For this example above, 3 minutes will be enough.
```
/system scheduler add interval=3m on-event=roamingScript name=Roaming
```
```
/system scheduler add interval=3m on-event=failoverScript name=Failover
```
Keep in mind that a "home" SIM card will consume some roaming data because changing SIM slots does not happen instantly.