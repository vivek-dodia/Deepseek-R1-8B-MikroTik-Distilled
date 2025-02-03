---
title: NetFlow analysis with Elasticsearch
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/282132674/NetFlow+analysis+with+Elasticsearch,
crawled_date: 2025-02-02T21:15:16.561190
section: mikrotik_docs
type: documentation
---

# 2Introduction3Prerequisites4Setup4.1Elastic4.2RouterOS5Using Kibana6Log retation6.1Use a different ILM policy
* 2Introduction
* 3Prerequisites
* 4Setup4.1Elastic4.2RouterOS
* 5Using Kibana
* 6Log retation6.1Use a different ILM policy
* 4.1Elastic
* 4.2RouterOS
* 6.1Use a different ILM policy
# Introduction
Elasticsearch is a popular NoSQL database that can be used to store a wide range of data, including NetFlow logs. Alongside with Kibana you can create a powerful tool to analyze NetFlow data from your RouterOS devices. This guide will rely on Elasticsearch integrations and for it to work you need to have a working Elasticsearch setup. This guide will not cover setup instructions for Elasticsearch and Kibana, but will cover the relevant steps to setup NetFlow log collection and analysis.
There are many possible configurations that can be made with Elasticsearch, but for the sake of this guide we will use the following principle:
* A RouterOS (10.0.0.1) device sends out NetFlow data to a server (10.0.0.2) runningNetFlow integration
* The server (10.0.0.2) running NetFlow integration ingests NetFlow data, processes the data and sends it to aFleet Server(10.0.0.3)
* A Fleet Server (10.0.0.3) stores the data inElasticsearch(10.0.0.4)
* Kibana(10.0.0.5) retrieves data from Elasticsearch (10.0.0.4), analyzes it and allows you to search the data
# Prerequisites
* Setup Elasticsearch
* Setup kibana
* Setup Fleet Server
# Setup
The setup instructions are divided into two parts: Elastic (configuration regarding Elasticsearch, Kibana and Fleet Server) and RouterOS (configuration that is relevant to your RouterOS device).
## Elastic
* Log into your Kibana
* Open theFleetsection under the main menu
* Open the "Agent policies" section
* Press "Create agent policy" button tocreate a new Agent Policy
* Give the policy a name, for example, "NetFlow policy", adjust advance settings if required, create the policy
* Open your newly created policy by clicking on it's name
* Press "Add integration"
* Search for "NetfFlow Records" and press "Add NetFlow Records"
* Adjust configuration, make sure:- Specify "UDP host to listen on" to the IP address of your server that is going to run the NetFlow Records integration , in this example the address should be "10.0.0.2"
* Save the integration
* Press the "Add Elastic Agent to your host" button
* Follow the instructions on how to add Elastic Agent to your host
* Make sure you have opened the NetFlow port on your host and elsewhere in the path from your RouterOS device (10.0.0.1), the default destination port is 2055/UDP.
* Your Elastic Agent is now ready to receive NetFlow data!
## RouterOS
* (optional) Create anInterface list(for example, "NetFlow_interfaces") and add interface that need NetFlow data analysis/interface list
add name=NetFlow_interfaces
/interface list member
add interface=VLAN3000 list=NetFlow_interfaces
* ConfigureTraffic-flowto send NetFlow data to your Elastic Agent (10.0.0.2)/ip traffic-flow
enabled=yes interfaces=NetFlow_interfaces
/ip traffic-flow target
add dst-address=10.0.0.2
* You should now start to see NetFlow data being ingested!
* Continue the guide to start using Kibana
```
/interface list
add name=NetFlow_interfaces
/interface list member
add interface=VLAN3000 list=NetFlow_interfaces
```
```
/ip traffic-flow
enabled=yes interfaces=NetFlow_interfaces
/ip traffic-flow target
add dst-address=10.0.0.2
```
# Using Kibana
The NetFlow Records integration provides some useful assets that can be used to analyze NetFlow data. Make sure youinstall the assetsfirst before continuing. The following section will give you some basic ways how to see NetFlow data.
* Log into your Kibana
* Open the "Dashboards" menu in the main menu
* Search the Dashboards and find "NetFlow"
You should now see multiple NetFlow Dashboards. For example, try opening the "[Logs Netflow] Overview". If your NetFlow data is properly ingested, then you should now see graphs that summarizes your traffic.
Another useful Dashboard is the "[Logs Netflow] Flow records", which shows you exact NetFlow records. A very useful feature is the filtering option (the + button on top), that allows you add filters to NetFlow data, for example, you can filter the records to show only a single IP address:
There are other options such as searching for a specific time range. You should read more aboutDiscoverto understand the possibilities better.
For quick reference, these are the fields that you are most likely going to want to use for searching NEtFlow data:
* source.ip
* source.port
* destination.ip
* destination.port
* network.transport
If you want to examine a single record, it is recommended to use theDiscoverview. NetFlow data can be found as "data_stream.dataset: netflow.log".
# Log retation
Depending on your local laws you might be required to store NetFlow data for a specified period of time. Be aware that busy networks can generated a lot of NetFlow data, even terabytes per day. You are most likely going to want to adjustLIfecycle Policy. By default the NetFlow data should go under the "logs" policy. If you have multiple Elasticsearch nodes, you can utilize "phases", which allows you to store data on different types of storage media, but if you only have a single Elasticsearch node, your options are limited and you will most likely want todeleteold data. For example, if you want to delete data after 6 months, then you can simply change the ILM policy to delete data after 6 months or use this API request:
```
PUT _ilm/policy/logs
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_age": "30d",
            "max_primary_shard_size": "50gb"
          },
          "set_priority": {
            "priority": 101
          }
        }
      },
      "delete": {
        "min_age": "180d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
```
## Use a different ILM policy
If you want your NetFlow data to have a different retention period, then you need to do the following steps:
* Create a new ILM policy, give it a new name and set the desired period for the delete phase, or use this API request:PUT _ilm/policy/netflow-logs
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_age": "30d",
            "max_primary_shard_size": "50gb"
          },
          "set_priority": {
            "priority": 101
          }
        }
      },
      "delete": {
        "min_age": "1000d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
* Goto Kibana, open "Stack Management", then go to "Index Management" and then "Component Templates"
* Search for "logs-netflow.log@custom", open it and edit it
* Go to the "Index settings" section
* Paste in the following:{
  "index": {
    "lifecycle": {
      "name": "netflow-logs"
    }
  }
}
* Press "Next" and then "Save component template"
```
PUT _ilm/policy/netflow-logs
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_age": "30d",
            "max_primary_shard_size": "50gb"
          },
          "set_priority": {
            "priority": 101
          }
        }
      },
      "delete": {
        "min_age": "1000d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
```
```
{
  "index": {
    "lifecycle": {
      "name": "netflow-logs"
    }
  }
}
```