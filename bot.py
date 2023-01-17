from pyrogram import *
import vars


tony = Client(name="My Tony", api_id=vars.api_id, api_hash=vars.api_hash, bot_token=vars.bot_token)

@tony.on_message(filters.command('start'))
def start(client, message):
    print("Welcome to tony bot")

tony.run()
