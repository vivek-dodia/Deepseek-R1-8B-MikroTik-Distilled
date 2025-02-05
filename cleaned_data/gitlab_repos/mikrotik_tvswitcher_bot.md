# Repository Information
Name: mikrotik_tvswitcher_bot

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
	url = https://gitlab.com/glad2rest/mikrotik_tvswitcher_bot.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: mikrotik_tvswitchbot.py
================================================
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import paramiko
import asyncio
import os
from dotenv import load_dotenv
## GLOBALS
load_dotenv()
MIKROTIK_IP = os.getenv('MIKROTIK_IP')
MIKROTIK_USER = os.getenv('MIKROTIK_USER')
TOKEN = os.getenv('TOKEN')
RSA_PATH = os.getenv('RSA_PATH')
VPN_INTERFACE = os.getenv('VPN_INTERFACE')
nest_asyncio.apply()
async def ssh_command(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(RSA_PATH)
    client.connect(hostname=MIKROTIK_IP, username=MIKROTIK_USER, pkey=private_key)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output
async def is_interface_up() -> bool:
    result = await ssh_command('/put [/interface/wireguard/get wg1 value-name=disabled]')
    result = result.strip()
    return result == 'false'
async def get_button():
    vpn_enabled = await is_interface_up()
    keyboard_choices = {
        'on': [InlineKeyboardButton("ON", callback_data='on')],
        'off': [InlineKeyboardButton("OFF", callback_data='off')],
    }
    return keyboard_choices.get('off') if vpn_enabled else keyboard_choices.get('on')
async def get_message():
    return 'VPN включен' if await is_interface_up() else 'VPN выключен'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [await get_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    vpn_enabled = await is_interface_up()
    await update.message.reply_text(f'{await get_message()}:', reply_markup=reply_markup)
async def send_buttons(message):
    keyboard = [await get_button()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text(f'{await get_message()}', reply_markup=reply_markup)
async def switch_interface():
    disabled = 'no'
    if vpn_enabled := await is_interface_up():
        disabled = 'yes'
    list_commands = [
        f'/interface/wireguard/set {VPN_INTERFACE} disabled={disabled}',
        '/ip/dns/cache/flush',
        'beep frequency=2000 length=1',
    ]
    for num, command in enumerate(list_commands, start=0):
        await ssh_command(command)
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    response = await switch_interface()
    await send_buttons(query.message)
async def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    await application.run_polling()
if __name__ == '__main__':
    asyncio.run(main())
================================================

File: README.md
================================================
# Setting Up the Bot
# 1. Clone the Repository
To get started, you need to clone the repository to your local machine. Use the following command:
```bash
git clone https://gitlab.com/glad2rest/mikrotik_tvswitcher_bot.git
```
# 2. Create the .env File and Define Variables
Next, you need to create a .env file in the root directory of your project. This file will contain environment variables required by your bot.
Here is an example of what the .env file might look like:
```env
TELEGRAM_BOT_TOKEN = '<YOUR_TOKEN_HERE>'
MIKROTIK_IP = '<YOUR_HOST_HERE>'
MIKROTIK_USER = '<YOUR_SUPERUSER_HERE>'
RSA_PATH = '<PATH_TO_RSA_HERE>'
VPN_INTERFACE = '<YOUR_INTERFACE_NAME_HERE>'
```
Replace the '\<placeholders>' with your actual values.
# 3. Initialize and Install Dependencies with Poetry
To manage your project's dependencies, you can use Poetry. Follow these steps:
## Initialize Poetry
Navigate to the root directory of your project and run:
```bash
poetry init
```
Follow the prompts to set up your pyproject.toml file.
## Install Dependencies
After initializing Poetry, install the dependencies specified in your pyproject.toml file:
```bash
poetry install
```
## 4. Create a Linux Service to Run the Bot
To ensure that your bot runs continuously, you can create a Linux service. Follow these steps:
## Create a Service File
#### Create a new service file in the /etc/systemd/system/ directory. You can name it mybot.service.
```bash
sudo vi /etc/systemd/system/mybot.service
```
Add the Following Content to the Service File
```
[Unit]
Description=My Bot Service
After=network.target
[Service]
ExecStart=/usr/bin/python3 /path/to/your/bot.py
WorkingDirectory=/path/to/your
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root
[Install]
WantedBy=multi-user.target
```
Replace /path/to/your/bot.py with the actual path to your bot script.
Reload the Systemd Daemon
```bash
sudo systemctl daemon-reload
```
Enable and Start the Service
```bash
sudo systemctl enable --now mybot.service
```
This will ensure that your bot runs continuously and restarts automatically if it crashes.