# Thread Information
Title: Thread-1123006
Section: RouterOS
Thread ID: 1123006

# Discussion

## Initial Question
Hello everyone @ mikrotiki would like to ask uif there is a possibility toget a pure arm64 version of winboxfor raspeberry pi 4 and 5thanks ---

## Response 1
Best to ask support but I guess you will have to revert to using Wine. ---

## Response 2
Best to ask support but I guess you will have to revert to using Wine.wine doesnt worksnative implementation will be nice ---

## Response 3
wine doesnt worksnative implementation will be niceWhy not ? It should work.https://pimylifeup.com/raspberry-pi-win ... 0for%20ARM.Again: ask support. This is a USER forum. MT staff sometimes frequents this place but not always and certainly not everywhere.To be honest: I doubt they will put much effort in it right now, not until ARM64 laptops become a lot more mainstream.Alternatives: use webfig (access via webbrowser)Or SSH, since you're running a PI4 or PI5 you should be familiar with command line, no ?Drawback: you probably can not use MAC access (I'm not even sure you can do that using Wine, never used it myself). ---

## Response 4
wine doesnt worksnative implementation will be niceWhy not ? It should work.https://pimylifeup.com/raspberry-pi-win ... 0for%20ARM.Again: ask support. This is a USER forum. MT staff sometimes frequents this place but not always and certainly not everywhere.To be honest: I doubt they will put much effort in it right now, not until ARM64 laptops become a lot more mainstream.Alternatives: use webfig (access via webbrowser)Or SSH, since you're running a PI4 or PI5 you should be familiar with command line, no ?Drawback: you probably can not use MAC access (I'm not even sure you can do that using Wine, never used it myself).thanks ---

## Response 5
Drawback: you probably can not use MAC access (I'm not even sure you can do that using Wine, never used it myself).It's possible to use winbox over MAC using wine (just tried winbox 3.35 x64 in linux). For CLI over MAC I guess there's no real option now, MT doesn't provide MAC telnet client for windows/linux/whatever. There used to be MAC telnet client, but it only worked until 6.4x or something (when authentication got strengthened). ---

## Response 6
Hello, Winbox 3.xx is currently working quite well on arm64. I'm not a power user on Winbox, but to me all the base feature are working well.To make it work, it's a serious imbrication of emulation !You need to use box64 in order to execute wine-x64 on your arm64 and execute winbox with wine-x64.check this :https://github.com/ptitSeb/box64/blob/m ... X64WINE.mdfor the MAC issue, I think there is a specific right to give to wine in order it can deal with base network features that are only allowed to root. ---

## Response 7
here is a screenshotScreenshot from 2024-12-28 11-35-01.png ---

## Response 8
Now that there is winbox 4 which is native Linux, we shoud be able to run Winbox 4 using directly Box64 (which emulates x64 instruction on arm64) thus getting the rid of the wine64 (which emulate windows on linux) layer.But I'm stuck ! there was some errors at startup regarding some function wrapping with box64, and I could make it go away with the support of box64 dev guy (thanks to him !).Currently Winbox 4 Linux is now launching without errors, but the GUI is not appearing.Screenshot from 2024-12-28 11-49-11.pngThe process stay there until I kill it, showing that it seems to run, but no GUI, no logs, no error message...Maybe I can activate debug log on box64 part and also on winbox part in order to go further.If someone has an idea please tell meIt would be such a bullshit to have to still run Winbox 4 Windows on arm64 using the complete emulation stack despite there is a native Linux App.Let see ---

## Response 9
For CLI over MAC I guess there's no real option now, MT doesn't provide MAC telnet client for windows/linux/whatever. There used to be MAC telnet client, but it only worked until 6.4x or something (when authentication got strengthened).It got fixed, and it works !https://github.com/haakonnessjoen/MAC-Telnet ---