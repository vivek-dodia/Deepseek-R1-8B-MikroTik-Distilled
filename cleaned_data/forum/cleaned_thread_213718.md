# Thread Information
Title: Thread-213718
Section: RouterOS
Thread ID: 213718

# Discussion

## Initial Question
Hi, referring to this official downgrade procedure here...https://help.mikrotik.com/docs/spaces/R ... g+RouterOS...I am wondering if this also applies if I want to downgrade from a ROS >=7.13 to 7.12.x or earlier, as there were significant changes regarding the packages?Cheers ---

## Response 1
As the documentation states, you can always downgrade. But not below factory installed version.What does/system/resource/printshow? ---

## Response 2
You can, given restrictions as indicated above.If it's a device with wifi radio, you need to take care adding the correct wireless/wifi package. That's where the biggest difference with respect to handling of packages is with that version. ---

## Response 3
Thanks for your replies! Factory-installed version is an old 6.44, so this is definitely not a problem. I was only wondering regarding pre/post 7.13 as the structure of the packages was highly modified starting with 7.13.If you UPGRADE from 7.10 to 7.13+ for instance, you have to go through 7.12 as per the release notes. This is why I was wondering if there was maybe a specific downgrade path as well. ---

## Response 4
That's because in 7.12 all hooks are present to have an upgrade to 7.13 use "automagically" the correct packages for wifi or wireless.Even so magically that on a simple switch wireless is also loaded when passing towards 7.13 ---

## Response 5
I tried, unfortunately the wireless package is not available for public download for 7.12 and earlier (and I got the "system, error: missing package wireless" log entry). So for the moment I'm stuck with 7.13 and can't go earlier.I will need to contact support and see if they can send me a link. ---

## Response 6
Could be some config hooks from post-7.13 are still hanging around.What device are you downgrading ?Already tried with netinstall (in order to be sure there is no backdoor config hanging around from whatever version) ? Make sure to export your current config first (and verify it is complete) !! ---

## Response 7
The device I'm trying to downgrade is a LtAP mini RB912R-2nD-LTm revision 3.Nope, I only tried to downgrade it from the GUI/CLI, not with netinstall (yet). As I am not physically at the device's location, I'd like to exhaust the easy options first.Yes, I always have up-to-date (and tested!) config backups and exports at hand. ---

## Response 8
SOLVED, I found a way around:before downgrading from 7.13 to a pre-7.12 version, you have to remove the wireless package using the following command:/system/package/uninstall wirelessthen, you have to reboot, and only after this step you can upload the ros .npk files and perform the downgrade using the following command:/system/package/downgrade ---

## Response 9
Good catch !Any specific reason why you want to downgrade ? ---

## Response 10
Thx! (I hope this procedure will also help others in the future).Regarding the reasons for the downgrade:1) I like to have all production devices running the same version, which is, in my case, 7.11.3 for the time being. I am still craving for a ROS7 long-term to be released...2) I always read the release notes carefully, and as long as I don't need new features and there are no related bug or security fixes in the new firmware that would apply to my infrastructure, there is no point of upgrading. Security fixes aside, I always prefer proven stability (for my specific environment) over new versions full of new features and inevitably, new undocumented bugs.3) I do test newer versions on non-critical devices from time to time. This is why I was running 7.16 on the LtAP mini RB912R-2nD-LT, but I experienced some nasty bugs with the script execution (which kinda prouves my point 2), so I had to roll-back. ---

## Response 11
Only as a side note, it is refreshing to see someone that reasonably does not upgrade to latest-latest (your point #2) the "production" machines.Bravo!I understand how the forum is largely populated by people that like to experiment and tinker with Mikrotik newish releases, but often upgrading to latest-latest is advised to newcomers without any real reason.The way the release notes are made does not help, but the "if it ain't broke don't fix it" approach has traditionally given better results than the "let's try this new hip thing" ---

## Response 12
I too wish there was a long-term channel, since I too like more time after "stable" before upgrading production things... since sometime "stable" isn't quite stable.But I suspect your #3 problem isn't going away, since they have changed some of the permissions scheme (i.e. some scripts need "policy" and/or "test" rights in recent releases), among other subtle changes that may require manual mitigation during upgrade.This is why I was running 7.16 on the LtAP mini RB912R-2nD-LT, but I experienced some nasty bugs with the script execution (which kinda prouves my point 2), so I had to roll-back.So whether they are "bugs" or security/other "fixes" may be a matter of opinion. So you may still want to get to the bottom of the root causes of script errors, since any actual security fixes would likely only go into a "stable" ... since, unfortunately, there isn't a long-term to use if there was a real security patch.Anyway, good work figuring out you needed to remove wireless package to downgrade - logical in hindsight - but not sure I'd figure that one out before giving up and using netinstall. ---

## Response 13
Thanks for your kind words, guys!Well, of course, I completely agree that having it working again now does not mean I should't investigate the root cause. This is now definitely on my task list. But in the meantime, at least I have a stable, running system and I can sleep at night. As you pointed out, the rights/policy have been changed in one of la later releases, I suspect as well this might have something to do with my problem indeed...as said, I need and I will to dig into it.Don't get me wrong, I don't have anything against newer stable or even RC or beta releases. On some lab/test setups, I'm usually running RC's (not only with Mikrotik but for other systems as well). Someone has to "find" bugs in order for the devs to be able to improve the software. The earlier, the better. I truly believe this is a task all users should share, but only on selected systems. It all depends on the risk vs impact, which needs to be analyzed beforehands. In my case, its "production=play it safe" ; "lab=play around with new features and help finding bugs". (And we still have to keep in mind that a Mikrotik RC or even beta is infinitely more stable than any software from consumer-grade home routers!)Even when I was a Cisco Gold-Platinum-Neutron-Star-Double-Rainbow partner, I had the TAC telling me more than once I had to "upgrade the the latest version" to address a specific problem. I always asked (kindly, of course) the TAC to provide me with an official statement that this specific bug was addressed in the IOS/NXOS version they wanted me to upgrade to. And guess what, in most cases, it was not. Interestingly, this has always been a starting point for good collaboration and real troubleshooting, and we've always come up with a real solution in the end. Most of the time, it was fixed by an intermediate release, and in some cases I had found new bugs that had to be fixed in a completely new release.I had a focus on industrial system engineering during my studies, and this "always-get-the-latest-stuff" may be good enough for all-purpose usage (and to increase sales), but believe me, I've seen highly critical system work on old, reliable machines. As an example, I have a client who is still running a critical infra in a harsh environment over BEST Ferrups UPS systems from the late 80s (long before the Eaton era), which they even service in-house. And they run like a charm. And on a more personal topic, I'm still driving a '94 Mercedes on a daily basis with over 650.000km on the clock, and I'm not even thinking about replacing it...guess why ---

## Response 14
Well, I have just replaced in december (with a Mikrotik Ax Lite) a self-made router (a repurposed Fujitsu Siemens S200 running Zeroshell) that had been ticking 24/7 since 2012.The actual device was produced in 2004 or so, processor is Transmeta!I originally got one of these on the cheap (like 20 Euro or so, intending to use it as a silent media server at home.Then suddenly I needed (like on a saturday afternoon) a router at the office and slapped in it a no-name ehernet card and Zeroshell.After an initial nightmare to get the hang on the way zeroshell works it replaced (temporariily) a (largely under-used) Cisco.But it worked so well (for the very simple needs) that I got another one (as spare and to test new releases) and it just became definitive.Only a couple CF-cards replacements in these years. ---