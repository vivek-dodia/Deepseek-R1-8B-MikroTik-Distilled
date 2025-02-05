# Repository Information
Name: mikrotik-rancher

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
	url = https://gitlab.com/aheadrox/mikrotik-rancher.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .gitlab-ci.yml
================================================
image: docker:latest
services:
  - docker:dind
stages:
  - build
before_script:
  - docker info
build_container:
  stage: build
  script:
    - docker build --no-cache --force-rm --rm=true -t registry.gitlab.com/aheadrox/mikrotik-rancher:latest .
    - docker images
    - docker login -u gitlab-ci-token -p $CI_BUILD_TOKEN registry.gitlab.com
    - docker push registry.gitlab.com/aheadrox/mikrotik-rancher
  only:
    - master
================================================

File: Dockerfile
================================================
FROM rancher/vm-base:0.0.3
MAINTAINER Denis Grigoryev dgrigoryev@maprox.net
RUN apt-get -qq update && apt-get install unzip && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD http://download2.mikrotik.com/routeros/6.34.6/chr-6.34.6.img.zip ./chr-6.34.6.img.zip
RUN unzip ./chr-6.34.6.img.zip -d /base_image/ && ls /base_image && rm ./chr-6.34.6.img.zip
EXPOSE 80 8291