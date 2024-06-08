from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from globals_mod import GlobalState


### <<<-------------------------------------------- Exchanges Menu -------------------------------------------->>> ###
async def exchanges_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ", callback_data="exchange_nobitex_menu")],
        [InlineKeyboardButton("صرافی بیت‌پین (BitPin)", callback_data="exchange_bitpin_menu")],
        [InlineKeyboardButton("صرافی بینگ‌اکس (BingX)", callback_data="exchange_bingx_menu")],
        [InlineKeyboardButton("صرافی کوینکس (CoinEx)", callback_data="exchange_coinex_menu")],
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
    return GlobalState.getInstance().EXCHANGES_MENU


### <<<-------------------------------------------- Nobitex Exchange Menu -------------------------------------------->>> ###
async def exchange_nobitex_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("آموزش ثبت نام", callback_data="exchange_nobitex_reg_tutorial")],
        [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ", url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().EXCHANGE_NOBITEX_MENU

### <<<-------------------------------------------- BitPin Exchange Menu -------------------------------------------->>> ###
async def exchange_bitpin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("آموزش ثبت نام", callback_data="exchange_bitpin_reg_tutorial")],
        [InlineKeyboardButton("صرافی بیت‌پین (BitPin)", url='https://bitpin.ir/signup/?ref=aP0DtoVG')],
        [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().EXCHANGE_BITPIN_MENU

### <<<-------------------------------------------- BingX Exchange Menu -------------------------------------------->>> ###
async def exchange_bingx_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("آموزش ثبت نام", callback_data="exchange_bingx_reg_tutorial")],
        [InlineKeyboardButton("صرافی بینک‌اکس (BingX)", url='https://bingx.com/invite/NLQIKZI2')],
        [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().EXCHANGE_BINGX_MENU

### <<<-------------------------------------------- Coinex Exchange Menu -------------------------------------------->>> ###
async def exchange_coinex_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("آموزش ثبت نام", callback_data="exchange_nobitex_reg_tutorial")],
        [InlineKeyboardButton("صرافی کوینکس (CoinEx)", url='https://www.coinex.com/register?refer_code=s95m7')],
        [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
"""
    await query.edit_message_text(
        text=text,
        reply_markup=key_markup
    )
    return GlobalState.getInstance().EXCHANGE_COINEX_MENU


### <<<-------------------------------------------- Nobitex Exchange Register Tutorial -------------------------------------------->>> ###
# async def exchange_nobitex_reg_tutorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()

#     keyboard = [
#         [InlineKeyboardButton(
#             "آموزش ثبت نام", callback_data="exchange_nobitex_reg_tutorial")],
#         [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ",
#                               url='https://nobitex.ir/signup/?refcode=1557073')],
#         [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
#     ]
#     key_markup = InlineKeyboardMarkup(keyboard)
#     text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
# آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
# """
#     await query.edit_message_text(
#         text=text,
#         reply_markup=key_markup
#     )
#     return GlobalState.getInstance().EXCHANGE_NOBITEX_MENU


### <<<-------------------------------------------- BitPin Exchange Register Tutorial -------------------------------------------->>> ###
# async def exchange_bitpin_reg_tutorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()

#     keyboard = [
#         [InlineKeyboardButton(
#             "آموزش ثبت نام", callback_data="exchange_nobitex_reg_tutorial")],
#         [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ",
#                               url='https://nobitex.ir/signup/?refcode=1557073')],
#         [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
#     ]
#     key_markup = InlineKeyboardMarkup(keyboard)
#     text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید.
# آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
# """
#     await query.edit_message_text(
#         text=text,
#         reply_markup=key_markup
#     )
#     return GlobalState.getInstance().EXCHANGE_NOBITEX_MENU


### <<<-------------------------------------------- BingX Exchange Register Tutorial -------------------------------------------->>> ###
# async def exchange_bingx_reg_tutorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()

#     keyboard = [
#         [InlineKeyboardButton(
#             "آموزش ثبت نام", callback_data="exchange_nobitex_reg_tutorial")],
#         [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ",
#                               url='https://nobitex.ir/signup/?refcode=1557073')],
#         [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
#     ]
#     key_markup = InlineKeyboardMarkup(keyboard)
#     text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید.
# آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
# """
#     await query.edit_message_text(
#         text=text,
#         reply_markup=key_markup
#     )
#     return GlobalState.getInstance().EXCHANGE_NOBITEX_MENU


### <<<-------------------------------------------- CoinEx Exchange Register Tutorial -------------------------------------------->>> ###
# async def exchange_coinex_reg_tutorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()

#     keyboard = [
#         [InlineKeyboardButton(
#             "آموزش ثبت نام", callback_data="exchange_nobitex_reg_tutorial")],
#         [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ",
#                               url='https://nobitex.ir/signup/?refcode=1557073')],
#         [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
#     ]
#     key_markup = InlineKeyboardMarkup(keyboard)
#     text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید.
# آموزش ثبت‌نام در هر یک از صرافی‌ها به زودی بارگذاری خواهد شد.
# """
#     await query.edit_message_text(
#         text=text,
#         reply_markup=key_markup
#     )
#     return GlobalState.getInstance().EXCHANGE_NOBITEX_MENU
