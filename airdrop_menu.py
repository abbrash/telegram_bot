from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals import GlobalState

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
