from pyrogram import *
import vars


tony = Client(name="My Tony", api_id=vars.api_id, api_hash=vars.api_hash, bot_token=vars.bot_token)

@tony.on_message(filters.command('start') & filters.private)
def start(client, message):
    message.reply_text(text="welcome to ANToNi rip bot")
    print("Welcome to tony bot")

@tony.on_message(filters.command('help') & filters.private)
def help(client, message):
    if help:
       message.reply_text(text="Helps")
    else:
       message.reply_text(text="No helps")

print("starting bot!..")
print("Bot started../")

tony.run()
