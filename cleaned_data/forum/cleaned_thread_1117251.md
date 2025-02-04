# Thread Information
Title: Thread-1117251
Section: RouterOS
Thread ID: 1117251

# Discussion

## Initial Question
Boa noite, estou com um problema bem estranho com uma CRS, ela esta taxando erro somente e uma interface " Tx Drop", já foi feito a troca do cordão, Gbic e porta. Porem ela taxa " Tx Drop" sentindo a Borda apenas.Teriam alguma ideia ?.Seria algum problema na CRS ?Good evening, I have a very strange problem with a CRS, it is only reporting an error and a "Tx Drop" interface, the cord, Gbic and port have already been replaced. However, it only reports "Tx Drop" when sensing the Edge. Do you have any ideas? Could it be a problem with the CRS? ---

## Response 1
welcome to the forum this is an english forum ---

## Response 2
consider upgrading to routeros 7.16.2, then you can enable qos hw offload and obtain detailed drop stats, then if needed you can tune switch buffers to prevent dropsdont forget to do backup and export your settings to your PC before upgradingalso after upgrading RouterOS dont forget to upgrade routerboot to current version (system routerboard upgrade)after upgrading Switch-qos menu wil be avalilable on winbox ---

## Response 3
consider upgrading to routeros 7.16.2, then you can enable qos hw offload and obtain detailed drop stats, then if needed you can tune switch buffers to prevent dropsdont forget to do backup and export your settings to your PC before upgradingalso after upgrading RouterOS dont forget to upgrade routerboot to current version (system routerboard upgrade)after upgrading Switch-qos menu wil be avalilable on winboxGood evening, could you send me a link to a tutorial teaching how to adjust these buffers, so that I don't get the "Tx Drop" error. Or would just updating to version 7.16.2 solve the problem?But send me the link with the tutorial because if, after the update, there is a "Tx Drop" charge, I can do it by following the tutorial. ---

## Response 4
consider upgrading to routeros 7.16.2, then you can enable qos hw offload and obtain detailed drop stats, then if needed you can tune switch buffers to prevent dropsdont forget to do backup and export your settings to your PC before upgradingalso after upgrading RouterOS dont forget to upgrade routerboot to current version (system routerboard upgrade)after upgrading Switch-qos menu wil be avalilable on winboxToday the network consumes 4 to 5 Gbps in media, if possible, tell me what the configuration would look like to enable QOS hardware offloading and adjust the buffers. ---

## Response 5
documentationhttps://help.mikrotik.com/docs/spaces/R ... of+Service ---

## Response 6
documentationhttps://help.mikrotik.com/docs/spaces/R ... of+ServiceGood afternoon, read the documentation, but I don't understand what will apply here in my case, the CRS 317, could you explain the commands I will use? ---