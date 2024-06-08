import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from telegram.error import BadRequest

from globals_mod import GlobalState

### <<<-------------------------------------------- AirDrop Template Sub-Menu -------------------------------------------->>> ###

async def air_drop_template_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Delete the previous photo if it exists
    # Used .get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance(
        ).message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance(
        ).message_ids[GlobalState.getInstance().chat_id].pop(0)

    GlobalState.getInstance().current_index_template_swap = 0
    GlobalState.getInstance().first_time_loop_template_swap = True

    GlobalState.getInstance().current_index_template_stake = 0
    GlobalState.getInstance().first_time_loop_template_stake = True

    GlobalState.getInstance().current_index_template_unstake = 0
    GlobalState.getInstance().first_time_loop_template_unstake = True

    keyboard = [
        [InlineKeyboardButton("1. سواپ کردن (Swap) 💵🔄", callback_data="phantom_swap")],
        [InlineKeyboardButton("2. استیک کردن (Stake) 💵💰", callback_data="phantom_stake")],
        [InlineKeyboardButton("3. آن‌استیک کردن (Unstake) 💵🧾", callback_data="phantom_unstake")],
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="back_to_air_drop_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """template
"""

    # Select an image to send
    image_filename = os.path.join('img', 'airdrop', 'phantom_wallet', 'phantom_wallet_img.jpg')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML"
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=key_markup)

    else:
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML"
        )

    return GlobalState.getInstance().AIRDROP_TEMPLATE



### <<<-------------------------------------------- AirDrop Template - Swap -------------------------------------------->>> ###

async def airdrop_template(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    print(f"Current index: {GlobalState.getInstance().current_index_template_swap}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_template_swap:
            await query.delete_message()
            GlobalState.getInstance().current_index_template_swap = 0
            GlobalState.getInstance().first_time_loop_template_swap = False
        else:
            GlobalState.getInstance().current_index_template_swap = int(query.data)
    elif query.data == "template_swap":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_template_swap = 0
        GlobalState.getInstance().first_time_loop_template_swap = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'airdro_template_swap_directory'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_template_swap + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_template_swap = max(
        0, min(GlobalState.getInstance().current_index_template_swap, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""template_swap"""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_template_swap]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_template_swap == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_template_swap + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="airdrop_template_menu")]
        ]
    elif GlobalState.getInstance().current_index_template_swap == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="airdrop_template_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_template_swap - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_template_swap - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_template_swap + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    GlobalState.getInstance().chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=GlobalState.getInstance().chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

        # Store the message ID
        if GlobalState.getInstance().chat_id not in GlobalState.getInstance().message_ids:
            # initialize a list to store further information
            GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id] = []
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].append(
            sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().AIRDROP_TEMPLATE_SWAP









# # Add the following to constants and variables to globals.py 
# # Initialize constants
# self.AIRDROP_TEMPLATE, self.AIRDROP_TEMPLATE_SWAP = range(12, 14)
# # Initialize variables
# self.first_time_loop_airdrop_template_swap = True
# self.current_index_airdrop_template_swap = 0



# # Add the following lines to the main.py
# from airdrop_tamplate_mod import *

# GlobalState.getInstance().AIRDROP_TEMPLATE: [  # The buttons callbacks of the "Template Airdrop Menu"
#     CallbackQueryHandler(airdrop_template_swap, pattern="^" + "airdrop_template_swap" + "$"),
#     CallbackQueryHandler(airdrop_template_menu, pattern="^" + "airdrop_template_menu" + "$")
# ],
# GlobalState.getInstance().AIRDROP_TEMPLATE_SWAP: [
#     CallbackQueryHandler(airdrop_template_swap, pattern="^(\d+)$"),
#     CallbackQueryHandler(airdrop_template_menu, pattern="^" + "airdrop_template_menu" + "$")
# ]
