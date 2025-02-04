# Document Information
Title: TFTP
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/131366922/TFTP,

# Content
# Introduction
Trivial File Transfer Protocol or simply TFTP is a very simple protocol used to transfer files. Each nonterminal packet is acknowledged separately.
```
ip/tftp/
```
This menu contains all TFTP access rules. If in this menu are no rules, the TFTP server is not started when RouterOS boots. This menu only shows 1 additional attribute compared to what you can set when creating a rule.
# Parameters
Property | Description
----------------------
ip-address(required) | Range of IP addresses accepted as clients if empty0.0.0.0/0will be used
allow-rollover(Default: No) | If set toyesTFTP server will allow the sequence number to roll over when the maximum value is reached. This is used to enable large downloads using the TFTP server.
req-filename | Requested filename asaregular expression (regex)if a field is left empty it defaults to.*
real-filename | Ifreq-filenameandreal-filenamevalues are set and valid, the requested filename will be replaced with matched file. This field has to be set. If multipleregexis specified inreq-filename, with this field you can set which ones should match, so this rule is validated.Thereal-filenameformat for using multipleregexisfilename\0\5\6
allow(default: yes) | To allow connection if the above fields are set. ifno, a connection will be interrupted
read-only(default: no) | Sets if a file can be written to, if set to "yes" write attempt will fail with error
hits(read-only) | How many times this access rule entry has been used (read-only)
# Settings
```
/ip/tftp/settings
```
This menu contains all TFTP settings.
Property | Description
----------------------
max-block-size(default:4096) | Maximum accepted block size value. During the transfer negotiation phase, the RouterOS device will not negotiate a larger value than this.
# Regexp
Req-filename field allowed regexp, allowed regexp in this field are:
brackets ()- marking subsection:
```
example 1a(sd|fg)will match asd or afg
```
asterisk "*"- match zero or more times preceding symbol:
```
example 1a*will match any length name consisting purely of symbolsaor no symbols at all
example 2.*will match any length name, also, empty field
example 3as*dfwill match adf, asdf, assdf, asssdf etc.
```
plus "+"will match one or more times the preceding symbol:
```
example: as+df will match asdf, assdf etc.
```
dot "."- matches any symbol:
```
exampleas.fwill match asdf, asbf ashf etc.
```
square brackets []- variation between:
```
exampleas[df]will matchasdandasf
```
question mark "?"will match one or no symbols:
```
exampleasd?fwill matchasdfandasf
```
caret "^"- used at the beginning of the line means that the line starts with;
dollar "$"- means at the end of the line.
# Examples
If a file is requested return the file from the store called sata1:
```
/ip tftp add req-filename=file.txt real-filename=/sata1/file.txt allow=yes read-only=yes
```
If we want to give out one specificfileno matter what the user is requesting:
```
/ip tftp add req-filename=.* real-filename=/sata1/file.txt allow=yes read-only=yes
```
If the user requestsaaa.binorbbb.binthen give themccc.bin:
```
/ip tftp add req-filename="(aaa.bin)|(bbb.bin)" real-filename="/sata1/ccc.bin\\0" allow=yes read-only=yes
```