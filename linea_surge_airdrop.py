import os 
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

from globals import GlobalState


### <<<-------------------------------------------- Linea Surge AirDrop -------------------------------------------->>> ###

async def air_drop_linea_surge_stake(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # global current_index_linea_surge_stake, first_time_loop_linea_surge_stake, message_ids
    # global chat_id

    print(
        f"Current index: {GlobalState.getInstance().current_index_linea_surge_stake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_linea_surge_stake:
            GlobalState.getInstance().current_index_linea_surge_stake = 0
            GlobalState.getInstance().first_time_loop_linea_surge_stake = False
        else:
            GlobalState.getInstance().current_index_linea_surge_stake = int(query.data)
    elif query.data == "linea_surge_stake":
        # Reset current_index when "air_drop_01" is clicked
        GlobalState.getInstance().current_index_linea_surge_stake = 0
        GlobalState.getInstance().first_time_loop_linea_surge_stake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/linea_surge/stake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_linea_surge_stake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_linea_surge_stake = max(
        0, min(GlobalState.getInstance().current_index_linea_surge_stake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """ابتدا وارد سایت <a href='https://www.syncswap.com'>SyncSwap</a> شوید. 
1️⃣ روی گزینه Trade کلیک کنید.
2️⃣ در این بخش آدرس کیف پول نمایش داده می‌شود. 
⚠️⚠️⚠️ اگر گزینه Connect Wallet را می‌بینید، روی آن کلیک کنید تا کیف پولتان به سایت وصل شود.
3️⃣ روی این گزینه کلیک کنید. 
4️⃣ از منوی باز شده شبکه Linea را انتخاب کنید. 
""",
        """
1️⃣ توکن ETH را انتخاب کنید.
2️⃣ توکن weETH را انتخاب کنید.
3️⃣ مقدار اتریومی که می‌خواهید به weETH تبدیل کنید را وارد کنید. (عدد نوشته شده در کادر کوچک، معادل دلاری ETH را نشان می‌دهد.)
4️⃣ مقدار دریافتی برای شما نمایش داده می‌شود. (عدد نوشته شده در کادر کوچک، معادل دلاری weETH را نشان می‌دهد.)

5️⃣ عدد نوشته شده در کادر کوچک، میزان کارمزد معامله را نمایش می‌دهد.
اگر مقدار کارمزد نمایش داده شده در حد چند سنت است (در اینجا 3 سنت)، روی دکمه Swap کلیک کنید. 
""",
        """
1️⃣ مقدار کارمزد کل تراکنش را نمایش می‌دهد.
2️⃣ ارزش کل تراکنش (مقدار اتریومی که می‌خواهید تبدیل کنید + کارمزد تراکنش) را نمایش می‌دهد.
3️⃣ اگر مقدار کارمزد تراکنش کم است، روی دکمه Confirm کلیک کنید. 
""",
        """از نوار بالا روی Pool کلیک کنید و در منوی باز شده Pools را انتخاب کنید.""",
        """در کادر مشخص شده عبارت weeth را جستجو کنید و از میان نتایج به دست آمده استخر نقدینگی مربوط به ETH/weETH از نوع Classic را انتخاب کنید.""",
        """
1️⃣ روی گزینه Deposit کلیک کنید.
2️⃣ تیک مشخص شده را فعال کنید.
3️⃣ مقدار weETH که می‌خواهید واریز کنید را مشخص کنید. در این حالت بصورت خودکار، مقدار ETH معادل نیز در کادر پایین نمایش داده می‌شود.
4️⃣ روی دکمه Unlock weETH کلیک کنید. 
""",
        """
1️⃣ در این باید به سایت برای برداشت weETH دسترسی دهید. مقداری که در بخش 3 مرحله قبلی وارد کردید را وارد کنید. (برای اطمینان می‌توانید کمی بیشتر وارد کنید.) 
2️⃣ روی دکمه Next کلیک کنید.
""",
        """
1️⃣ کارمزد تراکنش نمایش داده شده است. 
2️⃣ اگر کارمزد کم است، روی دکمه Approve کلیک کنید.
""",
        """روی دکمه Deposit کلیک کنید. """,
        """
1️⃣ مقدار کارمزد کل تراکنش را نمایش می‌دهد.
2️⃣ ارزش کل تراکنش (ارزش دلاری توکن‌هایی که می‌خواهید واریز کنید + کارمزد تراکنش) را نمایش می‌دهد.
3️⃣ اگر مقدار کارمزد تراکنش کم است، روی دکمه Confirm کلیک کنید. 
"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_linea_surge_stake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_linea_surge_stake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_linea_surge_stake + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ لینیا 🏠⬅️ ",
                                  callback_data="air_drop_linea_surge_menu_over")]
        ]
    elif GlobalState.getInstance().current_index_linea_surge_stake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="air_drop_linea_surge_menu_over")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_linea_surge_stake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_linea_surge_stake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_linea_surge_stake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    GlobalState.getInstance().chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=GlobalState.getInstance().chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode='HTML'
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
            GlobalState.getInstance(
            ).message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().LINEA_SURGE_AIRDROP_STAKE


### << *** Phantom AirDrop - Stake *** >>> ###

async def air_drop_linea_surge_unstake(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # global current_index_linea_surge_unstake, first_time_loop_linea_surge_unstake
    # global chat_id

    print(f"Current index: {GlobalState.getInstance().current_index_linea_surge_unstake}")

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_linea_surge_unstake:
            GlobalState.getInstance().current_index_linea_surge_unstake = 0
            GlobalState.getInstance().first_time_loop_linea_surge_unstake = False
        else:
            GlobalState.getInstance().current_index_linea_surge_unstake = int(query.data)
    elif query.data == "linea_surge_unstake":
        # Reset current_index when "air_drop_01" is clicked
        GlobalState.getInstance().current_index_linea_surge_unstake = 0
        GlobalState.getInstance().first_time_loop_linea_surge_unstake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/airdrop/linea_surge/unstake'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_linea_surge_unstake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_linea_surge_unstake = max(
        0, min(GlobalState.getInstance().current_index_linea_surge_unstake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """برای برداشت پول از سایت SyncSwap این مراحل را انجام دهید.
ابتدا وارد سایت <a href='https://www.syncswap.com'>SyncSwap</a> شوید. از نوار بالا روی گزینه Pool کلیک کنید و از منوی باز شده Positionsرا انتخاب کنید.
""",
        """در اینجا Position مشخص شده را انتخاب کنید.""",
        """
1️⃣ روی Withdraw کلیک کنید.
2️⃣ برای برداشت کل موجودی، روی Max کلیک کنید. (می‌توانید بصورت دستی، هر مقداری را وارد کنید.)
3️⃣ گزینه Balanced را انتخاب کنید.
""",
        """روی Unlock LP Token کلیک کنید.""",
        """
1️⃣ در این باید به سایت برای برداشت weETH دسترسی دهید. مقداری که در مرحله قبلی وارد کردید را مجدداً وارد کنید. (برای اطمینان می‌توانید کمی بیشتر وارد کنید.) 
2️⃣ روی Next کلیک کنید.
""",
        """
1️⃣ کارمزد تراکنش نمایش داده شده است.
2️⃣ روی Approve کلیک کنید.
""",
        """روی Withdraw Liquidity کلیک کنید.""",
        """
1️⃣ کارمزد تراکنش نمایش داده شده است.
2️⃣ روی Confirm کلیک کنید.
"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_linea_surge_unstake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_linea_surge_unstake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_linea_surge_unstake + 1))],
            [InlineKeyboardButton("بازگشت به منوی ایردراپ لینیا 🏠⬅️ ",
                                  callback_data="air_drop_linea_surge_menu_over")]
        ]
    elif GlobalState.getInstance().current_index_linea_surge_unstake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="air_drop_linea_surge_menu_over")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_linea_surge_unstake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_linea_surge_unstake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_linea_surge_unstake + 1))]
        ]

    reply_markup = InlineKeyboardMarkup(buttons)

    # Send the current photo with caption and navigation buttons
    GlobalState.getInstance().chat_id = update.effective_chat.id

    with open(image_filename, 'rb') as photo:
        sent_photo = await context.bot.send_photo(
            chat_id=GlobalState.getInstance().chat_id,
            photo=photo,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode='HTML'
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
            GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().LINEA_SURGE_AIRDROP_UNSTAKE


async def air_drop_linea_surge_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # global chat_id

    # Delete the previous photo if it exists
    # Use.get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    # global current_index_linea_surge_stake, first_time_loop_linea_surge_stake
    GlobalState.getInstance().current_index_linea_surge_stake = 0
    GlobalState.getInstance().first_time_loop_linea_surge_stake = True

    # global current_index_linea_surge_unstake, first_time_loop_linea_surge_unstake
    GlobalState.getInstance().current_index_linea_surge_unstake = 0
    GlobalState.getInstance().first_time_loop_linea_surge_unstake = True

    keyboard = [
        [InlineKeyboardButton("1. واریز کردن (Stake) 💵💰",
                              callback_data="linea_surge_stake")],
        [InlineKeyboardButton("2. برداشت کردن (Unstake) 💵💰",
                              callback_data="linea_surge_unstake")],
        [InlineKeyboardButton(
            "بازگشت ⬅️", callback_data="back_to_air_drop_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """
<b>ایردراپ لینیا سرج (Linea Surge) </b>

🔄 نحوه فعالیت: 
تأمین نقدینگی 

💵 موجودی مورد نیاز:
حداقل: ندارد /  ایده‌آل: 100 تتر یا بیشتر

📰 وضعیت ایردراپ:
قطعی

📅 تاریخ توزیع: 
نامشخص

📖 توضیحات:
دقت کنید متناسب با حجم سرمایه‌ای که وارد می‌کنید و مدت زمان سپرده‌گذاری شما، امتیاز دریافت خواهید کرد. 
برای شرکت در ایردراپ لینیا سرج، لطفاً موارد زیر را به ترتیب انجام دهید.
"""

    # Select an image to send
    # Replace with the actual path to your image
    image_filename = os.path.join(
        'img', 'airdrop', 'linea_surge', 'linea_surge.png')

    # Send the image along with the text and buttons
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(image_filename, 'rb'),
        caption=text,
        reply_markup=key_markup,
        parse_mode="HTML"
    )

    return GlobalState.getInstance().LINEA_SURGE_AIRDROP


async def air_drop_linea_surge_menu_over(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # global chat_id

    # Delete the previous photo if it exists
    # Use.get() method to avoid KeyError if chat_id not found
    if len(GlobalState.getInstance().message_ids.get(GlobalState.getInstance().chat_id, [])) == 1:
        await context.bot.delete_message(chat_id=GlobalState.getInstance().chat_id, message_id=GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id][0])
        GlobalState.getInstance().message_ids[GlobalState.getInstance().chat_id].pop(0)

    return GlobalState.getInstance().LINEA_SURGE_AIRDROP
