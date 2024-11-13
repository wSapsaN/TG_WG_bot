# TG_WG_bot
This Telegram bot is for easy management of Wireguard on a remote server

The bot only works on adding and removing clients.
This development can make its add-ons up to a commercial project.
Which will be done in the future.

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

....