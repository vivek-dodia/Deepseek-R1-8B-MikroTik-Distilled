# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 210393

# Discussion

## Initial Question
Author: Sat Aug 24, 2024 6:15 pm
Hello all, with the new Wi-Fi drivers we have two options, antenna-gain and tx-power .The first one seems to be self explanatory andantenna-gain=3will lower the antenna gain, second onetx-power=10will limit to 10dBm the device, no matter if this is an hAP ac2 or hAP ax3.Is this correct? ---

## Response 1
Author: [SOLVED]Sat Aug 24, 2024 6:43 pm
Correct, these are the two ways to control signal strength.For antenna gain, you basically have to check the product page and round up to the next integer to get the default value. Each increment from there on will lower signal strength by 1 dB.Tx-power, on the other hand, sets the desired effective max signal strength, taking into account regulatory limits and antenna gain. I.e. especially if you are using different devices with different antennas, this is probably the easier setting to use.