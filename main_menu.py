from datetime import datetime
import pandas as pd
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals import GlobalState
from database import *

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    tel_user_id = update.effective_user.id

    if tel_user_id in data_base['tel_user_id'].values:
        tel_user_name = data_base[data_base['tel_user_id']
                                  == tel_user_id]['tel_user_name'].values[0]
        print_txt = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"

        keyboard = [
            [InlineKeyboardButton("صرافی‌های ایرانی  💱🇮🇷",
                                  callback_data="local_exchange")],
            [InlineKeyboardButton("صرافی‌های خارجی 💱🌐",
                                  callback_data="global_exchange")],
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
        GlobalState.getInstance().current_index_ph_swap = 0
        await query.answer()
        await query.edit_message_text(text=print_txt, reply_markup=reply_markup)

    return GlobalState.getInstance().START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    await query.answer()

    tel_user_id = update.effective_user.id

    if tel_user_id in data_base['tel_user_id'].values:
        tel_user_name = data_base[data_base['tel_user_id']
                                  == tel_user_id]['tel_user_name'].values[0]
        print_txt = f"Stay with us, {tel_user_name}"

        keyboard = [
            [InlineKeyboardButton("صرافی‌های ایرانی  💱🇮🇷",
                                  callback_data="local_exchange")],
            [InlineKeyboardButton("صرافی‌های خارجی 💱🌐",
                                  callback_data="global_exchange")],
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

    return GlobalState.getInstance().START_ROUTES


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
    return GlobalState.getInstance().EMAIL


async def local_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ",
                              url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton("صرافی بیت‌پین (BitPin)",
                              url='https://bitpin.ir/signup/?ref=aP0DtoVG')],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ",
                              callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().START_ROUTES


async def global_exchange(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("صرافی بینک‌اکس (BingX)",
                              url='https://bingx.com/invite/NLQIKZI2')],
        [InlineKeyboardButton(
            "صرافی کوینکس (CoinEx)", url='https://www.coinex.com/register?refer_code=s95m7')],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ",
                              callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().START_ROUTES


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
        return GlobalState.getInstance().END_ROUTES



async def air_drop_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    GlobalState.getInstance().current_index_ph_swap = 0
    GlobalState.getInstance().first_time_loop_ph_swap = True

    GlobalState.getInstance().current_index_ph_stake = 0
    GlobalState.getInstance().first_time_loop_ph_stake = True

    GlobalState.getInstance().current_index_ph_unstake = 0
    GlobalState.getInstance().first_time_loop_ph_unstake = True

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

    return GlobalState.getInstance().START_ROUTES
