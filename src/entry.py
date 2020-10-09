import telegram
import json
import logging


def entry(bot, update):
    # print(update.to_json())
    # print("\n")
    if update.message:
        if not update.message.reply_to_message:
            print("DELETING...")
            bot.delete_message(chat_id=update.message.chat.id, message_id=update.message.message_id)