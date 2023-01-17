from pyrogram import *
import vars


tony = Client (api_id=vars.id, api_hash=vars.hash, bot_token=vars.token)

@tony.on_message()
def hi(client, message)
    print(message)

print("Starting up bot../")

tony.run()
