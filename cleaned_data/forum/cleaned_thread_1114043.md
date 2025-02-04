# Thread Information
Title: Thread-1114043
Section: RouterOS
Thread ID: 1114043

# Discussion

## Initial Question
Is it possible to configure code 67 within an option set using option matcher? I've observed that unless I specify the boot file name under network settings, the boot file doesn't get applied, while other settings do. I'm seeking advice on how to effectively designate a boot file using either an option matcher or a MAC static lease, as both methods don't seem to be functioning as expected. Any guidance or suggestions would be greatly appreciated. Thank you.mikrotik 7.13rc4/ip dhcp-server optionadd code=60 name=DOCSIS_option value="'docsis'"add code=66 name=TFTPServer value="'100.64.0.1'"add code=67 name=BootFileName value="'20mb.bin'"add code=67 name=Wall value="'wall.bin'"add code=43 name=NTPServer value="'100.64.0.1'"add code=7 name=syslogserver value="'100.64.0.1'"/ip dhcp-server option setsadd name=DOCSIS3Options options=TFTPServer, NTPServer, syslogserver, BootFileNameadd name=Wall options=TFTPServer, Wall, NTPServer/ip pooladd name=dhcp_pool0 ranges=100.64.0.2-100.64.0.254/ip dhcp-serveradd address-pool=dhcp_pool0 interface=bridge1 name=dhcp1/ip dhcp-server matcheradd address-pool=dhcp_pool0 code=60 name=match1 option-set=DOCSIS3Options \value=docsis3.1/ip dhcp-server networkadd address=100.64.0.0/24 boot-file-name=20.bin dns-server=100.64.0.1 gateway=\100.64.0.1/ip tftpadd real-filename=fast.bin req-filename=20.binadd real-filename=wall.bin req-filename=wall.bin/system loggingadd topics=dhcp/system noteset show-at-login=no/system ntp serverset enabled=yes/tool snifferset filter-interface=ether1 filter-stream=yes streaming-enabled=yes \streaming-server=100.64.0.253if I don't set 20.bin the dhcp server network doesn't send the boot file nameas seen below (edited)image.pngdhcp offerimage1.png ---

## Response 1
Maybe, 67 file 20mb.bin and the file is 20.bin? ---

## Response 2
if that was the case 20.bin would in in the DHCP offer but it isn't.going forward assume 20.bin for everything. I did attempt to change it to 20mb.bin but no change. ---

## Response 3
Can anyone verify DHCP option matcher works? And provide a working configuration based on the info I provided? ---

## Response 4
I think you need to provide bootfile name via bootp via this commands.boot-file-name (string; Default: )next-server (IP; Default: )https://wiki.mikrotik.com/wiki/Manual:I ... r#Networks ---

## Response 5
If I want to have dynamic boot files for cable modems, I would like to make use of the mikrotiks built in DHCP options matcher and push next server and boot file. ---

## Response 6
I was finally able to fix the problem last night.apparently bootp need to be set to dynamic and dhcp option 66 has a bug where you have to put the value in hex? the rest of the settings work without an issue with strings. ---

## Response 7
Hello good morning how are you, I hope you are well, I am also trying to get the docsis provisioning to work through mikrotik, I was trying that same config, but I get an error from what I see in the modem log when it asks the configuration file "init(o) - modem ready to download config file" any suggestions? I also tried putting the dhcp option value ip in hexadecimal and I see that it gives me this error in the mikrotik log Unknown(66) = 64-40-00-01Thanks ---