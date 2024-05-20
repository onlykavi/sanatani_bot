from telethon import TelegramClient, events
import random
import re
from telethon.tl.functions.channels import GetParticipantsRequest
import os
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import MessageEntityCode
from telethon import TelegramClient, events, Button
import telethon.sync #lol copied from docs
import asyncio
import logging
import asyncio
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator

from telethon.tl.types import ChannelParticipantsAdmins

api_id = '28184846'
api_hash = 'b79094c50e87edb77def9e04dcff3aa5'
admin_ids = ['6265981509', '1661129466', '6468596992','5925882832','5232742343','6301771663','1483217059']
allowed_group_id = -1001940203596
BOT_TOKEN = '6899547930:AAEw0hcXWkXw3FNAVPzhGr6769dtm9mcC5Y'
client = TelegramClient('bot_username', api_id, api_hash)
spam_chats = []


name = 'main'
auction_mode = False  

@client.on(events.NewMessage(pattern='/auction on'))
async def auction_on_handler(event):
    global auction_mode
    auction_mode = True



@client.on(events.NewMessage)
async def check_message(event):
    global auction_mode
    if auction_mode and event.chat_id == allowed_group_id:
       
        if re.match(r'^(\d+(\.\d+)?|(\d+)?(pd|k|/pass))$', event.message.text.lower()) or event.message.text.strip() == '.':
           
            return

       
        admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admin_ids = [admin.id for admin in admins] 

        
        if event.sender_id in admin_ids:
        
            return
        else:
 
            await event.delete()
@client.on(events.NewMessage(pattern='/auction off'))
async def auction_off_handler(event):
    global auction_mode
    
    admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
    admin_ids = [admin.id for admin in admins] 
    auction_mode = False

dot_count = 0


import asyncio


@client.on(events.NewMessage)
async def auto_count_handler(event):
    
    if event.chat_id != allowed_group_id or not auction_mode:
        return

    message_text = event.message.text.strip()

    if message_text == '.' and str(event.sender_id) in admin_ids:
       
        sent_message = await event.reply('✨')
        await asyncio.sleep(1)  

        
        await sent_message.edit('✨✨')
        await asyncio.sleep(2)  

        await sent_message.edit('✨✨✨')
        await asyncio.sleep(2) 

       
        await sent_message.edit('✨✨✨✨')
      
        await asyncio.sleep(1)  
        await sent_message.edit('✨✨✨✨✨ /sold ')

from telethon.tl.types import ChannelParticipantsAdmins


@client.on(events.NewMessage(pattern='/sold'))
async def sold_handler(event):
    
    if not event.is_reply:
        await event.reply("Please use the /sold command by replying to the message of the item.")
        return

    
    custom_message = event.message.text.partition(' ')[2].strip()

   
    admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
    admin_ids = [admin.id for admin in admins] 

    if event.sender_id not in admin_ids:
        await event.reply("You are not authorized to use the /sold command.")
        return

    
    replied_message = await event.get_reply_message()

    
    user_identifier = "@" + replied_message.sender.username if replied_message.sender.username else replied_message.sender_id

    
    replied_message_content = replied_message.text

    
    sold_message = f"sold to :- {user_identifier} \n \n sold in :- {replied_message_content} k: {custom_message}"

   
    sold_reply = await replied_message.reply(sold_message)

    
    await client.pin_message(event.chat_id, sold_reply.id)


@client.on(events.NewMessage(pattern='/unsold'))
async def unsold_handler(event):
    
    admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
    admin_ids = [admin.id for admin in admins]  

    if event.sender_id not in admin_ids:
        await event.reply("You are not authorized to use the /unsold command.")
        return

    
    player_name = event.message.text.partition(' ')[2].strip()

    
    if player_name:
       
        unsold_message = f" {  player_name} was unsold"

        
        await event.reply(unsold_message)
    else:
        await event.reply("Please provide the player's name in the /unsold command.")


@client.on(events.NewMessage(pattern="^/tagall|@all|/mention|/all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.reply("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.reply(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" 🎶 [{usr.first_name}](tg://user?id={usr.id}), \n \n"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__Only admins can execute this command!__")
    if not event.chat_id in spam_chats:
        return await event.reply("__There is no proccess on going...__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped Mention.__")
    

async def main():
    await client.start(bot_token=BOT_TOKEN)
    await client.run_until_disconnected()


if name == 'main':
    client.loop.run_until_complete(main())
