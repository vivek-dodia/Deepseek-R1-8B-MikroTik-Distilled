# Thread Information
Title: Thread-213337
Section: RouterOS
Thread ID: 213337

# Discussion

## Initial Question
Hello, I was wondering if anyone else ran into this. I am running Beta 14 for MacOS. When adding a comment to an interface, if you aren't paying attention to where you click, you could inadvertently disable the port. Anyway the click to enable/disable a port could be lessened to only the check box area? Or better yet, moved to a different location away from the enable/disable button.If you are in a hurry, you could definitely bring down an entire router. I have attached a picture of the zone that you can click into and it will enable/disable the port.Screenshot 2024-12-17 at 1.05.34 PM.png ---

## Response 1
It's actually common UI behavior, at least in the Windows world, since decades, for checkbox controls placed inside (invisible) grid layout controls. The clickable area of the checkbox spans the whole cell of the "grid". It actually helps with accessibility (people have more difficulty hitting the small area of the checkmark). WinBox 3 behaves like that too, as you can see from this capture:https://imgur.com/lJAeJO4 ---

## Response 2
On either OS it is normal for the active area to encompass the box and its description ( "Enabled" here), not the box and blankness. ---

## Response 3
The "blankness" as you call it, is included in the hit area on other OSes too. Here is a capture from Android:https://imgur.com/ROKWLmeAs you can see, both toggle-boxes (a kind of checkbox) as well as radio-buttons (the single-choice round things) accept hits on the whole width of the layout grid. ---

## Response 4
Yes, with the text included in the active area. “Blankness” referred to without. ---

## Response 5
Mikrotik may want to consider moving the comment box to another location.You guys are correct, in all my years of using Winbox in Wine I have never noticed that you can click outside the check box and still check/un-check it. ---