from random import randint

import requests as r
from SaitamaRobot import SUPPORT_CHAT, WALL_API, dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async

# Wallpapers module by @TheRealPhoenix using wall.alphacoders.com


@run_async
def wall(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    args = context.args
    msg_id = update.effective_message.message_id
    bot = context.bot
    if query := " ".join(args):
        caption = query
        term = query.replace(" ", "%20")
        json_rep = r.get(
            f"https://wall.alphacoders.com/api2.0/get.php?auth={WALL_API}&method=search&term={term}",
        ).json()
        if json_rep.get("success"):
            if wallpapers := json_rep.get("wallpapers"):
                index = randint(0, len(wallpapers) - 1)  # Choose random index
                wallpaper = wallpapers[index]
                wallpaper = wallpaper.get("url_image")
                wallpaper = wallpaper.replace("\\", "")
                bot.send_photo(
                    chat_id,
                    photo=wallpaper,
                    caption="Preview",
                    reply_to_message_id=msg_id,
                    timeout=60,
                )
                bot.send_document(
                    chat_id,
                    document=wallpaper,
                    filename="wallpaper",
                    caption=caption,
                    reply_to_message_id=msg_id,
                    timeout=60,
                )
            else:
                msg.reply_text("No results found! Refine your search.")
                return
        else:
            msg.reply_text(f"An error occurred! Report this @{SUPPORT_CHAT}")
    else:
        msg.reply_text("Please enter a query!")
        return


WALLPAPER_HANDLER = DisableAbleCommandHandler("wall", wall)
dispatcher.add_handler(WALLPAPER_HANDLER)
