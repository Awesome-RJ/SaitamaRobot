from telethon import events, Button, custom

import re, os

from SaitamaRobot.events import register

from SaitamaRobot import telethn

PHOTO = "https://telegra.ph/file/c93c5bbc5494c0188a541.jpg "

@register(pattern=("/alive"))

async def awake(event):

  Megumin = event.sender.first_name

  Megumin = "**♡ I,m Megumin** \n\n"

  Megumin += "**♡ I'm Working with awesome speed**\n\n"

  Megumin += "**♡ Megumin : first version**\n\n"

  Megumin += "**♡ My Creator :** [heyaaman](t.me/heyaaman)\n\n"

  Megumin += "**♡ Telethon Version : 1.23.0**\n\n"

  BUTTON = [[Button.url("Support", "https://t.me/KazukoSupportChat"), Button.url("Update", "https://t.me/phoenix_empire")]]

  await telethn.send_file(event.chat_id, PHOTO, caption=Megumin, buttons=BUTTON)
