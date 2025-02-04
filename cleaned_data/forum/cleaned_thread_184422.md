# Thread Information
Title: Untitled Thread
Section: mikrotik_forum
Thread ID: 184422

# Discussion

## Initial Question
Author: [SOLVED]Fri Mar 25, 2022 2:35 am
``` add-type@" using System.Net; using System.Security.Cryptography.X509Certificates; public class TrustAllCertsPolicy : ICertificatePolicy { public bool CheckValidationResult( ServicePoint srvPoint, X509Certificate certificate, WebRequest request, int certificateProblem) { return true; } } "@[System.Net.ServicePointManager]::CertificatePolicy=New-ObjectTrustAllCertsPolicy$user='admin'$pass='1234'$pair="$($user):$($pass)"$encodedCreds=[System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))$basicAuthValue="Basic $encodedCreds"$Headers=@{Authorization=$basicAuthValue}$body=@{".id"="switchSimCard"}$routerOSHost="192.168.88.1"$url="https://$routerOSHOST/rest/system/script/run"Invoke-WebRequest-Uri$url-Body($body|ConvertTo-Json)-Headers$Headers-MethodPOST-ContentTypeapplication/json ``` I wrote a powershell script that runs a script on the RouterOS device remotely via REST API.https://gist.github.com/elico/9110bc2a7 ... 1b3e4f8c69
```
---
```

## Response 1
Author: Sat Aug 10, 2024 5:00 pm
``` <# .Synopsis Invoke-MikrotikRestAPI.ps1 uses Mikrotik's RouterOS-RestAPI to remotely trigger actions. .EXAMPLES Invoke-MikrotikRestAPI.ps1 -RouterIP 192.168.88.1 -User admin -Password "MyPassword" -ExecutionMode Command -Data "/log/info test" Invoke-MikrotikRestAPI.ps1 -RouterIP 192.168.88.1 -User admin -Password "MyPassword" -ExecutionMode Script -Data "MyScriptName" #> Param ( [Parameter(Mandatory = $true)][String]$RouterIP, [Parameter(Mandatory = $true)][String]$User, [Parameter(Mandatory = $true)][String]$Password, [Parameter(Mandatory = $true)][String]$Data, [ValidateSet("Script","Command")]$ExecutionMode="Command" ) add-type @" using System.Net; using System.Security.Cryptography.X509Certificates; public class TrustAllCertsPolicy : ICertificatePolicy { public bool CheckValidationResult(ServicePoint srvPoint, X509Certificate certificate, WebRequest request, int certificateProblem) { return true; } } "@ [System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy $encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("$($User):$($Password)")) $Headers = @{Authorization = "Basic $encodedCreds"} $ErrorActionPreference = "SilentlyContinue" $tc = [System.Net.Sockets.TcpClient]::new() $tc.Connect($RouterIP, 443) $ErrorActionPreference = "Continue" if ($tc.Connected) { if ($ExecutionMode -eq "Script") { $body = @{".id" = $Data} Invoke-WebRequest -Uri "http://$RouterIP/rest/system/script/run" -Body ($body|ConvertTo-Json) -Headers $Headers -Method POST -ContentType application/json } if ($ExecutionMode -eq "Command") { $body = @{"script" = $Data} Invoke-WebRequest -Uri "http://$RouterIP/rest/execute" -Body ($body|ConvertTo-Json) -Headers $Headers -Method POST -ContentType application/json } } else { Write-Error "Could not connect to $RouterIP via Port #443! Service ""www-ssl"" already activated in RouterOS under /ip/services ???" } $tc.Dispose() ``` I wrote a powershell script that runs a script on the RouterOS device remotely via REST API.Thank you for sharing this code-snippet. I added the feature to either launch a script or a single command and did some minor changes:
```
Save this code-snippet as "Invoke-MikrotikRestAPI.ps1" and enjoy
```