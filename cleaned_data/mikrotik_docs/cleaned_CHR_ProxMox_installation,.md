# Document Information
Title: CHR ProxMox installation
Section: mikrotik_docs
Source: https://help.mikrotik.com/docs/spaces/ROS/pages/48660553/CHR+ProxMox+installation,

# Content
Note:It's a good idea to create a second test VM so you can refer to it's.conf file to make sure you get the syntax right
# Alternative approach
```
qemu-img convert -f raw -O qcow2 chr-6.40.3.img vm-(VM_ID)-disk-1.qcow2
```
# Bash script approach
If you have access to the ProxMox host then CHR VM can also be created quickly via BASH script. Below is an example of one such script.
What this script does:
```
# !/bin/bash
# vars
version="nil"
vmID="nil"
echo "# Start of Script # # Checking if temp dir is available..."
if [ -d /root/temp ]
then
echo "-- Directory exists!"
else
echo "-- Creating temp dir!"
mkdir /root/temp
fi
# Ask user for version
echo "# Preparing for image download and VM creation!"
read -p "Please input CHR version to deploy (6.38.2, 6.40.1, etc):" version
# Check if image is available and download if needed
if [ -f /root/temp/chr-$version.img ]
then
echo "-- CHR image is available."
else
echo "-- Downloading CHR $version image file."
cd  /root/temp
echo "---------------------------------------------------------------------------"
wget https://download.mikrotik.com/routeros/$version/chr-$version.img.zip
unzip chr-$version.img.zip
echo "---------------------------------------------------------------------------"
fi
# List already existing VM's and ask for vmID
echo "== Printing list of VM's on this hypervisor!"
qm list
echo ""
read -p "Please Enter free vm ID to use:" vmID
echo ""
# Create storage dir for VM if needed.
if [ -d /var/lib/vz/images/$vmID ]
then
echo "-- VM Directory exists! Ideally try another vm ID!"
read -p "Please Enter free vm ID to use:" vmID
else
echo "-- Creating VM image dir!"
mkdir /var/lib/vz/images/$vmID
fi
# Creating qcow2 image for CHR.
echo "-- Converting image to qcow2 format "
qemu-img convert \
-f raw \
-O qcow2 \
/root/temp/chr-$version.img \
/var/lib/vz/images/$vmID/vm-$vmID-disk-1.qcow2
# Creating VM
echo "-- Creating new CHR VM"
qm create $vmID \
--name chr-$version \
--net0 virtio,bridge=vmbr0 \
--bootdisk virtio0 \
--ostype l26 \
--memory 256 \
--onboot no \
--sockets 1 \
--cores 1 \
--virtio0 local:$vmID/vm-$vmID-disk-1.qcow2
echo "# End of Script # "
```
# Useful tips
```
sed -i -e 's/\r$//' *.sh
```