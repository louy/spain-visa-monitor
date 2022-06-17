# Spain Visa Monitor

A telegram bot that notifies you of available appointments on the BLS spanish visa website as soon as they become available

Most agencies charge you about £100 for an urgent (within 1 week) appointment, this script should give you that for free.
If you find it useful, consider giving a small donation using the Sponsor button on Github.
## Set up
### Telegram
You need to create a telegram bot and grab your bot token and chat ID:

1) Send a message to [BotFather](https://telegram.me/botfather) using the command `/newbot` and grab the token and add it to [config.py](./utils/config.py) under `BOT_TOKEN`.
2) Grab a chat id (could be your own user's chat id or a group id). You can get it by messaging the `RawDataBot` on telegram, under `chat.id` in the bot's response. Add it to [config.py](./utils/config.py) as well.

### BLS Spain Visa
You need to have an application on the BLS website and be able to book an appointment. Once you're at that stage do the following:

1) Add your BLS account credentials to [config.py](./utils/config.py) under `USERNAME` and `PASSWORD`
2) Visit the BLS website and login to access your application, then click the `Book Appointment` link and copy the URL of that page. Add it to [config.py](./utils/config.py) under `OPENED_PAGE`.
### Installation
Install python dependencies via the following command:
```sh
pip install -r requirements.txt
```

### Usage
Start up the script using this command:
```sh
python monitor.py
```
You'll receive a message from the bot on telegram telling you that it has started.

When an appointment becomes available, you'll receive a message from the bot. Make sure to book your appointment as soon as you get the message (from my experience appointments are gone within 20 mins of becoming available).

Once you're done, use Ctrl-C to kill the bot. That's it. Good luck!
