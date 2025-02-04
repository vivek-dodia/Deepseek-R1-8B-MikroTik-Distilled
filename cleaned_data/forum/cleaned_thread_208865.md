# Thread Information
Title: Thread-208865
Section: RouterOS
Thread ID: 208865

# Discussion

## Initial Question
HelloI am using Debian 12. My Mikrotik devices are AX2 and CRS326 with RouterOS version 7.15.1 I recently purchased YubiKey. I generated an asymmetric key ed25519 with FIDO2 support:ssh-keygen -f ~/.ssh/mikrotikAX2Yubi -t ed25519-sk -b 521I copied it to the router and tried to import it in system>users>SSH Keys. Unfortunately, the import failed without displaying an error. You need to reset the router to be able to change anything in the SSH settings. After restarting, the ed25519 key is added without any problems, but without FIDO2 support. The problem occurs on both of my devices. Is this a known bug? ---

## Response 1
Hi, i'm running 7.16.2 on a CCR2004-1G-12S+2XS and i get an error when i try to import a ed25519-sk key. Unfortunately i assume they just have not implemented it (yet).I'd love to see this functionality. ---

## Response 2
It is not a bug. ed25519-sk is just not supported. Only recently the have added ed25519 support. ---