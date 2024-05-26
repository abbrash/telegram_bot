### <<<--------------------------------------------------------------------------------------------------->>> ###
### <<<-------------------------------------------- Libraries -------------------------------------------->>> ###
### <<<--------------------------------------------------------------------------------------------------->>> ###

import re, random, string, os, json
from datetime import datetime
from typing import Final
import pandas as pd
import numpy as np
from decouple import config
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackContext, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from telegram.error import BadRequest


### <<<----------------------------------------------------------------------------------------------------------------->>> ###
### <<<-------------------------------------------- Constants and Variables -------------------------------------------->>> ###
### <<<----------------------------------------------------------------------------------------------------------------->>> ###

# Stages
START_ROUTES, END_ROUTES, SEND_IMG, PH_AIRDROP, PH_AIRDROP_SWAP, PH_AIRDROP_STAKE, PH_AIRDROP_UNSTAKE, EMAIL, MESS_HANDL = range(9)
LINEA_SURGE_AIRDROP, LINEA_SURGE_AIRDROP_STAKE, LINEA_SURGE_AIRDROP_UNSTAKE = range(9,12)


global first_time_loop_ph_swap, first_time_loop_ph_stake, first_time_loop_ph_unstake 
global current_index_ph_swap, current_index_ph_stake, current_index_ph_unstake
first_time_loop_ph_swap = True
first_time_loop_ph_stake = True
first_time_loop_ph_unstake = True
current_index_ph_swap = 0
current_index_ph_stake = 0
current_index_ph_unstake = 0

global first_time_loop_linea_surge_stake, first_time_loop_linea_surge_unstake
global current_index_linea_surge_stake, current_index_linea_surge_unstake
first_time_loop_linea_surge_stake = True
first_time_loop_linea_surge_unstake = True
current_index_linea_surge_stake = 0
current_index_linea_surge_unstake = 0


# Assuming you have a global dictionary to store message IDs
message_ids = {}

global chat_id
chat_id = None


### <<<-------------------------------------------------------------------------------------------------------->>> ###
### <<<-------------------------------------------- Sync Functions -------------------------------------------->>> ### 
### <<<-------------------------------------------------------------------------------------------------------->>> ###


# Define the path to save CSV file
data_file_add = 'data_base.csv'

# Define the path to save CSV file using os.getcwd() to get the current working directory
data_file_path = os.path.join(os.getcwd(), 'data_base.csv')

# Function to save email data to CSV
def save_email_data(df):
    df.to_csv(data_file_path, index=False)

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



### <<<--------------------------------------------------------------------------------------------------------->>> ###
### <<<--------------------------------------------------------------------------------------------------------->>> ###
### <<<-------------------------------------------- Async Functions -------------------------------------------->>> ###
### <<<--------------------------------------------------------------------------------------------------------->>> ###
### <<<--------------------------------------------------------------------------------------------------------->>> ###


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    
    tel_user_id = update.effective_user.id

    if tel_user_id in data_base['tel_user_id'].values:
        tel_user_name = data_base[data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
        print_txt = f"Hello my Fren, {tel_user_name}"

        keyboard = [
            [InlineKeyboardButton("صرافی‌های ایرانی  💱🇮🇷", callback_data="local_exchange")],
            [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
            [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [
            [InlineKeyboardButton("ثبت نام", callback_data="submit_email")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print_txt = "به کانال کریپتیک خوش آمدید:"

    if update.message:
        await update.message.reply_text(text=print_txt, reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        current_index_ph_swap = 0 
        await query.answer()
        await query.edit_message_text(text=print_txt, reply_markup=reply_markup)

    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    await query.answer()

    tel_user_id = update.effective_user.id

    if tel_user_id in data_base['tel_user_id'].values:
        tel_user_name = data_base[data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
        print_txt = f"Stay with us, {tel_user_name}"

        keyboard = [
            [InlineKeyboardButton("صرافی‌های ایرانی  💱🇮🇷", callback_data="local_exchange")],
            [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
            [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [
            [InlineKeyboardButton("ثبت نام", callback_data="submit_email")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        print_txt = "به کانال کریپتیک خوش آمدید:"

    try:
        # Try to edit the message text
        await query.edit_message_text(text=print_txt, reply_markup=reply_markup)
    except BadRequest:
        # If the message doesn't have text content, send a new message
        await query.message.reply_text(text=print_txt, reply_markup=reply_markup)

    return START_ROUTES


async def confirm_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
            await context.bot.send_message(chat_id=update.effective_chat.id, 
                                           text="آدرس ایمیل وارد شده توسط شخص دیگری ثبت شده است، لطفاً آدرس ایمیل خودتان را وارد کنید:")
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

            # await context.bot.send_message(chat_id=update.effective_chat.id, text=f"New email address added with ID: {tel_user_id}")
            # Show the main menu instead of sending a message
            return await main_menu(update, context)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text="آدرس ایمیل وارد شده نادرست است، لطفاً دوباره تلاش کنید:")


async def submit_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    text = """لطفاً آدرس ایمیل خود را وارد ارسال کنید:"""
    await query.edit_message_text(text=text)
    return EMAIL

async def local_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ", url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton("صرافی بیت‌پین (BitPin)", url='https://bitpin.ir/signup/?ref=aP0DtoVG')],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return START_ROUTES

async def global_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("صرافی بینک‌اکس (BingX)", url='https://bingx.com/invite/NLQIKZI2')],
        [InlineKeyboardButton("صرافی کوینکس (CoinEx)", url='https://www.coinex.com/register?refer_code=s95m7')],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return START_ROUTES


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    if update.message:
        # Handle text messages
        return await start(update, context)
    elif update.callback_query:
        # Handle callback queries
        query = update.callback_query
        await query.answer()
        return await start_over(update, context)
    else:
        # Handle other update types (not expected)
        return END_ROUTES


### <<<-------------------------------------------- Phantom AirDrop -------------------------------------------->>> ###
### << *** Phantom AirDrop - Swap *** >>> ###

async def air_drop_phantom_swap(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    global current_index_ph_swap, first_time_loop_ph_swap, message_ids
    global chat_id

    print(f"Current index: {current_index_ph_swap}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_ph_swap:
            current_index_ph_swap = 0
            first_time_loop_ph_swap = False
        else:
            current_index_ph_swap = int(query.data)
    elif query.data == "phantom_swap":
        # Reset current_index when "air_drop_01" is clicked
        current_index_ph_swap = 0
        first_time_loop_ph_swap = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/swap'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_ph_swap + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_ph_swap = max(
        0, min(current_index_ph_swap, len(os.listdir(img_add)) - 1))
    

    # Define your list of captions here
    captions_list = [
        """در بخش نشان‌داده شده، مقدار موجودی سولانا(SOL) در کیف پول شما نمایش داده شده است.
        روی آن کلیک کنید.
        """,
        """روی گزینه سواپ (Swap) کلیک کنید.""",
        """در اینجا باید توکنی که سولانا به آن تبدیل می‌شود را انتخاب کنید. 
روی بخش مشخص شده کلیک کنید.
        """,
        """توکن USDC را انتخاب کنید.""",
        """
1️⃣  مقدار سولانایی که می‌خواهید تبدیل کنید را وارد کنید.
2️⃣  بصورت خودکار میزان USDC دریافتی نمایش داده می‌شود.
3️⃣  روی دکمه Review Order کلیک کنید. 
""",
        """
1️⃣ میزان کارمزد تراکنش نمایش داده می‌شود.
2️⃣ روی دکمه Swap کلیک کنید.
"""
        ]  

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_ph_swap]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_ph_swap == 0:
        buttons = [
                [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_swap + 1))],
                [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="air_drop_phantom_menu_over")]
    ]
    elif current_index_ph_swap == len(os.listdir(img_add)) - 1:
        buttons = [
                [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_phantom_menu_over")],
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_swap - 1))]
    ]
    else:
        buttons = [
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_swap - 1)),
                InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_swap + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )
        
        # Store the message ID
        if chat_id not in message_ids:
            message_ids[chat_id] = []           # initialize a list to store further information
        message_ids[chat_id].append(sent_photo.message_id)
        
        # Delete the previous photo if it exists
        if len(message_ids.get(chat_id, [])) > 1:  # Use.get() method to avoid KeyError if chat_id not found
            await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
            message_ids[chat_id].pop(0)

    return PH_AIRDROP_SWAP


### << *** Phantom AirDrop - Stake *** >>> ###

async def air_drop_phantom_stake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    global current_index_ph_stake, first_time_loop_ph_stake
    global chat_id

    print(f"Current index: {current_index_ph_stake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_ph_stake:
            current_index_ph_stake = 0
            first_time_loop_ph_stake = False
        else:
            current_index_ph_stake = int(query.data)
    elif query.data == "phantom_stake":
        # Reset current_index when "air_drop_01" is clicked
        current_index_ph_stake = 0
        first_time_loop_ph_stake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/stake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_ph_stake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_ph_stake = max(
        0, min(current_index_ph_stake, len(os.listdir(img_add)) - 1))


    # Define your list of captions here
    captions_list = [
        """در بخش نشان‌داده شده، مقدار موجودی سولانا (SOL) در کیف پول شما نمایش داده شده است.
روی آن کلیک کنید.
""",
"""برای استیک کردن سولانا، روی بخش مشخص شده کلیک کنید.""",
"""از میان گزینه‌های نمایش داده شده، Phantom Validator را انتخاب کنید.""",
"""
1️⃣ مقدار سولانای مورد نظر را برای استیک کردن انتخاب کنید.
2️⃣ روی گزینه Stake کلیک کنید.
""",
        """منتظر بمانید تا حساب استیک برای شما ایجاد شود.
⚠️⚠️⚠️ اگر با پیغام خطا مواجه شدید دوباره تلاش کنید.
""",
"""در این حالت سولانای ارسال شده با موفقیت استیک شده است.""",
"""اگر تمام مراحل را با موفقیت انجام داده باشید، در صحفه اول کیف پولتان، حساب استیک سولانا نمایش داده می‌شود. 
روی آن کلیک کنید.
""",
"""فعال‌شدن حساب شما کمی زمان می‌برد. """,
"""پس از اینکه حسابتان فعال شد، گزینه سبز رنگ Active برای شما نمایش داده می‌شود."""
        ]  

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_ph_stake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_ph_stake == 0:
        buttons = [
                [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_stake + 1))],
                [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="air_drop_phantom_menu_over")]
    ]
    elif current_index_ph_stake == len(os.listdir(img_add)) - 1:
        buttons = [
                [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_phantom_menu_over")],
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_stake - 1))]
    ]
    else:
        buttons = [
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_stake - 1)),
                InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_stake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

        # Store the message ID
        if chat_id not in message_ids:
            # initialize a list to store further information
            message_ids[chat_id] = []
        message_ids[chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(message_ids.get(chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
            message_ids[chat_id].pop(0)

    return PH_AIRDROP_STAKE


### << *** Phantom AirDrop - Unstake *** >>> ###

async def air_drop_phantom_unstake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    global current_index_ph_unstake, first_time_loop_ph_unstake
    global chat_id

    print(f"Current index: {current_index_ph_unstake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_ph_unstake:
            current_index_ph_unstake = 0
            first_time_loop_ph_unstake = False
        else:
            current_index_ph_unstake = int(query.data)
    elif query.data == "phantom_unstake":
        # Reset current_index when "air_drop_01" is clicked
        current_index_ph_unstake = 0
        first_time_loop_ph_unstake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/unstake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_ph_unstake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_ph_unstake = max(
        0, min(current_index_ph_unstake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
"""پس از فعال‌سازی حساب استیک سولانا، می‌توانید برای برداشت پولی که استیک کرده‌اید اقدام کنید. 
برای این منظور در بخش نشان‌داده شده، مقدار موجودی سولانا (SOL) در کیف پول شما نمایش داده شده است.
روی آن کلیک کنید.
""",
"""روی گزینه Unstake کلیک کنید.""",
"""در این حالت فرآیند غیرفعال‌سازی حساب استیک شما آغاز می‌شود.""",
"""پس از نمایش این صفحه، حساب استیک شما با موفقیت غیرفعال شده است.
روی گزینه Close کلیک کنید.
""",
        """در این حالت با ورود به حساب استیک سولانا، عبارت Deactivating نمایش داده می‌شود.
⚠️⚠️⚠️ دقت کنید این مرحله ممکن است تا چند روز طول بکشید.
""",
"""با نمایش واژه قرمز رنگ Inactive حساب استیک سولانا شما به صورت کامل غیرفعال شده است.
اکنون می‌توانید پول خود را برداشت کنید. 
روی آن کلیک کنید.
""",
"""روی گزینه Withdraw Stake کلیک کنید.""",
"""فرآیند برداشت پول شما آغاز شده است. 
⚠️⚠️⚠️ اگر با پیغام خطا مواجه شدید دوباره تلاش کنید.
""",
"""پول شما با موفقیت برداشت شد و به موجودی سولانا در کیف پولتان اضافه گردید. """
        ]  

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_ph_unstake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_ph_unstake == 0:
        buttons = [
                [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_unstake + 1))],
                [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="air_drop_phantom_menu_over")]
    ]
    elif current_index_ph_unstake == len(os.listdir(img_add)) - 1:
        buttons = [
                [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_phantom_menu_over")],
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_unstake - 1))]
    ]
    else:
        buttons = [
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_unstake - 1)),
                 InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_unstake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

        # Store the message ID
        if chat_id not in message_ids:
            # initialize a list to store further information
            message_ids[chat_id] = []
        message_ids[chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(message_ids.get(chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
            message_ids[chat_id].pop(0)

    return PH_AIRDROP_UNSTAKE


### <<<-------------------------------------------- Phantom AirDrop Sub-Menu -------------------------------------------->>> ###

async def air_drop_phantom_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    global chat_id

    # Delete the previous photo if it exists
    # Use.get() method to avoid KeyError if chat_id not found
    if len(message_ids.get(chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
        message_ids[chat_id].pop(0)

    global current_index_ph_swap, first_time_loop_ph_swap
    current_index_ph_swap = 0
    first_time_loop_ph_swap = True

    global current_index_ph_stake, first_time_loop_ph_stake
    current_index_ph_stake = 0
    first_time_loop_ph_stake = True

    global current_index_ph_unstake, first_time_loop_ph_unstake
    current_index_ph_unstake = 0
    first_time_loop_ph_unstake = True

    keyboard = [
        [InlineKeyboardButton("1. سواپ کردن (Swap) 💵🔄",
                              callback_data="phantom_swap")],
        [InlineKeyboardButton("2. استیک کردن (Stake) 💵💰",
                              callback_data="phantom_stake")],
        [InlineKeyboardButton("3. آن‌استیک کردن (Unstake) 💵🧾",
                              callback_data="phantom_unstake")],
        [InlineKeyboardButton(
            "بازگشت ⬅️", callback_data="back_to_air_drop_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """
<b>ایردراپ فانتوم (Phantom) </b>

🔄 نحوه فعالیت: 
هفتگی یا ماهیانه

💵 موجودی مورد نیاز:
30 تتر 

📰 وضعیت ایردراپ:
احتمالی

📅 تاریخ توزیع: 
نامشخص

📖 توضیحات:
برای شرکت در ایردراپ فانتوم، لطفاً موارد زیر را به ترتیب انجام دهید.
"""

    # Select an image to send
    # Replace with the actual path to your image
    image_filename = os.path.join('img', 'airdrop', 'phantom_wallet', 'phantom_wallet_img.jpg')

    # Send the image along with the text and buttons
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(image_filename, 'rb'),
        caption=text,
        reply_markup=key_markup,
        parse_mode="HTML"
    )

    return PH_AIRDROP


async def air_drop_phantom_menu_over(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    global chat_id

    # Delete the previous photo if it exists
    # Use.get() method to avoid KeyError if chat_id not found
    if len(message_ids.get(chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
        message_ids[chat_id].pop(0)

    return PH_AIRDROP



### <<<-------------------------------------------- Linea Surge AirDrop -------------------------------------------->>> ###

async def air_drop_linea_surge_stake(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    global current_index_linea_surge_stake, first_time_loop_linea_surge_stake, message_ids
    global chat_id

    print(f"Current index: {current_index_linea_surge_stake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_linea_surge_stake:
            current_index_linea_surge_stake = 0
            first_time_loop_linea_surge_stake = False
        else:
            current_index_linea_surge_stake = int(query.data)
    elif query.data == "linea_surge_stake":
        # Reset current_index when "air_drop_01" is clicked
        current_index_linea_surge_stake = 0
        first_time_loop_linea_surge_stake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/linea_surge/stake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_linea_surge_stake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_linea_surge_stake = max(
        0, min(current_index_linea_surge_stake, len(os.listdir(img_add)) - 1))
    

    # Define your list of captions here
    captions_list = [
        """با استفاده از این لینک وارد سایت SyncSwap شوید. 
1️⃣ روی گزینه Trade کلیک کنید.
2️⃣ در این بخش آدرس کیف پول نمایش داده می‌شود. 
⚠️⚠️⚠️ اگر گزینه Connect Wallet را می‌بینید، روی آن کلیک کنید تا کیف پولتان به سایت وصل شود.
3️⃣ روی این گزینه کلیک کنید. 
4️⃣ از منوی باز شده شبکه Linea را انتخاب کنید. 
""",
"""
1️⃣ توکن ETH را انتخاب کنید.
2️⃣ توکن weETH را انتخاب کنید.
3️⃣ مقدار اتریومی که می‌خواهید به weETH تبدیل کنید را وارد کنید. (عدد نوشته شده در کادر کوچک، معادل دلاری ETH را نشان می‌دهد.)
4️⃣ مقدار دریافتی برای شما نمایش داده می‌شود. (عدد نوشته شده در کادر کوچک، معادل دلاری weETH را نشان می‌دهد.)

5️⃣ عدد نوشته شده در کادر کوچک، میزان کارمزد معامله را نمایش می‌دهد.
اگر مقدار کارمزد نمایش داده شده در حد چند سنت است (در اینجا 3 سنت)، روی دکمه Swap کلیک کنید. 
""",
"""
1️⃣ مقدار کارمزد کل تراکنش را نمایش می‌دهد.
2️⃣ ارزش کل تراکنش (مقدار اتریومی که می‌خواهید تبدیل کنید + کارمزد تراکنش) را نمایش می‌دهد.
3️⃣ اگر مقدار کارمزد تراکنش کم است، روی دکمه Confirm کلیک کنید. 
""",
"""از نوار بالا روی Pool کلیک کنید و در منوی باز شده Pools را انتخاب کنید.""",
"""در کادر مشخص شده عبارت weeth را جستجو کنید و از میان نتایج به دست آمده استخر نقدینگی مربوط به ETH/weETH از نوع Classic را انتخاب کنید.""",
"""
1️⃣ روی گزینه Deposit کلیک کنید.
2️⃣ تیک مشخص شده را فعال کنید.
3️⃣ مقدار weETH که می‌خواهید واریز کنید را مشخص کنید. در این حالت بصورت خودکار، مقدار ETH معادل نیز در کادر پایین نمایش داده می‌شود.
4️⃣ روی دکمه Unlock weETH کلیک کنید. 
""",
"""
1️⃣ در این باید به سایت برای برداشت weETH دسترسی دهید. مقداری که در بخش 3 مرحله قبلی وارد کردید را وارد کنید. (برای اطمینان می‌توانید کمی بیشتر وارد کنید.) 
2️⃣ روی دکمه Next کلیک کنید.
""",
"""
1️⃣ کارمزد تراکنش نمایش داده شده است. 
2️⃣ اگر کارمزد کم است، روی دکمه Approve کلیک کنید.
""",
"""روی دکمه Deposit کلیک کنید. """,
        """
1️⃣ مقدار کارمزد کل تراکنش را نمایش می‌دهد.
2️⃣ ارزش کل تراکنش (ارزش دلاری توکن‌هایی که می‌خواهید واریز کنید + کارمزد تراکنش) را نمایش می‌دهد.
3️⃣ اگر مقدار کارمزد تراکنش کم است، روی دکمه Confirm کلیک کنید. 
"""
        ]  

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_linea_surge_stake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_linea_surge_stake == 0:
        buttons = [
                [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_linea_surge_stake + 1))],
                [InlineKeyboardButton("بازگشت به منوی ایردراپ لینیا 🏠⬅️ ", callback_data="air_drop_linea_surge_menu_over")]
    ]
    elif current_index_linea_surge_stake == len(os.listdir(img_add)) - 1:
        buttons = [
                [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_linea_surge_menu_over")],
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_linea_surge_stake - 1))]
    ]
    else:
        buttons = [
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_linea_surge_stake - 1)),
                 InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_linea_surge_stake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )
        
        # Store the message ID
        if chat_id not in message_ids:
            message_ids[chat_id] = []           # initialize a list to store further information
        message_ids[chat_id].append(sent_photo.message_id)
        
        # Delete the previous photo if it exists
        if len(message_ids.get(chat_id, [])) > 1:  # Use.get() method to avoid KeyError if chat_id not found
            await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
            message_ids[chat_id].pop(0)

    return LINEA_SURGE_AIRDROP_STAKE



### << *** Phantom AirDrop - Stake *** >>> ###

async def air_drop_linea_surge_unstake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    global current_index_linea_surge_unstake, first_time_loop_linea_surge_unstake
    global chat_id

    print(f"Current index: {current_index_linea_surge_unstake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_linea_surge_unstake:
            current_index_linea_surge_unstake = 0
            first_time_loop_linea_surge_unstake = False
        else:
            current_index_linea_surge_unstake = int(query.data)
    elif query.data == "linea_surge_unstake":
        # Reset current_index when "air_drop_01" is clicked
        current_index_linea_surge_unstake = 0
        first_time_loop_linea_surge_unstake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/linea_surge/unstake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_linea_surge_unstake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_linea_surge_unstake = max(
        0, min(current_index_linea_surge_unstake, len(os.listdir(img_add)) - 1))


    # Define your list of captions here
    captions_list = [
        """برای برداشت پول از سایت SyncSwap این مراحل را انجام دهید.
از نوار بالا روی گزینه Pool کلیک کنید و از منوی باز شده Positionsرا انتخاب کنید.
""",
"""در اینجا Position مشخص شده را انتخاب کنید.""",
"""
1️⃣ روی Withdraw کلیک کنید.
2️⃣ برای برداشت کل موجودی، روی Max کلیک کنید. (می‌توانید بصورت دستی، هر مقداری را وارد کنید.)
3️⃣ گزینه Balanced را انتخاب کنید.
""",
"""روی Unlock LP Token کلیک کنید.""",
"""
1️⃣ در این باید به سایت برای برداشت weETH دسترسی دهید. مقداری که در مرحله قبلی وارد کردید را مجدداً وارد کنید. (برای اطمینان می‌توانید کمی بیشتر وارد کنید.) 
2️⃣ روی Next کلیک کنید.
""",
"""
1️⃣ کارمزد تراکنش نمایش داده شده است.
2️⃣ روی Approve کلیک کنید.
""",
"""روی Withdraw Liquidity کلیک کنید.""",
"""
1️⃣ کارمزد تراکنش نمایش داده شده است.
2️⃣ روی Confirm کلیک کنید.
"""
        ]  

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_linea_surge_unstake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_linea_surge_unstake == 0:
        buttons = [
                [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_linea_surge_unstake + 1))],
                [InlineKeyboardButton("بازگشت به منوی ایردراپ لینیا 🏠⬅️ ", callback_data="air_drop_linea_surge_menu_over")]
    ]
    elif current_index_linea_surge_unstake == len(os.listdir(img_add)) - 1:
        buttons = [
                [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_linea_surge_menu_over")],
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_linea_surge_unstake - 1))]
    ]
    else:
        buttons = [
                [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_linea_surge_unstake - 1)),
                 InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_linea_surge_unstake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

        # Store the message ID
        if chat_id not in message_ids:
            # initialize a list to store further information
            message_ids[chat_id] = []
        message_ids[chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        
        # Use.get() method to avoid KeyError if chat_id not found
        if len(message_ids.get(chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
            message_ids[chat_id].pop(0)

    return LINEA_SURGE_AIRDROP_UNSTAKE


async def air_drop_linea_surge_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    global chat_id

    # Delete the previous photo if it exists
    if len(message_ids.get(chat_id, [])) == 1: # Use.get() method to avoid KeyError if chat_id not found
        await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
        message_ids[chat_id].pop(0)

    global current_index_linea_surge_stake, first_time_loop_linea_surge_stake
    current_index_linea_surge_stake = 0
    first_time_loop_linea_surge_stake = True

    global current_index_linea_surge_unstake, first_time_loop_linea_surge_unstake
    current_index_linea_surge_unstake = 0
    first_time_loop_linea_surge_unstake = True


    keyboard = [
        [InlineKeyboardButton("1. واریز کردن (Stake) 💵💰", callback_data="linea_surge_stake")],
        [InlineKeyboardButton("2. برداشت کردن (Unstake) 💵💰", callback_data="linea_surge_unstake")],
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="back_to_air_drop_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """
<b>ایردراپ فانتوم (Phantom) </b>

🔄 نحوه فعالیت: 
هفتگی یا ماهیانه

💵 موجودی مورد نیاز:
30 تتر 

📰 وضعیت ایردراپ:
احتمالی

📅 تاریخ توزیع: 
نامشخص

📖 توضیحات:
برای شرکت در ایردراپ فانتوم، لطفاً موارد زیر را به ترتیب انجام دهید.
"""

    # Select an image to send
    # Replace with the actual path to your image
    image_filename = os.path.join('img', 'airdrop', 'linea_surge', 'linea_surge.png')

    # Send the image along with the text and buttons
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(image_filename, 'rb'),
        caption=text,
        reply_markup=key_markup,
        parse_mode="HTML"
    )

    return LINEA_SURGE_AIRDROP


async def air_drop_linea_surge_menu_over(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    global chat_id

    # Delete the previous photo if it exists
    if len(message_ids.get(chat_id, [])) == 1: # Use.get() method to avoid KeyError if chat_id not found
        await context.bot.delete_message(chat_id=chat_id, message_id=message_ids[chat_id][0])
        message_ids[chat_id].pop(0)

    return LINEA_SURGE_AIRDROP

### <<<-------------------------------------------- Scroll AirDrop -------------------------------------------->>> ###

### <<<-------------------------------------------- Blast AirDrop -------------------------------------------->>> ###

### <<<-------------------------------------------- Sound AirDrop -------------------------------------------->>> ###

### <<<-------------------------------------------- Phaver AirDrop -------------------------------------------->>> ###

### <<<-------------------------------------------- Lens AirDrop -------------------------------------------->>> ###


async def air_drop_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    global current_index_ph_swap, first_time_loop_ph_swap
    current_index_ph_swap = 0
    first_time_loop_ph_swap = True

    global current_index_ph_stake, first_time_loop_ph_stake
    current_index_ph_stake = 0
    first_time_loop_ph_stake = True

    global current_index_ph_unstake, first_time_loop_ph_unstake
    current_index_ph_unstake = 0
    first_time_loop_ph_unstake = True

    keyboard = [
        [InlineKeyboardButton("ایردراپ فانتوم (Phantom)", callback_data="air_drop_phantom_menu"),
         InlineKeyboardButton("ایردراپ لینیا سرج (Linea Surge)", callback_data="air_drop_linea_surge_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """
لطفاً برای شرکت در هر ایردراپ، روی دکمه مورد نظر کلیک کنید.
توضیحات مربوط به نحوه شرکت در هر یک از ایردراپ‌ها برای شما نمایش داده خواهد شد.
"""

    if query.message and query.message.text:
        try:
            await query.edit_message_text(text=text, reply_markup=key_markup)
        except BadRequest:
            await query.message.reply_text(text=text, reply_markup=key_markup)
    else:
        await query.message.reply_text(text=text, reply_markup=key_markup)

    return START_ROUTES



### <<<------------------------------------------------------------------------------------------------------->>> ###
### <<<------------------------------------------------------------------------------------------------------->>> ###
### <<<-------------------------------------------- Main Function -------------------------------------------->>> ###
### <<<------------------------------------------------------------------------------------------------------->>> ###
### <<<------------------------------------------------------------------------------------------------------->>> ###

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(Tk).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(submit_email, pattern="^" + "submit_email" + "$"),
                CallbackQueryHandler(local_exchange, pattern="^" + "local_exchange" + "$"),
                CallbackQueryHandler(global_exchange, pattern="^" + "global_exchange" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$"),
                CallbackQueryHandler(air_drop_menu, pattern="^" + "air_drops" + "$"),
                CallbackQueryHandler(air_drop_phantom_menu, pattern="^" + "air_drop_phantom_menu" + "$"),
                CallbackQueryHandler(air_drop_linea_surge_menu, pattern="^" + "air_drop_linea_surge_menu" + "$")
            ],
            END_ROUTES: [
                CallbackQueryHandler(start_over, pattern="^" + "main_menu" + "$")
            ],
            SEND_IMG: [
                CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            ],
            PH_AIRDROP: [ 
                CallbackQueryHandler(air_drop_phantom_swap, pattern="^" + "phantom_swap" + "$"),
                CallbackQueryHandler(air_drop_phantom_stake, pattern="^" + "phantom_stake" + "$"),
                CallbackQueryHandler(air_drop_phantom_unstake, pattern="^" + "phantom_unstake" + "$"),
                CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            ],
            PH_AIRDROP_SWAP: [ 
                CallbackQueryHandler(air_drop_phantom_swap, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_phantom_menu_over, pattern="^" + "air_drop_phantom_menu_over" + "$")
            ],
            PH_AIRDROP_STAKE: [ 
                CallbackQueryHandler(air_drop_phantom_stake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_phantom_menu_over, pattern="^" + "air_drop_phantom_menu_over" + "$")
            ],
            PH_AIRDROP_UNSTAKE: [ 
                CallbackQueryHandler(air_drop_phantom_unstake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_phantom_menu_over, pattern="^" + "air_drop_phantom_menu_over" + "$")
            ],
            LINEA_SURGE_AIRDROP: [ 
                CallbackQueryHandler(air_drop_linea_surge_stake, pattern="^" + "linea_surge_stake" + "$"),
                CallbackQueryHandler(air_drop_linea_surge_unstake, pattern="^" + "linea_surge_unstake" + "$"),
                CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            ],
            LINEA_SURGE_AIRDROP_STAKE: [ 
                CallbackQueryHandler(air_drop_linea_surge_stake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_linea_surge_menu_over, pattern="^" + "air_drop_linea_surge_menu_over" + "$")
            ],
            LINEA_SURGE_AIRDROP_UNSTAKE: [ 
                CallbackQueryHandler(air_drop_linea_surge_unstake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_linea_surge_menu_over, pattern="^" + "air_drop_linea_surge_menu_over" + "$")
            ],
            EMAIL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_email)
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

### <<<------------------------------------------------------------------------------------------------------------>>> ###
### <<<------------------------------------------------------------------------------------------------------------>>> ###
### <<<-------------------------------------------- Initiation The Bot -------------------------------------------->>> ###
### <<<------------------------------------------------------------------------------------------------------------>>> ###
### <<<------------------------------------------------------------------------------------------------------------>>> ###

# Load the email_ids dictionary when the bot starts
data_base = load_data_base()

print('Starting up bot...')

Tk = config('token')

if __name__ == "__main__":
    main()
