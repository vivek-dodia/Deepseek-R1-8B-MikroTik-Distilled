# Repository Information
Name: winbox-mac

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
	url = https://gitlab.com/yysofiyan/winbox-mac.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: CHANGELOG.md
================================================
# Changelog
## 3.14
- added support for new style authentication and encryption for connections to RouterOS v6.43;
- make all connections in secure mode (all data is encrypted with AES128-CBC-SHA);
- make winbox self upgrade check .exe signature;
- make up/down keys select previous/next entry in address/neighbors list in connect window while login name or password fields are in focus;
- make mouse wheel work anywere in connect window if login or password fields are in focus;
- remember Romon Neighbours Table column widths;
- fixed problem where selected table items were moved to the top if the table filters dropdown button was clicked twice;
## 3.13
- abandoned support for connecting to older RouterOS versions (older than v6), no DLLs will ever be downloaded;
- winbox.exe is now signed executable;
## 3.12
- added new menu entry - "Export Without Passwords";
- make Enter start filtering in Connect window if some of the filters are changed instead of connecting to router;
- do not keep old passwords if user unselected Keep-Password later;
- make file copy & paste work between routers again;
- make Enter key activate Connect if one of connect fields were active even when master password field has not been entered yet;
- fixed Reconnect in RoMON mode with "Open In New Window" enabled;
- other fixes.
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2017 nrlquaker
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
# winbox-mac
![Downloads count](https://img.shields.io/github/downloads/nrlquaker/winbox-mac/total.svg)
winbox-mac is [MikroTik](https://mikrotik.com) Winbox converted to macOS app using [WineBottler](http://winebottler.kronenberg.org).
Icon is from [Winbox4Mac](http://joshaven.com/resources/tools/winbox-for-mac/) used with [Joshaven Potter](http://joshaven.com/#contact) permission.
## Installation
Can be easily installed with [Homebrew Cask](https://caskroom.github.io):
```sh
brew tap nrlquaker/personal
brew cask install winbox-mac
```
## Notes
Managed addresses are saved to app folder so if you want keep them after update to newer version need to save them in the old version using `Tools -> Export...` then load in the new one `Tools -> Import...`
## Version
Current version is based on [Winbox 3.14](https://download.mikrotik.com/routeros/winbox/3.14/winbox.exe)
## Screenshot
![winbox-mac screenshot](screenshot.png)
## License
winbox-mac is released under the [MIT License](https://github.com/nrlquaker/nfov/blob/master/LICENSE)