from telegram.ext import ContextTypes, ConversationHandler, filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler
import random
import time
from admins_mod import admin_dict, is_admin, get_admin_name
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.error import BadRequest

from globals_mod import GlobalState

from admins_mod import *

admin_ids = [107998330, 1108290862]

### <<<-------------------------------------------- Support Menu -------------------------------------------->>> ###
# async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     protect_content = not is_admin(update._effective_user.id)

#     keyboard = [
#         [InlineKeyboardButton("ارسال", callback_data="support")],
#         [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
#     ]
#     key_markup = InlineKeyboardMarkup(keyboard)

#     text = """asda"""

#     if query.message and query.message.text:
#         try:
#             await query.delete_message()
#             await context.bot.send_message(chat_id=update._effective_user.id, 
#                                            text=text, 
#                                            reply_markup=key_markup,
#                                            protect_content=protect_content
#                                            )

#         except BadRequest:
#             await context.bot.send_message(chat_id=update._effective_user.id, 
#                                            text=text, 
#                                            reply_markup=key_markup,
#                                            protect_content=protect_content
#                                            )

#     else:
#         await query.delete_message()
#         await context.bot.send_message(chat_id=update._effective_user.id, 
#                                        text=text, 
#                                        reply_markup=key_markup,
#                                        protect_content=protect_content
#                                        )

#     return GlobalState.getInstance().SUPPORT_MENU


####################################################################################################

# async def support_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     await query.edit_message_text(
#         "Please send your message or photo. Our admins will review it. You can use /cancel at any time to cancel this request.")
#     # Set a conversation state to handle the next message
#     return GlobalState.getInstance().AWAITING_SUPPORT_MESSAGE


# async def handle_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.effective_user
#     message = update.message

#     keyboard = [
#         [InlineKeyboardButton("Accept", callback_data=f'accept_{user.id}'),
#          InlineKeyboardButton("Reject", callback_data=f'reject_{user.id}')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     for admin_id in admin_ids:
#         if message.photo:
#             await context.bot.send_photo(chat_id=admin_id, photo=message.photo[-1].file_id,
#                                          caption=f"Support request from {user.first_name} (ID: {user.id}):",
#                                          reply_markup=reply_markup)
#         else:
#             await context.bot.send_message(chat_id=admin_id, text=f"Support request from {user.first_name} (ID: {user.id}):\n\n{message.text}",
#                                            reply_markup=reply_markup)

#     await update.message.reply_text(
#         "Your message has been sent to our admins. Please wait for their response.")
#     return ConversationHandler.END


# async def admin_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     data = query.data.split('_')
#     action, user_id = data[0], int(data[1])

#     if action == 'accept':
#         await query.edit_message_text(
#             f"You've accepted the request from user {user_id}. Reply to this message to respond.")
#         context.user_data['reply_to_user'] = user_id
#         return GlobalState.getInstance().AWAITING_ADMIN_REPLY
#     else:  # reject
#         await query.edit_message_text(
#             f"You've rejected the request from user {user_id}.")
#         await context.bot.send_message(
#             chat_id=user_id, text="Sorry, your request has been rejected.")
#         return ConversationHandler.END


# async def handle_admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = context.user_data.get('reply_to_user')
#     if user_id:
#         await context.bot.send_message(
#             chat_id=user_id, text=f"Admin's response: {update.message.text}")
#         del context.user_data['reply_to_user']
#     return ConversationHandler.END


# async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = update.effective_user
#     await update.message.reply_text(
#         f"Conversation cancelled by {user.first_name}. You can start a new conversation or return to the main menu."
#     )
#     return ConversationHandler.END

# conv_handler = ConversationHandler(
#     entry_points=[CallbackQueryHandler(support_callback, pattern='^support$')],
#     states={
#         AWAITING_SUPPORT_MESSAGE: [MessageHandler(Filters.text | Filters.photo, handle_support_message)],
#         AWAITING_ADMIN_REPLY: [MessageHandler(
#             Filters.text & ~Filters.command, handle_admin_reply)]
#     },
#     fallbacks=[CommandHandler('cancel', cancel)]
# )

# dispatcher.add_handler(conv_handler)
# dispatcher.add_handler(CallbackQueryHandler(
#     admin_response, pattern='^(accept|reject)_'))


# Import your GlobalState and other necessary modules


async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update.effective_user.id)

    keyboard = [
        [InlineKeyboardButton("ارسال", callback_data="support")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠",
                              callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """asda"""

    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_message(chat_id=update.effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content)
        except BadRequest:
            await context.bot.send_message(chat_id=update.effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content)
    else:
        await query.delete_message()
        await context.bot.send_message(chat_id=update.effective_user.id,
                                       text=text,
                                       reply_markup=key_markup,
                                       protect_content=protect_content)

    return GlobalState.getInstance().SUPPORT_MENU


async def support_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "Please send your message or photo. Our admins will review it. You can use /cancel at any time to cancel this request.")
    return GlobalState.getInstance().AWAITING_SUPPORT_MESSAGE


async def handle_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    message = update.message

    keyboard = [
        [InlineKeyboardButton("Accept", callback_data=f'accept_{user.id}'),
         InlineKeyboardButton("Reject", callback_data=f'reject_{user.id}')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    for admin_id in admin_ids:  # Make sure admin_ids is defined
        if message.photo:
            await context.bot.send_photo(chat_id=admin_id, photo=message.photo[-1].file_id,
                                         caption=f"Support request from {user.first_name} (ID: {user.id}):",
                                         reply_markup=reply_markup)
        else:
            await context.bot.send_message(chat_id=admin_id, text=f"Support request from {user.first_name} (ID: {user.id}):\n\n{message.text}",
                                           reply_markup=reply_markup)

    await update.message.reply_text(
        "Your message has been sent to our admins. Please wait for their response.")
    return ConversationHandler.END


async def admin_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    data = query.data.split('_')
    action, user_id = data[0], int(data[1])

    if action == 'accept':
        await query.edit_message_text(
            f"You've accepted the request from user {user_id}. Reply to this message to respond.")
        context.user_data['reply_to_user'] = user_id
        return GlobalState.getInstance().AWAITING_ADMIN_REPLY
    else:  # reject
        await query.edit_message_text(
            f"You've rejected the request from user {user_id}.")
        await context.bot.send_message(
            chat_id=user_id, text="Sorry, your request has been rejected.")
        return ConversationHandler.END


async def handle_admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = context.user_data.get('reply_to_user')
    if user_id:
        await context.bot.send_message(
            chat_id=user_id, text=f"Admin's response: {update.message.text}")
        del context.user_data['reply_to_user']
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    await update.message.reply_text(
        f"Conversation cancelled by {user.first_name}. You can start a new conversation or return to the main menu."
    )
    return ConversationHandler.END
