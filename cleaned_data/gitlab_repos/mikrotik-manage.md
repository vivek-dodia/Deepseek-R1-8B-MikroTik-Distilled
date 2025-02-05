# Repository Information
Name: mikrotik-manage

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
	url = https://gitlab.com/dannybombastic/mikrotik-manage.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: admin.py
================================================
from django.contrib import admin
# Register your models here.
from .models import Device
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_per_page = 200
    ordering = ('user',)
    list_display = (
        'ipv4',
        'macaddress',
        'model',
        'interface',
        'user'
    )
    search_fields = ['user__username', 'macaddress', 'create', 'model']
    list_filter = (
        'macaddress',
        'user',
        'create',
        'model'
    )
================================================

File: apps.py
================================================
from django.apps import AppConfig
class DiscoverConfig(AppConfig):
    name = 'discover'
================================================

File: mikrotik_update.py
================================================
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from ...models import Device
from os import listdir, sys, getenv, path
from datetime import datetime, timedelta
from django.db import connection
from django.utils import timezone
import json
import re
import pexpect
import subprocess
import time
import logging
class Loger:
    filename = None
    logger = None
    ft = '%(filename)s | %(levelname)s | %(asctime)s |--------------------|%(message)s'
    def __init__(self, filename, name):
        self.filename = filename
        logging.basicConfig(
            filename=self.filename,
            filemode='a',
            format=self.ft,
            datefmt='%m/%d/%Y %I:%M:%S %p',
        )
        self.logger = logging.getLogger(name)
        self.log_info('Startring proccess')
    def log_debug(self, msg):
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(msg)
    def log_info(self, msg):
        self.logger.setLevel(logging.INFO)
        self.logger.info(msg)
    def log_warning(self, msg):
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(msg)
    def console_info(self, msg):
        msg_console = self.bcolors.OKGREEN + \
            '| {0: >50} |'.format(msg) + self.bcolors.ENDC
        print(msg_console)
        self.log_info(msg)
    def console_success(self, msg):
        msg_console = self.bcolors.OKBLUE + \
            '| {0: >50} |'.format(msg) + self.bcolors.ENDC
        print(msg_console)
        self.log_info(msg)
    def console_warning(self, msg):
        msg_console = self.bcolors.WARNING + \
            '|{0: >50}|'.format(msg) + self.bcolors.ENDC
        print(msg_console)
        self.log_warning(msg)
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
log = Loger('./mikrotik.log', 'Mikrotik')
class Command(BaseCommand):
    USER = None
    CPE = None
    PASSWORD = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.USER = getenv('LOGNAME')
        self.routers = []
    def add_arguments(self, parser):
        try:
            parser.add_argument(
                '-u', '--update', type=str, help='Elige el nodo que quieres actualizar ej 192.168.0.1', )
            parser.add_argument(
                '-l', '--list', type=int, help='Escanea la red en busca de MACs',  default=10)
        except AttributeError as e:
            self.stderr.write(str(e))
    def handle(self, *args, **options):
        try:
            if options['update']:
                self.stderr.write('Actualizando')
                value = options['update']
                print(f'Actualizando {value}')
                self.get_conection()
            if options['list']:
                self.stderr.write('Listando')
                value = options['list']
                print(f'Listando {value}')
                self.scan(value)
        except AttributeError as e:
            self.stderr.write(str(e))
    def scan(self, timeout=10):
        """ scan for device info """
        mac_list = []
        list_mikrotik = subprocess.Popen(
            ["mactelnet", "-l", f"-t {timeout}"], stdout=subprocess.PIPE)
        while list_mikrotik.stdout.readable():
            line = list_mikrotik.stdout.readline()
            if not line:
                break
            ###############
            # header info off
            if 'MAC' not in line.strip().decode('ascii'):
                mac_list.append(line.strip().decode('ascii'))
        mac_list = set(mac_list)
        i = 0
        for device in mac_list:
            i += 1
            model = re.search(r'\((.*())\)', device)
            interface = re.search(r'hours (.*)', device)
            split_chain = device.split(' ')
            ipv4 = split_chain[0]
            mac = re.compile(r'(?:[0-9a-fA-F]:?){12}').search(device)
            device_model = Device()
            if mac:
                device_model.model = model.group(1)
                device_model.macaddress = device[mac.start():mac.end()]
                device_model.ipv4 = ipv4
                device_model.interface = interface.group(1)
                device_model.user = self.create_user()
                device_model.save()
                self.format_device_list(device_model, i)
    def format_device_list(self, device, index):
        template = f"""  {log.bcolors.OKGREEN}
option:{log.bcolors.OKBLUE} ({index}) {log.bcolors.ENDC} {log.bcolors.OKGREEN}
Ipv4: {device.ipv4}
MacAddress: {device.macaddress} 
model: {device.model}
Interface: {device.interface}
User: {device.user}                       
                    """
        print(template)
    def create_user(self):
        user = ''
        if not User.objects.filter(username=self.USER).exists():
            user = User.objects.create(username=self.USER)
        else:
            user = User.objects.get(username=self.USER)
        return user
    def automate_login(self):
        list_mikrotik = subprocess.run(["mactelnet", "-l", "-t 10"])
        # child = pexpect.spawn('mactelnet',['D4:CA:6D:C1:99:1A'])
        # child.expect('Login:')
        # child.sendline('admin\r')
        # child.expect('Password:')
        # child.sendline("\r")
        # i = child.expect('[Conneting to .*]')
        # print(i)
        # child.delaybeforesend = 50
        # child.sendline('/ip address print')
        # child.expect('[Mikrotik]')
        # child.sendline('/interface ethernet\r')
        # child.expect('[ethernet ]')
        # child.sendline('set [ find default-name=ether1 ] comment="cpeXXXX_VIDEOS_chaptin"\r')
        # child.delaybeforesend = 10
        # child.sendline('/interface wireless\r')
        # child.expect('[wireless ]')
        # child.sendline('set [ find default-name=wlan1 ] comment="cpeXXXX_VIDEOS_chapatin"\r')
        # child.expect('[wireless]')
        # child.delaybeforesend = 45
        # child.sendline('/quit\r\n')
        # child.expect(pexpect.EOF)
        # child.wait()
        # child.interact()
        mac_telnet = pexpect.spawn('mactelnet', ['D4:CA:6D:C1:99:1A'])
        mac_telnet.expect('Login:')
        mac_telnet.sendline('admin\r')
        mac_telnet.expect('Password:')
        mac_telnet.sendline("\r")
        try:
            index = mac_telnet.expect(['done', pexpect.TIMEOUT], timeout=60)
        except pexpect.EOF:
            pass
        print(f'{index}')
        if index == 1:
            print('TIMEOUT in ps command...')
            print(str(mac_telnet))
            time.sleep(13)
        if index == 0:
            print('conectando...')
            mac_telnet.delaybeforesend = 50
            mac_telnet.sendline(
                '/interface wireless; set [ find default-name=wlan1 ] comment="cpeXXXX_VIDEOS_chapa"; /interface ethernet; set [ find default-name=ether1 ] comment="cpeXXXX_VIDEOS_chapo"\r')
            mac_telnet.expect('[Mikrotik ]')
            mac_telnet.delaybeforesend = 10
            mac_telnet.sendline(
                '/interface wireless; set [ find default-name=wlan1 ] comment="cpeXXXX_VIDEOS_chapa"; '
                + '/interface ethernet; set [ find default-name=ether1 ] comment="cpeXXXX_VIDEOS_chapo"\r')
            mac_telnet.expect('[Mikrotik ]')
            mac_telnet.delaybeforesend = 10
            mac_telnet.sendline(
                '/interface wireless; set [ find default-name=wlan1 ] comment="cpeXXXX_VIDEOS_chapa"; '
                + '/interface ethernet; set [ find default-name=ether1 ] comment="cpeXXXX_VIDEOS_chapo"\r')
            mac_telnet.expect('[Mikrotik ]')
# while True:
#         ps = pexpect.spawn ('ps')
#         time.sleep (1)
#         index = ps.expect (['/usr/bin/ssh', pexpect.EOF, pexpect.TIMEOUT])
#         if index == 2:
#             print('TIMEOUT in ps command...')
#             print(str(ps))
#             time.sleep (13)
#         if index == 1:
#             print(time.asctime(), end=' ')
#             print('restarting tunnel')
#             start_tunnel ()
#             time.sleep (11)
#             print('tunnel OK')
#         else:
#             # print 'tunnel OK'
#             time.sleep (7)
================================================

File: 0001_initial.py
================================================
# Generated by Django 3.0.9 on 2020-08-04 14:03
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=255)),
                ('version', models.CharField(blank=True, max_length=220, null=True)),
                ('macaddress', models.CharField(blank=True, max_length=220, null=True)),
                ('interface', models.CharField(blank=True, max_length=220, null=True)),
                ('ipv4', models.CharField(blank=True, max_length=220, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
================================================

File: 0002_auto_20200804_1442.py
================================================
# Generated by Django 3.0.9 on 2020-08-04 14:42
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discover', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='device',
            name='create',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
================================================

File: 0003_remove_device_version.py
================================================
# Generated by Django 3.0.9 on 2020-08-04 16:58
from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('discover', '0002_auto_20200804_1442'),
    ]
    operations = [
        migrations.RemoveField(
            model_name='device',
            name='version',
        ),
    ]
================================================

File: 0004_auto_20200805_0806.py
================================================
# Generated by Django 3.0.9 on 2020-08-05 08:06
from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('discover', '0003_remove_device_version'),
    ]
    operations = [
        migrations.AddField(
            model_name='device',
            name='cpe',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='cpe_pass',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
================================================

File: models.py
================================================
from django.db import models
from django.contrib.auth.models import User
class Device(models.Model):
    user = models.ForeignKey(User, blank=True,
                             null=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=255,
                             blank=True)
    macaddress = models.CharField(max_length=220,
                                  blank=True, null=True)
    interface = models.CharField(max_length=220,
                                 blank=True, null=True)
    ipv4 = models.CharField(max_length=220,
                            blank=True, null=True)
    cpe = models.CharField(max_length=220,
                            blank=True, null=True)
    cpe_pass = models.CharField(max_length=220,
                            blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Model : {self.model} , Version {self.version}, Mac-Address: {self.macaddress} Interface {self.interface}, Ipv4 {self.ipv4}'
================================================

File: tests.py
================================================
from django.test import TestCase
# Create your tests here.
================================================

File: views.py
================================================
from django.shortcuts import render
# Create your views here.
================================================

File: loger.py
================================================
import logging
class Loger:
    filename = None
    logger = None
    ft = '%(filename)s | %(levelname)s | %(asctime)s |--------------------|%(message)s'
    def __init__(self, filename, name):
        self.filename = filename
        logging.basicConfig(
            filename=self.filename,
            filemode='a',
            format=self.ft,
            datefmt='%m/%d/%Y %I:%M:%S %p',
        )
        self.logger = logging.getLogger(name)
        print("filename ", filename)
    def log_debug(self, msg):
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(msg)
    def log_info(self, msg):
        self.logger.setLevel(logging.INFO)
        self.logger.info(msg)
    def log_warning(self, msg):
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(msg)
    def console_info(self, msg):
        msg_console = self.bcolors.OKGREEN + '| {0: >50} |'.format(msg) + self.bcolors.ENDC
        print(msg_console)
        self.log_info(msg)
    def console_success(self, msg):
        msg_console = self.bcolors.OKBLUE + '| {0: >50} |'.format(msg) + self.bcolors.ENDC
        print(msg_console)
        self.log_info(msg)
    def console_warning(self, msg):
        msg_console = self.bcolors.WARNING + '|{0: >50}|'.format(msg)+ self.bcolors.ENDC
        print(msg_console)
        self.log_warning(msg)
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
================================================

File: manage.py
================================================
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikrotik.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()
================================================

File: asgi.py
================================================
"""
ASGI config for mikrotik project.
It exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikrotik.settings')
application = get_asgi_application()
================================================

File: settings.py
================================================
"""
Django settings for mikrotik project.
Generated by 'django-admin startproject' using Django 3.0.8.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z4l($s5c+upg$yqh%m2_-lqb2xo*-i8b85c1%#!1!0y(blyu)4'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'discover'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'mikrotik.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'mikrotik.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
================================================

File: urls.py
================================================
"""mikrotik URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
]
================================================

File: wsgi.py
================================================
"""
WSGI config for mikrotik project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikrotik.settings')
application = get_wsgi_application()
================================================

File: requirements.txt
================================================
netifaces==0.10.9
routeros==0.1.1
RouterOS-api==0.17.0
librouteros==3.0.2
print-schema==1.1.1
pprintjson==1.4.2
pexpect
Django
================================================

File: plantilla_dani_mikrotik.rsc
================================================
# jan/02/1970 01:05:19 by RouterOS 6.33
# software id = 56NZ-W6K4
#
##
# LIMPIA CFG DE LA ANTENA solo ejecutar una sola vez
/system reset-configuration no-defaults=yes skip-backup=yes
######### empezamos carga de cfg, modificar cpeXXXX y passxxxx
/interface ethernet
set [ find default-name=ether1 ] comment="cpeXXXX"
/ip neighbor discovery
set ether1 comment="cpeXXXX"
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk management-protection=allowed mode=\
    dynamic-keys name=MW-Profile supplicant-identity="" wpa2-pre-shared-key=\
    d9sdh30g8dn248d
/interface wireless
set [ find default-name=wlan1 ] ampdu-priorities=0,1,2,3,4,5,6,7 band=\
    5ghz-a/n channel-width=20/40mhz-Ce disabled=no frequency=5770 \
    frequency-mode=superchannel ht-supported-mcs="mcs-0,mcs-1,mcs-2,mcs-3,mcs-\
    4,mcs-5,mcs-6,mcs-7,mcs-16,mcs-17,mcs-18,mcs-19,mcs-20,mcs-21,mcs-22,mcs-2\
    3" nv2-preshared-key=d9sdh30g8dn248d nv2-security=enabled radio-name=\
    cpeXXXX scan-list=4900-6100 security-profile=MW-Profile ssid=\
    CR_Sector supported-rates-a/g=6Mbps,9Mbps,12Mbps,18Mbps,24Mbps \
    wmm-support=enabled
/interface pppoe-client
add add-default-route=yes default-route-distance=1 disabled=no interface=\
    wlan1 max-mru=1480 max-mtu=1480 name=pppoe-out1 password=passxxxx \
    use-peer-dns=yes user=cpeXXXX
/interface wireless nstreme
set wlan1 enable-nstreme=yes
/ip neighbor discovery
set wlan1 discover=no
/ip ipsec proposal
set [ find default=yes ] enc-algorithms=3des
/ip pool
add name=dhcp_pool1 ranges=192.168.100.2-192.168.100.254
/ip dhcp-server
add address-pool=dhcp_pool1 disabled=no interface=ether1 lease-time=1h name=\
    dhcp1
/snmp community
set [ find default=yes ] name=mwdata
/system logging action
set 0 memory-lines=100
/ip address
add address=192.168.100.1/24 comment="eth1 configuration" interface=ether1 \
    network=192.168.100.0
/ip dhcp-server network
add address=192.168.100.0/24 dns-server=192.168.100.1 gateway=192.168.100.1
/ip dns
set allow-remote-requests=yes
/ip dns static
add address=192.168.100.1 name=router
/ip firewall filter
add chain=input comment="default configuration" protocol=icmp
add chain=input comment="default configuration" dst-port=8291 protocol=tcp
add chain=input comment="default configuration" connection-state=established
add chain=input comment="default configuration" connection-state=related
# pppoe-out1 not ready
add action=drop chain=input comment="default configuration" in-interface=\
    pppoe-out1
/ip firewall nat
# pppoe-out1 not ready
add action=masquerade chain=srcnat comment="Masquerade local net to internet" \
    out-interface=pppoe-out1 to-addresses=0.0.0.0
# pppoe-out1 not ready
add action=dst-nat chain=dstnat comment=\
    "Redirect all ports to 192.168.100.254" dst-port=!8291 in-interface=\
    pppoe-out1 protocol=tcp to-addresses=192.168.100.254 to-ports=0-65535
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh disabled=yes
set api disabled=yes
set api-ssl disabled=yes
/snmp
set contact=Conred enabled=yes location=Conred_Cliente
/system clock
set time-zone-autodetect=no time-zone-name=Europe/Madrid
/system identity
set name=cpeXXXX
/system leds
set 0 interface=wlan1
/system logging
add action=disk topics=critical
add action=disk topics=error
add action=disk topics=info
add action=disk topics=warning
/system ntp client
set enabled=yes primary-ntp=10.190.10.1 secondary-ntp=10.190.12.1
/tool mac-server
set [ find default=yes ] disabled=yes
add interface=ether1
/tool mac-server mac-winbox
set [ find default=yes ] disabled=yes
add interface=ether1
/tool romon port
set [ find default=yes ] cost=100 forbid=no interface=all secrets=""
user set password=1add2020! admin