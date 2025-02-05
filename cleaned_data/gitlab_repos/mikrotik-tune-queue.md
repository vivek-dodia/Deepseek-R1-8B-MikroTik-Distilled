# Repository Information
Name: mikrotik-tune-queue

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
	url = https://gitlab.com/fatahnuram/mikrotik-tune-queue.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: cleanup.sh
================================================
#!/usr/bin/env bash
# check args num
if [[ $# -gt 0 ]]; then
    # any args inserted
    echo
    echo "Don't need any arguments to run this! Aborting.."
    echo
    exit 1
fi
# prompt user
echo
echo "Cleaning up environment.."
# unset all variables
unset MIKROTIK_RULE_TYPE
unset MIKROTIK_USER
unset MIKROTIK_ADDR
unset MIKROTIK_ADDR_TYPE
unset MIKROTIK_IP_START
unset MIKROTIK_IP_END
unset MIKROTIK_ID_START
unset MIKROTIK_ID_END
unset MIKROTIK_IP_TO_CONF
unset MIKROTIK_ID_TO_CONF
unset MIKROTIK_MAX_UPLOAD
unset MIKROTIK_MAX_DOWNLOAD
unset MIKROTIK_BURST_LIMIT_UPLOAD
unset MIKROTIK_BURST_LIMIT_DOWNLOAD
unset MIKROTIK_BURST_THRESHOLD_UPLOAD
unset MIKROTIK_BURST_THRESHOLD_DOWNLOAD
unset MIKROTIK_BURST_TIME_UPLOAD
unset MIKROTIK_BURST_TIME_DOWNLOAD
unset MIKROTIK_LIMIT_AT_UPLOAD
unset MIKROTIK_LIMIT_AT_DOWNLOAD
unset MIKROTIK_PRIORITY_UPLOAD
unset MIKROTIK_PRIORITY_DOWNLOAD
unset MIKROTIK_RULE_PREFIX
unset MIKROTIK_RULE_SUFFIX
unset MIKROTIK_COMMENT
# prompt user
echo
echo "Done!"
echo
================================================

File: configure.sh
================================================
#!/usr/bin/env bash
# predefined function to check if variable is present or not
var_check() {
    if [[ -z ${1} ]]; then
        echo
        echo "Missing value! Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify configuration type
verify_rule_type() {
    # todo: combine if rules when all supported
    if [[ ${1} == add ]]; then
        # add new configurations
        echo
        echo "Not yet supported! Quitting.."
        echo
        exit 0
    elif [[ ${1} == edit ]]; then
        # edit existing configurations
        # do nothing
        true
    elif [[ ${1} == del ]]; then
        # delete existing configurations
        echo
        echo "Not yet supported! Quitting.."
        echo
        exit 0
    else
        # value not in range
        echo
        echo "Value must be 'add', 'edit', or 'delete' !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify addresses type
verify_address_type() {
    if [[ ${1} == range ]] || [[ ${1} == custom ]]; then
        # verified
        true
    else
        # value not in range
        echo
        echo "Value must be 'range' or 'custom' !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify ip address
verify_ip_address() {
    if [[ ${1} =~ ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$ ]]; then
        # valid ip address
        true
    else
        # invalid ip address
        echo
        echo "IP address invalid! Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify last octet of ip address
verify_last_octet(){
    if [[ ${1} =~ ^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$ ]]; then
        # valid last octet ip address
        true
    else
        # invalid last octet ip address
        echo
        echo "Value invalid! Must be between 0 and 255 !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify ID number
verify_id_num(){
    if [[ ${1} =~ ^([0-9]|[1-9][0-9]|[1-9][0-9]{2})$ ]]; then
        # valid last octet ip address
        true
    else
        # invalid last octet ip address
        echo
        echo "Value invalid! Must be between 0 and 999 !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify ip range
verify_ip_range(){
    # check if zero or minus value
    local CALCULATE=$((${1} - ${2}))
    if [[ ${CALCULATE} -lt 0 ]]; then
        # valid range
        true
    else
        # invalid range
        echo
        echo "Start IP must greater than End IP address! Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify queue priority
verify_priority(){
    if [[ ${1} =~ ^[1-8]$ ]]; then
        # valid priority
        true
    else
        # invalid priority
        echo
        echo "Value must between 1 and 8 !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to verify burst time
verify_burst_time(){
    if [[ ${1} =~ ^([1-9]|[1-5][0-9])$ ]]; then
        # valid priority
        true
    else
        # invalid priority
        echo
        echo "Value must between 1 and 59 !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to insert config type
insert_config_type(){
    printf "Configuration type (add, edit, del): "
    read RULE_TYPE
    var_check ${RULE_TYPE}
    verify_rule_type ${RULE_TYPE}
    printf "Address type (range, custom): "
    read ADDR_TYPE
    var_check ${ADDR_TYPE}
    verify_address_type ${ADDR_TYPE}
    echo
}
# predefined function to insert credentials
insert_credentials(){
    printf "User for login: "
    read USER
    var_check ${USER}
    printf "MikroTik IP address: "
    read ADDR
    var_check ${ADDR}
    verify_ip_address ${ADDR}
    echo
}
# predefined function to insert ip addresses to configure
insert_ip_target() {
    # check addresses type
    if [[ ${1} == range ]]; then
        # insert ip address range
        printf "Start IP (last octet): "
        read IP_START
        var_check ${IP_START}
        verify_last_octet ${IP_START}
        printf "End IP (last octet): "
        read IP_END
        var_check ${IP_END}
        verify_last_octet ${IP_END}
        verify_ip_range ${IP_START} ${IP_END}
        printf "Start ID (0-999, based on MikroTik simple queue rule): "
        read ID_START
        var_check ${ID_START}
        verify_id_num ${ID_START}
        # count last ID from IP given
        ID_END=$((${IP_END} - ${IP_START} + ${ID_START}))
        echo
    elif [[ ${1} == custom ]]; then
        # insert custom ip address with matching ip addresses
        echo "Insert IP address(es) to config (last octet, space separated):"
        read IP_TO_CONF
        var_check ${IP_TO_CONF}
        echo "Insert matching ID from IP above to config (space separated):"
        read ID_TO_CONF
        var_check ${ID_TO_CONF}
        echo
    else
        # value not in range
        echo
        echo "Value must be 'range' or 'custom' !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to print target ip address for setting conf file
export_ip_target() {
    # export address type
    echo "export MIKROTIK_ADDR_TYPE=${ADDR_TYPE}" >> mikrotik.conf
    # check address type
    if [[ ${1} == range ]]; then
        echo "export MIKROTIK_IP_START=${IP_START}" >> mikrotik.conf
        echo "export MIKROTIK_IP_END=${IP_END}" >> mikrotik.conf
        echo "export MIKROTIK_ID_START=${ID_START}" >> mikrotik.conf
        echo "export MIKROTIK_ID_END=${ID_END}" >> mikrotik.conf
    elif [[ ${1} == custom ]]; then
        echo "export MIKROTIK_IP_TO_CONF=\"${IP_TO_CONF}\"" >> mikrotik.conf
        echo "export MIKROTIK_ID_TO_CONF=\"${ID_TO_CONF}\"" >> mikrotik.conf
    else
        # value not in range
        echo
        echo "Value must be 'range' or 'custom' !"
        echo "Aborting.."
        echo
        exit 1
    fi
}
# predefined function to insert configurations
insert_config(){
    # todo: regex validation
    echo "Permitted value:"
    echo "unlimited, 64k, 128k, 256k, 384k, 512k, 768k, 1M, 2M, 3M, 4M, 5M, 10M"
    echo
    printf "Upload max limit (choose one): "
    read MAX_UPLOAD
    var_check ${MAX_UPLOAD}
    printf "Download max limit (choose one): "
    read MAX_DOWNLOAD
    var_check ${MAX_DOWNLOAD}
    printf "Upload burst limit (choose one): "
    read BURST_LIMIT_UPLOAD
    var_check ${BURST_LIMIT_UPLOAD}
    printf "Download burst limit (choose one): "
    read BURST_LIMIT_DOWNLOAD
    var_check ${BURST_LIMIT_DOWNLOAD}
    printf "Upload burst threshold (choose one): "
    read BURST_THRESHOLD_UPLOAD
    var_check ${BURST_THRESHOLD_UPLOAD}
    printf "Download burst threshold (choose one): "
    read BURST_THRESHOLD_DOWNLOAD
    var_check ${BURST_THRESHOLD_DOWNLOAD}
    printf "Upload burst time (1-59): "
    read BURST_TIME_UPLOAD
    var_check ${BURST_TIME_UPLOAD}
    verify_burst_time ${BURST_TIME_UPLOAD}
    printf "Download burst time (1-59): "
    read BURST_TIME_DOWNLOAD
    var_check ${BURST_TIME_DOWNLOAD}
    verify_burst_time ${BURST_TIME_UPLOAD}
    printf "Upload limit at (choose one): "
    read LIMIT_AT_UPLOAD
    var_check ${LIMIT_AT_UPLOAD}
    printf "Download limit at (choose one): "
    read LIMIT_AT_DOWNLOAD
    var_check ${LIMIT_AT_DOWNLOAD}
    printf "Upload priority (1-8, smaller higher): "
    read PRIORITY_UPLOAD
    var_check ${PRIORITY_UPLOAD}
    verify_priority ${PRIORITY_UPLOAD}
    printf "Download priority (1-8, smaller higher): "
    read PRIORITY_DOWNLOAD
    var_check ${PRIORITY_DOWNLOAD}
    verify_priority ${PRIORITY_DOWNLOAD}
    echo
}
# predefined function to insert customized optional config
insert_config_optional(){
    printf "Rule name prefix (optional): "
    read RULE_PREFIX
    printf "Rule name suffix (optional): "
    read RULE_SUFFIX
    printf "Comment (optional): "
    read COMMENT
    echo
}
# predefined function to export all variables
export_all(){
    echo "export MIKROTIK_RULE_TYPE=${RULE_TYPE}" > mikrotik.conf
    echo "export MIKROTIK_USER=${USER}" >> mikrotik.conf
    echo "export MIKROTIK_ADDR=${ADDR}" >> mikrotik.conf
    export_ip_target ${ADDR_TYPE}
    echo "export MIKROTIK_MAX_UPLOAD=${MAX_UPLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_MAX_DOWNLOAD=${MAX_DOWNLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_BURST_LIMIT_UPLOAD=${BURST_LIMIT_UPLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_BURST_LIMIT_DOWNLOAD=${BURST_LIMIT_DOWNLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_BURST_THRESHOLD_UPLOAD=${BURST_THRESHOLD_UPLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_BURST_THRESHOLD_DOWNLOAD=${BURST_THRESHOLD_DOWNLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_BURST_TIME_UPLOAD=${BURST_TIME_UPLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_BURST_TIME_DOWNLOAD=${BURST_TIME_DOWNLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_LIMIT_AT_UPLOAD=${LIMIT_AT_UPLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_LIMIT_AT_DOWNLOAD=${LIMIT_AT_DOWNLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_PRIORITY_UPLOAD=${PRIORITY_UPLOAD}" >> mikrotik.conf
    echo "export MIKROTIK_PRIORITY_DOWNLOAD=${PRIORITY_DOWNLOAD}" >> mikrotik.conf
    # optional variables
    if [[ ! -z ${RULE_PREFIX} ]]; then
        echo "export MIKROTIK_RULE_PREFIX=\"${RULE_PREFIX}\"" >> mikrotik.conf
    fi
    if [[ ! -z ${RULE_SUFFIX} ]]; then
        echo "export MIKROTIK_RULE_SUFFIX=\"${RULE_SUFFIX}\"" >> mikrotik.conf
    fi
    if [[ ! -z ${COMMENT} ]]; then
        echo "export MIKROTIK_COMMENT=\"${COMMENT}\"" >> mikrotik.conf
    fi
}
# check args num
if [[ $# -gt 0 ]]; then
    # any args inserted
    echo
    echo "Don't need any arguments to run this! Aborting.."
    echo
    exit 1
fi
# get configuration type
insert_config_type
# get mikrotik credentials
insert_credentials
# get IP rules to be configured
insert_ip_target ${ADDR_TYPE}
# get expected configurations
insert_config
# get customized configuration names
insert_config_optional
# export all variables saved into file
export_all
# prompt user
echo
echo "Configuration saved! You can use them by running:"
echo "source mikrotik.conf"
echo
echo "And then run the script to configure your router:"
echo "./tune-queue.sh"
echo
================================================

File: help.md
================================================
# Help
This page is for helping people understand all about this project.
## Variable terminologies
There are some terminologies used for variable input:
- **Configuration type**: type of rules that wanted to be configured (**add** new rules, **edit** existing, or **delete** existing rules).
- **User**: user for SSH through MikroTik to configure the router.
- **MikroTik IP address**: IP address of MikroTik router to configure. Note that right now, this input can only support address in the same subnet.
- **Start IP**: this is the last octet of first IP address to be configured by MikroTik. Note that you only need to give the last octet instead of the whole IP address.
- **End IP**: this is the last octet of last IP address to be configured by MikroTik. Note that you only need to give the last octet instead of the whole IP address.
- **Start ID**: this is the ID in MikroTik's simple queue rule that match the first IP given before. This variable is for matching between the queue rule ID with the IP address to be configured.
- **Rule name prefix**: rule names that will be added into created or edited rules as prefix.
- **Rule name suffix**: rule names that will be added into created or edited rules as suffix.
- **Comment**: comment of the rules that will be created or edited.
================================================

File: README.md
================================================
# mikrotik-tune-queue
Bash script for automating simple queue management for MikroTik via SSH
## Notes
This repository is now **working** (only for **edit** until now). However, this repository is still **in development phase**.
## Requirements
Requirements to be fulfilled for this script to be working:
- SSH port enabled on MikroTik
- User can login without password to MikroTik (using SSH key)
## How to run
Make sure the script executable
```bash
chmod +x *.sh
```
Configure script to match your network needs
```bash
./configure.sh
```
Export variables from script
```bash
source mikrotik.conf
```
Finally, run the script
```bash
./tune-queue.sh
```
Don't forget to clean up your workspace after tuning your router
```bash
source cleanup.sh
```
## Limitations
Some limitations for this script (until now):
- Only port 22 for SSH login (hopefully can support custom port later)
- Can only configure for IPs with prefix /24 (subnet mask 255.255.255.0)
- Only support for simple queue management in MikroTik
- Created rule is for per IP, not the whole network queue limit
- Until now only support for edit existing rule in MikroTik
- etc..
## Help
For help, you can click [this link](/help.md).
## LICENSE
![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png "WTFPL")
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004
Copyright (C) 2018 Fatah Nur Alam Majid <fatahnuram@gmail.com>
Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
0. You just DO WHAT THE FUCK YOU WANT TO.
================================================

File: tune-queue.sh
================================================
#!/usr/bin/env bash
# check exported vars if exist
if [[ -z ${MIKROTIK_RULE_TYPE} ]] || [[ -z ${MIKROTIK_USER} ]] \
|| [[ -z ${MIKROTIK_ADDR} ]] || [[ -z ${MIKROTIK_ADDR_TYPE} ]] \
|| [[ -z ${MIKROTIK_MAX_UPLOAD} ]] || [[ -z ${MIKROTIK_MAX_DOWNLOAD} ]] \
|| [[ -z ${MIKROTIK_BURST_LIMIT_UPLOAD} ]] || [[ -z ${MIKROTIK_BURST_LIMIT_DOWNLOAD} ]] \
|| [[ -z ${MIKROTIK_BURST_THRESHOLD_UPLOAD} ]] || [[ -z ${MIKROTIK_BURST_THRESHOLD_DOWNLOAD} ]] \
|| [[ -z ${MIKROTIK_BURST_TIME_UPLOAD} ]] || [[ -z ${MIKROTIK_BURST_TIME_DOWNLOAD} ]] \
|| [[ -z ${MIKROTIK_LIMIT_AT_UPLOAD} ]] || [[ -z ${MIKROTIK_LIMIT_AT_DOWNLOAD} ]] \
|| [[ -z ${MIKROTIK_PRIORITY_UPLOAD} ]] || [[ -z ${MIKROTIK_PRIORITY_DOWNLOAD} ]]; then
    # missing expected exported variables
    echo
    echo "Looks like you don't source the conf yet!"
    echo "Please run ./configure.sh first!"
    echo "Aborting.."
    echo
    exit 1
fi
# check dependent exported vars if exist
if [[ ${MIKROTIK_ADDR_TYPE} == range ]]; then
    # check vars if exported
    if [[ -z ${MIKROTIK_IP_START} ]] || [[ -z ${MIKROTIK_IP_END} ]] \
    || [[ -z ${MIKROTIK_ID_START} ]] || [[ -z ${MIKROTIK_ID_END} ]]; then
        # missing expected exported variables
        echo
        echo "Looks like you don't source the conf correctly!"
        echo "Please run ./configure.sh again!"
        echo "Aborting.."
        echo
        exit 1
    fi
elif [[ ${MIKROTIK_ADDR_TYPE} == custom ]]; then
    # check vars if exported
    if [[ -z ${MIKROTIK_IP_TO_CONF} ]] || [[ -z ${MIKROTIK_ID_TO_CONF} ]]; then
        # missing expected exported variables
        echo
        echo "Looks like you don't source the conf correctly!"
        echo "Please run ./configure.sh again!"
        echo "Aborting.."
        echo
        exit 1
    fi
else
    # unknown error
    echo
    echo "Unknown error occured, aborting.."
    echo
    exit 1
fi
# predefined function to do remote command on mikrotik router
remote_command() {
    ssh ${MIKROTIK_USER}@${MIKROTIK_ADDR} "$@"
    echo "$@"
    echo
    sleep 2
}
# predefined function to build query and exec on mikrotik
exec_tune(){
    # check address type
    if [[ ${1} == range ]]; then
        # get loop count
        LOOP=$((${MIKROTIK_ID_END} - ${MIKROTIK_ID_START}))
        # loop
        for i in $(seq 0 ${LOOP}); do
            # get current ID
            current_id=$((${i} + ${MIKROTIK_ID_START}))
            current_ip=$((${i} + ${MIKROTIK_IP_START}))
            # prompt user
            echo
            echo "Processing for IP ${current_ip}.."
            # build query
            query="/queue simple"
            query="${query} set ${current_id}" # to-do: match with rule type (add, edit, del)
            query="${query} name=\"${MIKROTIK_RULE_PREFIX}${current_ip}${MIKROTIK_RULE_SUFFIX}\""
            query="${query} disabled=no" # enable rule
            query="${query} max-limit=${MIKROTIK_MAX_UPLOAD}/${MIKROTIK_MAX_DOWNLOAD}"
            query="${query} burst-limit=${MIKROTIK_BURST_LIMIT_UPLOAD}/${MIKROTIK_BURST_LIMIT_DOWNLOAD}"
            query="${query} burst-threshold=${MIKROTIK_BURST_THRESHOLD_UPLOAD}/${MIKROTIK_BURST_THRESHOLD_DOWNLOAD}"
            query="${query} burst-time=${MIKROTIK_BURST_TIME_UPLOAD}/${MIKROTIK_BURST_TIME_DOWNLOAD}"
            query="${query} limit-at=${MIKROTIK_LIMIT_AT_UPLOAD}/${MIKROTIK_LIMIT_AT_DOWNLOAD}"
            query="${query} priority=${MIKROTIK_PRIORITY_UPLOAD}/${MIKROTIK_PRIORITY_DOWNLOAD}"
            # optional variables
            if [[ ! -z ${MIKROTIK_COMMENT} ]]; then
                query="${query} comment=\"${MIKROTIK_COMMENT}\""
            else
                query="${query} comment=\"\"" # remove comment
            fi
            # exec
            remote_command ${query} &>> rules.log
        done
    elif [[ ${1} == custom ]]; then
        # parse input as array
        ARR_IP=(${MIKROTIK_IP_TO_CONF})
        ARR_ID=(${MIKROTIK_ID_TO_CONF})
        # loop
        for i in ${!ARR_IP[@]}; do
            # get current status
            current_id=${ARR_ID[${i}]}
            current_ip=${ARR_IP[${i}]}
            # prompt user
            echo
            echo "Processing for IP ${current_ip}.."
            # build query
            query="/queue simple"
            query="${query} set ${current_id}" # to-do: match with rule type (add, edit, del)
            query="${query} name=\"${MIKROTIK_RULE_PREFIX}${current_ip}${MIKROTIK_RULE_SUFFIX}\""
            query="${query} disabled=no" # enable rule
            query="${query} max-limit=${MIKROTIK_MAX_UPLOAD}/${MIKROTIK_MAX_DOWNLOAD}"
            query="${query} burst-limit=${MIKROTIK_BURST_LIMIT_UPLOAD}/${MIKROTIK_BURST_LIMIT_DOWNLOAD}"
            query="${query} burst-threshold=${MIKROTIK_BURST_THRESHOLD_UPLOAD}/${MIKROTIK_BURST_THRESHOLD_DOWNLOAD}"
            query="${query} burst-time=${MIKROTIK_BURST_TIME_UPLOAD}/${MIKROTIK_BURST_TIME_DOWNLOAD}"
            query="${query} limit-at=${MIKROTIK_LIMIT_AT_UPLOAD}/${MIKROTIK_LIMIT_AT_DOWNLOAD}"
            query="${query} priority=${MIKROTIK_PRIORITY_UPLOAD}/${MIKROTIK_PRIORITY_DOWNLOAD}"
            # optional variables
            if [[ ! -z ${MIKROTIK_COMMENT} ]]; then
                query="${query} comment=\"${MIKROTIK_COMMENT}\""
            else
                query="${query} comment=\"\"" # remove comment
            fi
            # exec
            remote_command ${query} &>> rules.log
        done
    else
        # error defining address type
        echo
        echo "Error occured when building queries! Aborting.."
        echo
        exit 1
    fi
}
# predefined function to cleanup log files
cleanup_log(){
    echo
    echo "Cleaning up log files.."
    echo
    rm -f *.tmp # cleanup all temp files
    mkdir -p log
    rm -f log/*
    mv *.log log/ # move all log files
}
# check args num
if [[ $# -gt 0 ]]; then
    # any args inserted
    echo
    echo "Don't need any arguments to run this! Aborting.."
    echo
    exit 1
fi
# show ssh credentials
echo
echo "Running SSH for ${MIKROTIK_USER}@${MIKROTIK_ADDR} .."
# print simple queue rules and prompt user
echo
echo "Getting current rules.."
echo
remote_command '/queue simple print' &> current_rules.log
# prepare log
echo "" > rules.log
# execute on mikrotik
exec_tune ${MIKROTIK_ADDR_TYPE}
echo
echo "Getting modified rules.."
echo
remote_command '/queue simple print' &> modified_rules.log
# cleanup by moving all log files
cleanup_log
# todo: cleanup vars after tuning queue
# prompt user when done
echo
echo "Done!"
echo "Logs and results are saved into log directory"
echo
echo "Don't forget to clean your leftover by running:"
echo "source cleanup.sh"
echo