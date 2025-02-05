# Repository Information
Name: mikrotik-backup

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
	url = https://gitlab.com/mikrotik-shiroe/mikrotik-backup.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: backup-script.txt
================================================
:global IdentityID [/system identity get name];
:local YandexLogin "mail.login";
:local YandexPassword "mail.pass";
:local MailTo "mail.to";
:local MailSubject "MikroTik $IdentityID Backup";
:local CurrentTime [/system clock get time];
:local CurrentDate [/system clock get date];
:local Hour [:tostr [:pick $CurrentTime 0 2]];
:local Min [:tostr [:pick $CurrentTime 3 5]];
:local Day [:tostr [:pick $CurrentDate 4 6]];
:local Month [:tostr [:pick $CurrentDate 0 3]];
:local Year [:tostr [:pick $CurrentDate 7 [:len $CurrentDate]]];
:local smtpserv [:resolve "smtp.yandex.ru"];
:log info "Flushing DNS cache...";
/ip dns cache flush;
:delay 5;
:do {
  :local FileName ([/system identity get name]."___$Year-$Month-$Day_$Hour:$Min.backup");
  /system backup save encryption=aes-sha256 password=ug17kxdbXDVl name=$FileName;
  :log info "Backup file ($FileName) created success";
  :local Exportfile ([/system identity get name]."___$Year-$Month-$Day_$Hour:$Min.rsc");
  :log info "Backup file ($Exportfile) created success";
  /export file=$Exportfile;
  :local ExportfileVerbose ([/system identity get name]."___$Year-$Month-$Day_$Hour:$Min_Verbose.rsc");
  /export verbose file=$ExportfileVerbose;
  :log info "Backup file ($ExportfileVerbose) created success";
  :local files {$FileName;$Exportfile;$ExportfileVerbose};
  :do {
    :delay 3s;
    :global logMessages;
    :set logMessages ""
    :foreach i in=[/log find ] do={ 
      :set logMessages ($logMessages. [/log get $i time ]. " "); 
      :set logMessages ($logMessages. [/log get $i message ]); 
      :set logMessages ($logMessages. "\n")
    }
    /tool e-mail send server=$smtpserv port=587 start-tls=yes user=$YandexLogin \
      password=$YandexPassword to=$MailTo from=$YandexLogin \
      subject=($MailSubject." ($Day/$Month/$Year $Hour:$Min)") \
      body=( \
        "System information:". \
        "\n____________________\n \n". \
        "Board name: ".[/system resource get platform]." ".[/system resource get board-name]."\n". \
        "Identity: ".[/system identity get name]."\n". \
        "Version: ".[/system resource get version]."\n". \
        "CPU: ".[/system resource get cpu]." (load ".[/system resource get cpu-load]."%)\n". \
        "Free HDD space: ".[/system resource get free-hdd-space]." (total: ".[/system resource get total-hdd-space].")\n". \
        "Free memory: ".[/system resource get free-memory]." (total: ".[/system resource get total-memory].")\n". \
        "Uptime: ".[/system resource get uptime]. \
        "\n \n \n". \
        "Last log messages:". \
        "\n____________________\n \n". \
        $logMessages \
      ) file=$files;
    :log info "Mail with backup sending success";
    :do {
      :delay 5s;
      /file remove $FileName;
	  :delay 5s;
	  /file remove $Exportfile;
      :delay 5s;
	  /file remove $ExportfileVerbose;
      :log info "Remove backup file success";
    } on-error={
      :log warning "Cannot remove backup file $FileName";
    };
  } on-error={
	  :log warning "Email sending failed!";
	  :log warning "Deleting creating backups files";
	  :delay 5s;
      /file remove $FileName;
	  :delay 5s;
	  /file remove $Exportfile;
      :delay 5s;
	  /file remove $ExportfileVerbose;
      :log info "Remove backup file success";
  };
} on-error={
  :log error "Backup creation failed!";
};
================================================

File: README.md
================================================
# Mikrotik-Backup