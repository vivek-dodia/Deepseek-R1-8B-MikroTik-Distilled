# Thread Information
Title: Thread-1117396
Section: RouterOS
Thread ID: 1117396

# Discussion

## Initial Question
I am a network engineer at a company that just acquired a WISP where all of the infrastructure routers, nearly all of the customer routers, and some of the switches are Mikrotik, and we only have access to about 90% of the infrastructure via username+password. Customer routers are sometimes accessible with a known username+password, sometimes not.There is a workstation here still running Ubuntu 16.04 that we want to upgrade or replace, but we dare not touch any configuration until everything (software, hardware, etc) is accessible via our preferred login mechanism, instead of SSH keys (we don't control some of the private keys, but they are configured into some important software that controls multiple important functions). This workstation (supposedly) has the .sh files, and some (all?) of the .rsc files used to configure the routers prior to customer deployment. There are (supposedly) some .sh files for updating users on deployed routers, and configurations on those routers, but none of us on the engineering team (there are three of us) are sure how to use them.Hopefully I painted the picture well enough to explain the predicament so my questions will make more sense.I successfully created a key, modified the customer router configuration script to add the key to a router, but I can't figure out how to login with it. When I attempt to login with "ssh -l admin -i ~/.ssh/key_rsa", I get the key password prompt, but then I get a user password prompt too. Of course, no passwords for any of the logins are known, and I am not sure that I have figured out how to add a user to the router configuration. Is it possible to login with just the key? ---

## Response 1
Yes, it is possible to login by ssh key. ---

## Response 2
You doing this:https://help.mikrotik.com/docs/spaces/R ... privatekey ---

## Response 3
Yes, I used that to add a key by adding this to one of the script files.# add auth settings/user ssh-keys import public-key-file=id1_rsa.pub user=admin/user add name=user password=user group=fullGood news! I don't know if this is applicable in all instances, but it was stopping me.When I attempted to authenticate with the key using "ssh -i ~/.ssh/id1_rsa admin@192.168.88.1", I was prompted for the key password, and then again for the user password. As a test, I removed all of the other commands to import and associate other keys with "admin", and now I am authenticated without even entering the password for the key.Thank you for confirming I was doing things right, but it seems like the environment is modified by something in one of the script files that I haven't identified yet. Either way, I am now closer to success. ---