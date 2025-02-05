# Repository Information
Name: mssqlipbanner

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
	url = https://gitlab.com/LinhyCZ/mssqlipbanner.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: App.config
================================================
﻿<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.6.1" />
    </startup>
</configuration>
================================================

File: Config.cs
================================================
﻿using Newtonsoft.Json;
namespace MSSQLIPBanner
{
    public class Config
    {
        private static Config instance;
        public static void setConfig(Config config)
        {
            instance = config;
        }
        public static string _SSHLogin() { return instance.SSHLogin; }
        public static string _SSHPassword() { return instance.SSHPassword; }
        public static int _SSHPort() { return instance.SSHPort; }
        public static string _SSHIP() { return instance.SSHIP; }
        public static LogLevel _logLevel() { return instance.logLevel; }
        public static string _MSSQL_EVENT_ID() { return instance.MSSQL_EVENT_ID; }
        public static string _SECURITY_AUDIT_EVENT_ID() { return instance.SECURITY_AUDIT_EVENT_ID; }
        public static int _BLOCK_LIMIT() { return instance.BLOCK_LIMIT; }
        public static string _FILE_PATH() { return instance.FILE_PATH; }
        public static string[] _WHITELISTED_IPS() { return instance.WHITELISTED_IPS; }
        [JsonProperty]
        public string SSHLogin;
        [JsonProperty]
        private string SSHPassword;
        [JsonProperty]
        private int SSHPort;
        [JsonProperty]
        private string SSHIP;
        [JsonProperty]
        private LogLevel logLevel;
        [JsonProperty]
        private string MSSQL_EVENT_ID;
        [JsonProperty]
        private string SECURITY_AUDIT_EVENT_ID;
        [JsonProperty]
        private int BLOCK_LIMIT;
        [JsonProperty]
        private string FILE_PATH;
        [JsonProperty]
        private string[] WHITELISTED_IPS;
    }
}
================================================

File: Config.sample.json
================================================
{
  "SSHLogin":"login",
  "SSHPassword":"password",
  "SSHPort":22,
  "SSHIP":"192.168.0.1",
  "logLevel":0,
  "MSSQL_EVENT_ID":"3221243928",
  "SECURITY_AUDIT_EVENT_ID":"4625",
  "BLOCK_LIMIT":5,
  "FILE_PATH":"log/log.txt",
  "WHITELISTED_IPS": [
    "1.2.3.*",
  ]
}
================================================

File: packages.config
================================================
﻿<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="Newtonsoft.Json" version="12.0.3" targetFramework="net461" />
  <package id="SSH.NET" version="2016.1.0" targetFramework="net461" />
</packages>
================================================