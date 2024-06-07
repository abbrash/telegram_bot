import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from telegram.error import BadRequest

from globals import GlobalState

### <<<-------------------------------------------- Phantom AirDrop -------------------------------------------->>> ###

### <<<-------------------------------------------- Phantom AirDrop Sub-Menu -------------------------------------------->>> ###

async def air_drop_phantom_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Delete the previous photo if it exists
    # Used .get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    GlobalState.getInstance().current_index_ph_swap = 0
    GlobalState.getInstance().first_time_loop_ph_swap = True

    GlobalState.getInstance().current_index_ph_stake = 0
    GlobalState.getInstance().first_time_loop_ph_stake = True

    GlobalState.getInstance().current_index_ph_unstake = 0
    GlobalState.getInstance().first_time_loop_ph_unstake = True

    keyboard = [
        [InlineKeyboardButton("1. سواپ کردن (Swap) 💵🔄", callback_data="phantom_swap")],
        [InlineKeyboardButton("2. استیک کردن (Stake) 💵💰", callback_data="phantom_stake")],
        [InlineKeyboardButton("3. آن‌استیک کردن (Unstake) 💵🧾", callback_data="phantom_unstake")],
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="back_to_air_drop_menu")]
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
        # await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=key_markup)
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML"
            )

    return GlobalState.getInstance().PH_AIRDROP


# async def air_drop_phantom_menu_over(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     # Delete the previous photo if it exists
#     # Used .get() method to avoid KeyError if chat_id not found
#     if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
#         await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
#         GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

#     return GlobalState.getInstance().PH_AIRDROP


### <<<-------------------------------------------- Phantom AirDrop - Swap -------------------------------------------->>> ###

async def air_drop_phantom_swap(update: Update, context: CallbackContext) -> int:
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
    elif query.data == "phantom_swap":
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
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="air_drop_phantom_menu_over")]
        ]
    elif GlobalState.getInstance().current_index_ph_swap == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_phantom_menu_over")],
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
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().PH_AIRDROP_SWAP


### << *** Phantom AirDrop - Stake *** >>> ###

async def air_drop_phantom_stake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # global current_index_ph_stake, first_time_loop_ph_stake
    # global chat_id

    print(f"Current index: {GlobalState.getInstance().current_index_ph_stake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_ph_stake:
            current_index_ph_stake = 0
            first_time_loop_ph_stake = False
        else:
            current_index_ph_stake = int(query.data)
    elif query.data == "phantom_stake":
        # Reset current_index when "air_drop_01" is clicked
        current_index_ph_stake = 0
        first_time_loop_ph_stake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/stake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_ph_stake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_ph_stake = max(
        0, min(current_index_ph_stake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """در بخش نشان‌داده شده، مقدار موجودی سولانا (SOL) در کیف پول شما نمایش داده شده است.
روی آن کلیک کنید.
""",
        """برای استیک کردن سولانا، روی بخش مشخص شده کلیک کنید.""",
        """از میان گزینه‌های نمایش داده شده، Phantom Validator را انتخاب کنید.""",
        """
1️⃣ مقدار سولانای مورد نظر را برای استیک کردن انتخاب کنید.
2️⃣ روی گزینه Stake کلیک کنید.
""",
        """منتظر بمانید تا حساب استیک برای شما ایجاد شود.
⚠️⚠️⚠️ اگر با پیغام خطا مواجه شدید دوباره تلاش کنید.
""",
        """در این حالت سولانای ارسال شده با موفقیت استیک شده است.""",
        """اگر تمام مراحل را با موفقیت انجام داده باشید، در صحفه اول کیف پولتان، حساب استیک سولانا نمایش داده می‌شود. 
روی آن کلیک کنید.
""",
        """فعال‌شدن حساب شما کمی زمان می‌برد. """,
        """پس از اینکه حسابتان فعال شد، گزینه سبز رنگ Active برای شما نمایش داده می‌شود."""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_ph_stake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_ph_stake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_stake + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="air_drop_phantom_menu_over")]
        ]
    elif current_index_ph_stake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_phantom_menu_over")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str( current_index_ph_stake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_stake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_stake + 1))]
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
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id] = []
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().PH_AIRDROP_STAKE


### << *** Phantom AirDrop - Unstake *** >>> ###

async def air_drop_phantom_unstake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # global current_index_ph_unstake, first_time_loop_ph_unstake
    # global chat_id

    print(
        f"Current index: {GlobalState.getInstance().current_index_ph_unstake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if first_time_loop_ph_unstake:
            current_index_ph_unstake = 0
            first_time_loop_ph_unstake = False
        else:
            current_index_ph_unstake = int(query.data)
    elif query.data == "phantom_unstake":
        # Reset current_index when "air_drop_01" is clicked
        current_index_ph_unstake = 0
        first_time_loop_ph_unstake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/phantom_wallet/unstake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(current_index_ph_unstake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    current_index_ph_unstake = max(
        0, min(current_index_ph_unstake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """پس از فعال‌سازی حساب استیک سولانا، می‌توانید برای برداشت پولی که استیک کرده‌اید اقدام کنید. 
برای این منظور در بخش نشان‌داده شده، مقدار موجودی سولانا (SOL) در کیف پول شما نمایش داده شده است.
روی آن کلیک کنید.
""",
        """روی گزینه Unstake کلیک کنید.""",
        """در این حالت فرآیند غیرفعال‌سازی حساب استیک شما آغاز می‌شود.""",
        """پس از نمایش این صفحه، حساب استیک شما با موفقیت غیرفعال شده است.
روی گزینه Close کلیک کنید.
""",
        """در این حالت با ورود به حساب استیک سولانا، عبارت Deactivating نمایش داده می‌شود.
⚠️⚠️⚠️ دقت کنید این مرحله ممکن است تا چند روز طول بکشید.
""",
        """با نمایش واژه قرمز رنگ Inactive حساب استیک سولانا شما به صورت کامل غیرفعال شده است.
اکنون می‌توانید پول خود را برداشت کنید. 
روی آن کلیک کنید.
""",
        """روی گزینه Withdraw Stake کلیک کنید.""",
        """فرآیند برداشت پول شما آغاز شده است. 
⚠️⚠️⚠️ اگر با پیغام خطا مواجه شدید دوباره تلاش کنید.
""",
        """پول شما با موفقیت برداشت شد و به موجودی سولانا در کیف پولتان اضافه گردید. """
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[current_index_ph_unstake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if current_index_ph_unstake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_unstake + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ فانتوم 🏠⬅️ ", callback_data="air_drop_phantom_menu_over")]
        ]
    elif current_index_ph_unstake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="air_drop_phantom_menu_over")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_unstake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(current_index_ph_unstake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(current_index_ph_unstake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup
        )

        # Store the message ID
        if chat_id not in GlobalState.getInstance().message_ids:
            # initialize a list to store further information
            GlobalState.getInstance().message_ids[chat_id] = []
        GlobalState.getInstance().message_ids[chat_id].append(sent_photo.message_id)

        # Delete the previous photo if it exists
        # Use.get() method to avoid KeyError if chat_id not found
        if len(GlobalState.getInstance().message_ids.get(chat_id, [])) > 1:
            await context.bot.delete_message(chat_id=chat_id, message_id=GlobalState.getInstance().message_ids[chat_id][0])
            GlobalState.getInstance().message_ids[chat_id].pop(0)

    return GlobalState.getInstance().PH_AIRDROP_UNSTAKE
