# Telegram Visa Channel Monitor

Python script to monitor a telegram channel and forward the filtered messages to personal channel.

## Use Case

1. The channel that we intend to monitor follows certain pattern when posting messages/ photos
2. Forward all the messages that contain photo
3. Filter all the messages that match our pattern and forward them

## Python Modules/ Dependancies

1. telethon (TelegramClient, events)
2. datetime
3. re

## Required Configuration

1. Install Telethon python library (https://docs.telethon.dev/en/latest/basic/installation.html)
2. Get your Telegram API ID and Hash and set it in "constants.py" file (https://docs.telethon.dev/en/latest/basic/signing-in.html)
3. Adjust Channel Ids and pattern match string in the "constants.py" file as needed
