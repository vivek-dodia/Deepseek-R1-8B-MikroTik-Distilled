# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 206482

# Discussion

## Initial Question
Author: Fri Apr 05, 2024 2:31 pm
``` {:do{/tool fetch url=https://pki.goog/roots.pem dst-path=roots-goog.pem;/certificateremove[findwhereauthority expired];/certificateimportfile-name=roots-goog.pem passphrase="";/fileremoveroots-goog.pem;:log info("Updated certificate trust store");}on-error={:log error("Failed to update certificate trust store");};} ``` Following on this old post:viewtopic.php?t=169662&sid=6818e151144b ... d9a4004745My version looks like this but generates the error every other run. I run it once, it fails (i.e. it writes the error to the log), run it again and it passes (i.e. it writes the success message to the log). If I manually enter the commands they work fine on their own. Any reason why it would fail 50% of the time?
```
---
```

## Response 1
Author: [SOLVED]Fri Apr 05, 2024 4:33 pm
``` { :do { /tool fetch url="https://pki.goog/roots.pem" dst-path="roots-goog.pem" :delay 2s /certificate remove [find where authority expired] import file-name="roots-goog.pem" passphrase="" /file remove [find where name="roots-goog.pem"] :log info "Updated certificate trust store" } on-error={ :log error "Failed to update certificate trust store" } } ``` remove frills, improve logicsexample code