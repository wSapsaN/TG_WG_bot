# TG_WG_bot
This Telegram bot is for easy management of Wireguard on a remote server

The bot only works on adding and removing clients.
This development can make its add-ons up to a commercial project.
Which will be done in the future.


---

The bot is a framework for something bigger.
At the time of the last commit, no problems with the bot were found.

**If the commercial project fails, I will post its code in a separate repository.**

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

To give my user rights to execute the command from sudo without password.
I used sudoers.d setup:
```bash
user ALL=(ALL:ALL) NOPASSWD: /home/user/creat_client.sh
```

## How setup WireGuard?

Topic:
- [ruSetup]("https://youtu.be/5Aql0V-ta8A?si=34Wcg4AgwSvE2fFX")
- [enSetup]("https://youtu.be/bVKNSf1p1d0?si=E6KMjJOb7xEkbKbu")

# Launch the application

It's simple, before launching you need to create a config.py file in the bot directory, and specify your bot token there.
And also a bash file for a test launch of the bot:
```bash
#!/usr/bin/env bash
#
# Script fot automatic add of users.
#

local_address_client=$2

private_key="private_key"
public_key="public_key"

cat << EOF >> "${user_name}.conf"
[Interface]
PrivateKey = ${private_key}
Address = ${local_address_client}/32
DNS = 8.8.8.8

[Peer]
PublicKey = /JjRTRuWZvKn5KIOKuIYeuL0LvEz1N/dm6RHD5If3Gk=
Endpoint = 193.124.92.75:51820 
AllowedIPs = 0.0.0.0/0 
PersistentKeepalive = 20
EOF

cat << EOF >> wg-test.conf
[Peer]
PublicKey = ${public_key}
AllowedIPs = ${local_address_client}/32
EOF

# systemctl restart wg-quick@wg0

# chown uniq:uniq ${user_name}.conf

exit 0

### THE END ###
```

In the future this file will not exist, I use it exclusively for tests, but you can also substitute the creat_client.sh file, just make sure there are no errors here.
I have a poor understanding of writing branches in bash scripts and there may be syntax errors.

You can also connect any other SQL DB.

Since the bot is not finished, unpredictable behavior may occur. Although I have not noticed anything like that yet.

In the near future I want to connect logging and finish writing instructions for connecting to a VPN.