from datetime import datetime
import pandas as pd
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals import GlobalState
from database import *
from airdrop_menu import * 

# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

#     tel_user_id = update.effective_user.id

#     if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
#         tel_user_name = GlobalState.getInstance().data_base[GlobalState.getInstance().data_base['tel_user_id']
#                                   == tel_user_id]['tel_user_name'].values[0]
#         print_txt = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"

#         keyboard = [
#             [InlineKeyboardButton("صرافی‌های ایرانی  💱🇮🇷", callback_data="local_exchange")],
#             [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
#             [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
#             [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#     else:
#         keyboard = [
#             [InlineKeyboardButton("ثبت نام", callback_data="submit_email")]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         print_txt = "به کانال کریپتیک خوش آمدید:"

#     if update.message:
#         await update.message.reply_text(text=print_txt, reply_markup=reply_markup)
#     elif update.callback_query:
#         query = update.callback_query
#         GlobalState.getInstance().current_index_ph_swap = 0
#         await query.answer()
#         await query.edit_message_text(text=print_txt, reply_markup=reply_markup)

#     return GlobalState.getInstance().START_ROUTES


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    tel_user_id = update.effective_user.id
    if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
        tel_user_name = GlobalState.getInstance().data_base[GlobalState.getInstance(
        ).data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
        text = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"
        keyboard = [
            [InlineKeyboardButton("صرافی‌های ایرانی 💱🇮🇷", callback_data="local_exchange")],
            [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
            [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
            [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [[InlineKeyboardButton("ثبت نام", callback_data="submit_email")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "به کانال کریپتیک خوش آمدید:"

    if update.message:
        await update.message.reply_text(text=text, reply_markup=reply_markup)

    # if update.message:
    #     sent_message = await update.message.reply_text(text=print_txt, reply_markup=reply_markup)
    #     GlobalState.getInstance().mess_id_prev[tel_user_id] = sent_message.message_id   # added line

    # elif update.callback_query:
    #     query = update.callback_query
    #     # GlobalState.getInstance().current_index_ph_swap = 0
    #     await query.answer()
    #     # sent_message = await query.edit_message_text(text=print_txt, reply_markup=reply_markup) 
    #     # await query.message.delete()
    #     await query.delete_message()
    #     sent_message = await query.message.reply_text(text=print_txt, reply_markup=reply_markup)
    #     GlobalState.getInstance().mess_id_prev[tel_user_id] = sent_message.message_id   # added line

    return GlobalState.getInstance().START_ROUTES




# async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Prompt same text & keyboard as `start` does but not as new message"""
#     query = update.callback_query
#     await query.answer()

#     tel_user_id = update.effective_user.id

#     if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
#         tel_user_name = GlobalState.getInstance().data_base[GlobalState.getInstance().data_base['tel_user_id']
#                                   == tel_user_id]['tel_user_name'].values[0]
#         print_txt = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"

#         keyboard = [
#             [InlineKeyboardButton("صرافی‌های ایرانی  💱🇮🇷", callback_data="local_exchange")],
#             [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
#             [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
#             [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#     else:
#         keyboard = [
#             [InlineKeyboardButton("ثبت نام", callback_data="submit_email")]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         print_txt = "به کانال کریپتیک خوش آمدید:"

#     try:
#         # Try to edit the message text
#         await query.edit_message_text(text=print_txt, reply_markup=reply_markup)
#     except BadRequest:
#         # If the message doesn't have text content, send a new message
#         await query.message.reply_text(text=print_txt, reply_markup=reply_markup)

#     return GlobalState.getInstance().START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    await query.answer()
    tel_user_id = update.effective_user.id

    # if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
    #     tel_user_name = GlobalState.getInstance().data_base[GlobalState.getInstance(
    #     ).data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
    #     print_txt = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"
    #     keyboard = [
    #         [InlineKeyboardButton("صرافی‌های ایرانی 💱🇮🇷", callback_data="local_exchange")],
    #         [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
    #         [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
    #         [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
    #     ]
    #     reply_markup = InlineKeyboardMarkup(keyboard)
    # else:
    #     keyboard = [[InlineKeyboardButton("ثبت نام", callback_data="submit_email")]]
    #     reply_markup = InlineKeyboardMarkup(keyboard)
    #     print_txt = "به کانال کریپتیک خوش آمدید:"

    # try:
    #     # Try to edit the message text
    #     sent_message = await query.edit_message_text(text=print_txt, reply_markup=reply_markup)
    #     GlobalState.getInstance().mess_id_prev[tel_user_id] = sent_message.message_id
    # except BadRequest:
    #     # If the message doesn't have text content, send a new message
    #     sent_message = await query.message.reply_text(text=print_txt, reply_markup=reply_markup)
    #     GlobalState.getInstance().mess_id_prev[tel_user_id] = sent_message.message_id

    if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
        keyboard = [
                [InlineKeyboardButton("صرافی‌های ایرانی 💱🇮🇷", callback_data="local_exchange")],
                [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
                [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
                [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
            ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        tel_user_name = GlobalState.getInstance().data_base[GlobalState.getInstance(
            ).data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]

        text = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"

    else:
        keyboard = [[InlineKeyboardButton("ثبت نام", callback_data="submit_email")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "به کانال کریپتیک خوش آمدید:"


    if update.message:
        await update.message.reply_text(text=text, reply_markup=reply_markup)
        print("start over: update.message.reply_text")
    try:
        # Try to edit the message text
        await query.edit_message_text(text=text, reply_markup=reply_markup)
        print("start over: query.edit_message_text")
    except BadRequest:
        # If the message doesn't have text content, send a new message
        await query.message.reply_text(text=text, reply_markup=reply_markup)
        print("start over: query.message.reply_text")

    return GlobalState.getInstance().START_ROUTES

    

# async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

#     if update.message:
#         # Handle text messages
#         return await start(update, context)
#     elif update.callback_query:
#         # Handle callback queries
#         query = update.callback_query
#         await query.answer()
#         return await start_over(update, context)
#     else:
#         # Handle other update types (not expected)
#         return GlobalState.getInstance().END_ROUTES

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    # tel_user_id = update.effective_user.id
    # if update.message:
    #     # Handle text messages
    #     sent_message = await start(update, context)
    #     GlobalState.getInstance().mess_id_prev[tel_user_id] = sent_message.message_id
    #     return sent_message
    # elif update.callback_query:
    #     # Handle callback queries
    #     query = update.callback_query
    #     await query.answer()
    #     sent_message = await start_over(update, context)
    #     GlobalState.getInstance().mess_id_prev[tel_user_id] = sent_message.message_id
    #     return sent_message
    # else:
    #     # Handle other update types (not expected)
    #     return GlobalState.getInstance().END_ROUTES
    
    if update.message:
        # Handle text messages
        await start(update, context)
    elif update.callback_query:
        # Handle callback queries
        query = update.callback_query
        await query.answer()
        await start_over(update, context)
    else:
        # Handle other update types (not expected)
        return GlobalState.getInstance().END_ROUTES
    
