import re, random, string, os, json
from datetime import datetime
from typing import Final
import pandas as pd
import numpy as np
from decouple import config

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, ConversationHandler
from telegram.ext import MessageHandler, filters
from telegram.error import BadRequest

# Define the path to the JSON and CSV files
data_file_add = 'data_base.csv'

# Function to save email data to CSV
def save_email_data(df):
    df.to_csv(data_file_add, index=False)

# Function to load email data from CSV
def load_data_base():
    if os.path.exists(data_file_add):
        return pd.read_csv(data_file_add)
    else:
        return pd.DataFrame(columns=['ch_user_id', 'tel_user_name', 'tel_user_id', 'email_id', 'date'])

# Check if the email is already registered
def is_email(input_str):
    # Regular expression pattern for email validation
    email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    # Using re.match to check if the input string matches the email pattern
    if re.match(email_pattern, input_str):
        return True
    else:
        return False

def gen_uniq_channel_id(existing_ids):
    """
    Generate a unique 10-digit channel ID.
    
    :param existing_ids: A set of existing channel IDs
    :return: A unique 10-digit channel ID
    """
    while True:
        # Generate a random 10-digit ID
        channel_id = ''.join(random.choices(string.digits, k=10))
        # Check if this ID is unique
        if channel_id not in existing_ids:
            return channel_id

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Load the email_ids dictionary when the bot starts
data_base = load_data_base()

print('Starting up bot...')

Tk = config('token')

# Stages
START_ROUTES, END_ROUTES, SEND_IMG, MESS_HANDL = range(4)
# Callback data
SUBMIT_EMAIL, LOC_EX, GLOB_EX, MAIN_MENU, AIR_DROPS, MY_PROGRESS = range(6)

TEN, TWENTY, THIRTY = range(10, 40, 10)

# EMAIL_CONF = int(100)
EMAIL = 100

execution_counter = 0
IMG_IDX_COUNTER = 0
# current_index = 0 
first_time_loop = True


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    # global air_drop_counter
    # air_drop_counter = 0
    global current_index, first_time_loop
    current_index = 0  # Reset current_index to 0
    first_time_loop = True
    tel_user_id = update.effective_user.id

    if tel_user_id in data_base['tel_user_id'].values:
        tel_user_name = data_base[data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
        print_txt = f"Hello my Fren, {tel_user_name}"

        keyboard = [
            [InlineKeyboardButton("Local Exchange Referral Links", callback_data=str(LOC_EX))],
            [InlineKeyboardButton("Global Exchange Referral Links", callback_data=str(GLOB_EX))],
            [InlineKeyboardButton("Air Drops", callback_data=str(AIR_DROPS))],
            [InlineKeyboardButton("My Progress", callback_data=str(MY_PROGRESS))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [
            [InlineKeyboardButton("Join Now!", callback_data=str(SUBMIT_EMAIL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print_txt = 'Welcome to Crypto Channel'

    if update.message:
        await update.message.reply_text(text=print_txt, reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        current_index = 0 
        await query.answer()
        await query.edit_message_text(text=print_txt, reply_markup=reply_markup)

    
    # Reset the execution_counter when send_airdrops_album is called from start
    if update.callback_query and update.callback_query.data == str(AIR_DROPS):
        global execution_counter
        execution_counter = 0

    return START_ROUTES

# async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Prompt same text & keyboard as `start` does but not as new message"""
#     query = update.callback_query
#     await query.answer()

#     air_drop_counter = 0
#     tel_user_id = update.effective_user.id

#     if tel_user_id in data_base['tel_user_id'].values:
#         tel_user_name = data_base[data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
#         print_txt = f"Hello my Fren, {tel_user_name}"

#         keyboard = [
#             [InlineKeyboardButton("Local Exchange Referral Links", callback_data=str(LOC_EX))],
#             [InlineKeyboardButton("Global Exchange Referral Links", callback_data=str(GLOB_EX))],
#             [InlineKeyboardButton("Air Drops", callback_data=str(AIR_DROPS))],
#             [InlineKeyboardButton("My Progress", callback_data=str(MY_PROGRESS))]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#     else:
#         keyboard = [
#             [InlineKeyboardButton("Join Now!", callback_data=str(SUBMIT_EMAIL))]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         print_txt = 'Welcome to Crypto Channel'

#     await query.edit_message_text(text=print_txt, reply_markup=reply_markup)
#     return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    await query.answer()

    air_drop_counter = 0
    tel_user_id = update.effective_user.id

    if tel_user_id in data_base['tel_user_id'].values:
        tel_user_name = data_base[data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
        print_txt = f"Hello my Fren, {tel_user_name}"

        keyboard = [
            [InlineKeyboardButton("Local Exchange Referral Links", callback_data=str(LOC_EX))],
            [InlineKeyboardButton("Global Exchange Referral Links", callback_data=str(GLOB_EX))],
            [InlineKeyboardButton("Air Drops", callback_data=str(AIR_DROPS))],
            [InlineKeyboardButton("My Progress", callback_data=str(MY_PROGRESS))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [
            [InlineKeyboardButton("Join Now!", callback_data=str(SUBMIT_EMAIL))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print_txt = 'Welcome to Crypto Channel'

    try:
        # Try to edit the message text
        await query.edit_message_text(text=print_txt, reply_markup=reply_markup)
    except BadRequest:
        # If the message doesn't have text content, send a new message
        await query.message.reply_text(text=print_txt, reply_markup=reply_markup)

    return START_ROUTES




async def email_confirming(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global data_base

    tel_user_id = update.effective_user.id
    message_text = update.effective_message.text.lower()

    if update.effective_user.name:
        tel_user_name = update.effective_user.name
    else:
        tel_user_name = "no_tel_user_name"

    print('email confirming is executed')

    if is_email(message_text):
        if message_text in data_base['email_id'].values:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Email address already exists in our database.")
        else:
            ch_user_id = gen_uniq_channel_id(data_base['ch_user_id'].values)
            new_user = {
                'ch_user_id': ch_user_id,
                'tel_user_name': tel_user_name,
                'tel_user_id': tel_user_id,
                'email_id': message_text,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            new_user = pd.DataFrame([new_user])

            # Update email data DataFrame
            data_base = pd.concat([data_base, new_user], ignore_index=True)
            save_email_data(data_base)

            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"New email address added with ID: {tel_user_id}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid email address. Please try again.")

async def submit_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text='Please send your email address:')
    return EMAIL

async def local_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton('Nobitex', url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton('BitPin', url='https://bitpin.ir/signup/?ref=aP0DtoVG')],
        [InlineKeyboardButton('Back', callback_data=str(MAIN_MENU))]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text='Please use the links below to join the exchange',
        reply_markup=key_markup
    )
    return START_ROUTES

async def global_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton('BingX', url='https://bingx.com/invite/NLQIKZI2')],
        [InlineKeyboardButton('CoinEx', url='https://www.coinex.com/register?refer_code=s95m7')],
        [InlineKeyboardButton('Back', callback_data=str(MAIN_MENU))]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text='Please use the links below to join the exchange',
        reply_markup=key_markup
    )
    return START_ROUTES

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # Reset current_index when main_menu is called
    global current_index, first_time_loop
    current_index = 0
    first_time_loop = True

    return await start_over(update, context)


###############################################################################

# async def send_airdrops_album(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()
    
#     global current_index

#     # Get the index from the callback data
#     if query.data.isdigit():
#         current_index = int(query.data)
#     else:
#         current_index = 0



#     print('---')
#     print(update.callback_query.data)
#     print('---')

#     print('***')
#     print(update.callback_query)
#     print('***')

#     if update.callback_query and update.callback_query.data:
#         print('exeasagsg')
#         print(update.callback_query.data)
#         print(update.callback_query.data.split("_")[-1])

#     # List of photo file_ids or URLs
#     photo_list = [
#         'https://th.bing.com/th/id/OIP.TzP2op3lkhlTh6oOHamacAHaHa?rs=1&pid=ImgDetMain',
#         'https://th.bing.com/th/id/OIP.RH2gc-Oe1qSvCjD3IRYAyQHaE7?rs=1&pid=ImgDetMain',
#         'https://th.bing.com/th/id/OIP.AW8VfeeCp9v_xzlVdciPpAHaEo?rs=1&pid=ImgDetMain',
#         'https://th.bing.com/th/id/OIP.R3U06JEJvoROC7iFM1AnzAHaEK?rs=1&pid=ImgDetMain'
#     ]

#     # # Determine the current index
#     # if update.callback_query and update.callback_query.data:
#     #     current_index = int(update.callback_query.data.split("_")[-1])
#     # else:
#     #     current_index = 0

#     # Ensure current_index stays within the bounds of photo_list
#     current_index = max(0, min(current_index, len(photo_list) - 1))

#     # # If "Finish" button is clicked, show the main menu
#     # if update.callback_query and update.callback_query.data == "FINISH":
#     #     await main_menu(update, context)
#     #     return START_ROUTES

#     # Construct caption with current index and total number of photos
#     caption = f"{current_index + 1} out of {len(photo_list)}"

#     # Construct InlineKeyboardMarkup based on current message index
#     buttons = []
#     if current_index == 0:
#         buttons.append([InlineKeyboardButton("Next", callback_data=str(current_index + 1)),
#                         InlineKeyboardButton("Back to Main Menu", callback_data=str(MAIN_MENU))])
#     elif current_index == len(photo_list) - 1:
#         buttons.append([InlineKeyboardButton("Finish", callback_data=str(MAIN_MENU)),
#                         InlineKeyboardButton("Previous", callback_data=str(current_index - 1))])
#     else:
#         buttons.append([InlineKeyboardButton("Next", callback_data=str(current_index + 1)),
#                         InlineKeyboardButton("Previous", callback_data=str(current_index - 1))])

#     reply_markup = InlineKeyboardMarkup(buttons)
#     print(current_index)
#     # Send the current photo with caption and navigation buttons
#     await context.bot.send_photo(
#         chat_id=update.effective_chat.id,
#         photo=photo_list[current_index],
#         caption=caption,
#         reply_markup=reply_markup
#     )

#     return SEND_IMG

###############################################################################
async def send_airdrops_album(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    global current_index, first_time_loop

    print(f"it is digit: {current_index}")

    # # Get the index from the callback data
    # if query.data.isdigit():
    #     current_index = int(query.data)
    #     print(f"it is digit: {current_index}")


    # Get the index from the callback data
    if query.data.isdigit() and first_time_loop:
        current_index = 0
        first_time_loop = False
        print(f"it is first time: {current_index}")
    else: 
        current_index = int(query.data)
        print(f"it is not first time: {current_index}")

    # List of photo file_ids or URLs
    photo_list = [
        'https://th.bing.com/th/id/OIP.TzP2op3lkhlTh6oOHamacAHaHa?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.RH2gc-Oe1qSvCjD3IRYAyQHaE7?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.AW8VfeeCp9v_xzlVdciPpAHaEo?rs=1&pid=ImgDetMain',
        'https://th.bing.com/th/id/OIP.R3U06JEJvoROC7iFM1AnzAHaEK?rs=1&pid=ImgDetMain'
    ]

    # Ensure current_index stays within the bounds of photo_list
    current_index = max(0, min(current_index, len(photo_list) - 1))

    # Construct caption with current index and total number of photos
    caption = f"{current_index + 1} out of {len(photo_list)}"

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index == 0:
        buttons.append([InlineKeyboardButton("Next", callback_data=str(current_index + 1)),
                        InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")])
    elif current_index == len(photo_list) - 1:
        buttons.append([InlineKeyboardButton("Finish", callback_data="main_menu"),
                        InlineKeyboardButton("Previous", callback_data=str(current_index - 1))])
    else:
        buttons.append([InlineKeyboardButton("Next", callback_data=str(current_index + 1)),
                        InlineKeyboardButton("Previous", callback_data=str(current_index - 1))])

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=photo_list[current_index],
        caption=caption,
        reply_markup=reply_markup
    )

    return SEND_IMG



def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(Tk).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(submit_email, pattern="^" + str(SUBMIT_EMAIL) + "$"),
                CallbackQueryHandler(local_exchange, pattern="^" + str(LOC_EX) + "$"),
                CallbackQueryHandler(global_exchange, pattern="^" + str(GLOB_EX) + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + str(MAIN_MENU) + "$"),
                CallbackQueryHandler(send_airdrops_album, pattern="^" + str(AIR_DROPS) + "$")
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(MAIN_MENU) + "$")
            ],
            SEND_IMG: [
                CallbackQueryHandler(send_airdrops_album, pattern="^(\d+)$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            EMAIL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, email_confirming)
            ]
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(
        allowed_updates=Update.ALL_TYPES, poll_interval=3, timeout=60
    )

if __name__ == "__main__":
    main()
