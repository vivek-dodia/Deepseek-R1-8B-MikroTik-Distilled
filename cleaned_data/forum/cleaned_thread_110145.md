# Thread Information
Title: Thread-110145
Section: RouterOS
Thread ID: 110145

# Discussion

## Initial Question
EDIT: Enabling strong-crypto for ssh sets these, I managed to miss this in my testing! Leaving this here for people arriving by Google.I discovered today that I could not SSH to any of my routers as a result of our new corporate security policy.The only MACs (Message Authentication Code, for other readers) that appear to be currently supported by the RouterOS SSH server are: `hmac-sha1, hmac-md5`Our corporate policy only allows stronger MACs such as `hmac-sha2-256` or `hmac-sha2-512`. (Ideally we would like to be able to disable the other MACs, specifically `hmac-md5`, but that is not crucial here)Would it be possible to enable support for these MACs in a future RouterOS release?Thanks! ---

## Response 1
You can enable strong-cryptohttp://wiki.mikrotik.com/wiki/Manual:IP/SSH ---

## Response 2
You can enable strong-cryptohttp://wiki.mikrotik.com/wiki/Manual:IP/SSHNow athttps://help.mikrotik.com/docs/spaces/R ... 350014/SSHorhttps://wiki.mikrotik.com/Manual:IP/SSH.But it doesn't seem to work on RouterOS v6 (tested with v6.49.. Enabled strong-crypto but I still can't connect without re-enabling SHA1 (disabled by default on CentOS 9):https://serverfault.com/a/1095899/132219. I get:
```
ssh-oMACs=hmac-sha2-256user@MikroTik system identityprintUnableto negotiatewithMikroTikport22:nomatching MAC found.Theiroffer:hmac-sha1,hmac-md5

---
```

## Response 3
Now athttps://help.mikrotik.com/docs/spaces/R ... 350014/SSHorhttps://wiki.mikrotik.com/Manual:IP/SSH.But it doesn't seem to work on RouterOS v6 (tested with v6.49.8 ).Unfortunately Mikrotik's documentation doesn't include history ... e.g. which ROS version brought certain feature or change in behaviour. So mostly it conforms to latest ROS version (e.g. 7.16) except when it doesn't (e.g. when they forget to update docs). General rule of thumb is that wiki pages (being abandoned) are about v6 and help pages are about v7.As to ssh: OpenSSH (and distribution maintainers) deprecated many older key exchange algorithms snd cyphering algorithms ... many of those are considered "state of art" in ROS (yes, SSH implementation in ROS has falklen pretty much behind mainstream). So wgen using modern linux (or other) SSH client, one has to enable a few deprecated algorithms to allow connection to even latest ROS.Regarding your ROS version: you may need to update to latest 6.49 ... 6.49.17 is latest stable, it might make a difference. ---