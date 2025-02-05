# Repository Information
Name: mikrotik-nagios

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
	url = https://gitlab.com/awc-samples/mikrotik-nagios.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: check_snmp_mikrotik.bash
================================================
#!/bin/bash
#title       :check_snmp_mikrotik.bash
#description :Check health of a mikrotik device for nagios via
#	     :SNMP.
#
#author      :Aaron Coach
declare -A newByteIn=()
declare -A newByteOut=()
declare -A oldByteIn=()
declare -A oldByteOut=()
# full path of external programs
SNMPGET="/usr/bin/snmpget"
SNMPWALK="/usr/bin/snmpwalk"
DATE="/bin/date"
ECHO="/bin/echo"
CAT="/bin/cat"
GREP="/bin/grep"
CUT="/usr/bin/cut"
AWK="/usr/bin/awk"
BC="/usr/bin/bc"
# defaults
SNMPVersion="3"
SNMPV2Community="public"
SNMPTimeout="10"
warningTemperature="40"
criticalTemperature="45"
warningMemory="80"
criticalMemory="95"
warningLoad="90"
criticalLoad="95"
hostname=""
healthWarningStatus=0
healthCriticalStatus=0
verbose="no"
home=$(echo ~)
filePathPrefix="${home}/check_snmp_mikrotik_"
interfaces=""
#OID declarations
OID_model=".1.3.6.1.2.1.47.1.1.1.1.2.65536"
OID_buildTime=".1.3.6.1.4.1.14988.1.1.7.6.0"
OID_voltage=".1.3.6.1.4.1.14988.1.1.3.8.0"
OID_temperature=".1.3.6.1.4.1.14988.1.1.3.10.0"
OID_totalMemory=".1.3.6.1.2.1.25.2.3.1.5.65536"
OID_usedMemory=".1.3.6.1.2.1.25.2.3.1.6.65536"
OID_cpuFrequency=".1.3.6.1.4.1.14988.1.1.3.14.0"
OID_cpuLoad=".1.3.6.1.2.1.25.3.3.1.2.1"
OID_interfaces=".1.3.6.1.2.1.2.2.1.2"
OID_bytesIn=".1.3.6.1.2.1.31.1.1.1.6."
OID_bytesOut=".1.3.6.1.2.1.31.1.1.1.10."
usage()
{
    $ECHO "Usage: ./check_snmp_mikrotik.sh [option] -H [hostname] -u [username] -p [password]"
    $ECHO "options:"
    $ECHO "            -u [snmp username]       Username for SNMPv3"
    $ECHO "            -p [snmp password]       Password for SNMPv3"
    $ECHO ""
    $ECHO ""
    $ECHO "            -I [interfaces]          Interfaces (for traffic average) (Wrap in \"\" if more than 1)"
    $ECHO ""
    $ECHO ""
    $ECHO "            -W [warning temp]        Warning temperature (for processor & mikrotik) (default $warningTemperature)"
    $ECHO "            -C [critical temp]       Critical temperature (for processor & mikrotik) (default $criticalTemperature)"
    $ECHO ""
    $ECHO ""
    $ECHO "            -w [warning %]           Warning memory usage percentage (default $warningMemory)"
    $ECHO "            -c [critical %]          Critical memory usage percentage (default $criticalMemory)"
    $ECHO ""
    $ECHO ""
    $ECHO "            -K [warning %]           Warning cpu load percentage (default $warningLoad)"
    $ECHO "            -L [critical %]          Critical cpu load percentage (default $criticalLoad)"
    $ECHO ""
    $ECHO ""
    $ECHO "            -v                       Verbose - print all informations about your Mikrotik"
    $ECHO ""
    $ECHO ""
    $ECHO "examples:    ./check_snmp_mikrotik -u admin -p 1234 -H router.intranet"
    $ECHO "             ./check_snmp_mikrotik.sh -H router.intranet -u admin -p Password -I \"ether11 ether12\""
    exit 3
}
if [ "$1" == "--help" ]; then
    usage; exit 0
fi
while getopts ":2:H:u:p:W:C:w:c:K:L:I:v" OPTNAME; do
	case $OPTNAME in
        2)
            SNMPVersion="2"
            SNMPV2Community="$OPTARG"
            ;;
        H)
	    hostname="$OPTARG"
	    ;;
        u)
            SNMPUser="$OPTARG"
            ;;
        p)
            SNMPPassword="$OPTARG"
            ;;
        W)
            warningTemperature="$OPTARG"
            ;;
	C)
	    criticalTemperature="$OPTARG"
	    ;;
	w)
	    warningMemory="$OPTARG"
	    ;;
	c)
	    criticalMemory="$OPTARG"
	    ;;
        K)
            warningLoad="$OPTARG"
            ;;
        L)
            criticalLoad="$OPTARG"
            ;;
        I)
            interfaces="$OPTARG"
            ;;
        v)
            verbose="yes"
            ;;
	*)
            usage
	    ;;
	esac
done
if [ "$warningTemperature" -gt "$criticalTemperature" ] ; then
    echo "Critical temperature must be higher than warning temperature"
    echo "Warning temperature: $warningTemperature"
    echo "Critical temperature: $criticalTemperature"
    echo ""
    echo "For more information:  ./${0##*/} --help" 
    exit 1 
fi
if [ "$warningMemory" -gt "$criticalMemory" ] ; then
    echo "The Critical memory usage percentage  must be higher than the warning memory usage percentage"
    echo "Warning: $warningMemory"
    echo "Critical: $criticalMemory"
    echo ""
    echo "For more information:  ./${0##*/} --help"
    exit 1
fi
if [ "$hostname" = "" ] || ([ "$SNMPVersion" = "3" ] && [ "$SNMPUser" = "" ]) || ([ "$SNMPVersion" = "3" ] && [ "$SNMPPassword" = "" ]); then
    usage
else
    if [ "$SNMPVersion" = "2" ]; then
        SNMPArgs=" -OQne -v 2c -c $SNMPV2Community -t $SNMPTimeout"
    else
        SNMPArgs=" -OQne -v 3 -u $SNMPUser -A $SNMPPassword -l authNoPriv -a MD5 -t $SNMPTimeout"
    fi
    interfacesFile=${filePathPrefix}${hostname}"_interfaces.txt"
    if ! [ -z "$interfaces" ]; then
        if [ ! -f $interfacesFile ]; then
            if touch $interfacesFile 2>/dev/null; then
                $SNMPWALK $SNMPArgs $hostname $OID_interfaces > $interfacesFile 2>/dev/null
                if [ "$?" != "0" ] ; then
                    echo "CRITICAL - Problem with SNMP request, check user/password/host"
                    exit 2
                fi
            else
                echo "CRITICAL - Interfaces file could not be created at $interfacesFile"
                exit 2
            fi
        fi
        interfacesTemp=$(cat $interfacesFile)
        for interface in $interfaces; do
            if interfaceIDTemp=$($ECHO "$interfacesTemp" | $GREP -i $interface\"); then
                OID_interfaceIds+=${OID_bytesIn}$($ECHO "$interfaceIDTemp" | $CUT -d " " -f 1 | $CUT -d . -f 12)" "
                OID_interfaceIds+=${OID_bytesOut}$($ECHO "$interfaceIDTemp" | $CUT -d " " -f 1 | $CUT -d . -f 12)" "
            else
                echo "CRITICAL - Interface $interface not found, check name"
                exit 2
            fi
        done
    fi
    mikrotik=$($SNMPGET $SNMPArgs $hostname $OID_model $OID_buildTime $OID_voltage $OID_temperature $OID_totalMemory $OID_usedMemory \
                                            $OID_cpuFrequency $OID_cpuLoad $OID_interfaceIds 2> /dev/null)
    if [ "$?" != "0" ] ; then
        echo "CRITICAL - Problem with SNMP request, check user/password/host"
        exit 2
    fi
    model="$(echo "$mikrotik" | grep $OID_model | cut -d \" -f 2)"
    buildTime="$(echo "$mikrotik" | grep $OID_buildTime | cut -d \" -f 2)"
    voltage=$(echo "$mikrotik" | grep $OID_voltage | cut -d " " -f 3 | gawk -v OFS=. -v FIELDWIDTHS="2 1" '{$1=$1; print}')
    temperature=$(echo "$mikrotik" | grep $OID_temperature | cut -d " " -f 3 | gawk -v OFS=. -v FIELDWIDTHS="2 1" '{$1=$1; print}')
    totalMemory=$(echo "$mikrotik" | grep $OID_totalMemory | cut -d " " -f 3)
    usedMemory=$(echo "$mikrotik" | grep $OID_usedMemory | cut -d " " -f 3)
    cpuFrequency=$(echo "$mikrotik" | grep $OID_cpuFrequency | cut -d " " -f 3)
    cpuLoad=$(echo "$mikrotik" | grep $OID_cpuLoad | cut -d " " -f 3)
    if ! [ -z "$interfaces" ]; then
        historyFile=${filePathPrefix}${hostname}"_traffic.txt"
        writeHistoryFile()
        {
            $ECHO "oldUnixTime="$($DATE +%s) > $historyFile
            for interface in $interfaces; do
                $ECHO "oldByteIn[$interface]="${newByteIn[$interface]} >> $historyFile
                $ECHO "oldByteOut[$interface]="${newByteOut[$interface]} >> $historyFile
            done
        }
        newBytes=$(echo "$mikrotik" | grep -e $OID_bytesIn -e $OID_bytesOut | $AWK {'print $3'})
        i=1
        for interface in $interfaces; do
            newByteIn[$interface]=$($ECHO "$newBytes" | $AWK "NR==$i")
            newByteOut[$interface]=$($ECHO "$newBytes" | $AWK "NR==$(( $i + 1 ))")
            i=$(( $i + 2 ))
        done
        if [ ! -f $historyFile ]; then
            if touch $historyFile 2>/dev/null; then
                writeHistoryFile
            else
                $ECHO "CRITICAL - History file could not be created at $historyFile"
                exit 1
            fi
        fi
        . $historyFile
        writeHistoryFile
        time=$(( $($DATE +%s) - $oldUnixTime ))
        for interface in $interfaces; do
            if [ -z ${oldByteIn[$interface]} ] || [ -z ${newByteIn[$interface]} ]; then
                byteIn=0
            else
                byteIn=$(( ${newByteIn[$interface]} - ${oldByteIn[$interface]} ))
            fi
            if [ -z ${oldByteOut[$interface]} ] || [ -z ${newByteOut[$interface]} ]; then
                byteOut=0
            else
                byteOut=$(( ${newByteOut[$interface]} - ${oldByteOut[$interface]} ))
            fi
            if ! [ $byteIn -le 0 ]; then
                in=$(printf '%3.2f\n' $($BC -l <<< "scale=2; ($byteIn/$time)/(1024*1024)"))
            else
                in=0.00
            fi
            if ! [ $byteOut -le 0 ]; then
                out=$(printf '%3.2f\n' $($BC -l <<< "scale=2; ($byteOut/$time)/(1024*1024)"))
            else
                out=0.00
            fi
            metricString+="'$interface in average'=${in}MB;0;0;0;0 '$interface out average'=${out}MB;0;0;0;0 "
        done
    fi
    healthString="Mikrotik $model"
    metricString+="'temperature'=$temperature;$warningTemperature;$criticalTemperature;0;0 "
    if [ "$(echo $temperature | cut -d "." -f 1)" -ge "$warningTemperature" ]; then
        if [ "$(echo $temperature | cut -d "." -f 1)" -ge "$criticalTemperature" ]; then
            temperature="${temperature}C (CRITICAL)"
            healthCriticalStatus=1
            healthString+=", temperature: $temperature "
        else
            temperature="${temperature}C (WARNING)"
            healthWarningStatus=1
            healthString+=", temperature: $temperature "
        fi
    else
        temperature="${temperature}C (Normal)"
    fi
    metricString+="'cpu load'=$cpuLoad%;$warningLoad;$criticalLoad;0;0 "
    if [ "$cpuLoad" -ge "$warningLoad" ]; then
        if [ "$cpuLoad" -ge "$criticalLoad" ]; then
            cpuLoad="$cpuLoad% (CRITICAL)"
            healthCriticalStatus=1
            healthString+=", cpu load: $cpuLoad "
        else
            cpuLoad="$cpuLoad% (WARNING)"
            healthWarningStatus=1
            healthString+=", cpu load: $cpuLoad "
        fi
    else
        cpuLoad="$cpuLoad% (Normal)"
    fi
    percentMemory=$((usedMemory / ($totalMemory / 100)))
    metricString+="'memory usage'=$percentMemory%;$warningMemory;$criticalMemory;0;0 "
    if [ "$percentMemory" -ge "$warningMemory" ]; then
        if [ "$percentMemory" -ge "$criticalMemory" ]; then
            percentMemory="$percentMemory% (CRITICAL)"
            healthCriticalStatus=1
            healthString+=", memory: $percentMemory "
        else
            percentMemory="$percentMemory% (WARNING)"
            healthWarningStatus=1
            healthString+=", memory: $percentMemory "
        fi
    else
        memory+="% (Normal)"
    fi
    if [ "$verbose" = "yes" ] ; then
        echo "Mikrotik model:       $model"
        echo "RouterOS build date:  $buildTime"
        echo "Voltage:              ${voltage}V"
        echo "Temperature:          $temperature"
        echo "Total memory:         ${totalMemory}KB"
        echo "Used memory:          ${usedMemory}KB"
        echo "CPU frequency:        ${cpuFrequency}MHz"
        echo "CPU load:             $cpuLoad"
    fi
    if [ "$healthCriticalStatus" = "1" ] ; then
        echo "CRITICAL - $healthString | $metricString"
        exit 2
    fi
    if [ "$healthWarningStatus" = "1" ] ; then
        echo "WARNING - $healthString | $metricString"
        exit 1
    fi
    if [ "$healthCriticalStatus" = "0" ] && [ "$healthWarningStatus" = "0" ] ; then
        echo "OK - $healthString is in good health | $metricString"
        exit 0
    fi
fi