# Repository Information
Name: maas-ros-helper

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
	url = https://gitlab.com/eviltoast3r/maas-ros-helper.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: config.json.sample
================================================
{
  "mikrotik":{
    "name":"hapAC2",
    "ip":"127.0.0.1",
    "username":"root",
    "password":"P@SSW0RD",
  },
  "system":{
        "log":"./logs/"
        "cert":"/path/to/server/cert/",
        "key":"/path/to/server/key/"
  }
}
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2023 Maddog0057
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: maas-ros-helper.py
================================================
from flask import Flask,request,json
import jsonify
import routeros_api
import logging
import sys
from logging.handlers import RotatingFileHandler
with open("config.json", 'r') as json_data_file:
    config = json.load(json_data_file)
logDir = config["system"]["log"]
logFile = logDir+config["mikrotik"]["name"]+".log"
class StreamToLogger(object):
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''
   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())
   def flush(self):
      pass
handler = RotatingFileHandler(logFile,"a",maxBytes=1048576,backupCount=5)
logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   handlers = [ handler ]
)
stdout_logger = logging.getLogger('STDOUT')
sl = StreamToLogger(stdout_logger, logging.INFO)
sys.stdout = sl
stderr_logger = logging.getLogger('STDERR')
sl = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = sl
global pstat
pstat = str()
rosip = config["mikrotik"]["ip"]
rosusn = config["mikrotik"]["username"]
rossec = config["mikrotik"]["password"]
maascert = config["system"]["cert"]
maaskey = config["system"]["key"]
connection = routeros_api.RouterOsApiPool(
   rosip, 
   username=rosusn, 
   password=rossec,
   port=8728,
   use_ssl=False,
   ssl_verify=False,
   ssl_verify_hostname=False,
   plaintext_login=True
)
api = connection.get_api()
def ros_usb_reset():
    api.get_resource('/system/routerboard/usb/').call('power-reset')
    return 'USB Interface Reset'
app = Flask(__name__)
@app.route('/usb-reset', methods=["POST", "GET"])
def pwr_reset():
    usb_pwr=ros_usb_reset()
    global pstat
    pstat = "running"
    return pstat
@app.route('/usb-off', methods=["POST", "GET"])
def pwr_off():
    global pstat
    pstat = "stopped"
    return pstat
@app.route('/usb-on', methods=["POST", "GET"])
def pwr_on():
    global pstat
    pstat = "running"
    return pstat
@app.route('/usb-status', methods=["POST", "GET"])
def pwr_status():
    global pstat
    if pstat is "":
       pstat = "running"
    pwr_stat = {"status":pstat}
    return pwr_stat
if __name__ == '__main__':
    context = (maascert, maaskey)
    app.run(host='0.0.0.0', port=6437, debug=True, ssl_context=context)
================================================

File: requirements.txt
================================================
aiohttp==3.8.3
aiosignal==1.2.0
async-timeout==4.0.2
attrs==22.1.0
blinker==1.6.2
certifi==2022.9.24
charset-normalizer==2.1.1
click==8.1.3
discord==2.0.0
discord.py==2.0.1
espn-api==0.25.0
Flask==2.3.2
frozenlist==1.3.1
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
jsonify==0.5
MarkupSafe==2.1.2
multidict==6.0.2
requests==2.28.1
RouterOS-api==0.17.0
six==1.16.0
urllib3==1.26.12
Werkzeug==2.3.4
yarl==1.8.1