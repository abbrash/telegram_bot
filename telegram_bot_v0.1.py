import re
import random
import os
import json
from datetime import datetime
from typing import Final
import pandas as pd
import numpy as np
from decouple import config

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, ConversationHandler
from telegram.ext import MessageHandler, filters, Updater

# Define the path to the JSON and CSV files
EMAIL_IDS_FILE = 'email_ids.json'
DATA_FILE = 'email_data.csv'

# Function to save the email_ids dictionary to a JSON file
def save_email_ids(email_ids):
    with open(EMAIL_IDS_FILE, 'w') as f:
        json.dump(email_ids, f)

# Function to load the email_ids dictionary from a JSON file
def load_email_ids():
    if os.path.exists(EMAIL_IDS_FILE):
        with open(EMAIL_IDS_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

# Function to save email data to CSV
def save_email_data(df):
    df.to_csv(DATA_FILE, index=False)

# Function to load email data from CSV
def load_email_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        # return pd.DataFrame(columns=['Email', 'ID', 'Time Added'])
        return pd.DataFrame(columns=['user_id', 'name', 'tel_user_id', 'email_id', 'date'])

# Ckeck if the email is already registered
def is_email(input_str):
    # Regular expression pattern for email validation
    email_pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    # Using re.match to check if the input string matches the email pattern
    if re.match(email_pattern, input_str):
        return True
    else:
        return False

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Load the email_ids dictionary when the bot starts
email_ids = load_email_ids()
email_data = load_email_data()



# print(email_data)
# print()
print('Starting up bot...')


Tk = config('token')
BOT_USERNAME: Final = '@CrypticChannelBot'

# print(Tk)

# Stages
START_ROUTES, END_ROUTES, MESS_HANDL = range(3)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

TEN, TWENTY, THIRTY = range(10, 40, 10)

# EMAIL_CONF = int(100)
EMAIL = 100




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user_id = update.effective_user.id
    if user_id in email_data['tel_user_id'].values:
        user_name = email_data[email_data['tel_user_id'] == user_id]['name'].values[0]
        print_txt = f"Hello my Fren, {user_name}"

        keyboard = [
            [
                InlineKeyboardButton("Start1", callback_data=str(ONE)),
                InlineKeyboardButton("Start2", callback_data=str(TWO)),
                InlineKeyboardButton("Start3", callback_data=str(THREE)),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

    else:

        keyboard = [
            [
                InlineKeyboardButton("Join Now!", callback_data=str(ONE)),
                InlineKeyboardButton("Start2", callback_data=str(TWENTY)),
                InlineKeyboardButton("Start3", callback_data=str(THIRTY)),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        print_txt = 'Welcome to Crypto Channel' 

    await update.message.reply_text(text=print_txt, reply_markup=reply_markup)

    
    # Send message with text and appended InlineKeyboard
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    await query.edit_message_text(text="Start handler, Choose a route", reply_markup=reply_markup)
    return START_ROUTES


async def email_confirming(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    global email_data

    print('email confirming is executed')

    user_id = update.effective_user.id
    message_text = update.effective_message.text.lower()

    if is_email(message_text):
         
         if message_text in email_ids:
             context.bot.send_message(chat_id=update.effective_chat.id, text="Email address already exists on our database.")
         else:
            new_user = {
                        'user_id': 'user_id',
                        'name': 'new_user',
                        'tel_user_id': user_id,
                        'email_id': message_text,
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }

            new_user = pd.DataFrame([new_user])

                    # Update email data DataFrame
            email_data = pd.concat(
                        [email_data, new_user], ignore_index=True)
            save_email_data(email_data)

            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"New email address added with ID: {user_id}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid email address. Please try again.")



async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Please send your email address:')
    return EMAIL


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(
        "7029020592:AAGYmkIiqRPL99oGfIW0vvyTIhSJYKDbl9U").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$")],

            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$")],

            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email_confirming)]
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(
        allowed_updates=Update.ALL_TYPES, poll_interval=3, timeout=60)



if __name__ == "__main__":
    main()