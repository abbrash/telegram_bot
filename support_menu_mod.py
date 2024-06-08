from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.error import BadRequest

from globals_mod import GlobalState

from admins_mod import *

admin_id = 107998330

### <<<-------------------------------------------- Support Menu -------------------------------------------->>> ###
# async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     protect_content = not is_admin(update._effective_user.id)

#     keyboard = [
#         [InlineKeyboardButton("ارسال", callback_data="support_message")],
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


# async def support_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     context.user_data['support_message'] = update.message.text
#     return GlobalState.getInstance().SUPPORT_MENU


# async def support_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     context.user_data['support_photo'] = update.message.photo[-1].file_id
#     return GlobalState.getInstance().SUPPORT_MENU


# async def submit(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     query.answer()

#     protect_content = not is_admin(update._effective_user.id)

#     if 'support_message' in context.user_data:
#         context.bot.send_message(
#             chat_id=admin_id, 
#             text=f"Support message from user {update.effective_user.id}:\n{context.user_data['support_message']}",
#             protect_content=protect_content
#             )
#         del context.user_data['support_message']

#     if 'support_photo' in context.user_data:
#         context.bot.send_photo(
#             chat_id=admin_id, 
#             photo=context.user_data['support_photo'], 
#             caption=f"Support photo from user {update.effective_user.id}",
#             protect_content=protect_content
#             )
#         del context.user_data['support_photo']

#     query.edit_message_text("Your message has been sent to our support team. They will get back to you soon.")
#     return ConversationHandler.END


####################################################################################################

async def support_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Initialize an empty list to store user messages
    context.user_data['support_messages'] = []

    keyboard = [
        [InlineKeyboardButton("ارسال به پشتیبانی", callback_data="submit_support")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = "لطفا پیام یا عکس خود را ارسال کنید. شما می توانید چندین پیام و عکس ارسال کنید. وقتی تمام شد، روی «ارسال به پشتیبانی» کلیک کنید تا همه پیام ها به تیم پشتیبانی ارسال شوند."

    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content)
        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content)
    else:
        await query.delete_message()
        await context.bot.send_message(chat_id=update._effective_user.id,
                                       text=text,
                                       reply_markup=key_markup,
                                       protect_content=protect_content)

    return GlobalState.getInstance().SUPPORT_MENU


async def receive_support_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        if update.message.text:
            context.user_data['support_messages'].append(
                f"پیام: {update.message.text}")
            await update.message.reply_text("پیام شما دریافت شد. می توانید پیام یا عکس دیگری ارسال کنید، یا روی «ارسال به پشتیبانی» کلیک کنید.")
        elif update.message.photo:
            file_id = update.message.photo[-1].file_id
            context.user_data['support_messages'].append(f"عکس: {file_id}")
            await update.message.reply_text("عکس شما دریافت شد. می توانید پیام یا عکس دیگری ارسال کنید، یا روی «ارسال به پشتیبانی» کلیک کنید.")
    return GlobalState.getInstance().SUPPORT_MENU


async def submit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    if 'support_messages' in context.user_data and context.user_data['support_messages']:
        full_message = f"پیام های پشتیبانی از کاربر {update._effective_user.id}:\n\n"
        for msg in context.user_data['support_messages']:
            if msg.startswith("پیام:"):
                await context.bot.send_message(chat_id=admin_id, text=full_message + msg, protect_content=protect_content)
                full_message = ""
            elif msg.startswith("عکس:"):
                file_id = msg.split(": ")[1]
                await context.bot.send_photo(chat_id=admin_id, photo=file_id, caption=full_message, protect_content=protect_content)
                full_message = ""

        if full_message:  # Send any remaining text messages
            await context.bot.send_message(chat_id=admin_id, text=full_message, protect_content=protect_content)

        del context.user_data['support_messages']
        await query.edit_message_text("پیام های شما به تیم پشتیبانی ارسال شد. به زودی با شما تماس خواهند گرفت.")
    else:
        await query.edit_message_text("هیچ پیامی برای ارسال وجود ندارد. لطفا ابتدا پیام یا عکس خود را ارسال کنید.")

    return ConversationHandler.END































####################################################################################################
# # Define states for the conversation
# SUPPORT_MESSAGE, SUPPORT_PHOTO = range(2)

# # Replace with your bot token and admin's user ID
# TOKEN = "YOUR_BOT_TOKEN"
# ADMIN_ID = 123456789  # Replace with the actual user ID of the admin


# def start(update: Update, context):
#     # Create the "Support" button
#     keyboard = [[InlineKeyboardButton("Support", callback_data='support')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     update.message.reply_text(
#         "Welcome! Click the button below for support.", reply_markup=reply_markup)


# def support(update: Update, context):
#     query = update.callback_query
#     query.answer()
#     query.edit_message_text(
#         "Please send your message or photo. Then click 'Submit' to send it to our support team.")

#     # Create the "Submit" button
#     keyboard = [[InlineKeyboardButton("Submit", callback_data='submit')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     query.message.reply_text(
#         "Click 'Submit' when you're ready:", reply_markup=reply_markup)

#     return SUPPORT_MESSAGE


# def support_message(update: Update, context):
#     context.user_data['support_message'] = update.message.text
#     return SUPPORT_MESSAGE


# def support_photo(update: Update, context):
#     context.user_data['support_photo'] = update.message.photo[-1].file_id
#     return SUPPORT_MESSAGE


# def submit(update: Update, context):
#     query = update.callback_query
#     query.answer()

#     if 'support_message' in context.user_data:
#         context.bot.send_message(
#             chat_id=ADMIN_ID, text=f"Support message from user {update.effective_user.id}:\n{context.user_data['support_message']}")
#         del context.user_data['support_message']

#     if 'support_photo' in context.user_data:
#         context.bot.send_photo(
#             chat_id=ADMIN_ID, photo=context.user_data['support_photo'], caption=f"Support photo from user {update.effective_user.id}")
#         del context.user_data['support_photo']

#     query.edit_message_text(
#         "Your message has been sent to our support team. They will get back to you soon.")
#     return ConversationHandler.END


# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     # Define conversation handler
#     conv_handler = ConversationHandler(
#         entry_points=[CallbackQueryHandler(support, pattern='^support$')],
#         states={
#             SUPPORT_MESSAGE: [
#                 MessageHandler(Filters.text & ~Filters.command,
#                                support_message),
#                 MessageHandler(Filters.photo, support_photo),
#                 CallbackQueryHandler(submit, pattern='^submit$')
#             ],
#         },
#         fallbacks=[]
#     )

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(conv_handler)

#     updater.start_polling()
#     updater.idle()


# if __name__ == '__main__':
#     main()
