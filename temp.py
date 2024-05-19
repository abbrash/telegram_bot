import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Define the list of image URLs
photo_list = [
    'https://th.bing.com/th/id/OIP.TzP2op3lkhlTh6oOHamacAHaHa?rs=1&pid=ImgDetMain',
    'https://th.bing.com/th/id/OIP.RH2gc-Oe1qSvCjD3IRYAyQHaE7?rs=1&pid=ImgDetMain',
    'https://th.bing.com/th/id/OIP.AW8VfeeCp9v_xzlVdciPpAHaEo?rs=1&pid=ImgDetMain',
    'https://th.bing.com/th/id/OIP.R3U06JEJvoROC7iFM1AnzAHaEK?rs=1&pid=ImgDetMain'
]

# Define the initial index for the current image
current_index = 0

# Function to handle the /start command


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_image(update.effective_chat.id, context)

# Function to send the current image and inline keyboard


async def send_image(chat_id, context):
    global current_index

    # Get the current image URL
    image_url = photo_list[current_index]

    # Download the image data
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = response.content
    else:
        await context.bot.send_message(chat_id=chat_id, text="Failed to download the image.")
        return

    # Check if it's the last image
    if current_index == len(photo_list) - 1:
        keyboard = [[]]  # Empty keyboard for the last image
    else:
        keyboard = [[InlineKeyboardButton(
            "NEXT", callback_data=str(current_index + 1))]]

    # Send the image with the inline keyboard
    await context.bot.send_photo(chat_id=chat_id, photo=image_data, reply_markup=InlineKeyboardMarkup(keyboard))

# Function to handle the button click


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global current_index
    query = update.callback_query

    # Update the current index based on the button click
    current_index = int(query.data)

    # Send the updated image
    await send_image(query.message.chat_id, context)

    # Answer the callback query to prevent further updates
    await query.answer()

# Set up the bot and handlers


def main() -> None:
    application = Application.builder().token('7029020592:AAGYmkIiqRPL99oGfIW0vvyTIhSJYKDbl9U').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_click))

    application.run_polling()


if __name__ == "__main__":
    main()
