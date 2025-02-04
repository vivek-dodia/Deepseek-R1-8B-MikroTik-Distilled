# Thread Information
Title: Thread-1116148
Section: RouterOS
Thread ID: 1116148

# Discussion

## Initial Question
Hello everyone am new here, I'm trying to configure my rb951 to access Internet from ISP router but after setting the static IP ( 192.168.100.100/24) and checking routes and when I try to ping google.com it displays this "admin@MikroTik] > pingwww.google.cominvalid value for argument address:invalid value of mac-address, mac address requiredinvalid value for argument ipv6-addresswhile resolving ip-address: could not get answer from dns server of" ---

## Response 1
Please share the config to get some relevant feedback:
```
/exportfile=anynameyoulikeRemove serial and any other private info, post between code tags by using the </> button.

---
```

## Response 2
I'm trying to configure my rb951 to access Internet from ISP router but after setting the static IP ( 192.168.100.100/24) and checking routes and when I try to ping google.comDoes your ISP support DHCP as means of obtaining IP config for clients? If it does, then use it, it's usually less error-prone than static setup.According to error messages you posted it's likely that you didn't set IP address(es) of DNS servers for router to use. ---