# Thread Information
Title: Thread-1116114
Section: RouterOS
Thread ID: 1116114

# Discussion

## Initial Question
I have RB5009 and I want to setup Home Assistant there.There is a USB flash installed and used for container
```
[admin@MikroTik]>diskprintFlags:B-BLOCK-DEVICE;M-MOUNTEDColumns:SLOT,MODEL,SERIAL,INTERFACE,SIZE#    SLOT  MODEL                    SERIAL                    INTERFACE                     SIZE0BM usb1KingstonDT microDuo3C408D5CBF8874E7A0895E075AUSB3.205000Mbps248034361344[admin@MikroTik]>I have successfully installed the image
```

```
[admin@MikroTik]>containerexport# 2024-06-24 10:11:11 by RouterOS 7.15.1# software id = 82T1-PVIK## model = RB5009UPr+S+# serial number = XXXXXXXXX/container mountsadddst=/config name=ha_config src=/usb1/ha_config/containeraddenvlist=ha_envinterface=veth2 logging=yes mounts=ha_config root-dir=usb1/ha/container configsetregistry-url=https://registry-1.docker.io tmpdir=/usb1/pull/container envsaddkey=TZ name=ha_envvalue=Europe/Kyiv[admin@MikroTik]>containerprint0name="7d52c00c-6c85-439b-9e52-efdcb90a2842"tag="homeassistant/home-assistant"os=""arch=""interface=veth2 
   envlist="ha_env"root-dir=usb1/ha mounts=ha_config dns=""logging=yes status=stoppedHowever, whatever I do it does not starts...No log records appears when I'm trying to start it.Any ideas how to make it running?

---
```

## Response 1
Have you tried enabling logging "container, debug"? Maybe he'll show what he's missing? ---

## Response 2
Have just logging=yes in the container it salves.Can you give me a hint how to enable debug logging? ---

## Response 3
```
/system loggingaddtopics=container,debug action=memory

---
```

## Response 4
Thank you, but does not helps. No records in log aftercontainer start 0 ---

## Response 5
Also check if all the points specified in this article are followed.https://help.mikrotik.com/docs/display/ ... eAssistant ---

## Response 6
When I'm pulling the image it does shows log records ---

## Response 7
Has the container been downloaded completely? No errors at the end? (this happens sometimes)Is container mode enabled?
```
/system/device-mode/update container=yes

---
```

## Response 8
It it has status "extracting" for a while and I can see how it is pulling layers in the log.Than the status is tiring into "stopped".Sure containers are enabled otherwise I won't be able to pull an image.
```
[admin@MikroTik]>/system/device-modeprintmode:enterprise
  container:yes

---
```

## Response 9
Can you please provide your full configuration?
```
/exportfile=config

---
```

## Response 10
The last message in the log before container status turns to "stop" is
```
getting layer sha256:aa900376fa4645b30a0d731f2962ade576b143016fc7e8b4d4f12bbd34c30fcaIn all other layers such record is followed bydownloadedrecord. But not this one.Previous layers are like this
```

```
getting layer sha256:e0989a23912da051dea50b9091f0c93d4493d425c7b5bd55c88729eaf83b3a08
layer sha256:e0989a23912da051dea50b9091f0c93d4493d425c7b5bd55c88729eaf83b3a08 downloaded

---
```

## Response 11
Also i think your container is not properly deployed, from your recording it is visible that OS and arch is missing.
```
name="7d52c00c-6c85-439b-9e52-efdcb90a2842"tag="homeassistant/home-assistant"os=""arch=""interface=veth2 
   envlist="ha_env"root-dir=usb1/ha mounts=ha_config dns=""logging=yes status=stopped

---
```

## Response 12
Try removing the container completely. Format USB and try again ---

## Response 13
I've had the same problem for months, I've never been able to figure out where the problem was.I tried to format the USB disk also changing the filesystem but nothing to do, it always stops at the same point:mikrotik ha.pngThe file download always stops at 171BI don't know if it's a ROS bug... ---

## Response 14
I'm trying to pullstableimage.Errors a totally random every time.Some times it pulls arch and os and some times it is not.I was trying all formats of the flash. With and without MBR.What is consistent is it is always stuck on this layer.From it's size I can see it is that one
```
40.RUN|1QEMU_CPU=/bin/ash-o295.15MBIn some cases it shows this at the end
```

```
was unable toimport,container8e14971f-a423-4ae1-8b05-d584e1568386

---
```

## Response 15
I had issues with my HASS container not starting on my hAP AX3 and after some debugging I determined that I needed to disable jemalloc which is described here -https://www.home-assistant.io/installat ... imizationsYou can disable it by simply adding the env variable DISABLE_JEMALLOC=1Might not be your case but thought it worth mentioning. Runs fine after this is set for me. ---

## Response 16
You can disable it by simply adding the env variable DISABLE_JEMALLOC=1Thank you, but it doesn't helps in my case.If the flash is formatted with MBD it always ends up witherrorstatus.If the flash is formatted without MBD it always ends up withstoppedstatus and not starts no matter what.(Sure I'm changing path everywhere accordingly usb1/usb1-part1) ---

## Response 17
Try to load as a file. With no luck so far...After command
```
/container/addfile=usb1-part1/docker/ha_stable.tarinterface=veth2 root-dir=/usb1-part1/containers/ha mounts=ha_config envli
st=tz,mem logging=yesI see in the log
```

```
11:42:18container,info,debug importing tar archived image:ha_stable.tar11:42:18container,info,debug error getting layer file11:42:18container,info,debug failed to loadnextentry11:42:18container,info,debugimportfinished butnoimage foundHowever the file created using buildx looks on on the host machine
```

```
docker buildx build--platform linux/arm64-t homeassistant/home-assistant:latest--load.docker save-o ha_stable.tar homeassistant/home-assistant:latest
```

```
➜Downloadstar-tzf ha_stable.tar   
blobs/blobs/sha256/blobs/sha256/089bcd0e76ff34a78b2d3ea7720796a7c78d56e7905166946deb9ecc15aeb883blobs/sha256/0b428f02d932bb619d00cb44e832e90bac821ca585b51a723cfd164c7bb97493blobs/sha256/1ce2b149aa42c9648dea843a1d6a357f243cc98fc6dff3f127ade4a7932977cablobs/sha256/2bcb6d9605f15ca89685e17dea0d85c1ec34d74216f0c0f0cef5556d93534206blobs/sha256/2d9a48781ec1a9e471f32f83780efc4a499e4e5a2d837b8ac10e6c1dd3dfb328blobs/sha256/31da2b26774818938b6809cd3d46d34e1b64273ea84d91364d6d9729b323b8d1blobs/sha256/3df2116198045c13b4a5686e1547dc430d41c029907c83f068b8194a96b24b3cblobs/sha256/3fcdbfacc4a9b25a485e84dfb54712d873b83eda4f7c237135fa60a3b3f41880blobs/sha256/4938e607b6d78689af7fdeb343e7fc955c317ca7ad1345a0992cb8668c18f866blobs/sha256/4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1blobs/sha256/5765303681ca44fd73671d2d677816f9ee76a5f138cba58315544f4e5c597e44blobs/sha256/66b066939690947e97de35014d9346b46f2e7873e20626e99b182bf7273659b0blobs/sha256/6718b0d2600aa668dffa4ac25c5f2d794a5a978bf96d8afc399d788a5e2f32afblobs/sha256/6c1deb6d01089cf88e1d430b154a1d1b58aee580e708f7964fc972ac02770455blobs/sha256/6f5034e08dd7913e475e27e218473a20e6960f071c19db6c5f78eb5ff1e9a82bblobs/sha256/6fef378a8ecbc81681350e322a5e0a135bd4a81e58dffd9c6426bd6bb6b0c5edblobs/sha256/73c5fcf46683d9eca12f93709bc6f49e206bb3f5363c7290878e20b98902c47eblobs/sha256/7510e47ef9afab6c762b8ff4a33af1b5d9204b50ed7d84beee23bf97b08ed5f0blobs/sha256/75aa6da3016aef71bd1d129fe2fb667d240c06bfc611079b30d29cccf53e4ac8blobs/sha256/77024b8c709d61bbdfadde2749d713d23a2fb292112eed377170ab9209588a80blobs/sha256/79f326c1b5bf84081f88d80457cc50d8399c750836c8d89ae5eaa774b5f441a0blobs/sha256/97b8596a4cf5199f4185ce8edfd57ada7a58368d6a7faef1ba5a4b4d0e721eb6blobs/sha256/aa900376fa4645b30a0d731f2962ade576b143016fc7e8b4d4f12bbd34c30fca
blobs/sha256/bac8bb614983e301adbcce34a2c8cda1ee3c05ccafd3724c8bf25fe779f606ca
blobs/sha256/bca4290a96390d7a6fc6f2f9929370d06f8dfcacba591c76e3d5c5044e7f420c
blobs/sha256/bcb19f2aaa8ba275a9b27a2699111c7392c07b2ceec984d99d3ab0a0b002c716
blobs/sha256/c3b6c4007cc2ec1091c55140712b40b9e8fc6c43e261713f6a65e2389ee8211f
blobs/sha256/d0dab9d61593c322f6725686d2bd925a9fa5fc55faad1e75cea7e3345bdc5d97
blobs/sha256/e0989a23912da051dea50b9091f0c93d4493d425c7b5bd55c88729eaf83b3a08
blobs/sha256/e2788bb47bb3bcde9b1f02f81309c24ba64f28d94b5e592bb7d2665ba0f925f7
blobs/sha256/fb64257fde615a7834ae3fb0137d3bafc4411a20fb74d56b99f36d8747d824c6
blobs/sha256/fc06312c1f7a144fec5167a933d18c4e43432dace9386343620095c643e734ae
index.json
manifest.json
oci-layout

---
```

## Response 18
Try to load as a file. With no luck so far...I also tried to load as file a few weeks ago without success... at this point only MikroTik support can help us, have you already created a ticket? ---

## Response 19
..only MikroTik support can help us, have you already created a ticket?No. I do not think they will help with 3rd party software which HA is. ---

## Response 20
Out of curiosity I tried now with a hAP ax3 and it works perfectly!ha2.pngha1.png ---

## Response 21
I checked on hAP ac3 and everything works. Perhaps something with the RB5009, but I don't have it to check ---

## Response 22
It is interesting, is anybody has positive experience installing HA on RB5009? ---

## Response 23
It is interesting, is anybody has positive experience installing HA on RB5009?In a quick test on RB5009 (arm64), I get a layer error (specifically, "error getting layer: resolving error" when downloading a layer). On RB1100Ahx4 (arm/v7), it imports and goes to start.There is a Traefik container that works fine on same RB5009, so /container is enabled/working otherwise. You might want to try an older tag of HA instead of latest, dunno.It should work since Mikrotik specifically documents how to set it up:https://help.mikrotik.com/docs/display/ ... eAssistant ---

## Response 24
Finally make it work...a) Reset docker settingsb) docker pull homeassistant/home-assistant:latest@sha256:17d159928122e6f374bd39b0e75904522bc7d7c2a64e88b248948734e4c4d444 on my host machinec) docker save -o ha_arm64.tard) Upload it to routere) /container/add file="usb1/img/ha.tar" interface="veth1" envlist="envha" cmd="python3 -m homeassistant --config /config" hostname="homeassistant" workdir="/config" root-dir="usb1/containers/homeassistant" mounts="homeassistant" logging=yesNow it works and I can access it.However I have 2 questions to solvea) I need ffmpeg inside of the docker. It eats like it is not there.b) The container is in 10.10.0.1 and all my devices are in 192.168.88.1. And it seams like 10.10.0.1 is not visible from within 192.168.88.1. So I can't add the home assistant as a hub to Apple Home so far.UPDATE:ffmpeg is there but working with some errors. But it is not related to Mikrotik for sure ---

## Response 25
To all:It is not possible to pull the latest image or even stable image of homeassistant for arm64 on Mikrotik RB5009, because the size of image is more then 1.5GB, but the storage on RB5009 is only 1GB, you must change your settings in container to use usb disk for pulling-downloading images:
```
container/config/settmpdir=usb1/pullBest regards!

---
```

## Response 26
Finally make it work...a) Reset docker settingsb) docker pull homeassistant/home-assistant:latest@sha256:17d159928122e6f374bd39b0e75904522bc7d7c2a64e88b248948734e4c4d444 on my host machinec) docker save -o ha_arm64.tard) Upload it to routere) /container/add file="usb1/img/ha.tar" interface="veth1" envlist="envha" cmd="python3 -m homeassistant --config /config" hostname="homeassistant" workdir="/config" root-dir="usb1/containers/homeassistant" mounts="homeassistant" logging=yesNow it works and I can access it.However I have 2 questions to solvea) I need ffmpeg inside of the docker. It eats like it is not there.b) The container is in 10.10.0.1 and all my devices are in 192.168.88.1. And it seams like 10.10.0.1 is not visible from within 192.168.88.1. So I can't add the home assistant as a hub to Apple Home so far.UPDATE:ffmpeg is there but working with some errors. But it is not related to Mikrotik for sureUsing Docker for windows I got the first command to go thru but not the second listed belowdocker pull homeassistant/home-assistant:latest@sha256:17d159928122e6f374bd39b0e75904522bc7d7c2a64e88b24The error I get is:PS C:\Users\allan> docker save -o ha_arm64.tar"docker save" requires at least 1 argument.See 'docker save --help'.Usage: docker save [OPTIONS] IMAGE [IMAGE...]Save one or more images to a tar archive (streamed to STDOUT by default) ---

## Response 27
PS C:\Users\allan> docker save -o ha_arm64.tarEven if "ha_arm64.tar" wasn't bound as the option to the -o flag, making it unavailable to be interpreted as the "IMAGE" argument, it it isn't an "IMAGE" in the context of that command at all. The -o flag names an OCI imagearchive, not the same thing. The "save" command wants the actualinputimage name:
```
docker save-o ha_arm64.tar homeassistant/home-assistant:latestBeware thedocumented limitationsof the HASS container. I faced this decision myself just yesterday, and while I found lack of one-click upgrades of little concern — the container engine handles that for you — lack of add-on support and broken backups doesn't work for me at all. I went with the HAOS VM image instead, now running on my NAS.

---
```

## Response 28
Has anyone found a solution to this problem. The image is showing in usb1/pull as a tar.gzip file, was around 300mb but now showing as 171B.I am using Mikrotik L009 which supports container and advertises that it supports home assistant.I am following the Mikrotik instructions to the letter.Any help would be appreciated. ---

## Response 29
was around 300mb but now showing as 171B.See my previous message:viewtopic.php?t=208697&sid=87d3bc06e309 ... a#p1082019I have the same problem with hAP ac2 and I have never been able to understand the cause. ---

## Response 30
having same problem with caddy image on my hap ax3. worked for almost a year with no problem, but now - it manages to pull container every 5th time, otherwise - error. ---