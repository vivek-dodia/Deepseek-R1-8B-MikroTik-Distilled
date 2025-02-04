# Thread Information
Title: Thread-213306
Section: RouterOS
Thread ID: 213306

# Discussion

## Initial Question
Hello, I'm trying to implement Mikrotik VPN login with Windows Server 2022 Active Directory users.Mikrotik model: RB3011 UiASI followed the steps on this page:https://wisp.net.au/forum/t/mikrotik-vp ... WRrLr9Mqf3But it won't let me access the vpn with the active directory user. This error appears:This error means that the VPN is unable to connect to the server. There is no concrete solution, but there are some actions that can be taken to help fix it.Does anyone know what configuration is failing or if I'm missing any other option for it to work correctly?Thanks! ---

## Response 1
The content of that link is wrong what you have to do is configure the ad users to the radius that you configured in the mikrotik and then create an authentication certificate for the l2tp. Otherwise you will not be able to connect from the vpn ---

## Response 2
I followed this and it still works after 5 years (ROS v.6 and Win2022)https://mivilisnet.wordpress.com/2018/1 ... indows-ad/ ---