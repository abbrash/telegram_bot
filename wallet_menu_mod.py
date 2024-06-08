from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals_mod import GlobalState


async def wallet_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("کیف پول متامسک (MetaMask)", callback_data="metamask_menu")],
        [InlineKeyboardButton("کیف پول فانتوم (Phantom)", callback_data="phantom_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = "لطفاً برای دسترسی به آموزش ساخت کیف پول‌های مختلف، روی گزینه مورد نظر کلیک کنید:"

    # await query.edit_message_text(
    #     text=text,
    #     reply_markup=key_markup
    # )
    # return GlobalState.getInstance().WALLET

    if query.message and query.message.text:
        try:
            await query.edit_message_text(text=text, reply_markup=key_markup)
        except BadRequest:
            await query.message.reply_text(text=text, reply_markup=key_markup)
    else:
        await query.message.reply_text(text=text, reply_markup=key_markup)

    chat_id = GlobalState.getInstance().mess_id_prev.keys()
    message_id = GlobalState.getInstance().mess_id_prev[chat_id]
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)


    return GlobalState.getInstance().WALLET
