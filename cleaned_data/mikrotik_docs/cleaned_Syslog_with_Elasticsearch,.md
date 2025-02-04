# Document Information
Title: Syslog with Elasticsearch
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/282132697/Syslog+with+Elasticsearch,

# Content
# Introduction
Elasticsearch is a popular NoSQL database that can be used to store a wide range of data, including Syslog data. Alongside with Kibana you can create a powerful tool to analyze Syslog data from your RouterOS devices. This guide will rely on Elasticsearch integrations and for it to work you need to have a working Elasticsearch setup. This guide will not cover setup instructions for Elasticsearch and Kibana, but will cover the relevant steps to setup Syslog data collection and analysis.
There are many possible configurations that can be made with Elasticsearch, but for the sake of this guide we will use the following principle:
# Prerequisites
# Setup
The setup instructions are divided into two parts: Elastic (configuration regarding Elasticsearch, Kibana and Fleet Server) and RouterOS (configuration that is relevant to your RouterOS device).
# Elastic
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
"index": {
"lifecycle": {
"name": "logs"
},
"default_pipeline": "logs-routeros@custom"
}
}
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
logs-routeros@custom
ecs@mappings
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
# RouterOS
set [find where name="remote"] bsd-syslog=yes remote=10.0.0.2 remote-port=5514 syslog-facility=syslog
add action=remote topics=info
add action=remote topics=error
add action=remote topics=critical
add action=remote topics=warning
add action=remote topics=bridge,stp
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
Select operator: IS
Select a value: routeros
```
Select a field: data_stream.dataset
Select operator: IS
Select a value: routeros
```