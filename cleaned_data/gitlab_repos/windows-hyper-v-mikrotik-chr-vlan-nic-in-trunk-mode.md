# Repository Information
Name: windows-hyper-v-mikrotik-chr-vlan-nic-in-trunk-mode

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
	url = https://gitlab.com/wiki28/mikrotik/windows-hyper-v-mikrotik-chr-vlan-nic-in-trunk-mode.git
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
# Windows Hyper-V + Mikrotik CHR + Vlan nic in trunk mode
### Когда порт Mikrotik'a работает в режиме Trunk'a Vlan'ы не отрабатывают.
Для решения данной проблемы мы должны хостовой системе сказать, что на сетевом интерфейсе у нас поднят Trunk и по нему ходят Vlan'ы
1. Получим список сетевых адаптеров и их Mac-адреса у нашей виртуальной машины
```
Get-VMNetworkAdapter -VMName "*" | ft VMName, SwitchName, MacAddress
```
2. Добавим Trunk на нужный сетевой адаптер и укажем Vlan'ы
```
Get-VMNetworkAdapter -VMName "%vmname%" | Where { $_.MacAddress -eq "%mac%" } | Set-VMNetworkAdapterVlan -Trunk -NativeVlanId 0 -AllowedVlanIdList "%vlanid%,%vlanid%"
```
3. Включим спуфинг mac-адресов
```
Get-VMNetworkAdapter -VMName "%vmname%" | Where { $_.MacAddress -eq "%mac%" } | Set-VMNetworkAdapter -MacAddressSpoofing On
```
4. Проверим внесенные изменения
```
Get-VMNetworkAdapter -VMName "%vmname%" | Where { $_.MacAddress -eq "%mac%" } | Get-VMNetworkAdapterVlan
Get-VMNetworkAdapter -VMName "%vmname%" | ft VMName, SwitchName, MacAddress, MacAddressSpoofing
```
### Описание переменных
%vmname% - имя виртуальной машины \
%mac% - мас-адрес сетевого интерфейса, который у нас будет Trunk'ом \
%vlanid% - номера vlan'ов