import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals_mod import GlobalState
from admins_mod import *

### <<<-------------------------------------------- Wallets Menu -------------------------------------------->>> ###
async def wallets_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        [InlineKeyboardButton("کیف پول متامسک (MetaMask)", callback_data="wallet_metamask_menu")],
        [InlineKeyboardButton("کیف پول فانتوم (Phantom)", callback_data="wallet_phantom_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """برای شرکت در ایردراپ‌های مختلف به کیف پول‌ غیرحضانتی نیاز دارید. در این بخش آموزش ساخت و کار با تعدادی از کیف‌ پول‌های پرکاربرد آورده شده است. 
لطفاً برای دسترسی به آموزش ساخت کیف پول‌های مختلف، روی گزینه مورد نظر کلیک کنید.
"""

    # if query.message and query.message.text:
    #     try:
    #         await query.delete_message()
    #         await context.bot.send_message(chat_id=update._effective_user.id,
    #                                        text=text, 
    #                                        reply_markup=key_markup, 
    #                                        protect_content=protect_content
    #                                        )

    #     except BadRequest:
    #         await context.bot.send_message(chat_id=update._effective_user.id,
    #                                        text=text, 
    #                                        reply_markup=key_markup, 
    #                                        protect_content=protect_content
    #                                        )

    # else:
    #     await query.delete_message()
    #     await context.bot.send_message(chat_id=update._effective_user.id,
    #                                    text=text, 
    #                                    reply_markup=key_markup, 
    #                                    protect_content=protect_content
    #                                    )

    # Select an image to send
    image_filename = os.path.join('img', 'wallet', 'wallets_img.jpg').replace('\\', '/')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update._effective_user.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML",
                protect_content=protect_content
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content
                                           )

    else:
        await context.bot.send_photo(
            chat_id=update._effective_user.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML",
            protect_content=protect_content
        )

    return GlobalState.getInstance().WALLETS_MENU
