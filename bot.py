from pyrogram import *
import vars
import os
import sys
from os import path as os_path

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

@tony.on_message(filters.command('shell') & filters.private)
def shell(client, message):
    message = update.effective_message
    cmd = message.text
    process = srun(cmd, capture_output=True, shell=True)
    reply = ''
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')
    if len(stdout) != 0:
        reply += f"<b>Stdout</b>\n<code>{stdout}</code>\n"
    if len(stderr) != 0:
        reply += f"<b>Stderr</b>\n<code>{stderr}</code>\n"
    if len(reply) > 3000:
        with open('output.txt', 'w') as file:
            file.write(reply)
        with open('output.txt', 'rb') as doc:
            context.bot.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id)
    elif len(reply) != 0:
        sendMessage(reply, context.bot, update.message)
    else:
        sendMessage('Executed', context.bot, update.message)

print("starting bot!..")
print("Bot started../")

tony.run()
