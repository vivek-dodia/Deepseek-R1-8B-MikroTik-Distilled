---
title: Syslog with Elasticsearch
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/282132697/Syslog+with+Elasticsearch,
crawled_date: 2025-02-02T21:14:59.319058
section: mikrotik_docs
type: documentation
---

* 1Introduction
* 2Prerequisites
* 3Setup3.1Elastic3.2RouterOS
* 4Using Kibana
* 3.1Elastic
* 3.2RouterOS
# Introduction
Elasticsearch is a popular NoSQL database that can be used to store a wide range of data, including Syslog data. Alongside with Kibana you can create a powerful tool to analyze Syslog data from your RouterOS devices. This guide will rely on Elasticsearch integrations and for it to work you need to have a working Elasticsearch setup. This guide will not cover setup instructions for Elasticsearch and Kibana, but will cover the relevant steps to setup Syslog data collection and analysis.
There are many possible configurations that can be made with Elasticsearch, but for the sake of this guide we will use the following principle:
* A RouterOS (10.0.0.1) device sends out NetFlow data to a server (10.0.0.2) runningCustom UDP logs
* The server (10.0.0.2) running Custom UDP logs integration ingests Syslog data, processes the data and sends it to aFleet Server(10.0.0.3)
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
* Give the policy a name, for example, "Syslog policy", adjust advance settings if required, create the policy. Or you can use the API request below:sadsPOST kbn:/api/fleet/agent_policies
{
  "name": "Syslog policy",
  "description": "",
  "namespace": "default",
  "monitoring_enabled": [
    "logs",
    "metrics"
  ],
  "inactivity_timeout": 1209600,
  "is_protected": false
}
* Open your newly created policy by clicking on it's name
* Press "Add integration"
* Search for "Custom UDP logs" and press "Add Custom UDP logs"
* Adjust configuration, make sure:- Specify "Listen Address" to the IP address of your server that is going to run the Custom UDP logs integration , in this example the address should be "10.0.0.2"- Set "Listen Port" to "5514"- Set" Dataset name" to "routeros"- Set "Ingest Pipeline" to "logs-routeros@custom"- Set "Syslog Parsing" to "Yes"
* Save the integration
* Press the "Add Elastic Agent to your host" button
* Follow the instructions on how to add Elastic Agent to your host
* Go to "Stack Management" on the main menu, then open "Ingest Pipelines"
* Create a new Ingest Pipeline by pressing "Create pipeline" then "New pipeline"
* Set "Name" to "logs-routeros@custom"
* Press "Import processors" and paste the following processors:[
  {
    "grok": {
      "field": "message",
      "patterns": [
        "^first L2TP UDP packet received from %{IP:source.ip}$",
        "^login failure for user %{USERNAME:user.name} from %{IP:source.ip} via %{DATA:service.name}$",
        "^%{USERNAME:user.name} logged in, %{IP:client.ip} from %{IP:source.ip}$",
        "^dhcp alert on %{DATA}: discovered unknown dhcp server, mac %{MAC:source.mac}, ip %{IP:source.ip}$",
        "in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport} \\(%{DATA}\\), %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
        "in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport}, %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
        "^%{DATA:network.name} (deassigned|assigned) %{IP:client.ip} for %{MAC:client.mac} %{DATA}$",
        "^%{DATA:user.name} logged out, %{INT:event.duration} %{INT} %{INT} %{INT} %{INT} from %{IP:client.ip}$",
        "^user %{DATA:user.name} logged out from %{IP:source.ip} via %{DATA:service.name}$",
        "^user %{DATA:user.name} logged in from %{IP:source.ip} via %{DATA:service.name}$",
        "^%{DATA:network.name} client %{MAC:client.mac} declines IP address %{IP:client.ip}$",
        "^%{DATA:network.name} link up \\(speed %{DATA}\\)$",
        "^%{DATA:network.name} link down$",
        "^user %{DATA:user.name} authentication failed$",
        "^%{DATA:network.name} fcs error on link$",
        "^phase1 negotiation failed due to time up %{IP:source.ip}\\[%{INT:source.port}\\]<=>%{IP:destination.ip}\\[%{INT:destination.port}\\] %{DATA}:%{DATA}$",
        "^%{DATA:network.name} (learning|forwarding)$",
        "^user %{DATA:user.name} is already active$",
        "^%{GREEDYDATA}$"
      ]
    }
  },
  {
    "lowercase": {
      "field": "network.transport",
      "ignore_missing": true
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "authentication"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(login failure for user|logged in from|logged in,)/",
      "ignore_failure": true,
      "description": "Enrich logon events"
    }
  },
  {
    "append": {
      "field": "event.outcome",
      "value": [
        "success"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(logged in from|logged in,)/",
      "ignore_failure": true,
      "description": "Enrich successful login events"
    }
  },
  {
    "append": {
      "field": "event.outcome",
      "value": [
        "failure"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(login failure for user)/",
      "ignore_failure": true,
      "description": "Enrich failed login events"
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "network"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /( fcs error on link| link down| link up)/",
      "ignore_failure": true,
      "description": "Enrich network events"
    }
  },
  {
    "append": {
      "field": "event.outcome",
      "value": [
        "failure"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /( fcs error on link)/",
      "ignore_failure": true,
      "description": "Enrich network failures"
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "session"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(logged out)/",
      "ignore_failure": true
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "threat"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(from address that has not seen before)/",
      "ignore_failure": true
    }
  },
  {
    "append": {
      "field": "service.name",
      "value": [
        "l2tp"
      ],
      "if": "ctx.message =~ /(^L2TP\\/IPsec VPN)/",
      "ignore_failure": true
    }
  },
  {
    "geoip": {
      "field": "source.ip",
      "target_field": "source.geo",
      "ignore_missing": true,
      "ignore_failure": true
    }
  },
  {
    "geoip": {
      "field": "destination.ip",
      "target_field": "destination.geo",
      "ignore_missing": true,
      "ignore_failure": true
    }
  },
  {
    "geoip": {
      "field": "client.ip",
      "target_field": "client.geo",
      "ignore_missing": true,
      "ignore_failure": true
    }
  }
]
* Press "Save pipeline"
* Go to "Stack Management" on the main menu, then select "Index Management" and then select "Component templates"
* Create a new template by pressing "Create component template".
* Set the "Name" to "logs-routeros@custom"
* Under "Index settings" section, paste the following:{
  "index": {
    "lifecycle": {
      "name": "logs"
    },
    "default_pipeline": "logs-routeros@custom"
  }
}
* Under "Mappings" section, press "Load JSON" and paste the following:{
  "dynamic_templates": [],
  "properties": {
    "service": {
      "type": "object",
      "properties": {
        "name": {
          "type": "keyword"
        }
      }
    },
    "destination": {
      "type": "object",
      "properties": {
        "port": {
          "type": "long"
        },
        "ip": {
          "type": "ip"
        }
      }
    },
    "host": {
      "type": "object",
      "properties": {
        "ip": {
          "type": "ip"
        }
      }
    },
    "client": {
      "type": "object",
      "properties": {
        "ip": {
          "type": "ip"
        },
        "mac": {
          "type": "keyword"
        }
      }
    },
    "source": {
      "type": "object",
      "properties": {
        "geo": {
          "type": "object",
          "properties": {
            "continent_name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "region_iso_code": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "city_name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "country_iso_code": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "country_name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "location": {
              "type": "geo_point"
            },
            "region_name": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "as": {
          "type": "object",
          "properties": {
            "number": {
              "type": "long"
            },
            "organization": {
              "type": "object",
              "properties": {
                "name": {
                  "ignore_above": 1024,
                  "type": "keyword",
                  "fields": {
                    "text": {
                      "type": "match_only_text"
                    }
                  }
                }
              }
            }
          }
        },
        "address": {
          "ignore_above": 1024,
          "type": "keyword"
        },
        "port": {
          "type": "long"
        },
        "domain": {
          "ignore_above": 1024,
          "type": "keyword"
        },
        "ip": {
          "type": "ip"
        },
        "mac": {
          "type": "keyword"
        }
      }
    },
    "event": {
      "type": "object",
      "properties": {
        "duration": {
          "type": "long"
        },
        "category": {
          "type": "keyword"
        },
        "outcome": {
          "type": "keyword"
        }
      }
    },
    "message": {
      "type": "match_only_text"
    },
    "user": {
      "type": "object",
      "properties": {
        "name": {
          "type": "keyword"
        }
      }
    },
    "network": {
      "type": "object",
      "properties": {
        "bytes": {
          "type": "long"
        },
        "name": {
          "type": "keyword"
        },
        "transport": {
          "type": "keyword"
        }
      }
    },
    "tags": {
      "ignore_above": 1024,
      "type": "keyword"
    }
  }
}
* Press "Next" and then press "Save component template"
* Go to "Stack Management" on the main menu, then select "Index Management" and then select "Index templates"
* Create a new template by pressing "Create template"
* Set the "Name" to "logs-routeros"
* Set "Index patterns" to "logs-routeros-*"
* Under "Component templates" section add the following templates to your new Index template:logs@settings
logs-routeros@custom
ecs@mappings
* Press "Next" and then "Save template"
* Make sure you have opened the 5514/UDP port on your host and elsewhere in the path from your RouterOS device (10.0.0.1).
* Your Elastic Agent is now ready to receive Syslog data!
```
POST kbn:/api/fleet/agent_policies
{
  "name": "Syslog policy",
  "description": "",
  "namespace": "default",
  "monitoring_enabled": [
    "logs",
    "metrics"
  ],
  "inactivity_timeout": 1209600,
  "is_protected": false
}
```
```
[
  {
    "grok": {
      "field": "message",
      "patterns": [
        "^first L2TP UDP packet received from %{IP:source.ip}$",
        "^login failure for user %{USERNAME:user.name} from %{IP:source.ip} via %{DATA:service.name}$",
        "^%{USERNAME:user.name} logged in, %{IP:client.ip} from %{IP:source.ip}$",
        "^dhcp alert on %{DATA}: discovered unknown dhcp server, mac %{MAC:source.mac}, ip %{IP:source.ip}$",
        "in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport} \\(%{DATA}\\), %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
        "in:%{DATA} out:%{DATA}, ?(connection-state:%{DATA},|)?(src-mac %{MAC:source.mac},|) proto %{DATA:network.transport}, %{IP:source.ip}:?(%{INT:source.port}|)->%{IP:destination.ip}:?(%{INT:destination.port}|), len %{INT:network.bytes}$",
        "^%{DATA:network.name} (deassigned|assigned) %{IP:client.ip} for %{MAC:client.mac} %{DATA}$",
        "^%{DATA:user.name} logged out, %{INT:event.duration} %{INT} %{INT} %{INT} %{INT} from %{IP:client.ip}$",
        "^user %{DATA:user.name} logged out from %{IP:source.ip} via %{DATA:service.name}$",
        "^user %{DATA:user.name} logged in from %{IP:source.ip} via %{DATA:service.name}$",
        "^%{DATA:network.name} client %{MAC:client.mac} declines IP address %{IP:client.ip}$",
        "^%{DATA:network.name} link up \\(speed %{DATA}\\)$",
        "^%{DATA:network.name} link down$",
        "^user %{DATA:user.name} authentication failed$",
        "^%{DATA:network.name} fcs error on link$",
        "^phase1 negotiation failed due to time up %{IP:source.ip}\\[%{INT:source.port}\\]<=>%{IP:destination.ip}\\[%{INT:destination.port}\\] %{DATA}:%{DATA}$",
        "^%{DATA:network.name} (learning|forwarding)$",
        "^user %{DATA:user.name} is already active$",
        "^%{GREEDYDATA}$"
      ]
    }
  },
  {
    "lowercase": {
      "field": "network.transport",
      "ignore_missing": true
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "authentication"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(login failure for user|logged in from|logged in,)/",
      "ignore_failure": true,
      "description": "Enrich logon events"
    }
  },
  {
    "append": {
      "field": "event.outcome",
      "value": [
        "success"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(logged in from|logged in,)/",
      "ignore_failure": true,
      "description": "Enrich successful login events"
    }
  },
  {
    "append": {
      "field": "event.outcome",
      "value": [
        "failure"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(login failure for user)/",
      "ignore_failure": true,
      "description": "Enrich failed login events"
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "network"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /( fcs error on link| link down| link up)/",
      "ignore_failure": true,
      "description": "Enrich network events"
    }
  },
  {
    "append": {
      "field": "event.outcome",
      "value": [
        "failure"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /( fcs error on link)/",
      "ignore_failure": true,
      "description": "Enrich network failures"
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "session"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(logged out)/",
      "ignore_failure": true
    }
  },
  {
    "append": {
      "field": "event.category",
      "value": [
        "threat"
      ],
      "allow_duplicates": false,
      "if": "ctx.message =~ /(from address that has not seen before)/",
      "ignore_failure": true
    }
  },
  {
    "append": {
      "field": "service.name",
      "value": [
        "l2tp"
      ],
      "if": "ctx.message =~ /(^L2TP\\/IPsec VPN)/",
      "ignore_failure": true
    }
  },
  {
    "geoip": {
      "field": "source.ip",
      "target_field": "source.geo",
      "ignore_missing": true,
      "ignore_failure": true
    }
  },
  {
    "geoip": {
      "field": "destination.ip",
      "target_field": "destination.geo",
      "ignore_missing": true,
      "ignore_failure": true
    }
  },
  {
    "geoip": {
      "field": "client.ip",
      "target_field": "client.geo",
      "ignore_missing": true,
      "ignore_failure": true
    }
  }
]
```
```
{
  "index": {
    "lifecycle": {
      "name": "logs"
    },
    "default_pipeline": "logs-routeros@custom"
  }
}
```
```
{
  "dynamic_templates": [],
  "properties": {
    "service": {
      "type": "object",
      "properties": {
        "name": {
          "type": "keyword"
        }
      }
    },
    "destination": {
      "type": "object",
      "properties": {
        "port": {
          "type": "long"
        },
        "ip": {
          "type": "ip"
        }
      }
    },
    "host": {
      "type": "object",
      "properties": {
        "ip": {
          "type": "ip"
        }
      }
    },
    "client": {
      "type": "object",
      "properties": {
        "ip": {
          "type": "ip"
        },
        "mac": {
          "type": "keyword"
        }
      }
    },
    "source": {
      "type": "object",
      "properties": {
        "geo": {
          "type": "object",
          "properties": {
            "continent_name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "region_iso_code": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "city_name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "country_iso_code": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "country_name": {
              "ignore_above": 1024,
              "type": "keyword"
            },
            "location": {
              "type": "geo_point"
            },
            "region_name": {
              "ignore_above": 1024,
              "type": "keyword"
            }
          }
        },
        "as": {
          "type": "object",
          "properties": {
            "number": {
              "type": "long"
            },
            "organization": {
              "type": "object",
              "properties": {
                "name": {
                  "ignore_above": 1024,
                  "type": "keyword",
                  "fields": {
                    "text": {
                      "type": "match_only_text"
                    }
                  }
                }
              }
            }
          }
        },
        "address": {
          "ignore_above": 1024,
          "type": "keyword"
        },
        "port": {
          "type": "long"
        },
        "domain": {
          "ignore_above": 1024,
          "type": "keyword"
        },
        "ip": {
          "type": "ip"
        },
        "mac": {
          "type": "keyword"
        }
      }
    },
    "event": {
      "type": "object",
      "properties": {
        "duration": {
          "type": "long"
        },
        "category": {
          "type": "keyword"
        },
        "outcome": {
          "type": "keyword"
        }
      }
    },
    "message": {
      "type": "match_only_text"
    },
    "user": {
      "type": "object",
      "properties": {
        "name": {
          "type": "keyword"
        }
      }
    },
    "network": {
      "type": "object",
      "properties": {
        "bytes": {
          "type": "long"
        },
        "name": {
          "type": "keyword"
        },
        "transport": {
          "type": "keyword"
        }
      }
    },
    "tags": {
      "ignore_above": 1024,
      "type": "keyword"
    }
  }
}
```
```
logs@settings
logs-routeros@custom
ecs@mappings
```
## RouterOS
* ConfigureLogging actionsettings on your RouterOS Device (10.0.0.1):/system logging action
set [find where name="remote"] bsd-syslog=yes remote=10.0.0.2 remote-port=5514 syslog-facility=syslog
* AddTopicsthat you wish to receive from RouterOS device (10.0.0.1), for example:/system logging
add action=remote topics=info
add action=remote topics=error
add action=remote topics=critical
add action=remote topics=warning
add action=remote topics=bridge,stp
* You should now start to see Syslog data being ingested!
* Continue the guide to start using Kibana
```
/system logging action
set [find where name="remote"] bsd-syslog=yes remote=10.0.0.2 remote-port=5514 syslog-facility=syslog
```
```
/system logging
add action=remote topics=info
add action=remote topics=error
add action=remote topics=critical
add action=remote topics=warning
add action=remote topics=bridge,stp
```
# Using Kibana
Kibana allows you to search the ingested Syslog data, to see ingested logs do the following:
* Log into your Kibana
* Open "Discover" from the main menu
* Add a filter, use the following parameters:Select a field: data_stream.dataset
Select operator: IS
Select a value: routeros
* For simplicity we recommendsearching for fieldsin the  Discover menu and searching for "message", then adding the field to the view
* We also recommend searching for "log.syslog.hostname" field and adding to the view as well.
* Considersaving the searchfor easier access later
* Done!
```
Select a field: data_stream.dataset
Select operator: IS
Select a value: routeros
```