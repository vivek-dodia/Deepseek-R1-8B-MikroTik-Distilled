# Thread Information
Title: Thread-1122196
Section: RouterOS
Thread ID: 1122196

# Discussion

## Initial Question
Hello everyone, I'm having trouble setting up a hotspot using my Mikrotik RB951Ui-2HnD router with version 7.17. I've encountered an issue that differs from the behavior when using version 6.4X.When setting up a hotspot on this device with version 6.4X, after creating it in the Files section, I can see a default "hotspot" file appear. However, when upgrading to versions 7.12 and 7.17, there is no such file directory present, even though I upload my custom hotspot theme with the same filename "hotspot". The issue persists regardless of whether I update the HTML directory or change it on server profiles.One workaround I've discovered involves editing the Server Profiles tab. When changing the HTML directory to just "hotspot", it will set to "flash/hotspot". the theme always returns to the default mikrotik. and if I change it on "Servers" (double click "hotspot1" and choose 'Profile' section) changed to "default" the theme display can change to custom theme.Can anyone help me figure out why this happens and is this a bug??Screen recording is in the link belowhttps://drive.google.com/drive/folders/1p4ab_hgc4-Cj9xT93fEHz_RbBZuWfAIN?usp=drive_link ---

## Response 1
I am also facing the same problem. ---

## Response 2
maybe we need to wait for the next update, and you can use the method below ---

## Response 3
I am also facing the same problem.After searching, I found a temporary solution. For those whose MikroTik routers do not have a flash directory, you just need to create it manually and place the "hotspot" directory files inside it. If you want to revert to the default theme settings, you need to delete the hotspot server as well as its flash directory and make new one.Note: The flash directory usually appears on older MikroTik routers. In newer MikroTik routers, most of the flash folders are missing or hidden. ---