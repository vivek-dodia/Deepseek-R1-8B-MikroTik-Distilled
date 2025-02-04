# Document Information
Title: /routing/fantasy
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/74678282/routing+fantasy,

# Content
Fantasy menu is a fancy way to generate large amount of routes for testing purposes. Main benefits of this approach compared to script is the generation speed and simplicity. It is easy to remove all fantasy generated routes just by disabling fantasy rule.
Fantasy uses random generator from hashed route sequence number, seed and other parameters.
# Configuration Options
Property | Description
----------------------
comment(string) |
count(integer:[0..4294967295]) | How many routes to generate.
dealer-id(start-[end]:: integer:[0..4294967295]) |
disabled(yes | no) | ID reference is not used.
dst-address(Prefix) | Prefix from which route will be generated.
gateway(string) |
instance-id(start-[end]:: integer:[0..4294967295]) |
name(string) | Reference name
offset(integer:[0..4294967295]) | Route sequence number offset
prefix-length(start-[end]::integer:[0..4294967295]) | Prefix length for generated route (can be specified as integer range). For example dst-address 192.168.0.0/16 and prefix-length 24 will generate /24 routes from 192.168.0.0/16 subnet.
priv-offset(start-[end]:: integer: [0..4294967295]) |
priv-size(start-[end]:: integer: [0..100000]) |
scope(start-[end]::integer: [0..255]) | Scope to be set, can be set as range
seed(string) | Random generator seed
target-scope(start-[end]::integer: [0..255]) | Target scope to be set, can be set as range
use-hold(yes | no) |
Property
Description