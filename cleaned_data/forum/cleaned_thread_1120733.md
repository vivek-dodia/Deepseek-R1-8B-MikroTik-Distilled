# Thread Information
Title: Thread-1120733
Section: RouterOS
Thread ID: 1120733

# Discussion

## Initial Question
In years gone by, firmware updates were decoupled from software updates. Lately, every software update has a corresponding firmware update, yet management tools like Dude only have software update functionality.Question is, are firmwares always really updated? Is it critical to have a firmware in sync with the software (unless specifically stated)?Updating in bulk is a chore with firmware required to be synced, even if auto update is enabled, I still need to update all devices, then ensure they are rebooted a second time to update the firmware.How do others tackle this? ---

## Response 1
Default is leave firmware (RouterBOOT) as is.RouterBOOT upgrades usually not critical; RoutBOOT does hardware initialization and some changes require firmware upgrade.Seehttps://help.mikrotik.com/docs/spaces/R ... outerBOARDfor "auto-upgrade" setting which automates a bit but requires second reboot to take full effect.I don't use auto-upgrade and perform both steps manually. ---