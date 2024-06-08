from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals_mod import GlobalState

### <<<-------------------------------------------- Wallets Menu -------------------------------------------->>> ###
async def wallets_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("کیف پول متامسک (MetaMask)", callback_data="wallet_metamask_menu")],
        [InlineKeyboardButton("کیف پول فانتوم (Phantom)", callback_data="wallet_phantom_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = "لطفاً برای دسترسی به آموزش ساخت کیف پول‌های مختلف، روی گزینه مورد نظر کلیک کنید:"

    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_message(chat_id=update._effective_user.id, text=text, reply_markup=key_markup)

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id, text=text, reply_markup=key_markup)

    else:
        await query.delete_message()
        await context.bot.send_message(chat_id=update._effective_user.id, text=text, reply_markup=key_markup)

    return GlobalState.getInstance().WALLETS_MENU
