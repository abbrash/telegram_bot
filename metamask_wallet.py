import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

from globals import GlobalState

### <<<-------------------------------------------- Metamask Wallet -------------------------------------------->>> ###
### << *** Metamask - Create Wallet *** >>> ###

async def wallet_metamask_create(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    print(f"Current index: {GlobalState.getInstance().current_index_metamask_create_wallet}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_metamask_create_wallet:
            GlobalState.getInstance().current_index_metamask_create_wallet = 0
            GlobalState.getInstance().first_time_loop_metamask_create_wallet = False
        else:
            GlobalState.getInstance().current_index_metamask_create_wallet = int(query.data)
    elif query.data == "metamask_wallet":
        # Reset current_index when "air_drop_01" is clicked
        GlobalState.getInstance().current_index_metamask_create_wallet = 0
        GlobalState.getInstance().first_time_loop_metamask_create_wallet = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_metamask_create_wallet + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_metamask_create_wallet = max(
        0, min(GlobalState.getInstance().current_index_metamask_create_wallet, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = []

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_metamask_create_wallet]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_metamask_create_wallet == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_metamask_create_wallet + 1))],
            [InlineKeyboardButton("بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu_over")]
        ]
    elif GlobalState.getInstance().current_index_metamask_create_wallet == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="wallet_metamask_menu_over")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_metamask_create_wallet - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_metamask_create_wallet - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_metamask_create_wallet + 1))]
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
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().METAMASK_WALLET_CREATE

### <<<-------------------------------------------- Metamask Wallet Sub-Menu -------------------------------------------->>> ###

async def wallet_metamask_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # global chat_id

    # Delete the previous photo if it exists
    # Use.get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance(
        ).message_ids[GlobalState.getInstance().chat_id].pop(0)

    # global GlobalState.getInstance().current_index_ph_swap, GlobalState.getInstance().first_time_loop_ph_swap
    GlobalState.getInstance().current_index_metamask_create_wallet = 0
    GlobalState.getInstance().first_time_loop_metamask_create_wallet = True

    keyboard = [
        [InlineKeyboardButton("1. ساخت کیف پول متامسک (MetaMask) ", callback_data="metamask_wallet_create")],
        [InlineKeyboardButton("2. بازیابی کیف پول متامسک (MetaMask)", callback_data="metamask_wallet_restore")],
        [InlineKeyboardButton("3. ارسال رمزارز (Send)", callback_data="metamask_wallet_send")],
        [InlineKeyboardButton("4. دریافت رمزارز (Receive)", callback_data="metamask_wallet_receive")],
        [InlineKeyboardButton("5. سواپ رمزارز (Swap)", callback_data="metamask_wallet_swap")],
        [InlineKeyboardButton("6. بریج رمزارز (Bridge)", callback_data="metamask_wallet_bridge")],
        [InlineKeyboardButton("7. استیک رمزارز (Stake)", callback_data="metamask_wallet_stake")],
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="back_to_wallet_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = ""

    # Select an image to send
    # Replace with the actual path to your image
    image_filename = os.path.join('img', 'wallet', 'metamask', 'metamask_wallet_img.jpg')

    # Send the image along with the text and buttons
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(image_filename, 'rb'),
        caption=text,
        reply_markup=key_markup,
        parse_mode="HTML"
    )

    return GlobalState.getInstance().METAMASK_WALLET


async def wallet_metamask_menu_over(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Delete the previous photo if it exists
    # Use.get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance(
        ).message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().METAMASK_WALLET
