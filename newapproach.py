from decouple import config
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from telegram.ext import ContextTypes
from telegram.error import BadRequest

START_ROUTES, END_ROUTES = range(2)

global mess_id_prev, tel_user_id, sent_message

mess_id_prev = {}



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    global tel_user_id, sent_message
    tel_user_id = update._effective_user.id

    keyboard = [
        [InlineKeyboardButton("صرافی‌های ایرانی 💱🇮🇷", callback_data="local_exchange")],
        [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
        [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
        [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Hello!"

    if update.message:
        sent_message = await update.message.reply_text(text=text, reply_markup=reply_markup)
        mess_id_prev[tel_user_id] = sent_message.message_id   # saving message_id
        print("start: update.message.reply_text")

    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        
    query = update.callback_query
    await query.answer()

    global tel_user_id, sent_message

    # tel_user_id = update._effective_user.id

    keyboard = [
        [InlineKeyboardButton("صرافی‌های ایرانی 💱🇮🇷", callback_data="local_exchange")],
        [InlineKeyboardButton("صرافی‌های خارجی 💱🌐", callback_data="global_exchange")],
        [InlineKeyboardButton("ایردراپ 🚀🎁", callback_data="air_drops")],
        [InlineKeyboardButton("کیف پول 💳💰", callback_data="wallet_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "welcome back!"

    if update.message:
        sent_message = await update.message.reply_text(text=text, reply_markup=reply_markup)
        print("start over: update.message.reply_text")
    try:
        # Try to edit the message text
        await query.edit_message_text(text=text, reply_markup=reply_markup)
        print("start over: query.edit_message_text")
    except BadRequest:
        # If the message doesn't have text content, send a new message
        await query.message.reply_text(text=text, reply_markup=reply_markup)
        print("start over: query.message.reply_text")

    return START_ROUTES


async def wallet_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    query = update.callback_query
    await query.answer()

    global tel_user_id, sent_message

    keyboard = [
        [InlineKeyboardButton("کیف پول متامسک (MetaMask)", callback_data="metamask_menu")],
        [InlineKeyboardButton("کیف پول فانتوم (Phantom)", callback_data="phantom_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = "Wallet Menu"

    image_filename = "img/test/01.jpg"
    if query.message and query.message.text:
        try:
            # await query.edit_message_text(text=text, reply_markup=key_markup)
            await query.delete_message()
            await context.bot.send_photo(chat_id=update.effective_chat.id,
                                         photo=open(image_filename, 'rb'),
                                         caption=text,
                                         reply_markup=key_markup,
                                         parse_mode="HTML")
            
            print("context.bot.sendMessage: try")

        except BadRequest:
            sent_message = await context.bot.sendMessage(chat_id=tel_user_id, text=text, reply_markup=key_markup)
            print("context.bot.sendMessage: except")
    else:
        sent_message = await context.bot.sendMessage(chat_id=tel_user_id, text=text, reply_markup=key_markup)
        print("context.bot.sendMessage: else")

    return START_ROUTES


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    if update.message:
        # Handle text messages
        return await start(update, context)
    elif update.callback_query:
        # Handle callback queries
        query = update.callback_query
        await query.answer()
        await query.delete_message()
        return await start_over(update, context)
    else:
        # Handle other update types (not expected)
        return END_ROUTES


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token('6264022397:AAF0AfVhD1YvP-Mqk8qwEAi_awRhC8XQxQw').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [  
                CallbackQueryHandler(wallet_menu, pattern="^" + "wallet_menu" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            END_ROUTES: [  # The buttons callbacks of the ...
                CallbackQueryHandler(start_over, pattern="^" + "main_menu" + "$")
            ]},
        fallbacks=[CommandHandler("start", start)],)

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES, poll_interval=3, timeout=60)


print('Starting up bot...')

Tk = config('token')

if __name__ == "__main__":
    main()
