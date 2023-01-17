from pyrogram import *
import vars


tony = Client(name="My Tony", api_id=vars.api_id, api_hash=vars.api_hash, bot_token=vars.bot_token)

@tony.on_message()
def hi(client, message):
    print(message)

print("Starting up bot../")

tony.run()
