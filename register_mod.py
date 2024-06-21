from datetime import datetime
import pandas as pd
from telegram import Update
from telegram.ext import ContextTypes

from globals_mod import GlobalState
from database_mod import *
from airdrops_menu_mod import *
from main_menu_mod import *
from admins_mod import *

async def confirm_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # global data_base

    protect_content = not is_admin(update._effective_user.id)

    message_text = update.effective_message.text.lower()

    if update.effective_user.name:
        tel_user_name = update.effective_user.name
    else:
        tel_user_name = "no_tel_user_name"

    print('email confirming is executed')

    if is_email(message_text):
        if message_text in GlobalState.getInstance().data_base['email_id'].values:
            text = "آدرس ایمیل وارد شده توسط شخص دیگری ثبت شده است، لطفاً آدرس ایمیل خودتان را وارد کنید:"
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           protect_content=protect_content
                                           )
        else:
            ch_user_id = gen_uniq_channel_id(
                GlobalState.getInstance().data_base['ch_user_id'].values)
            new_user = {
                'ch_user_id': ch_user_id,
                'tel_user_name': tel_user_name,
                'tel_user_id': update._effective_user.id,
                'email_id': message_text,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            new_user = pd.DataFrame([new_user])

            # Update email data DataFrame
            GlobalState.getInstance().data_base = pd.concat(
                [GlobalState.getInstance().data_base, new_user], ignore_index=True)
            save_email_data(GlobalState.getInstance().data_base)

            # Show the main menu instead of sending a message
            return await main_menu(update, context)
    else:
        text = "آدرس ایمیل وارد شده نادرست است، لطفاً دوباره تلاش کنید:"
        await context.bot.send_message(chat_id=update._effective_user.id,
                                       text=text, 
                                       protect_content=protect_content
                                       )


async def submit_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    text = """لطفاً آدرس ایمیل خود را وارد ارسال کنید:"""
    await query.edit_message_text(text=text)
    return GlobalState.getInstance().EMAIL
