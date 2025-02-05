# Repository Information
Name: mtikrtr

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/wymillerlinux/mtikrtr.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2017 Wyatt Miller
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
# mtikrtr
Configure basic settings on a MikroTik router.
Settings you can configure:
  * Network name (SSID)
  * Password (WPA, WPA2)
  * 2.4Ghz channels
Tested equipment:
  * hAP lite
To run, enter the current directory and run:
`python3 sandbox.py`
If you have any problems, email me or fix it yourself and send in your commits to the `dev` branch and make a PR. Commits on master will not be accepted unless through supreme authority (aka me).
If you would like to add tested equipment, email me as well and we can discuss things!
================================================

File: sandbox.py
================================================
'''
EZ Mikrotik Configuration
Created by Wyatt J. Miller (wjmiller2016@gmail.com), copyright 2017
Licensed by the MIT license (https://opensource.org/licenses/MIT)
Initially created for 186networks, formerally COLI Communications
What this script tries to do is download, configure, and upload a Mikrotik
configuration script the simpliest way possible. An easy way for the non-tech
savvy like my friend that not shall be named.
Modify this script to your liking.
'''
import os
import sys
import time
from ftplib import FTP
from paramiko import SSHClient, AutoAddPolicy
# whatfile = configure.rsc
def welcomeScreen():
    clearScreen()
    print(" - ---------------------- - ")
    print("- -MIKROTIK ROUTER CONFIG- -")
    print(" - ---------------------- - ")
    print()
    print("Welcome to the Mikrotik router config page!")
    print("Wyatt J. Miller 2017, MIT")
    print()
    continuePrompt()
    mainMenu()
def mainMenu():
    clearScreen()
    headerInfo("Main Menu")
    print("Please enter the corresponding number for the option you wish")
    print("to execute.")
    print()
    print("1) Configure")
    print("2) Credits")
    print("3) Exit")
    numberChoose = input("ENTER A FIGURE: ")
    if (numberChoose == "1"):
        headsUp()
    elif (numberChoose == "2"):
        madeByMe()
    elif (numberChoose == "3"):
        exitSuccess('0')
    else:
        print("You didn't enter a correct figure!")
        continuePrompt()
        mainMenu()
def sshApply():
    clearScreen()
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.load_system_host_keys()
    # making sure all SSH connections to the router are closed
    ssh.close()
    ssh.connect("192.168.88.1", 22, "admin", "")
    print("Connected via SSH!")
    time.sleep(1)
    print("Applying configuration...")
    time.sleep(3)
    print("Restarting router...")
    time.sleep(3)
    ssh.exec_command("/system reset-configuration run-after-reset=configure.rsc", timeout=64)
    ssh.close()
    print("Disconnected from SSH!")
    time.sleep(3)
def sshConfigure():
    clearScreen()
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.load_system_host_keys()
    # making sure all SSH connections to the router are closed
    ssh.close()
    ssh.connect("192.168.88.1", 22, "admin", "")
    ssh.exec_command("/export file=configure.rsc")
    print("Waiting for configuration file to generate...")
    time.sleep(20)
    ssh.close()
def madeByMe():
    clearScreen()
    headerInfo("Credits")
    print("Crafted by Wyatt J. Miller, copyright 2017")
    print("Inspiration was from Shaun Medvec")
    print("Initially made for 186networks, formerlly COLI Communications")
    print("http://www.186networks.net/")
    print("Licensed by MIT, https://opensource.org/licenses/MIT")
    print()
    continuePrompt()
    mainMenu()
def continuePrompt():
    input("Press the Enter key to continue... ")
def headerInfo(header):
    print(header)
    print()
def headsUp():
    clearScreen()
    headerInfo("Caution: A note for the non-tech savvy (aka Gavin)")
    print("Before cotniuing, there is some things you have to")
    print("do to your network interface. First, set the network interface to DHCP.")
    print("Second, plug the cable into said network interface and ports 2, 3 or")
    print("4 of the Mikrotik router. Third, make sure the network interface is")
    print("enabled. Lastly, reset the configuration in the router!")
    print("If you get any error codes, look in the Credits option.")
    print("If everything is set, then...")
    print()
    continuePrompt()
    downloadConfig()
def configOptions(appFile):
    clearScreen()
    headerInfo("Option Settings")
    networkName = input("Please enter the network name (SSID): ")
    wirelessPasskey = input("Please enter the passkey (WPA, WPA2): ")
    print("Please choose from the 802.11 channels: 1 (2.412Ghz), 2 (2.417Ghz),")
    channels = input("3 (2.422Ghz), 4 (2.427Ghz), 5 (2.432Ghz), 6 (2.437Ghz), 7 (2.442Ghz): ")
    gonnaRun = input("ARE YOU READY?? Press Y then the Enter key if you are, otherwise press N... ")
    if (gonnaRun == 'y' or gonnaRun == 'Y'):
        configWrite(networkName, wirelessPasskey, channels, appFile)
    elif (gonnaRun == 'n' or gonnaRun == 'N'):
        mainMenu()
    else:
        print("Gavin, this is simple, c'mon. We're gonna try this again...")
        continuePrompt()
        configOptions('configure.rsc')
def configWrite(ssid, wpak, channel, applicableFile):
    clearScreen()
    headerInfo("Writing to Configuration File")
    time.sleep(2)
    # script is figuring out what channel was entered and replacing 'auto' appropriately
    if (channel == str(1)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2412")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    elif (channel == str(2)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2417")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    elif (channel == str(3)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2422")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    elif (channel == str(4)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2427")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    elif (channel == str(5)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2432")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    elif (channel == str(6)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2437")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    elif (channel == str(7)):
        with open(applicableFile, 'r') as file :
          filedata = file.read()
        filedata = filedata.replace("frequency=auto", "frequency=2442")
        with open(applicableFile, 'w') as file:
          file.write(filedata)
    else:
        pass
    # replace SSID with desired one
    with open(applicableFile, 'r') as file :
      filedata = file.read()
    filedata = filedata.replace('MikroTik-E05F04', ssid)
    with open(applicableFile, 'w') as file:
      file.write(filedata)
    with open(applicableFile, 'r') as file :
      filedata = file.read()
    filedata = filedata.replace("set bridge comment=defconf", "set bridge comment=defconf\r\n /interface wireless security-profiles\r\n set [find default=yes] authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys wpa-pre-shared-key=" + wpak + " \ wpa2-pre-shared-key=" + wpak)
    with open(applicableFile, 'w') as file:
      file.write(filedata)
    # Get rid of the WebKitFormBoundry thing if exsits
    with open(applicableFile, 'r') as file :
      filedata = file.read()
    filedata = filedata.replace("------WebKitFormBoundarya7Swh7j4jxq2AxQT--", '')
    with open(applicableFile, 'w') as file:
      file.write(filedata)
    print("Complete!")
    time.sleep(3)
    uploadConfig()
def uploadConfig():
    clearScreen()
    headerInfo("Uploading Configuration Sequence")
    time.sleep(2)
    print("Uploading configuration...")
    time.sleep(1)
    print("Initalzing FTP session...")
    upArrow()
    time.sleep(3)
    ftp = FTP('192.168.88.1')
    ftp.login(user='admin', passwd='')
    filename = "configure.rsc"
    localfile = open(filename, 'rb')
    # ftp.delete(filename)
    ftp.storbinary('STOR ' + filename, localfile)
    print("Shutting down FTP session...")
    ftp.close()
    localfile.close()
    clearScreen()
    completeScreen()
    mainMenu()
def downloadConfig():
    sshConfigure()
    clearScreen()
    headerInfo("Getting Configuration Sequence")
    time.sleep(2)
    print("Initialzing FTP session...")
    time.sleep(1)
    print("Downloading configuration...")
    downArrow()
    time.sleep(3)
    ftp = FTP('192.168.88.1')
    filename = "configure.rsc"
    localfile = open(filename, 'wb')
    response = ftp.login(user='admin', passwd='')
    if (response == '230 User admin logged in'):
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
        print("Shutting down FTP session")
        localfile.close()
        ftp.close()
        time.sleep(2)
        configOptions('configure.rsc')
    else:
        print("Couldn't initialze FTP session!")
        exitError(str(-3))
        mainMenu()
def upArrow():
    print()
    print("        0   ")
    print("       000  ")
    print("     0000000")
    print("       000  ")
    print("       000  ")
    print("       000  ")
    print("       000  ")
    print("       000  ")
def downArrow():
    print()
    print("       000  ")
    print("       000  ")
    print("       000  ")
    print("       000  ")
    print("       000  ")
    print("     0000000")
    print("       000  ")
    print("        0   ")
def completeScreen():
    headerInfo("Complete! SSH will apply, and disconnect!")
    print("      000 ")
    print("      000 ")
    print("      000 ")
    print("      000 ")
    print("      000 ")
    print("         ")
    print("      000 ")
    print("      000 ")
    print()
    continuePrompt()
    sshApply()
def exitError(errorCode):
    print("Please read in the Credits option");
    print("about the following error code: " + errorCode)
    continuePrompt()
def clearScreen():
    if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')
    else:
        print("This operating system isn't supported!")
        print("This script will now shut down!")
        exitError(str(-1))
        sys.exit("0\n")
# don't know what this is used for but why not lol
def exitSuccess(happyCode):
    print("You successfully ran the script: " + happyCode)
    input("Thanks")
welcomeScreen()
#sshApply()
#sshDisconnect()