from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from globals import GlobalState


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
    return GlobalState.getInstance().START_ROUTES


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
    return GlobalState.getInstance().START_ROUTES
