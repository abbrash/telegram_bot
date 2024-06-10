from telegram.ext import ContextTypes, ConversationHandler, filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import datetime
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
async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        # [InlineKeyboardButton("ارسال", callback_data="support")],
        [InlineKeyboardButton("Collect Messages", callback_data="collect_messages")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """asda"""

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

    return GlobalState.getInstance().SUPPORT_MENU


async def support_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "Please send your message or photo. Our admins will review it. You can use /cancel at any time to cancel this request.")
    return GlobalState.getInstance().AWAITING_SUPPORT_MESSAGE

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

async def admin_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    print('admins_response executed!')

    data = query.data.split('_')
    print(f"query.data: {query.data}")
    action, user_id = data[0], int(data[1])

    support_data = context.bot_data.get(f'support_message_{user_id}', {})
    print(f"context.bot_data: {context.bot_data}")
    admin_messages = support_data.get('admin_messages', {})
    user_message = support_data.get('user_message', 'Unknown message')

    if action == 'accept':
        # Notify the handling admin
        await query.edit_message_text(
            f"You've accepted the request from user {user_id}.\n\nOriginal message: {user_message}\n\nReply to this message to respond."
        )

        # Notify other admins and delete their messages
        for admin_id, msg_id in admin_messages.items():
            if admin_id != update.effective_user.id:
                try:
                    # Delete the original message
                    await context.bot.delete_message(chat_id=admin_id, message_id=msg_id)

                    # Send a new notification
                    await context.bot.send_message(
                        chat_id=admin_id,
                        text=f"Support request from user {user_id} is being handled by {update.effective_user.first_name}."
                    )
                except BadRequest as e:
                    print(
                        f"Failed to handle message for admin {admin_id}: {e}")

        context.user_data['reply_to_user'] = user_id
        return GlobalState.getInstance().AWAITING_ADMIN_REPLY
    else:  # reject
        await query.edit_message_text(
            f"You've rejected the request from user {user_id}."
        )

        # Notify other admins and delete their messages
        for admin_id, msg_id in admin_messages.items():
            if admin_id != update.effective_user.id:
                try:
                    # Delete the original message
                    await context.bot.delete_message(chat_id=admin_id, message_id=msg_id)

                    # Send a new notification
                    await context.bot.send_message(
                        chat_id=admin_id,
                        text=f"Support request from user {user_id} has been rejected by {update.effective_user.first_name}."
                    )
                except BadRequest as e:
                    print(
                        f"Failed to handle message for admin {admin_id}: {e}")

        await context.bot.send_message(
            chat_id=user_id, text="Sorry, your request has been rejected."
        )
        return ConversationHandler.END

# async def handle_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user = update.effective_user
#     message = update.message

#     keyboard = [
#         [InlineKeyboardButton("Accept", callback_data=f'accept_{user.id}'),
#          InlineKeyboardButton("Reject", callback_data=f'reject_{user.id}')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     # Store message details in bot_data
#     context.bot_data[f'support_message_{user.id}'] = {
#         'admin_messages': {},
#         'user_message': message.text if message.text else f"[Photo]"
#     }

#     for admin_id in admin_ids:
#         if message.photo:
#             sent_message = await context.bot.send_photo(
#                 chat_id=admin_id, photo=message.photo[-1].file_id,
#                 caption=f"Support request from {user.first_name} (ID: {user.id}):",
#                 reply_markup=reply_markup
#             )
#         else:
#             sent_message = await context.bot.send_message(
#                 chat_id=admin_id,
#                 text=f"Support request from {user.first_name} (ID: {user.id}):\n\n{message.text}",
#                 reply_markup=reply_markup
#             )

#         context.bot_data[f'support_message_{user.id}']['admin_messages'][admin_id] = sent_message.message_id

#     await update.message.reply_text(
#         "Your message has been sent to our admins. Please wait for their response."
#     )
#     return ConversationHandler.END


async def collect_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # Initialize an empty list to store messages
    context.user_data['support_messages'] = []

    await query.edit_message_text(
        "Please send your messages or photos. Once you're done, click the 'Send to Admins' button below. You can use /cancel at any time to cancel this request.")

    keyboard = [[InlineKeyboardButton(
        "Send to Admins", callback_data="submit_support")]]
    await context.bot.send_message(
        chat_id=update._effective_user.id,
        text="Click here when you're ready to submit:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return GlobalState.getInstance().COLLECTING_SUPPORT_MESSAGES


async def collect_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    message = update.message
    user_messages = context.user_data.get('support_messages', [])

    if message.text:
        user_messages.append({"type": "text", "content": message.text})
    elif message.photo:
        user_messages.append(
            {"type": "photo", "content": message.photo[-1].file_id})

    context.user_data['support_messages'] = user_messages

    await message.reply_text("Message received. Send more or click 'Send to Admins' when done.")
    return GlobalState.getInstance().COLLECTING_SUPPORT_MESSAGES


# async def handle_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     query = update.callback_query
#     await query.answer()

#     user = update._effective_user
#     user_messages = context.user_data.get('support_messages', [])

#     keyboard = [
#         [InlineKeyboardButton("Accept", callback_data=f'accept_{user.id}'),
#          InlineKeyboardButton("Reject", callback_data=f'reject_{user.id}')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     # Store message details in bot_data
#     context.bot_data[f'support_message_{user.id}'] = {
#         'admin_messages': {},
#         'user_messages': user_messages
#     }

#     for admin_id in admin_ids:
#         message_text = "\n\n".join(
#             [f"{'[Photo]' if msg['type'] == 'photo' else msg['content']}" for msg in user_messages])
#         sent_message = await context.bot.send_message(
#             chat_id=admin_id,
#             text=f"Support request from {user.first_name} (ID: {user.id}):\n\n{message_text}",
#             reply_markup=reply_markup
#         )

#         # Send photos separately
#         for msg in user_messages:
#             if msg['type'] == 'photo':
#                 await context.bot.send_photo(chat_id=admin_id, photo=msg['content'])

#         context.bot_data[f'support_message_{user.id}']['admin_messages'][admin_id] = sent_message.message_id

#     await context.bot.send_message(
#         chat_id=user.id,
#         text="Your messages have been sent to our admins. Please wait for their response."
#     )

#     # Clear the stored messages
#     context.user_data['support_messages'] = []

#     return ConversationHandler.END

async def handle_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()  # This will stop the "loading" animation

    user = query.from_user
    user_messages = context.user_data.get('support_messages', [])

    keyboard = [
        [InlineKeyboardButton("Accept", callback_data=f'accept_{user.id}'),
         InlineKeyboardButton("Reject", callback_data=f'reject_{user.id}')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Store message details in bot_data
    context.bot_data[f'support_message_{user.id}'] = {
        'admin_messages': {},
        'user_messages': user_messages
    }

    for admin_id in admin_ids:
        message_text = "\n\n".join(
            [f"{'[Photo]' if msg['type'] == 'photo' else msg['content']}" for msg in user_messages])
        sent_message = await context.bot.send_message(
            chat_id=admin_id,
            text=f"Support request from {user.first_name} (ID: {user.id}):\n\n{message_text}",
            reply_markup=reply_markup
        )

        # Send photos separately
        for msg in user_messages:
            if msg['type'] == 'photo':
                await context.bot.send_photo(chat_id=admin_id, photo=msg['content'])

        context.bot_data[f'support_message_{user.id}']['admin_messages'][admin_id] = sent_message.message_id

    await context.bot.send_message(
        chat_id=user.id,
        text="Your messages have been sent to our admins. Please wait for their response."
    )

    # Clear the stored messages
    context.user_data['support_messages'] = []

    return ConversationHandler.END
