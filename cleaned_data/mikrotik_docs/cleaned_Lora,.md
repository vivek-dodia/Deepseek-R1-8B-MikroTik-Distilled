# Document Information
Title: Lora
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/16351615/Lora,

# Content
Available settings:
# General Properties
Gateways initial steps and different LoRaWAN setup examples:
# Setup
The term "LoRa" represents the "radio" itself ("LoRa payloads" are packets broadcasted by the nodes using the LoRa frequencies), while the term "LoRaWAN" represents a logical/link layer on top, that enables the communication between "LoRa" devices. In other words, "LoRaWAN" is how the "LoRa" radio devices communicate.
R11e-LR8(operates in 863-870 MHz frequency),R11e-LR9(operates in 902-928 MHz frequency) andR11e-LR2(operates using 2.4 GHz frequencies) are concentrator Gateway cards for LoRa® technology in mini PCIe form factor based on Semtech chipset. They enable LoRa® connectivity for any MikroTik product that has mPCIe slot with connected USB lines.
A typical LoRaWAN topology consists of 3 main elements → the server, the node and the gateway. The gateway's job is to simply forward received LoRa packets that are broadcasted by the nodes (within the same supported frequency spectrum) to the server.
MikroTik LoRaWAN gateways are devices that have R11e-LRxminiPCIe card and have "iot"package(which enables LoRa drivers) installed.
The primary design for the MikroTik gateway devices is to operate as LoRaWAN devices. To achieve this, simply configure/select a correct server in the LoRa interface settings. A few examples can be found in thesetup section.
However, if you do not wish to use a LoRaWAN network/topology, and you wish to forward "raw LoRa" payloads to your own server, you have an option to do so. You can useMQTTorHTTP postto forward received payloads to your MQTT/HTTP server, but it will require additionalscripting. The script will have to collect information (payloads) from theIoT>LoRa>Traffictab, store those payloads as variables, structure MQTT/HTTP message out of the variables and post it.
```
IoT>LoRa>Traffic
```