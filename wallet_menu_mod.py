from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from globals import GlobalState


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

    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().WALLET
