from pyrogram import *
import vars
import os
import sys
from os import path as os_path

BLACKLISTED_EXTENSIONS = (".sex")

tony = Client(name="My Tony", api_id=vars.api_id, api_hash=vars.api_hash, bot_token=vars.bot_token)

@tony.on_message(filters.command('start') & filters.private)
def start(client, message):
    message.reply_text(text="welcome to ANToNi rip bot")
    print("Welcome to tony bot")

@tony.on_message(filters.command('help') & filters.private)
def help(client, message):
    if help:
       message.reply_text(text="this bot just for shell, made by @tont9848")
    else:
       message.reply_text(text="No helps")

async def run_comman_d(command_list):
    process = await asyncio.create_subprocess_shell(
        command_list,
        # stdout ni access cheyadaniki pipe kavalli ra subprocess.pipe
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # idi kavalli zumka 
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    return e_response, t_response

@tony.on_message(filters.command('shell') & filters.private)
def shell(client, message):
    cmd = message.text.split(' ', 1)
    sts = await message.reply_text("poonakalu loading...")
    if len(cmd) == 1:
        return await sts.edit('**Send a command**')
    cmd = cmd[1]
    for check in cmd.split(" "):
        if check.upper().endswith(BLACKLISTED_EXTENSIONS):
            return await sts.edit("you can't execute this cmd, because you gey")
    reply = ''
    stderr, stdout = await run_comman_d(cmd)
    newstdout = ""
    for line in stdout.split("\n"):
        if not line.upper().endswith(BLACKLISTED_EXTENSIONS):
            newstdout += line + "\n"
    if len(newstdout) != 0:
        reply += f"<b>Stdout</b>\n<code>{newstdout}</code>\n"
    if len(stderr) != 0:
        reply += f"<b>Stderr</b>\n<code>{stderr}</code>\n"
    if len(reply) > 3000:
        with open('output.txt', 'w') as file:
            file.write(reply)
        with open('output.txt', 'rb') as doc:
            await message.reply_document(
                document=doc,
                caption=f"`{cmd}`")
            await sts.delete()
    elif len(reply) != 0:
        await sts.edit(reply)
    else:
        await sts.edit('Executed')

print("well starting up")
print("Bot started..")

tony.run()
