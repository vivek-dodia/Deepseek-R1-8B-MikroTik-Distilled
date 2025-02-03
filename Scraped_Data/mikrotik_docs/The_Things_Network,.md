---
title: The Things Network
source_url: https://help.mikrotik.com/docs/spaces/ROS/pages/16351627/The+Things+Network,
crawled_date: 2025-02-02T21:14:22.012027
section: mikrotik_docs
type: documentation
---

Once you have installed the lora package on your router and created an account onThe Things Networkyou can set up a running gateway
```
The Things Networkyou can set up a running gateway
```
* Login into your account and go to Console and select Gateways
* Selectregister gatewayand fill in the blank spaces. Gateway EUI can be found in your lora interface
* You will have to manually add the Network Servers, or you can upgrade your router to the stable version6.48.2and these servers will be added automatically (highly recommended)https://wiki.mikrotik.com/wiki/Manual:Upgrading_RouterOS
/lora servers
* After everything is filled press Register Gateway at the bottom of the page. If you have set everything accordingly to the previous steps you should see that your lora gateway is now connected
* At this point everything is set and you have a working lora gateway. You can monitor incoming packets in Traffic section
*Later this year, The Things Network will be migrating to a new version of network server, calledThe Things Stack.