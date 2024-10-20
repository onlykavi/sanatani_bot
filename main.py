#千ㄥ|尺ㄒ乇尺 Ҝㄩ几 α あ #OFFLINEARC:
#7012523159:AAFFb5hWOdliq8Mti2vpxAKemvWS_rSA_J8
#https://wallpapers.com/images/hd/legendary-pokemon-pictures-7yo7x0f1l2b2tu0r.jpg
#https://t.me/IHG_Hexa_Auction
#https://t.me/IHGtradegroup

import telebot
from telebot import types
import time
import re
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InputMediaPhoto

API_TOKEN = '6796970894:AAFbyciSZJOf_DB4NIQrBe-euLcNehg0NZo'

bot = telebot.TeleBot(API_TOKEN)

user_join_status = {}
user_states = {}
started_users = set()
banned_users = set()
broad_users = []

def send_welcome_message(chat_id, username, first_name):
    markup = types.InlineKeyboardMarkup()
    join_auction_btn = types.InlineKeyboardButton("Join Auction channel", url=f"https://t.me/pokefest_hub_auc_chan")
    join_trade_btn = types.InlineKeyboardButton("Join group", url=f"https://t.me/pokefest_hub_auction")
    joined_btn = types.InlineKeyboardButton("Joined", callback_data="joined")

    markup.add(join_auction_btn, join_trade_btn)
    markup.add(joined_btn)

    caption = (
        f"🔸Welcome, [{first_name}](https://t.me/{username}) To PHG Auction Bot\n\n"
        "🔸You Can Submit Your Pokemon Through This Bot For Auction\n\n"
        "🔻But Before Using, You Have To Join Our Auction Group By Clicking The Two Buttons Below, "
        "And Then Click 'Joined'."
    )

    bot.send_photo(
        chat_id,
        photo="https://wallpapers.com/images/hd/legendary-pokemon-pictures-7yo7x0f1l2b2tu0r.jpg",
        caption=caption,
        reply_markup=markup,
        parse_mode='Markdown'
    )


@bot.message_handler(commands=['start'])
def handle_start(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        if message.chat.type == 'private':
            user_id = message.chat.id
            if user_id not in broad_users:
                broad_users.append(user_id)
            first_name = message.from_user.first_name
            username = message.from_user.username
            send_welcome_message(message.chat.id, username, first_name)
        else:
            bot.reply_to(message, "Please use this command in a private message.")



@bot.callback_query_handler(func=lambda call: call.data == "joined")
def handle_joined(call):
    user_id = call.from_user.id

    # Replace these with actual chat IDs of your group and channel
    auction_chat_id = -1002341528498  # Example chat ID for @pokefest_hub_auc_chan
    trade_chat_id = -1002266679524    # Example chat ID for @pokefest_hub_auction

    try:
        # Check the user's membership status in the auction channel and trade group
        auction_status = bot.get_chat_member(chat_id=auction_chat_id, user_id=user_id).status
        trade_status = bot.get_chat_member(chat_id=trade_chat_id, user_id=user_id).status

        # Log the retrieved statuses for debugging purposes
        print(f"User {user_id} - Auction Status: {auction_status}, Trade Status: {trade_status}")

        # Check if the user is a member in both
        has_joined_auction = auction_status in ['member', 'administrator', 'creator']
        has_joined_trade = trade_status in ['member', 'administrator', 'creator']
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error checking user {user_id}'s membership: {e}")
        has_joined_auction = False
        has_joined_trade = False

    # If the user has joined both, send success message
    if has_joined_auction and has_joined_trade:
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="Thanks for joining our groups 😊"
        )
    else:
        # Send alert if the user has not joined both groups
        bot.answer_callback_query(call.id, "Please join both groups before clicking 'Joined'.", show_alert=True)

@bot.message_handler(commands=['cancel'])
def handle_cancel(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        if message.chat.type == 'private':
            user_id = message.from_user.id
            if user_id in user_states:
                del user_states[user_id] 
            bot.send_message(message.chat.id, "All Running Command Has Been Cancelled ✅")
        else:
            bot.reply_to(message, "Please use this command in a private message.")


def is_admin(user_id):
    admin_ids = [1661129466, 6468596992, 6241067084, 1655924853, "kiya h"] 
    return user_id in admin_ids

admin_id = [1661129466, 6468596992, 6241067084, 1655924853] 


# Placeholder lists, replace these with actual data
dxgays = []  # List of user IDs that are in dxgays
xmods = [1661129466, 6468596992, 6241067084, 1655924853]   # List of user IDs that are xmods
user_cache = {}

# Constants, replace with actual values
AUCTION_GROUP_LINK = 'https://t.me/+2li_q1Xmvv1jNzVl'
AUCTION_GROUP_LINK = 'https://t.me/+mWi76-3J875kMWFl'
log_channel = -1002223984722  # Replace with your log channel ID
post_channel = -4581741999  # Replace with your post channel ID
approve_channel = -1002223984722  # Replace with your approve channel ID
reject_channel = -4539849027  # Replace with your reject channel ID

@bot.message_handler(commands=['add'])
def sell(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    if user_id in dxgays:
        bot.send_message(user_id, f"Ho Ho Ho\n\nIf you want to sell something in auction how about you sell your mom to xmods. "
                                 f"Although your moms are already free WHORE whose price is free for a year to use by anyone and they have such loose pussy.\n\n"
                                 f"{first_name} mom has got best whore award, {first_name} is trying to find about his real dad, when {first_name} fills any form in father section he writes xmods and 3.97 billion others.")
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Yes', callback_data='yes'))
        markup.add(types.InlineKeyboardButton('No', callback_data='No'))
        if username:
            bot.send_message(user_id, f"Hello @{username}!\n\nWould you like to sell something in auction?", reply_markup=markup)
        else:
            bot.send_message(user_id, "Hello!\n\nWould you like to sell something in auction?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'No', 'legendary', 'ol', 'shiny', 'tms', 'submit', 'delete', 'submi', 'delet', 'approve', 'reject', 'rejtrash', 'rejinco', 'highbase', 'scammer'])
def callback_handler(call):
    user_id = call.from_user.id
    if call.data == 'yes':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('LEGENDARY', callback_data='legendary'))
        markup.add(types.InlineKeyboardButton('0L/NON LEGENDARY', callback_data='ol'))
        markup.add(types.InlineKeyboardButton('SHINY', callback_data='shiny'))
        markup.add(types.InlineKeyboardButton('TMS', callback_data='tms'))
        bot.edit_message_text('So what would you like to sell?', call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'No':
        bot.edit_message_text('OK! Have a great day', call.message.chat.id, call.message.message_id)
    elif call.data == 'legendary':
        handle_legendary(call)
    elif call.data == 'ol':
        handle_non_legendary(call)
    elif call.data == 'shiny':
        handle_shiny(call)
    elif call.data == 'tms':
        handle_tms(call)
    elif call.data == 'submit':
        submit_item(call)
    elif call.data == 'delete':
        bot.edit_message_text("RESPONSE DELETED", call.message.chat.id, call.message.message_id)
    elif call.data == 'submi':
        submit_tm(call)
    elif call.data == 'delet':
        bot.edit_message_text("RESPONSE DELETED", call.message.chat.id, call.message.message_id)
    elif call.data in ['approve', 'reject', 'rejtrash', 'rejinco', 'highbase', 'scammer']:
        handle_admin_actions(call)

def handle_legendary(call):
    bot.edit_message_text('OK! Legendary', call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, 'Enter Pokemon name')
    bot.register_next_step_handler_by_chat_id(call.from_user.id, process_pokemon_name, 'legendary')

def handle_non_legendary(call):
    bot.edit_message_text('OK! NON Legendary', call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, 'Enter Pokemon name')
    bot.register_next_step_handler_by_chat_id(call.from_user.id, process_pokemon_name, 'non_legendary')

def handle_shiny(call):
    bot.edit_message_text('OK! Shiny', call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, 'Enter Pokemon name')
    bot.register_next_step_handler_by_chat_id(call.from_user.id, process_pokemon_name, 'shiny')

def handle_tms(call):
    bot.edit_message_text('OK! TMS', call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, 'Forward TM')
    bot.register_next_step_handler_by_chat_id(call.from_user.id, process_tm, 'tm')

def process_pokemon_name(message, item_type):
    pokemon_name = message.text
    bot.send_message(message.chat.id, 'Forward Nature Pic of pokemon')
    bot.register_next_step_handler(message, process_nature_pic, item_type, pokemon_name)

def process_nature_pic(message, item_type, pokemon_name):
    if message.photo:
        user_cache[message.chat.id] = {'pokemon_name': pokemon_name, 'nature_pic': message.photo[-1].file_id}
        bot.send_message(message.chat.id, 'Forward Evs Pic of pokemon')
        bot.register_next_step_handler(message, process_evs_pic, item_type, pokemon_name, message.caption)
    else:
        bot.send_message(message.chat.id, "An error occurred, please restart the process. Please forward the pic with nature too. If the pic isn't present, an error will happen again")

def process_evs_pic(message, item_type, pokemon_name, nature):
    if message.photo:
        user_cache[message.chat.id]['evs_pic'] = message.photo[-1].file_id
        bot.send_message(message.chat.id, 'Forward moveset pic of pokemon')
        bot.register_next_step_handler(message, process_moveset_pic, item_type, pokemon_name, nature, message.caption)
    else:
        bot.send_message(message.chat.id, "An error occurred, please restart the process. Please forward the pic with evs and ivs too. If the pic isn't present, an error will happen again")

def process_moveset_pic(message, item_type, pokemon_name, nature, evs):
    if message.photo:
        user_cache[message.chat.id]['moveset_pic'] = message.photo[-1].file_id
        bot.send_message(message.chat.id, 'IS ANY STAT BOOSTED? (Answer in only 1 message)')
        bot.register_next_step_handler(message, process_boosted_stat, item_type, pokemon_name, nature, evs, message.caption)
    else:
        bot.send_message(message.chat.id, "An error occurred, please restart the process. Please forward the pic with moveset too. If the pic isn't present, an error will happen again")

def process_boosted_stat(message, item_type, pokemon_name, nature, evs, moveset):
    boosted = message.text
    bot.send_message(message.chat.id, 'Set base')
    bot.register_next_step_handler(message, process_base, item_type, pokemon_name, nature, evs, moveset, boosted)

def process_base(message, item_type, pokemon_name, nature, evs, moveset, boosted):
    base = message.text
    user_id = message.chat.id
    text = f"#{item_type.capitalize()}\n\nPokemon Name: {pokemon_name}\n\nAbout Pokemon:- \n{nature}\n\nEvs and Ivs:-\n\n{evs}\n\nMoveset:- \n{moveset}\n\nBoosted - \n{boosted}\n\nBase - {base}\n \n User id - {user_id}\nUsername : @{message.from_user.username}"
    user_cache[user_id]['text'] = text
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('SUBMIT', callback_data='submit'))
    markup.add(types.InlineKeyboardButton('Delete', callback_data='delete'))
    bot.send_photo(user_id, user_cache[user_id]['nature_pic'], caption=text, reply_markup=markup)

def process_tm(message, item_type):
    name = message.text
    bot.send_message(message.chat.id, 'ENTER BASE')
    bot.register_next_step_handler(message, process_tm_base, name)

def process_tm_base(message, name):
    base = message.text
    user_id = message.chat.id
    text = f"#TMS\nUser id - {user_id}\nUsername : @{message.from_user.username}\n\nAbout TM:- \n{name}\n\nBase - {base}"
    user_cache[user_id] = {'text': text}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('SUBMIT', callback_data='submi'))
    markup.add(types.InlineKeyboardButton('Delete', callback_data='delet'))
    bot.send_message(user_id, text, reply_markup=markup)

def submit_item(call):
    user_id = call.from_user.id
    text = user_cache[user_id]['text']
    photo = user_cache[user_id]['nature_pic']
    bot.send_message(call.message.chat.id, text + "\n\nSUBMITTED\nUsually it takes 3-4 hours to get accepted or rejected, Check the buttons below", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('AUCTION GROUP', url=AUCTION_GROUP_LINK)))
    bot.send_photo(log_channel, photo, caption=text, reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('APPROVE', callback_data='approve'),
        types.InlineKeyboardButton('REJECT', callback_data='reject'),
        types.InlineKeyboardButton('REJECT TRASH', callback_data='rejtrash'),
        types.InlineKeyboardButton('REJECT INCOMPLETE', callback_data='rejinco'),
        types.InlineKeyboardButton('REJECT HIGHBASE', callback_data='highbase'),
        types.InlineKeyboardButton('REPORT AS SCAMMER', callback_data='scammer')))

def submit_tm(call):
    user_id = call.from_user.id
    text = user_cache[user_id]['text']
    bot.send_message(call.message.chat.id, text + "\n\nSUBMITTED\nUsually it takes 3-4 hours to get accepted or rejected, Check the buttons below", reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('AUCTION GROUP', url=AUCTION_GROUP_LINK)))
    bot.send_message(log_channel, text, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('APPROVE', callback_data='approve'),
                                                                                      types.InlineKeyboardButton('REJECT', callback_data='reject'),
                                                                                      types.InlineKeyboardButton('REJECT TRASH', callback_data='rejtrash'),
                                                                                      types.InlineKeyboardButton('REJECT INCOMPLETE', callback_data='rejinco'),
                                                                                      types.InlineKeyboardButton('REJECT HIGHBASE', callback_data='highbase'),
                                                                                      types.InlineKeyboardButton('REPORT AS SCAMMER', callback_data='scammer')))

def handle_admin_actions(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id  # Get the chat ID where the action is triggered
    
    # Get the user's status in the group or channel
    chat_member = bot.get_chat_member(chat_id, user_id)
    
    # Check if the user is an admin or creator in the group/channel
    if chat_member.status in ['administrator', 'creator']:
        # Remove the inline buttons once an action is taken
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        
        if call.data == 'approve':
            # Forward the message to the post and approve channels
            bot.forward_message(post_channel, log_channel, call.message.message_id)
            bot.forward_message(approve_channel, log_channel, call.message.message_id)
            bot.send_message(approve_channel, f"Accepted by @{call.from_user.username}")
        else:
            # Reject scenarios
            reject_message = {
                'reject': f"Rejected by @{call.from_user.username}",
                'rejtrash': f"Rejected as trash by @{call.from_user.username}",
                'rejinco': f"Rejected due to incomplete details by @{call.from_user.username}",
                'highbase': f"Rejected due to high base by @{call.from_user.username}",
                'scammer': f"Reported as scammer by @{call.from_user.username}"
            }
            
            # Forward the message to the reject channel and send the rejection reason
            bot.forward_message(reject_channel, log_channel, call.message.message_id)
            bot.send_message(reject_channel, reject_message[call.data])

        # Delete the message from the log channel after action is taken
        bot.delete_message(log_channel, call.message.message_id)
    else:
        # If the user is not an admin, show an alert
        bot.answer_callback_query(call.id, 'You are not authorized to take this action', show_alert=True)

@bot.message_handler(commands=['broad'])
def broadcast(message):
    user_id = message.from_user.id  # Get the ID of the user who issued the command
    
    # Check if the user is banned
    if str(user_id) in banned_users:
        bot.reply_to(message, "You are banned by an administrator.")
        return
    
    # Check if the user is an admin
    if str(user_id) in admin_ids:
        # Verify if the message contains something to broadcast
        if len(message.text.split()) >= 2:
            broadcast_message = ' '.join(message.text.split()[1:])  # Get the message to broadcast
            
            # Broadcast the message to all users in the broad_users list
            for broad_user_id in broad_users:
                try:
                    bot.send_message(broad_user_id, broadcast_message)
                except Exception as e:
                    print(f"Could not send message to {broad_user_id}: {e}")
            
            bot.reply_to(message, "Broadcast sent to all users.")
        else:
            bot.reply_to(message, "Please provide a message to broadcast using the syntax /broad (message).")
    else:
        bot.reply_to(message, "You're not authorized to perform this action.")

group_id = -1002266679524

@bot.message_handler(commands=['gban'])
def handle_ban(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        if str(message.from_user.id) not in str(admin_ids):
            bot.reply_to(message, "You are not authorized to use this command.")
            return

        try:
            _, user_id = message.text.split(maxsplit=1)
            banned_users.add(user_id)  
            bot.reply_to(message, f"User with ID {user_id} has been banned.")
        except ValueError:
            bot.reply_to(message, "Invalid syntax. Use /ban <user_id>")


@bot.message_handler(commands=['unban'])
def handle_unban(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        if str(message.from_user.id) not in str(admin_ids):
            bot.reply_to(message, "You are not authorized to use this command.")
            return
        try:
            _, user_id = message.text.split(maxsplit=1)
            if user_id in banned_users:
                banned_users.remove(user_id) 
                bot.reply_to(message, f"User with ID {user_id} has been unbanned.")
            else:
                bot.reply_to(message, f"User with ID {user_id} is not banned.")
        except ValueError:
            bot.reply_to(message, "Invalid syntax. Use /unban <user_id>")

@bot.message_handler(commands=['users'])
def handle_users(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        user_id = message.from_user.id
        if str(user_id) in str(admin_ids):
            num_users = len(started_users)
            bot.send_message(message.chat.id, f"Total users : {num_users}")
        else:
            bot.send_message(message.chat.id, "You are not authorized to use this command.")

nature_info = {
    "adamant": {"increase": "Attack", "decrease": "Special Attack"},
    "bashful": {"increase": "none", "decrease": "none"},
    "bold": {"increase": "Defense", "decrease": "Attack"},
    "brave": {"increase": "Attack", "decrease": "Speed"},
    "calm": {"increase": "Special Defense", "decrease": "Attack"},
    "careful": {"increase": "Special Defense", "decrease": "Special Attack"},
    "docile": {"increase": "none", "decrease": "none"},
    "gentle": {"increase": "Special Defense", "decrease": "Defense"},
    "hardy": {"increase": "none", "decrease": "none"},
    "hasty": {"increase": "Speed", "decrease": "Defense"},
    "impish": {"increase": "Defense", "decrease": "Special Attack"},
    "jolly": {"increase": "Speed", "decrease": "Special Attack"},
    "lax": {"increase": "Defense", "decrease": "Special Defense"},
    "lonely": {"increase": "Attack", "decrease": "Defense"},
    "mild": {"increase": "Special Attack", "decrease": "Defense"},
    "modest": {"increase": "Special Attack", "decrease": "Attack"},
    "naive": {"increase": "Speed", "decrease": "Special Defense"},
    "naughty": {"increase": "Attack", "decrease": "Special Defense"},
    "quiet": {"increase": "Special Attack", "decrease": "Speed"},
    "quirky": {"increase": "none", "decrease": "none"},
    "rash": {"increase": "Special Attack", "decrease": "Special Defense"},
    "relaxed": {"increase": "Defense", "decrease": "Speed"},
    "sassy": {"increase": "Special Defense", "decrease": "Speed"},
    "serious": {"increase": "none", "decrease": "none"},
    "timid": {"increase": "Speed", "decrease": "Attack"}
}

@bot.message_handler(func=lambda message: message.text.lower() in nature_info)
def handle_nature(message):
    nature_name = message.text.lower()
    info = nature_info[nature_name]
    response = f"Nature : {nature_name.capitalize()}\n\n▪️ Effects :\n\n"
    response += f"🔺 Stats Increase + : {info['increase']}\n"
    response += f"🔻 Stats Decrease - : {info['decrease']}\n"
    bot.reply_to(message, response)

@bot.message_handler(commands=['natures'])
def natures(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        response = "Nature Types:\n"
        for nature in nature_info:
            response += f"- {nature}\n"
        bot.reply_to(message, response)

user_groups = {}

@bot.message_handler(commands=['help'])
def handle_cmds(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        user_id = message.from_user.id
        bot.reply_to(message, '''
                     Users Commands :-
—————————————————————————
• /start - Start The Bot
• /add - Send Poke / TMs / Teams For Next Auction
• /cancel - Cancel All Running Commands Like add
• /admin - Get Bot All Admins List
• /help - Get Some Question With Answers Related To Auction
• /natures - Get All Natures List
• /tm00 - Get A TM Details (Replace 00 With Tm Number) 
• /host - Create Your Own Auction Bot
                         
''')
        

# Bot toke
# Admin list (store IDs as strings, including the new admin IDs)
admin_ids = ['1661129466', '6265981509']  # Updated admin list

# Helper function to get the username or ID
def get_username_or_id(user_id):
    try:
        user = bot.get_chat(user_id)
        if user.username:
            return f'@{user.username}'
        else:
            return f'{user.id}'
    except telebot.apihelper.ApiTelegramException:
        return f'{user_id} (unable to fetch details)'
# Helper function to get the username or ID
def get_username_or_id(user_id):
    try:
        user = bot.get_chat(user_id)
        if user.username:
            return f'@{user.username}'
        else:
            return f'{user.id}'
    except telebot.apihelper.ApiTelegramException:
        return f'{user_id} (unable to fetch details)'

# Admin command to promote a user to admin using username or ID
@bot.message_handler(commands=['admin'])
def add_admin(message):
    # Check if the user sending the command is an admin
    if str(message.from_user.id) not in admin_ids:
        bot.send_message(message.chat.id, "Only current admins can use this command.")
        return

    try:
        args = message.text.split()
        if len(args) != 2:
            bot.send_message(message.chat.id, "Usage: /admin <@username or user_id>")
            return
        
        identifier = args[1]

        # If a username is provided
        if identifier.startswith('@'):
            username = identifier[1:]
            try:
                # Try to get the user ID by username
                user = bot.get_chat_member(message.chat.id, username)
                user_id = user.user.id
            except Exception as e:
                bot.send_message(message.chat.id, f"User @{username} not found.")
                return
        
        # If an ID is provided
        else:
            try:
                user_id = int(identifier)
            except ValueError:
                bot.send_message(message.chat.id, "Invalid user ID.")
                return

        # Add the user to the admin list and xmods list if they're not already an admin
        if str(user_id) not in admin_ids:
            admin_ids.append(str(user_id))
            if str(user_id) not in xmods:
                xmods.append(str(user_id))
            bot.send_message(message.chat.id, f"User {get_username_or_id(user_id)} has been added to the admin and xmods lists.")
        else:
            bot.send_message(message.chat.id, f"User {get_username_or_id(user_id)} is already an admin.")
    
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while processing the request.")


tm_data = {
    2: {"name": "Dragon Claw", "power": 80, "accuracy": 100, "category": "P"},
    3: {"name": "Psyshock", "power": 80, "accuracy": 100, "category": "S"},
    9: {"name": "Venoshock", "power": 65, "accuracy": 100, "category": "S"},
    10: {"name": "Hidden Power", "power": 60, "accuracy": 100, "category": "S"},
    13: {"name": "Ice Beam", "power": 90, "accuracy": 100, "category": "S"},
    14: {"name": "Blizzard", "power": 110, "accuracy": 70, "category": "S"},
    15: {"name": "Hyper Beam", "power": 150, "accuracy": 90, "category": "S"},
    22: {"name": "Solar Beam", "power": 120, "accuracy": 100, "category": "S"},
    23: {"name": "Smack Down", "power": 50, "accuracy": 100, "category": "P"},
    24: {"name": "Thunderbolt", "power": 90, "accuracy": 100, "category": "S"},
    25: {"name": "Thunder", "power": 110, "accuracy": 70, "category": "P"},
    26: {"name": "Earthquake", "power": 100, "accuracy": 100, "category": "P"},
    28: {"name": "Leech Life", "power": 80, "accuracy": 100, "category": "P"},
    29: {"name": "Psychic", "power": 90, "accuracy": 100, "category": "S"},
    30: {"name": "Shadow Ball", "power": 80, "accuracy": 100, "category": "S"},
    31: {"name": "Brick Break", "power": 75, "accuracy": 100, "category": "P"},
    34: {"name": "Sludge Wave", "power": 95, "accuracy": 100, "category": "S"},
    35: {"name": "Flamethrower", "power": 90, "accuracy": 100, "category": "S"},
    36: {"name": "Sludge Bomb", "power": 90, "accuracy": 100, "category": "S"},
    38: {"name": "Fire Blast", "power": 110, "accuracy": 85, "category": "S"},
    39: {"name": "Rock Tomb", "power": 60, "accuracy": 95, "category": "P"},
    40: {"name": "Aerial Ace", "power": 60, "accuracy": 100, "category": "P"},
    42: {"name": "Facade", "power": 70, "accuracy": 100, "category": "P"},
    43: {"name": "Flame Charge", "power": 50, "accuracy": 100, "category": "P"},
    46: {"name": "Thief", "power": 60, "accuracy": 100, "category": "P"},
    47: {"name": "Low Sweep", "power": 65, "accuracy": 100, "category": "P"},
    48: {"name": "Round", "power": 60, "accuracy": 100, "category": "S"},
    49: {"name": "Echoed Voice", "power": 40, "accuracy": 100, "category": "S"},

50: {"name": "Overheat", "power": 130, "accuracy": 90, "category": "S"},
    51: {"name": "Steel Wing", "power": 70, "accuracy": 90, "category": "P"},
    52: {"name": "Focus Blast", "power": 120, "accuracy": 70, "category": "S"},
    53: {"name": "Energy Ball", "power": 90, "accuracy": 100, "category": "S"},
    54: {"name": "False Swipe", "power": 40, "accuracy": 100, "category": "P"},
    55: {"name": "Scald", "power": 80, "accuracy": 100, "category": "S"},
    57: {"name": "Charge Beam", "power": 50, "accuracy": 90, "category": "S"},
    58: {"name": "Sky Drop", "power": 60, "accuracy": 100, "category": "P"},
    59: {"name": "Brutal Swing", "power": 60, "accuracy": 100, "category": "P"},
    62: {"name": "Acrobatics", "power": 55, "accuracy": 100, "category": "P"},
    65: {"name": "Shadow Claw", "power": 70, "accuracy": 100, "category": "P"},
    66: {"name": "Payback", "power": 50, "accuracy": 100, "category": "P"},
    67: {"name": "Smart Strike", "power": 70, "accuracy": 100, "category": "P"},
    68: {"name": "Giga Impact", "power": 150, "accuracy": 90, "category": "P"},
    71: {"name": "Stone Edge", "power": 100, "accuracy": 80, "category": "P"},
    72: {"name": "Volt Switch", "power": 70, "accuracy": 100, "category": "S"},
    76: {"name": "Fly", "power": 90, "accuracy": 95, "category": "P"},
    78: {"name": "Bulldoze", "power": 60, "accuracy": 100, "category": "P"},
    79: {"name": "Frost Breath", "power": 60, "accuracy": 90, "category": "S"},
    80: {"name": "Rock Slide", "power": 75, "accuracy": 90, "category": "P"},
    81: {"name": "X-Scissor", "power": 80, "accuracy": 100, "category": "P"},
    82: {"name": "Dragon Tail", "power": 60, "accuracy": 90, "category": "P"},
    83: {"name": "Infestation", "power": 70, "accuracy": 100, "category": "S"},
    84: {"name": "Poison Jab", "power": 80, "accuracy": 100, "category": "P"},
    85: {"name": "Dream Eater", "power": 100, "accuracy": 100, "category": "S"},
    89: {"name": "U-Turn", "power": 70, "accuracy": 100, "category": "P"},
    91: {"name": "Flash Cannon", "power": 80, "accuracy": 100, "category": "S"},
    93: {"name": "Wild Charge", "power": 90, "accuracy": 100, "category": "P"},
    94: {"name": "Surf", "power": 90, "accuracy": 100, "category": "S"},
    95: {"name": "Snarl", "power": 55, "accuracy": 95, "category": "S"},
    97: {"name": "Dark Pulse", "power": 80, "accuracy": 100, "category": "S"},
    98: {"name": "Waterfall", "power": 80, "accuracy": 100, "category": "P"},
    99: {"name": "Dazzling Gleam", "power": 80, "accuracy": 100, "category": "S"},
}

@bot.message_handler(commands=['tm00'])
def handle_tm00(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        tm_list = "\n".join(f"|{tm_number}|{tm_info['name']}| {tm_info['power']}|{tm_info['accuracy']}|{tm_info['category']}|" for tm_number, tm_info in tm_data.items())
        bot.reply_to(message, f"TM List:\n\n{tm_list}")

@bot.message_handler(func=lambda message: re.match(r'tm\d{2}', message.text.lower()))
def handle_tm(message):
    match = re.match(r'tm(\d{2})', message.text.lower())
    tm_number = int(match.group(1))
    
    if tm_number not in tm_data:
        bot.reply_to(message, "TM not found. Please check the TM number and try again.")
        return
    
    tm_info = tm_data[tm_number]
    category = "Physical" if tm_info["category"] == "P" else "Special"
    response_message = (
        f"TM{tm_number} 💿:\n\n"
        f"{tm_info['name']} [{category}]\n"
        f"Power: {tm_info['power']}, Accuracy: {tm_info['accuracy']}\n\n"
        f"You can sell this TM for PDs 💵 in hexa"
    )
    
    bot.reply_to(message, response_message)
    
verified_emoji = "✅"

@bot.message_handler(commands=['host'])
def send_host(message):
    if str(message.from_user.id) in banned_users:
        bot.reply_to(message, "You Are Banned By an Administrator")
    else:
        if message.chat.type == 'private':
            host_message = "Want To Create Auction Bot Like This?"
            markup = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text='Contact', url='https://t.me/anime2005yes')
            markup.add(btn)
        
            bot.reply_to(message, host_message, reply_markup=markup)
        else:
            bot.reply_to(message, "This command can only be used in private messages.")

bot.skip_pending = True

user_ids = set()

bot.polling(non_stop=True)
