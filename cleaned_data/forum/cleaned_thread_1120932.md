# Thread Information
Title: Thread-1120932
Section: RouterOS
Thread ID: 1120932

# Discussion

## Initial Question
Hi, This router should be 1700MHz according to the datasheet.Or did i got the fast one?Cheers, Harry
```
[admin@x]/system/resource>printuptime:4m25sversion:7.16.2(stable)build-time:2024-11-2612:09:40factory-software:7.15free-memory:3764.3MiBtotal-memory:4096.0MiBcpu:ARM64
                cpu-count:4cpu-frequency:2000MHzcpu-load:0%free-hdd-space:107.0MiBtotal-hdd-space:128.0MiBwrite-sect-since-reboot:26write-sect-total:22263bad-blocks:0%architecture-name:arm64
               board-name:CCR2004-16G-2S+platform:MikroTik

---
```

## Response 1
Nominal CPU frequency is 1700MHz. But it's possible to overclock it by setting/system/routerboard/settings set cpu-frequency=<value>. Nowdays default setting isautowhich allows ROS to scale frequency up or down depending on CPU core load. Sometimes this doesn't work too well (it takes sone time to scale up and during that period of time router performance lags somehow). ---

## Response 2
I checked it, winbox doesn't show that option.CLI kind of the same:
```
[admin@x]/system/routerboard/settings>setcpu-frequency=1700input doesnotmatch anyvalueofcpu-frequency[admin@x]/system/routerboard/settings>setcpu-frequency=2000input doesnotmatch anyvalueofcpu-frequency[admin@x]/system/routerboard/settings>setcpu-frequency=autoinput doesnotmatch anyvalueofcpu-frequency[admin@x]/system/routerboard/settings>setcpu-frequency=[admin@x]/system/routerboard/settings>Running export doesn't show any changes to the default.I guess its a cosmetic bug.

---
```

## Response 3
If you useset cpu-frequency= and then TABwhat options do you get ? ---

## Response 4
Also check settings in/system/device-mode... Ithinkyou have to enablerouterboardproperty to change cpu frequency setting ... just don't know which particular ROS version started to require that (could be it's 7.17). ---

## Response 5
I get zero options. It like it did not press TAB.If you useset cpu-frequency= and then TABwhat options do you get ? ---

## Response 6
That's a good one.. but it seems i can not see the values. Maybe this is from v7.17 and later.I'm running v7.16.2
```
[admin@x]/system/device-mode>printmode:enterpriseAlso check settings in/system/device-mode... Ithinkyou have to enablerouterboardproperty to change cpu frequency setting ... just don't know which particular ROS version started to require that (could be it's 7.17).

---
```

## Response 7
I'm running v7.16.2Then yeah, you're locked by default.
```
/system/device-mode/update routerboard=yesbeware, you will be forced to reboot- it tells you to unplug power or press button, but pressing button will reboot.After the reboot, you will have settings available in/system/routerboard/set.And if you do/system/device-mode/print, it will say something like:
```

```
mode:enterprise
  routerboard:yes

---
```

## Response 8
HiI have upgrade and change the device mode.But nothing really change still the wrong value and no way to adjust it.Cheers, Harry
```
[admin@MR1]/system/device-mode>printmode:advanced     
     allowed-versions:7.13+,6.49.8+flagged:noflagging-enabled:yes          
            scheduler:yes          
                socks:yes          
                fetch:yes          
                 pptp:yes          
                 l2tp:yes          
       bandwidth-test:yes          
          traffic-gen:nosniffer:yes          
                ipsec:yes          
                romon:yes          
                proxy:yes          
              hotspot:yes          
                  smb:yes          
                email:yes          
             zerotier:yes          
            container:noinstall-any-version:nopartitions:norouterboard:yes          
        attempt-count:0[admin@MR1]/system/device-mode>/system/res
resource     reset-configuration[admin@MR1]/system/device-mode>/system/routerboard/printrouterboard:yes            
             model:CCR2004-16G-2S+revision:r3             
     serial-number:x
     firmware-type:al64           
  factory-firmware:7.15.2current-firmware:7.17upgrade-firmware:7.17[admin@MR1]/system/device-mode>/system/resource/printuptime:2m46sversion:7.17(stable)build-time:2025-01-1608:19:28factory-software:7.15free-memory:3782.0MiBtotal-memory:4096.0MiBcpu:ARM64              
                cpu-count:4cpu-frequency:2000MHzcpu-load:1%free-hdd-space:107.0MiBtotal-hdd-space:128.0MiBwrite-sect-since-reboot:37write-sect-total:40492bad-blocks:0%architecture-name:arm64              
               board-name:CCR2004-16G-2S+platform:MikroTik

---
```

## Response 9
You can't set CPU frequency like this?
```
/system/routerboard/settings/setcpu-frequency=auto(or press <TAB> before enteringautoto see possible values)

---
```