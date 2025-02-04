# Thread Information
Title: Thread-1116814
Section: RouterOS
Thread ID: 1116814

# Discussion

## Initial Question
I was experimenting with CapMan and for the central controller I loaded the Wireless and QCom package onto a CRS326-24G-2S+. The switch is running RouterOS version 7.16.2 (stable). The Wifi Menu is visible in the Router and I seem to be able to configure CapsMan.Capsman.pngThe issue that I am having is that I want to remove the wireless and qcom packages from the RouterOS but the packages are not listed in the Packages tab.Package.pngThey are also not seen in the CLI.cli.pngHow do I remove the packages from RouterOS now? ---

## Response 1
How do I remove the packages from RouterOS now?If they are not listed under Packages, then they are not installed. New CAPsMAN is included in core (routeros) package since version 7.13 (so running new CAPsMAN doesn't require any optional package). ---

## Response 2
Here is the part in the documentation mentioning this:https://help.mikrotik.com/docs/spaces/R ... i-Overview ---