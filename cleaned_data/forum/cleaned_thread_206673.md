# Thread Information
Title: Thread-206673
Section: RouterOS
Thread ID: 206673

# Discussion

## Initial Question
Dear All, I am using firmware 7.14.2 on routerboard model RB750Gr3 with firmware type mt7621LSince that version the table with the firewall rules ( IPv4 and IPv6 ) is almost unusable because of a strange column width layout.The third column (#) with the rule numbers is extremely wide, but the fourth column (Comment) is to too narrow.I testet with Chrome and Firefox with the latest version. In both browsers the same behaviour.Hopefully soon a fix in the next version.Kind regardsHans ---

## Response 1
You can change the webfig behavior if you want, just click here:Design skindesign.png ---

## Response 2
You should also be able to change the width of each column yourself? Hover with your mouse between two column headers, note that the mouse pointer turns into a double arrow and then drag left/right while holding the left mouse button to change the column width.If that doesn't work maybe one of stylesheets or scripts got blocked by your browser for whatever reason? Or maybe try incognito mode to make sure it doesn't use a corrupted browser cache.. ---

## Response 3
I have also seen this new thing in some of the settings menus.There you can expand the view.expand.pngMaybe Mikrotik has forget to add these in some menus. ---

## Response 4
Use Winbox and there will be no problems.https://mikrotik.com/download ---

## Response 5
Thanks to all for these hints.I cleared the cache, it worked. But then the issue came back.Working within an incognito window seems to be one solution.// Hans-- ---

## Response 6
Who uses Webfig? Just use SSH or API in production and Winbox at home. ---

## Response 7
One reason to use webconfig is to see memory leakage? ---

## Response 8
Also incognito window does not help. It looks ok when opening fresh but after a time the column width is destroyed.Changing the design skin does not solve the issue too.But this was not always so. It came with one of the last updates.As it's annoying I hope for a fix with an upgrade.// Hans-- ---

## Response 9
You don't like winbox so much? Use it and you won't have any problems. ---

## Response 10
You don't like winbox so much? Use it and you won't have any problems.I can't say.I am using a macbook with macOS. And winbox seems to be for MS.Sorry.// Hans-- ---

## Response 11
I just upgraded to Version 7.14.3But still the same issue.// Hans-- ---

## Response 12
Problem now fixed: firmware 7.17I think it was already fixe in 7.16.? or older.The new gui needs some habituation, but nice.// Hans-- ---