# Thread Information
Title: Thread-213478
Section: RouterOS
Thread ID: 213478

# Discussion

## Initial Question
Hey folks, I'm trying to use /tool/email to automatically send some emails using smtp.google.com and I'm having the following issue:ISSUEWhen I set tls=yes to enforce usage of tls I get "Error sending e-mail <test>: TLS handshake failed" and the mail is not sent. When I use tls=starttls it works fine and the mail is sent. So 2fa and app password is already set up and workingWHAT I'VE TRIEDI've tried setting smtp-relay.gmail.com (as per a suggestion in the forum), but that doesn't work either.IS THE TRAFFIC ENCRYPTED RIGHT NOW?Right now the relevant traffic is encrypted using TLS as shown in the .pcap file but starttls is susceptible to Mitm attacks as it leaves the possibility open for using unencrypted traffic.
```
server: smtp.gmail.com                   
          port: 587
           tls: yes
           vrf: main
          from: xxxxxx
          user: xxxxxxx
      password: xxxxxxxx
   last-status: failed
  last-address: xxxxxxxWhat do I go about solving this? I'm on rb4011 v 7.16.1

---
```

## Response 1
There are things to be set-up on gmail side, check their article:https://support.google.com/a/answer/2520500?hl=enThen it could be TLS support mismatch. AFAIK ROS supports up to TLS 1.2 and some sites already require minimum of TLS 1.3 (not sure if gmail does). ---

## Response 2
Thanks for the reply! I'll go read it in detail to see if I figure sth out. What's confusing is that the transfer IS encrypted with TLS when I set "starttls" which means that the TLS exchange works. It's a mystery to me why it fails with tls=yes. I've looked into the TLS mismatch thing but, if the google docs are up-to-date, smtp gmail supports TLS 1.0, 1.1, 1.2, 1.3 and uses the most recent version that's also available to the other side. ---

## Response 3
Ok I found it. Port 587 is meant to receive traffic with the starttls command so when I do not enable starttls my request is rejected. Port 465 is exposed for static tls setting and now it works properly and the traffic is encrypted with tls version 1.2. This is not clearly stated in the google documentation and it's easy to miss. ---