from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals_mod import GlobalState

from admins_mod import *

### <<<-------------------------------------------- Airdrops Menu -------------------------------------------->>> ###
async def airdrops_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    GlobalState.getInstance().current_index_phantom_swap = 0
    GlobalState.getInstance().first_time_loop_phantom_swap = True

    GlobalState.getInstance().current_index_phantom_stake = 0
    GlobalState.getInstance().first_time_loop_phantom_stake = True

    GlobalState.getInstance().current_index_phantom_unstake = 0
    GlobalState.getInstance().first_time_loop_phantom_unstake = True

    GlobalState.getInstance().current_index_linea_surge_stake = 0
    GlobalState.getInstance().first_time_loop_linea_surge_stake = True

    GlobalState.getInstance().current_index_linea_surge_unstake = 0
    GlobalState.getInstance().first_time_loop_linea_surge_unstake = True

    GlobalState.getInstance().current_index_wallet_metamask_create = 0
    GlobalState.getInstance().first_time_loop_wallet_metamask_create = True

    keyboard = [
        [InlineKeyboardButton("ایردراپ فانتوم (Phantom)", callback_data="airdrop_phantom_menu"),
         InlineKeyboardButton("ایردراپ لینیا سرج (Linea Surge)", callback_data="airdrop_linea_surge_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """
لطفاً برای شرکت در هر ایردراپ، روی دکمه مورد نظر کلیک کنید.
توضیحات مربوط به نحوه شرکت در هر یک از ایردراپ‌ها برای شما نمایش داده خواهد شد.
"""

    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text, 
                                           reply_markup=key_markup, 
                                           protect_content=protect_content
                                           )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text, 
                                           reply_markup=key_markup, 
                                           protect_content=protect_content
                                           )

    else:
        await query.delete_message()
        await context.bot.send_message(chat_id=update._effective_user.id,
                                       text=text, 
                                       reply_markup=key_markup, 
                                       protect_content=protect_content
                                       )

    return GlobalState.getInstance().AIRDROPS_MENU