from datetime import datetime
import pandas as pd
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals_mod import GlobalState
from database_mod import *
from airdrops_menu_mod import * 

### <<<-------------------------------------------- Log Errors -------------------------------------------->>> ###
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

### <<<-------------------------------------------- Start -------------------------------------------->>> ###
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    tel_user_id = update.effective_user.id
    if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
        tel_user_name = GlobalState.getInstance().data_base[GlobalState.getInstance(
        ).data_base['tel_user_id'] == tel_user_id]['tel_user_name'].values[0]
        text = f"{tel_user_name} " + "👋🏻🥰 !سلام دوست من"
        keyboard = [
            [InlineKeyboardButton("صرافی‌های پیشنهادی 💱🌐🇮🇷", callback_data="exchanges_menu")],
            [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="airdrops_menu")],
            [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallets_menu")],
            [InlineKeyboardButton("پشتیبانی 📞", callback_data="support_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        keyboard = [[InlineKeyboardButton("ثبت نام", callback_data="submit_email")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "به کانال کریپتیک خوش آمدید:"

    if update.message:
        await update.message.reply_text(text=text, reply_markup=reply_markup)

    return GlobalState.getInstance().START_ROUTES

### <<<-------------------------------------------- Start Over -------------------------------------------->>> ###
async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    await query.answer()
    tel_user_id = update.effective_user.id

    if tel_user_id in GlobalState.getInstance().data_base['tel_user_id'].values:
        keyboard = [
                [InlineKeyboardButton("صرافی‌های پیشنهادی 💱🌐🇮🇷", callback_data="exchanges_menu")],
                [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="airdrops_menu")],
                [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallets_menu")],
                [InlineKeyboardButton("پشتیبانی 📞", callback_data="support_menu")]
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
    try:
        # Try to edit the message text
        await query.edit_message_text(text=text, reply_markup=reply_markup)
    except BadRequest:
        # If the message doesn't have text content, send a new message
        await query.message.reply_text(text=text, reply_markup=reply_markup)

    return GlobalState.getInstance().START_ROUTES


### <<<-------------------------------------------- Main Menu -------------------------------------------->>> ###
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

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
    
