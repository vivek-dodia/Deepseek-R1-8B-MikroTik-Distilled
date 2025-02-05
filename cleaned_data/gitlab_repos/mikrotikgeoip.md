# Repository Information
Name: mikrotikgeoip

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
	url = https://gitlab.com/muqiuq/mikrotikgeoip.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .gitlab-ci.yml
================================================
image: python:3.11-bookworm
pages:
  script:
    - pip3 install -r requirements.txt
    - python main.py
  artifacts:
    paths:
      - public
================================================

File: config.py
================================================
REPOS = [
    {"url": "https://github.com/herrbischoff/country-ip-blocks"}
]
BLOCKLIST_URL = "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset"
WORKDIR_PATH = "workdir"
PUBLIC_PATH = "public"
================================================

File: main.py
================================================
import logging
import os.path
import requests
import config
import render
import repocollector
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, force=True)
repocollector.create_or_update_repos()
ipv4path = os.path.join(config.WORKDIR_PATH, "country-ip-blocks", "ipv4")
ipv4lists = os.listdir(ipv4path)
if not os.path.exists(config.PUBLIC_PATH):
    os.mkdir(config.PUBLIC_PATH)
def build_geoip():
    for ipv4list in ipv4lists:
        countryCode = ipv4list.split(".")[0]
        with open(os.path.join(ipv4path, ipv4list), "r") as infile:
            with open(os.path.join(config.PUBLIC_PATH, f"{countryCode}.rsc"), "w") as outfile:
                while True:
                    line = infile.readline()
                    if line == '':
                        break
                    oneIpv4 = line.strip()
                    if oneIpv4 != "" and not oneIpv4.startswith("#"):
                        outfile.write(f"/ip/firewall/address-list/add list=GeoIP-{countryCode} address={oneIpv4}\n")
def build_firehol():
    req = requests.get(config.BLOCKLIST_URL)
    lines = req.content.decode("utf-8").split("\n")
    with open(os.path.join(config.PUBLIC_PATH, f"blocklist.rsc"), "w") as outfile:
        for line in lines:
            oneIpv4 = line.strip()
            if oneIpv4 != "" and not oneIpv4.startswith("#"):
                outfile.write(f"/ip/firewall/address-list/add list=Blocklist address={oneIpv4}\n")
build_geoip()
build_firehol()
render.render_overview()
logging.info("Finished")
================================================

File: README.md
================================================
# MikroTik GeoIP
 - Built weekly
 - GeoIP Source: https://github.com/herrbischoff/country-ip-blocks
 - Blocklist Source: https://github.com/firehol/blocklist-ipsets
## Available lists
https://mikrotikgeoip-muqiuq-9d674e92c7d1b98594a57d5312a8dd06e6c6e7ff35.gitlab.io/
## GeoIP - Example for CH
```mikrotik
/ip firewall address-list remove [/ip firewall address-list find list="GeoIP-ch"]
/tool/fetch url="https://mikrotikgeoip-muqiuq-9d674e92c7d1b98594a57d5312a8dd06e6c6e7ff35.gitlab.io/ch.rsc" output=file dst-path=GeoIP.rsc
/import file-name=GeoIP.rsc
```
## GeoIP - Example for US
```mikrotik
/ip firewall address-list remove [/ip firewall address-list find list="GeoIP-us"]
/tool/fetch url="https://mikrotikgeoip-muqiuq-9d674e92c7d1b98594a57d5312a8dd06e6c6e7ff35.gitlab.io/us.rsc" output=file dst-path=GeoIP.rsc
/import file-name=GeoIP.rsc
```
## Blocklist - Firehol
```mikrotik
/ip firewall address-list remove [/ip firewall address-list find list="Blocklist"]
/tool/fetch url="https://mikrotikgeoip-muqiuq-9d674e92c7d1b98594a57d5312a8dd06e6c6e7ff35.gitlab.io/blocklist.rsc" output=file dst-path=Blocklist.rsc
/import file-name=Blocklist.rsc
```
================================================

File: render.py
================================================
import logging
import os
import jinja2
from jinja2 import FileSystemLoader
import config
jenv = jinja2.Environment(loader=FileSystemLoader("templates/"))
def render_overview():
    files = [x for x in os.listdir(config.PUBLIC_PATH) if x.endswith(".rsc")]
    overview_filename = os.path.join(config.PUBLIC_PATH, "index.html")
    template = jenv.get_template("index.jinja2")
    content = template.render(lists=files)
    with open(overview_filename, "w", encoding="utf-8") as fp:
        fp.write(content)
    logging.info(f"Created {overview_filename}")
================================================

File: repocollector.py
================================================
import logging
import os
from git import Repo
import config
def create_or_update_repos(no_update: bool = False):
    if not os.path.exists(config.WORKDIR_PATH):
        os.mkdir(config.WORKDIR_PATH)
    repos = []
    for repo_entity in config.REPOS:
        repo_url = repo_entity["url"]
        repo_name = repo_url.split('/')[-1]
        repo_path = str(os.path.join(config.WORKDIR_PATH, repo_name))
        logging.debug(f"Creating/Updating content for repo {repo_name}")
        repo: Repo = None
        if not os.path.exists(repo_path):
            repo = Repo.clone_from(repo_url, repo_path)
            logging.info(f"Cloned repo {repo_url} to {repo_path}")
        else:
            repo = Repo(repo_path)
            logging.info(f"Loaded existing repo {repo_url}")
            if not no_update:
                repo.git.reset('--hard')
                repo.remotes.origin.pull()
                logging.info(f"Pulled changes for repo {repo_url}")
        repos.append({"url": repo_url, "name": repo_name, "path": repo_path})
    return repos
================================================

File: requirements.txt
================================================
GitPython
requests
Jinja2
================================================