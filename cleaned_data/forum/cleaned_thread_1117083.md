# Thread Information
Title: Thread-1117083
Section: RouterOS
Thread ID: 1117083

# Discussion

## Initial Question
Hello, did anyone experienced the following problem?- BTH working on an HAP AC2 [ROS 17.6.2], configured with ANDROID BTH APP (should be version 0.34)- New share "XXX" created on the ANDROID app with "NEVER EXPIRES"- Link of "XXX" sent to another user via Whatsapp and opened with IPHONE BTH app (version 0.9)--> the "XXX" share created BUT unusable, greyed out since already "EXPIRED"NOTE#1: shares created with an "expire date", instead, work on IPHONE (only the "never expire" ones are greyed out)NOTE#2: Wireguard Desktop shares with "never expire" work on Desktop PCMany thanks ---

## Response 1
Perhaps never expire is not an option?? ---

## Response 2
Sorry, did not get if you are suggesting it is forbidden or if you’re asking a question.From Mikrotik docs, it seems it is possible to configure Expire = neverhttps://help.mikrotik.com/docs/spaces/R ... ck+To+Homeexpires (string; never | date: "YYYY-MM-DD HH:MM:SS";Default: never)Expiration time and date for user, cannot be changed once user is createdAnd also when you create a share, it defaults to never ---