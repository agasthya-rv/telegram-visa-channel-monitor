import constants
import re
from datetime import datetime
from telethon import TelegramClient, events

api_id = constants.API_ID
api_hash = constants.API_HASH
regExp = constants.REG_EXP_PATTERN
channel_to_monitor = []
channel_to_monitor.append(constants.CHANNEL_ID_TO_MONITOR)
print("Monitoring channel:",channel_to_monitor)

# https://docs.telethon.dev/en/latest/basic/quick-start.html#
client = TelegramClient('anon', api_id, api_hash)
client.start()
print("Starting Session:",datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

# Function to filter the messages matching the pattern
def pattern_match(msg_txt):
    return True if re.search(regExp, msg_txt) else False

# Fetch new messages from a channel, filter and forward to personal channel
@client.on(events.NewMessage(chats=channel_to_monitor))
async def forward_filtered_msg(event):
    msg = event.message
    msg_id = msg.id if msg else None
    msg_text = msg.message if msg else event.raw_text
    #print(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + ":" + msg_text)
    
    # Forward all the messages that contain photo
    if msg_id and msg.photo:
        await client.forward_messages(constants.MY_CHANNEL_ID, msg)
    # Forward all the messages that match the pattern string
    elif (msg_id and msg_text and msg_text[:1] != '/' and pattern_match(msg_text)):
        await client.forward_messages(constants.MY_CHANNEL_ID, msg)

client.run_until_disconnected()