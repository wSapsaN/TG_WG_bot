# TG_WG_bot
This Telegram bot is for easy management of Wireguard on a remote server

The bot only works on adding and removing clients.
This development can make its add-ons up to a commercial project.

The bot is a framework for something bigger.

---
# DataBase

The bot has a single database table that is connected using the ORM system.

The ORM will allow you to easily switch to another DB such as: MySQL or Postgresql

# Server

On the server, your user must first have access to the rights to execute the following commands as the superuser:
* wg
* cat
* systemctl
* chown

On the VPN server itself, there will be a TCP server that accepts requests from the bot (client) to add a user and enter settings into the config files. The TCP server simply accepts a command that needs to be executed on the server itself, then the bash script runs.

After TCP, the server returns the user's private certificate to send him the settings.
It is also assumed that it will work inside the VNP network and, if desired, you can connect SSL for greater security.

**However, you may encounter a problem associated with the fact that when applying new settings, the VPN is restarted, which can, in theory, break the TCP connection. Therefore, you can use a separate VPN tunnel.**

It is also assumed that the bot accepts requests from Reverse Nginx.

## How setup WireGuard?

Topic:
- [ruSetup]("https://youtu.be/5Aql0V-ta8A?si=34Wcg4AgwSvE2fFX")
- [enSetup]("https://youtu.be/bVKNSf1p1d0?si=E6KMjJOb7xEkbKbu")

# Launch the application

This describes how to run the bot locally.
But the code assumes that it will run on separate workstations.

## Preparing the settings

Create a config.py file in the bot directory.
The following variables must be written in this file:
```python
TOKEN='YOUR BOT TOKEN'

# this for webhook
WEBHOOK_SSL_CERT="cert/YOURPUBLIC.pem"
WEBHOOK_SSL_PRIV="cert/YOURPRIVATE.key"

# setup for client
IP_SERVER="IP YOUR SERVER OR LOCALHOST"
PORT=8580
```

Check your bash script settings in advance:
* server/wireguard_setup/server_addUS.sh 
* bot/bot_createUS.sh

## Let's launch

Compile and launch our server:
```bash
gcc server/server.c -o server
./server./server
```

We check that it works on the port specified in config.py.

If this is not the case, I recommend changing the port in this file.
This file is relevant only for python code.

What's the problem?

The thing is that the requested port is not always free.
And so the kernel issues another port for the application to run.

Now we prepare the python:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run:
```bash
python3 bot/app.py
```