# Repository Information
Name: Mikrotik-Bandwidth-Monitoring-Script

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
	url = https://gitlab.com/buananetpbun/Mikrotik-Bandwidth-Monitoring-Script.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
# Mikrotik Bandwidth Monitoring Script
Script Bandwidth monitoring ini hampir 100% akurat mungkin seakurat Cacti Monitoring, sebenarnya rencana awal saya gunakan untuk memantau FUP Quota Indihome namun saya tidak memahami algoritma yang digunakan sistem telkom seperti apa, makanya hasil selalu berbeda, mungkin ini berkaitan dengan streaming yang tidak termasuk dalam sistem FUP mereka.
![image](https://user-images.githubusercontent.com/42666125/111258795-40f16680-8650-11eb-94db-859fbe740518.png)
Silahkan paste script ini di terminal mikrotik
/system scheduler add interval="00:00:00" name="RXByte.log" on-event="1" start-time="00:00:00"  
 /system scheduler add interval="00:00:00" name="RXByteCur.log" on-event="1" start-time="00:00:00"  
 /system scheduler add interval="00:00:00" name="TXByte.log" on-event="1" start-time="00:00:00"  
 /system scheduler add interval="00:00:00" name="TXByteCur.log" on-event="1" start-time="00:00:00"  
 /system scheduler add interval="00:01:00" name="RESET-RXTX" start-time=startup  
 /system scheduler add interval="00:0:030" name="BANDWIDTH-MONITORING" start-time=startup  
Copy Paste Script reset bulanan ini dalam file Scheduler RESET-RXTX
<pre  style="font-family:arial;font-size:12px;border:1px dashed #CCCCCC;width:99%;height:auto;overflow:auto;background:#f0f0f0;;background-image:URL(http://2.bp.blogspot.com/_z5ltvMQPaa8/SjJXr_U2YBI/AAAAAAAAAAM/46OqEP32CJ8/s320/codebg.gif);padding:0px;color:#000000;text-align:left;line-height:20px;">
<code style="color:#000000;word-wrap:normal;"> ################################################################  
 # Script by Agus Ramadhani  
 # fb.com/buananet.pangkalanbun  
 # http://www.o-om.com  
 # SCRIPT MIKROTIK BANDWIDTH MONITORING  
 # Version 1.0  
 ################################################################  
 # Fungsi untuk reset Bulanan Setiap tanggal 1  
 ################################################################  
 :local varDate;  
 :local varDay;  
 :set varDate [/system clock get date];  
 :set varDay [:pick $varDate 4 6];  
 :if ($varDay = "01") do={   
 # jika har ini tanggal 1 reset RXTX ke nilai awal  
 /system scheduler set RXByte.log comment="1" on-event="1"  
 /system scheduler set RXByteCur.log comment="1" on-event="1"  
 /system scheduler set TXByte.log comment="1" on-event=$RXByteCount  
 /system scheduler set TXByteCur.log comment="1" on-event="1"  
 /system scheduler disable [/system scheduler find name="RESET-RXTX"]  
 }  
 ################################################################  
 </code></pre>
 Copy Paste Script Monitoring ini dalam file Scheduler BANDWIDTH-MONITORING
 <pre  style="font-family:arial;font-size:12px;border:1px dashed #CCCCCC;width:99%;height:auto;overflow:auto;background:#f0f0f0;;background-image:URL(http://2.bp.blogspot.com/_z5ltvMQPaa8/SjJXr_U2YBI/AAAAAAAAAAM/46OqEP32CJ8/s320/codebg.gif);padding:0px;color:#000000;text-align:left;line-height:20px;"><code style="color:#000000;word-wrap:normal;"> ################################################################  
 # Script by Agus Ramadhani  
 # fb.com/buananet.pangkalanbun  
 # http://www.o-om.com  
 # SCRIPT MIKROTIK BANDWIDTH MONITORING  
 # Version 1.0  
 ################################################################  
 :local INTMon WAN-WARNET;  
 # silahkan ganti dengan interface (ether) yang ingin dipantau  
 ################################################################  
 :local TOTQuota 500;  
 # Set total quota dalam GB misalkan ISP hanya memberikan hanya 500GB  
 ################################################################  
 :local RXByteCur [/interface get $INTMon rx-byte];  
 # Mengambil nilai RX-Byte saat ini pada interface terpilih  
 ################################################################  
 :local RXByteCount [/system scheduler get RXByteCur.log on-event];  
 # Mengambil nilai RX-Byte dalam file log RXByteCur  
 ################################################################  
 :local RXByte [/system scheduler get RXByte.log on-event];  
 # Mengambil nilai RX-Byte sebelumnya dalam file log RXByte  
 ################################################################  
 :local TXByteCur [/interface get $INTMon tx-byte];  
 # Mengambil nilai TX-Byte saat ini pada interface terpilih  
 ################################################################  
 :local TXByteCount [/system scheduler get TXByteCur.log on-event];  
 # Mengambil nilai TX-Byte saat ini dalam file log TXByteCur  
 ################################################################  
 :local TXByte [/system scheduler get TXByte.log on-event];  
 # Mengambil nilai TX-Byte saat ini dalam file Log TXByte  
 ################################################################  
 :local ifReboot 0;  
 # kita perlu mengetahui apakah router reboot   
 ################################################################  
 :if ($RXByteCur&gt;=$RXByteCount) do={} else={:set $ifReboot ($ifReboot+1);}  
 :if ($TXByteCur&gt;=$TXByteCount) do={} else={:set $ifReboot ($ifReboot+1);}  
 # Tandai jika nilai RXTX-Byte saat ini lebih besar dari RXTX-Byte pada log  
 ################################################################  
 :if ($ifReboot&gt;=1) do={  
 # Cek Jika Router Reboot  
 ################################################################  
 :set $RXByte ($RXByte+$RXByteCount);  
 /system scheduler set RXByte.log comment=$RXByte on-event=$RXByte  
 # jika komputer reboot jumlahkan total RX-Byte  
 ################################################################  
 :set $TXByte ($TXByte+$TXByteCount);  
 /system scheduler set TXByte.log comment=$TXByte on-event=$TXByte  
 } else={  
 # jika komputer reboot jumlahkan total TX-Byte  
 ################################################################  
 }  
 :set RXByteCount ($RXByteCur);  
 /system scheduler set RXByteCur.log comment=$RXByteCount on-event=$RXByteCount  
 # Perbaharui nilai RX-Byte saat ini pada file log RXByteCur  
 ################################################################  
 :set TXByteCount ($TXByteCur);  
 /system scheduler set TXByteCur.log comment=$TXByteCount on-event=$TXByteCount  
 # Perbaharui nilai TX-Byte saat ini pada file log TXByteCur  
 ################################################################  
 :local RXTot ($RXByte+$RXByteCur);  
 :local RXMB ($RXTot / 1024 / 1024);  
 :local RXGB ($RXTot / 1024 / 1024 / 1024);  
 # kalkulasi nilai RX-BYTE dalam MB dan GB  
 ################################################################  
 :local TXTot ($TXByte+$TXByteCur);  
 :local TXMB ($TXTot / 1024 / 1024);  
 :local TXGB ($TXTot / 1024 / 1024 / 1024);  
 # kalkulasi nilai TX-BYTE dalam MB dan GB  
 ################################################################  
 :local RXTX ($RXTot+$TXTot);  
 :local RXTXMB ($RXMB+$TXMB);  
 :local RXTXGB ($RXGB+$TXGB);  
 # Total kalkulasi nilai Total RXTX  
 ################################################################  
 :log warning "###############################################";  
 :log warning "BANDWIDTH MONITORING [ Router Identity: $[/system identity get name] ]";  
 :log warning "###############################################";  
 :log warning "Interface Monitoring For: $INTMon";  
 /interface monitor-traffic [/interface find name=$INTMon] once do={  
 :local tx (tx-bits-per-second / 1024);  
 :local rx (rx-bits-per-second / 1024);  
 :log warning "Live Monitor RX = $rx kbps / TX = $tx kbps";  
 }  
 # hanya untuk menampilkan rxtx saat ini  
 ###############################################################  
 :log warning "Total RX = $RXGB GB / $RXMB MB / $RXTot Bytes";  
 :log warning "Total TX = $TXGB GB / $TXMB MB / $TXTot Bytes";  
 :log warning "Total (RX+TX) = $RXTXGB GB / $RXTXMB MB / $RXTX Bytes";  
 :local percent ($RXTXGB*100 / $TOTQuota);  
 :log error "Used Quota On This Month = $RXTXGB GB = $percent% from $TOTQuota GB";  
 :log warning "###############################################";  
 # Tampilkan Info pada LOG Mikrotik   
 ################################################################  
 :local varDate;  
 :local varDay;  
 :set varDate [/system clock get date];  
 :set varDay [:pick $varDate 4 6];  
 :if ($varDay = "29") do={   
 # jika hari ini tanggal 29 aktifkan RESET-RXTX  
 /system scheduler enable [/system scheduler find name="RESET-RXTX"];  
 }  
 ################################################################  
</code></pre>
jangan lupa ganti nama ether dalam script sesuai interface masing2 yang ingin dipantau
:local INTMon WAN-WARNET;
jangan Lupa ganti total quota yang diberikan ISP masing2 dicontoh adalah 500GB
:local TOTQuota 500;
<img style="float:right; padding-top:10px" src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fbuananetpbun.github.io%2F&count_bg=%23C83D3D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" alt="Hits"/>
================================================