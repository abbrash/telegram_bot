import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from telegram.error import BadRequest

from globals_mod import GlobalState

### <<<-------------------------------------------- Phantom AirDrop - Menu -------------------------------------------->>> ###
async def airdrop_phantom_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Delete the previous photo if it exists
    # Used .get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    GlobalState.getInstance().current_index_ph_swap = 0
    GlobalState.getInstance().first_time_loop_ph_swap = True

    GlobalState.getInstance().current_index_ph_stake = 0
    GlobalState.getInstance().first_time_loop_ph_stake = True

    GlobalState.getInstance().current_index_ph_unstake = 0
    GlobalState.getInstance().first_time_loop_ph_unstake = True

    keyboard = [
        [InlineKeyboardButton("1. سواپ کردن (Swap) 💵🔄", callback_data="airdrop_phantom_swap")],
        [InlineKeyboardButton("2. استیک کردن (Stake) 💵💰", callback_data="airdrop_phantom_stake")],
        [InlineKeyboardButton("3. آن‌استیک کردن (Unstake) 💵🧾", callback_data="airdrop_phantom_unstake")],
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="airdrops_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """
<b>ایردراپ فانتوم (Phantom) </b>

🔄 نحوه فعالیت: 
سواپ (بصورت هفتگی یا ماهانه)، استیک و فعالیت‌های مشخص شده از سوی تیم پروژه 

💵 موجودی مورد نیاز:
30 تتر 

📰 وضعیت ایردراپ:
احتمالی

📅 تاریخ توزیع: 
نامشخص

📖 توضیحات:
برای شرکت در ایردراپ فانتوم، لطفاً موارد زیر را به ترتیب انجام دهید.
"""

    # Select an image to send
    image_filename = os.path.join(
        'img', 'airdrop', 'phantom_wallet', 'phantom_wallet_img.jpg')

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
            # await context.bot.delete_message()
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML"
            )

    return GlobalState.getInstance().AIRDROP_PHANTOM_MENU

### <<<-------------------------------------------- Phantom AirDrop - Swap -------------------------------------------->>> ###
async def airdrop_phantom_swap(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    print(f"Current index: {GlobalState.getInstance().current_index_ph_swap}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_ph_swap:
            await query.delete_message()
            GlobalState.getInstance().current_index_ph_swap = 0
            GlobalState.getInstance().first_time_loop_ph_swap = False
        else:
            GlobalState.getInstance().current_index_ph_swap = int(query.data)
    elif query.data == "airdrop_phantom_swap":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_ph_swap = 0
        GlobalState.getInstance().first_time_loop_ph_swap = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/swap'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_ph_swap + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_ph_swap = max(
        0, min(GlobalState.getInstance().current_index_ph_swap, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """در بخش نشان‌داده شده، مقدار موجودی سولانا(SOL) در کیف پول شما نمایش داده شده است.
        روی آن کلیک کنید.
        """,
        """روی گزینه سواپ (Swap) کلیک کنید.""",
        """در اینجا باید توکنی که سولانا به آن تبدیل می‌شود را انتخاب کنید. 
روی بخش مشخص شده کلیک کنید.
        """,
        """توکن USDC را انتخاب کنید.""",
        """
1️⃣  مقدار سولانایی که می‌خواهید تبدیل کنید را وارد کنید.
2️⃣  بصورت خودکار میزان USDC دریافتی نمایش داده می‌شود.
3️⃣  روی دکمه Review Order کلیک کنید. 
""",
        """
1️⃣ میزان کارمزد تراکنش نمایش داده می‌شود.
2️⃣ روی دکمه Swap کلیک کنید.
"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_ph_swap]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_ph_swap == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_ph_swap + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="airdrop_phantom_menu")]
        ]
    elif GlobalState.getInstance().current_index_ph_swap == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="airdrop_phantom_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_ph_swap - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_ph_swap - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_ph_swap + 1))]
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
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance(
                ).message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().AIRDROP_PHANTOM_SWAP

### <<<-------------------------------------------- Phantom AirDrop - Stake -------------------------------------------->>> ###
async def airdrop_phantom_stake(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    print(f"Current index: {GlobalState.getInstance().current_index_ph_stake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_ph_stake:
            await query.delete_message()
            GlobalState.getInstance().current_index_ph_stake = 0
            GlobalState.getInstance().first_time_loop_ph_stake = False
        else:
            GlobalState.getInstance().current_index_ph_stake = int(query.data)
    elif query.data == "airdrop_phantom_stake":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_ph_stake = 0
        GlobalState.getInstance().first_time_loop_ph_stake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/stake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_ph_stake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_ph_stake = max(
        0, min(GlobalState.getInstance().current_index_ph_stake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""template"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_ph_stake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_ph_stake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_ph_stake + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="airdrop_phantom_menu")]
        ]
    elif GlobalState.getInstance().current_index_ph_stake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="airdrop_phantom_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_ph_stake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_ph_stake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_ph_stake + 1))]
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
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().AIRDROP_PHANTOM_STAKE



### <<<-------------------------------------------- Phantom AirDrop - Unstake -------------------------------------------->>> ###
async def airdrop_phantom_unstake(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    print(f"Current index: {GlobalState.getInstance().current_index_ph_unstake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_ph_unstake:
            await query.delete_message()
            GlobalState.getInstance().current_index_ph_unstake = 0
            GlobalState.getInstance().first_time_loop_ph_unstake = False
        else:
            GlobalState.getInstance().current_index_ph_unstake = int(query.data)
    elif query.data == "airdrop_phantom_unstake":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_ph_unstake = 0
        GlobalState.getInstance().first_time_loop_ph_unstake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/unstake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_ph_unstake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_ph_unstake = max(
        0, min(GlobalState.getInstance().current_index_ph_unstake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""template"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_ph_unstake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_ph_unstake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_ph_unstake + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="airdrop_phantom_menu")]
        ]
    elif GlobalState.getInstance().current_index_ph_unstake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="airdrop_phantom_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_ph_unstake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_ph_unstake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_ph_unstake + 1))]
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
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().AIRDROP_PHANTOM_UNSTAKE

