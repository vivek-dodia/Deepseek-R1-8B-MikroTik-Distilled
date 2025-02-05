# Repository Information
Name: mikrotik-configuration-service

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
	url = https://gitlab.com/kkrolikowski/mikrotik-configuration-service.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: router.py
================================================
import routeros_api
class Router:
    def __init__(self, cfg):
        self.host = cfg['Router']['address']
        self.login = cfg['Router']['login']
        self.password = cfg['Router']['password']
        try:
            connection = routeros_api.RouterOsApiPool(self.host, username=self.login, password=self.password)
            self.api = connection.get_api()
        except Exception as e:
            print("Mikrotik connect error")
    def __getFW(self):
        try:
            fw_filter = self.api.get_resource('/ip/firewall/filter')
            return fw_filter
        except Exception:
            print("Error getting filter rules")
    def __findJump(self):
        rules = self.__getFW()
        for rule in rules.get():
            if rule['action'] == 'jump':
                return rule['id']
        else:
            return None
    def addMAC(self, mac):
        rules = self.__getFW()
        place_to_insert = self.__findJump()
        try:
            for rule in rules.get():
                if 'src-mac-address' in rule and rule['src-mac-address'].upper() == mac.upper():
                    return 302
            else:
                rules.add(chain='forward', 
                            action='accept', 
                            in_interface='ether2',
                            src_mac_address=mac,
                            place_before=place_to_insert)
                return 200
        except Exception as e:
            return 500
    def removeMAC(self,mac):
        rules = self.__getFW()
        try:
            for rule in rules.get():
                if 'src-mac-address' in rule and rule['src-mac-address'] == mac.upper():
                    rules.remove(id=rule['id'])
                    return 200
            else:
                return 404
        except Exception:
            return 500
================================================

File: setup.py
================================================
import logging
from systemd.journal import JournalHandler
import configparser
import sys
class Config:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
    def readConfig(self):
        try:
            self.cfg.read(sys.argv[1])
            return self.cfg
        except Exception:
            raise ValueError("Error reading configuration file")
class SystemdLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.__journald_handler = JournalHandler()
        self.__journald_handler.setFormatter(logging.Formatter(
            '[%(levelname)s] %(message)s'
        ))
        self.logger.addHandler(self.__journald_handler)
    def start(self):
        return self.logger
================================================

File: webapp.py
================================================
import sys
import configparser
import logging
from .router import Router
from .setup import Config, SystemdLogger
from tornado import web, escape, ioloop, httpclient, gen
from datetime import datetime
cfg = Config().readConfig()
mt = Router(cfg)
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
logger = SystemdLogger().start()
logger.setLevel(logging.INFO)
logger.info("Webservice started at: %s port", cfg['SERVICE']['http_port'])
class AddMacHandler(web.RequestHandler):
    SUPPORTED_METHODS = ("GET")
    def get(self, mac):
        try:
            status = mt.addMAC(mac)
            if status == 200:
                response = {
                    'status': 'DEVICE_ADDED'
                }
                self.set_status(200)
                self.write(response)
                logger.info("Device: %s added", mac)
            elif status == 302:
                response = {
                    'status': 'DEVICE_EXISTS'
                }
                self.set_status(302)
                self.write(response)
                logger.info("Device: %s already exists", mac)
        except Exception as e:
            response =  {
                'error': e.args[0]
            }
            self.set_status(500)
            self.write(response)
            print(timestamp, "Error adding device:", mac)
class RemoveMacHandler(web.RequestHandler):
    SUPPORTED_METHODS = ("GET")
    def get(self, mac):
        try:
            status = mt.removeMAC(mac)
            if status == 200:
                response = {
                    'staus': 'DEVICE_REMOVED'
                }
                self.set_status(200)
                self.write(response)
                print(timestamp, "Device:", mac, "removed")
            elif status == 404:
                response = {
                    'status': 'DEVICE_NOT_FOUND'
                }
                self.set_status(404)
                self.write(response)
                print(timestamp, "Device:", mac, "doesn't exist")
        except Exception as e:
            response =  {
                'error': e.args[0]
            }
            self.set_status(500)
            self.write(response)
            print(timestamp, "Error removing device:", mac)
================================================

File: main.conf
================================================
[Router]
address = mikrotik-address
login = mikrotik-user
password = mikrotik-pass
[SERVICE]
http_port = 8888
================================================

File: main.py
================================================
#!/usr/bin/env python3
import logging
from lib.webapp import AddMacHandler, RemoveMacHandler
from tornado import web, escape, ioloop, httpclient, gen
app = web.Application([
  (r"/add-device/(.*)", AddMacHandler),
  (r"/remove-device/(.*)", RemoveMacHandler)
])
if __name__ == '__main__':
  port = 8888
  try:
    logging.getLogger('tornado.access').disabled = True
    app.listen(port, address='127.0.0.1')
    ioloop.IOLoop.instance().start()
  except KeyboardInterrupt:
    print("Bye.")
  except Exception as e:
    print("Unknown exception error: ", e)
================================================

File: README.md
================================================
mikrotik-configuration-service