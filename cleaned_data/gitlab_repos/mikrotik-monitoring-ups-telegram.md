# Repository Information
Name: mikrotik-monitoring-ups-telegram

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
	url = https://gitlab.com/scripts31/mikrotik/monitoring/mikrotik-monitoring-ups-telegram.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
# Mikrotik monitoring UPS + Mikrotik Log + Telegram
## Отслеживаем состояние источника бесперебойного питания который подключен к Mikrotik'у
### Подготовка:
1. Mikrotik - RouterOS **v7.5** (на данной версии проводилось тестирование).
2. Mikrotik - установлен пакет **USP**.
3. Mikrotik - в настройках **RouterOS** добавлен источник бесперебойного питания.
4. Telegram - есть **Bot Token** и **Chat ID**.
### Настройка Mikrotik'а
1. Создадим скрипт для **Telegram Bot'a**:\
**Name** - Variables_Telegram\
**Don't Require Permissions** - да\
**Policy** - нет\
**Source** - [Ссылка на файл](/Scripts/Variables_Telegram.rsc)
Для работы скрипта необходимо указать свои значения переменных:
```
:local myBotToken "%token%"
:local myChatID "%id%"
```
![ALT](/Screenshots/mikrotik_variables_telegram.jpg)
2. Создадим скрипт для отслеживания состояния **UPS**:\
**Name** - Monitoring_UPS\
**Don't Require Permissions** - нет\
**Policy** - read, write, policy, test\
**Script** - [Ссылка на файл](/Scripts/Monitoring_UPS.rsc)
Получить список всех источников бесперебойного питания:
```
/system ups print brief
```
Для работы скрипта необходимо указать свои значения переменных:
```
:local myUpsName "%ups_name%"
:local myUPSBatteryChargeLevelDropeBelow "20"
:local myUPSVoltageUpperLineLimit "241"
:local myUPSVoltageLowerLineLimit "214"
:local myDelaySendNotifi "3"
```
![ALT](/Screenshots/mikrotik_monitoring_ups.jpg)
3. Создадим задание в планировщике:\
**Name** - Script_Monitoring_UPS\
**Start Date** - Jan/01/2000\
**Start Time** - 00:00:00\
**Interval** - 00:00:05 (частота запуска на ваше усмотрение)\
**Policy** - read, write, policy, test\
**On Event** - /system script run "Monitoring_UPS"
![ALT](/Screenshots/mikrotik_schedule_monitoring_ups.jpg)
### Примеры работы скрипта:
**Mikrotik -> System -> Scripts -> Environment**\
![ALT](/Screenshots/mikrotik_monitoring_ups_env_info.jpg)
**Mikrotik -> Log**\
![ALT](/Screenshots/mikrotik_monitoring_ups_logs.jpg)
**Telegram:**\
Источник бесперебойного питания подключен.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_ups_connected.jpg)
Источник бесперебойного питания отключен.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_ups_disconnected.jpg)
Сбой питания.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_power_failure.jpg)
Питание восстановлено.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_power_restore.jpg)
Уровень заряда батареи упал ниже порогового значения.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_battery_level_dropped_below.jpg)
Батарея полностью заряжена.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_battery_fully_charged.jpg)
Высокое входное напряжение.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_high_input_voltage.jpg)
Низкое входное напряжение.\
![ALT](/Screenshots/mikrotik_monitoring_ups_telegram_low_input_voltage.jpg)
================================================

File: Monitoring_UPS.rsc
================================================
#
#Script to monitoring uninterruptible power supplies
#Written by TooMooN
#RouterOS v7.5
#Version 3.1
#
#Set global variables
:global UPSStatus
:global UPSCharge
:global UPSVoltage
:global UPSOnLine
:global UPSOnBattery
:global UPSVoltageAboveUpperLimit
:global UPSVoltageBelowLowerLimit
#Set UPS variables
:local myUpsName "%ups_name%"
:local myUPSStatusBattery
:local myUPSStatusChargeLevel
:local myUPSStatusVoltage
:local myUPSBatteryChargeLevelDropeBelow "20"
:local myUPSVoltageUpperLineLimit "241"
:local myUPSVoltageLowerLineLimit "214"
#Set local variables
:local myDeviceID [/system identity get name]
:local myTime
:local myDate
:local time [/system clock get time]
:local date [/system clock get date]
:local month [:tostr ([:find "janfebmaraprmayjunjulaugsepoctnovdec" [:pick $date 0 3] ]/3+1)]
:if ([:tonum $month]<10) do={
    :set month "0$month"
   }
:set myDate ([:pick $date 7 11].".".$month.".".[:pick $date 4 6])
:set myTime ([:pick $time 0 2].":".[:pick $time 3 5].":".[:pick $time 6 8])
#Set Delay in sec for send notification if ISP down
:local myDelaySendNotifi "3"
#Set Telegram variables
:local myTgEmojiUPSConnected "\F0\9F\8C\90"
:local myTgEmojiUPSDisconnected "\E2\9D\97"
:local myTgEmojiUPSOnLine "\F0\9F\94\8C"
:local myTgEmojiUPSOnBattery "\F0\9F\94\B4"
:local myTgEmojiUPSBatteryCharge "\E2\9A\A1"
:local myTgEmojiUPSBatteryChargeFull "\F0\9F\94\8B"
:local myTgEmojiUPSVoltageAboveUpperLimit "\F0\9F\93\88"
:local myTgEmojiUPSVoltageBelowLowerLimit "\F0\9F\93\89"
:local myTgSendMessage [:parse [/system script get "Variables_Telegram" source]]
#Get UPS variables
/system ups monitor $myUpsName once do={
    :set myUPSStatusBattery $"on-battery"
    :set myUPSStatusChargeLevel $"battery-charge"
    :set myUPSStatusVoltage [:pick $"line-voltage" 0 3]
   }
#Set message text
:local myMsgBodyUPSConnected "Info: $myDeviceID [Date $myDate Time $myTime] - UPS Connected."
:local myMsgBodyUPSDisconnected "Critical: $myDeviceID [Date $myDate Time $myTime] - UPS Disconnected."
:local myMsgBodyUPSPowerFailure "Critical: $myDeviceID [Date $myDate Time $myTime] - UPS Power failure."
:local myMsgBodyUPSPowerRestore "Info: $myDeviceID [Date $myDate Time $myTime] - UPS Power restore."
:local myMsgBodyUPSBatteryChargeFull "Info: $myDeviceID [Date $myDate Time $myTime] - UPS Battery fully charged."
:local myMsgBodyUPSBatteryChargeLevelDropeBelow ("Warning: $myDeviceID [Date $myDate Time $myTime] - UPS Battery level dropped below $myUPSBatteryChargeLevelDropeBelow"."%.")
:local myMsgBodyUPSVoltageAboveUpperLimit ("Warning: $myDeviceID [Date $myDate Time $myTime] - UPS high input voltage - $myUPSStatusVoltage"."V.")
:local myMsgBodyUPSVoltageBelowLowerLimit ("Warning: $myDeviceID [Date $myDate Time $myTime] - UPS low input voltage - $myUPSStatusVoltage"."V.")
#######################################################################################################################
#UPS Check availability
#######################################################################################################################
:if ([:len [/system ups find invalid name=$myUpsName]]>0) do={
    :if ("$UPSStatus"!="Disconnected") do={
        :set UPSStatus "Disconnected"
        :set UPSCharge "Unavailable"
        :set UPSVoltage "Unavailable"
        :local myTgMsgText "$myTgEmojiUPSDisconnected $myMsgBodyUPSDisconnected"
        log error ("$myMsgBodyUPSDisconnected")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
        }
   } else={
:if ((!$myUPSStatusBattery) && ("$UPSStatus"="Disconnected")) do={
    :if ($myUPSStatusChargeLevel=100) do={
        :set UPSStatus "Online"
        :local myTgMsgText "$myTgEmojiUPSConnected $myMsgBodyUPSConnected"
        log warning ("$myMsgBodyUPSConnected")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
        } else={
        :local myTgMsgText "$myTgEmojiUPSConnected $myMsgBodyUPSConnected"
        log warning ("$myMsgBodyUPSConnected")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
    }
   }
#######################################################################################################################
#First run, initialize the global flags
#######################################################################################################################
:if ([:typeof $UPSStatus]="nothing") do={
    :set UPSStatus "Online"
   }
:if ([:typeof $UPSVoltage]="nothing") do={
    :set UPSVoltage "$myUPSStatusVoltage"
   }
#######################################################################################################################
#UPS Voltage above upper limit
#######################################################################################################################
:if ((!$myUPSStatusBattery) && ("$myUPSStatusVoltage">="$myUPSVoltageUpperLineLimit")) do={
    :if (("$myUPSStatusVoltage"!="$UPSVoltage") && ("$myUPSStatusVoltage"!="0")) do={
        :set UPSVoltage "$myUPSStatusVoltage"
        :set UPSVoltageAboveUpperLimit "Date $myDate Time $myTime"
        :local myTgMsgText "$myTgEmojiUPSVoltageAboveUpperLimit $myMsgBodyUPSVoltageAboveUpperLimit"
        log error ("$myMsgBodyUPSVoltageAboveUpperLimit")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
        }
    }
#######################################################################################################################
#UPS Voltage below lower limit
#######################################################################################################################
:if ((!$myUPSStatusBattery) && ("$myUPSStatusVoltage"<="$myUPSVoltageLowerLineLimit")) do={
    :if (("$myUPSStatusVoltage"!="$UPSVoltage") && ("$myUPSStatusVoltage"!="0")) do={
        :set UPSVoltage "$myUPSStatusVoltage"
        :set UPSVoltageBelowLowerLimit "Date $myDate Time $myTime"
        :local myTgMsgText "$myTgEmojiUPSVoltageBelowLowerLimit $myMsgBodyUPSVoltageBelowLowerLimit"
        log error ("$myMsgBodyUPSVoltageBelowLowerLimit")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
        }
    }
#######################################################################################################################
#UPS Set Voltage 
#######################################################################################################################
:if (!$myUPSStatusBattery) do={
    :set UPSVoltage "$myUPSStatusVoltage"
    }
#######################################################################################################################
#UPS Set Charge level 
#######################################################################################################################
:set UPSCharge "$myUPSStatusChargeLevel"
#######################################################################################################################
#UPS Power failure
#######################################################################################################################
:if (($myUPSStatusBattery) && ("$UPSStatus"="Online")) do={
    :set UPSOnBattery "Date $myDate Time $myTime"
    :set UPSStatus "On battery" 
    :local myTgMsgText "$myTgEmojiUPSOnBattery $myMsgBodyUPSPowerFailure"
    log error ("$myMsgBodyUPSPowerFailure")
    :delay $myDelaySendNotifi
    $myTgSendMessage myTgMessageText=$myTgMsgText
   }
:if (($myUPSStatusBattery) && ("$UPSStatus"="Charging")) do={
    :set UPSOnBattery "Date $myDate Time $myTime"
    :set UPSStatus "On battery" 
    :local myTgMsgText "$myTgEmojiUPSOnBattery $myMsgBodyUPSPowerFailure"
    log error ("$myMsgBodyUPSPowerFailure")
    :delay $myDelaySendNotifi
    $myTgSendMessage myTgMessageText=$myTgMsgText
   }
#######################################################################################################################
#UPS Power restore
#######################################################################################################################
:if ((!$myUPSStatusBattery) && ("$UPSStatus"="On battery")) do={
    :set UPSOnLine "Date $myDate Time $myTime"
    :set UPSStatus "Charging"
    :local myTgMsgText "$myTgEmojiUPSOnLine $myMsgBodyUPSPowerRestore"
    log warning ("$myMsgBodyUPSPowerRestore")
    :delay $myDelaySendNotifi
    $myTgSendMessage myTgMessageText=$myTgMsgText
   }
:if ((!$myUPSStatusBattery) && ("$UPSStatus"="Low battery level")) do={
    :set UPSOnLine "Date $myDate Time $myTime"
    :set UPSStatus "Charging"
    :local myTgMsgText "$myTgEmojiUPSOnLine $myMsgBodyUPSPowerRestore"
    log warning ("$myMsgBodyUPSPowerRestore")
    :delay $myDelaySendNotifi
    $myTgSendMessage myTgMessageText=$myTgMsgText  
   }
#######################################################################################################################
#UPS Charging
#######################################################################################################################
:if ((!$myUPSStatusBattery) && ($myUPSStatusChargeLevel<100)) do={
    :set UPSStatus "Charging"
   }
#######################################################################################################################
#UPS Full Charge
#######################################################################################################################
:if ((!$myUPSStatusBattery) && ($myUPSStatusChargeLevel=100)) do={
    :if ("$UPSStatus"!="Online") do={
        :set UPSStatus "Online"
        :local myTgMsgText "$myTgEmojiUPSBatteryChargeFull $myMsgBodyUPSBatteryChargeFull"
        log warning ("$myMsgBodyUPSBatteryChargeFull")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
        }
   }
#######################################################################################################################
#UPS Battery charge level drope below
#######################################################################################################################
:if (($myUPSStatusBattery) && ("$myUPSStatusChargeLevel"<="$myUPSBatteryChargeLevelDropeBelow")) do={
    :if ("$UPSStatus"!="Low battery level") do={
        :set UPSStatus "Low battery level"
        :local myTgMsgText "$myTgEmojiUPSBatteryCharge $myMsgBodyUPSBatteryChargeLevelDropeBelow"
        log error ("$myMsgBodyUPSBatteryChargeLevelDropeBelow")
        :delay $myDelaySendNotifi
        $myTgSendMessage myTgMessageText=$myTgMsgText
        }
   }
}
================================================

File: Variables_Telegram.rsc
================================================
#
#Variables for Telegram Bot
#Written by TooMooN
#RouterOS v7.5
#Version 1.0
#
#Bot token
:local myBotToken "%token%"
#Chat ID
:local myChatID "%id%"
#Message
:local myTgMessage [$myTgMessageText]
#Telegram API URL
:local myTgUrl "https://api.telegram.org/bot$myBotToken/sendMessage?chat_id=$myChatID&text=$myTgMessage"
/tool fetch url=$myTgUrl keep-result=no