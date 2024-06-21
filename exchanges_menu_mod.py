import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from globals_mod import GlobalState
from admins_mod import *

### <<<-------------------------------------------- Exchanges Menu -------------------------------------------->>> ###
async def exchanges_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        [InlineKeyboardButton("صرافی نوبیتکس (Nobitex) ", callback_data="exchange_nobitex_menu")],
        [InlineKeyboardButton("صرافی بیت‌پین (BitPin)", callback_data="exchange_bitpin_menu")],
        [InlineKeyboardButton("صرافی بینگ‌اکس (BingX)", callback_data="exchange_bingx_menu")],
        [InlineKeyboardButton("صرافی کوینکس (CoinEx)", callback_data="exchange_coinex_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
برای صرافی‌های داخلی طبق دستورالعمل وبسایت صرافی مورد نظر عمل کنید. 
آموزش ثبت‌نام در صرافی‌های خارجی نیز بصورت جداگانه فراهم شده است. 
"""

# Select an image to send
    image_filename = os.path.join('img', 'exchange', 'exchanges_logo.jpg').replace('\\', '/')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update._effective_user.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML",
                protect_content=protect_content
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content
                                           )

    else:
        await context.bot.send_photo(
            chat_id=update._effective_user.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML",
            protect_content=protect_content
        )

    return GlobalState.getInstance().EXCHANGES_MENU

### <<<-------------------------------------------- Nobitex Exchange Menu -------------------------------------------->>> ###
async def exchange_nobitex_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        [InlineKeyboardButton("لینک ثبت‌نام در صرافی نوبیتکس", url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton("بازگشت به منوی صرافی‌ها🏠⬅️ ", callback_data="exchanges_menu")]
    ]

    key_markup = InlineKeyboardMarkup(keyboard)
    text = """لطفاً برای ثبت‌نام در صرافی نوبیتکس روی دکمه "ثبت نام" کلیک کنید. 
با استفاده از این لینک می‌توانید 15 درصد از کارمزد معاملات خود را به حسابتان در صرافی بازگردانید. 
"""

# Select an image to send
    image_filename = os.path.join('img', 'exchange', 'local_exchange', 'nobitex_logo.jpg').replace('\\', '/')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update._effective_user.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML",
                protect_content=protect_content
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content
                                           )

    else:
        await context.bot.send_photo(
            chat_id=update._effective_user.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML",
            protect_content=protect_content
        )

    return GlobalState.getInstance().EXCHANGE_NOBITEX_MENU

### <<<-------------------------------------------- BitPin Exchange Menu -------------------------------------------->>> ###
async def exchange_bitpin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        [InlineKeyboardButton("لینک ثبت‌نام در صرافی بیت‌پین", url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton("بازگشت به منوی صرافی‌ها🏠⬅️ ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """لطفاً برای ثبت‌نام در صرافی بیت‌پین روی دکمه "ثبت نام" کلیک کنید. 
با استفاده از این لینک می‌توانید 15 درصد از کارمزد معاملات خود را به حسابتان در صرافی بازگردانید. 
"""

    # Select an image to send
    image_filename = os.path.join('img', 'exchange', 'local_exchange', 'bitpin_logo.jpg').replace('\\', '/')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update._effective_user.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML",
                protect_content=protect_content
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content
                                           )

    else:
        await context.bot.send_photo(
            chat_id=update._effective_user.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML",
            protect_content=protect_content
        )

    return GlobalState.getInstance().EXCHANGE_BITPIN_MENU

### <<<-------------------------------------------- BingX Exchange Menu -------------------------------------------->>> ###
async def exchange_bingx_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    GlobalState.getInstance().first_time_loop_bingx_reg = True
    GlobalState.getInstance().current_index_bingx_reg = 0

    keyboard = [
        [InlineKeyboardButton("آموزش ثبت‌نام", callback_data="exchange_bingx_reg_tutorial")],
        [InlineKeyboardButton("صرافی بینگ‌اکس (BingX)", url='https://bingx.com/invite/NLQIKZI2')],
        [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """لطفاً برای ثبت‌نام در صرافی بینگ‌اکس روی دکمه "ثبت‌نام" کلیک کنید. 
با استفاده از این لینک می‌توانید 5 درصد از کارمزد معاملات خود را به حسابتان در صرافی بازگردانید. 
با استفاده از بخش "آموزش ثبت‌نام" می‌توانید مراحل ثبت‌نام در صرافی را بصورت قدم به قدم ملاحظه بفرمایید.
"""

    # Select an image to send
    image_filename = os.path.join('img', 'exchange', 'global_exchange', 'bingx_logo.png').replace('\\','/')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update._effective_user.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML",
                protect_content=protect_content
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content
                                           )

    else:
        await context.bot.send_photo(
            chat_id=update._effective_user.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML",
            protect_content=protect_content
        )

    return GlobalState.getInstance().EXCHANGE_BINGX_MENU

### <<<-------------------------------------------- Coinex Exchange Menu -------------------------------------------->>> ###
async def exchange_coinex_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    GlobalState.getInstance().first_time_loop_coinex_reg = True
    GlobalState.getInstance().current_index_coinex_reg = 0

    keyboard = [
        [InlineKeyboardButton("آموزش ثبت‌نام", callback_data="exchange_coinex_reg_tutorial")],
        [InlineKeyboardButton("صرافی کوینکس (CoinEx)", url='https://www.coinex.com/register?refer_code=s95m7')],
        [InlineKeyboardButton("بازگشت  🏠 ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """لطفاً برای ثبت‌نام در صرافی کوینکس روی دکمه "ثبت‌نام" کلیک کنید. 
با استفاده از این لینک می‌توانید 7.5 درصد از کارمزد معاملات خود را به حسابتان در صرافی بازگردانید. 
با استفاده از بخش "آموزش ثبت‌نام" می‌توانید مراحل ثبت‌نام در صرافی را بصورت قدم به قدم ملاحظه بفرمایید.
"""
    
    # Select an image to send
    image_filename = os.path.join('img', 'exchange', 'global_exchange', 'coinex_logo.jpg').replace('\\','/')

    # Send the image along with the text and buttons
    if query.message and query.message.text:
        try:
            await query.delete_message()
            await context.bot.send_photo(
                chat_id=update._effective_user.id,
                photo=open(image_filename, 'rb'),
                caption=text,
                reply_markup=key_markup,
                parse_mode="HTML",
                protect_content=protect_content
            )

        except BadRequest:
            await context.bot.send_message(chat_id=update._effective_user.id,
                                           text=text,
                                           reply_markup=key_markup,
                                           protect_content=protect_content
                                           )

    else:
        await context.bot.send_photo(
            chat_id=update._effective_user.id,
            photo=open(image_filename, 'rb'),
            caption=text,
            reply_markup=key_markup,
            parse_mode="HTML",
            protect_content=protect_content
        )

    return GlobalState.getInstance().EXCHANGE_COINEX_MENU


## <<<-------------------------------------------- BingX Exchange Register Tutorial -------------------------------------------->>> ###
async def exchange_bingx_reg_tutorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bingx_reg:
            await query.delete_message()
            GlobalState.getInstance().current_index_bingx_reg = 0
            GlobalState.getInstance().first_time_loop_bingx_reg = False
        else:
            GlobalState.getInstance().current_index_bingx_reg = int(query.data)
    elif query.data == "exchange_bingx_reg_tutorial":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bingx_reg = 0
        GlobalState.getInstance().first_time_loop_bingx_reg = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/bingx_reg_tutorial'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bingx_reg + 1).zfill(2)}.jpg'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bingx_reg = max(
        0, min(GlobalState.getInstance().current_index_bingx_reg, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """در کادر 1 آدرس ایمیل خود را وارد کنید و یک رمز عبور دلخواه انتخاب کنید. """, 
        """کد ارسال شده به ایمیلتان را در این بخش وارد کنید و روی Claim Reward کلیک کنید.""",
        """روی آیکون مربوط به حساب کاربری کلیک کنید و از منوی باز شده روی Account & Security کلیک کنید.""",
        """در مقابل گزینه Google Authenticator روی Link کلیک کنید.""",
        """با اسکن کردن QR Code های نمایش داده شده برنامه Google Authenticator را از گوگل‌پلی یا اپ‌استور دانلود و نصب کنید.
روی Next کلیک کنید.
        """,
        """عبارت نمایش داده شده را در جای امن ذخیره کنید. 
با استفاده از گوشی خود وارد برنامه Google Authenticator شوید، با استفاده از گزینه Scan a QR code کد نمایش داده شده را اسکن کنید. 
دقت کنید پس از انجام این کار، باید ایمیلی که با استفاده از آن در صرافی BingX ثبت نام کردید در برنامه اضافه شده باشد. 
روی Next کلیک کنید. 
        """,
        """روی Get Code کلیک کنید و رمز ارسال شده به ایمیلتان را در اینجا وارد کنید. 
وارد برنامه Google Authenticator شوید و رمز 6 رقمی تولید شده را در این کادر وارد کنید.
روی Submit کلیک کنید. 
        """,
        """مجدداً وارد بخش Account & Security شوید، در بخش Anti-Phishing Code روی Set کلیک کنید. """,
        """یک کلمه 8 تا 20 کاراکتری انتخاب کنید. 
این کلمه در ایمیل ارسال شده از سمت صرافی برای شما نمایش داده می‌شود. به این ترتیب ایمیل‌های مشابه که به قصد سرقت اطلاعات شخصی شما ارسال شده‌اند قابل شناسایی خواهند بود. 
این کلمه باید نزد خودتان محفوظ بماند.
روی Continue کلیک کنید.
        """,
        """وارد برنامه Google Authenticator شوید و رمز 6 رقمی تولید شده را در این کادر وارد کنید."""
]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_bingx_reg]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bingx_reg == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_reg + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی بینگ‌اکس  🏠⬅️ ", callback_data="exchange_bingx_menu")]
        ]
    elif GlobalState.getInstance().current_index_bingx_reg == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_bingx_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_reg - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_reg - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_reg + 1))]
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
            protect_content=protect_content
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

    return GlobalState.getInstance().EXCHANGE_BINGX_REG


### <<<-------------------------------------------- CoinEx Exchange Register Tutorial -------------------------------------------->>> ###
async def exchange_coinex_reg_tutorial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_coinex_reg:
            await query.delete_message()
            GlobalState.getInstance().current_index_coinex_reg = 0
            GlobalState.getInstance().first_time_loop_coinex_reg = False
        else:
            GlobalState.getInstance().current_index_coinex_reg = int(query.data)
    elif query.data == "exchange_coinex_reg_tutorial":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_coinex_reg = 0
        GlobalState.getInstance().first_time_loop_coinex_reg = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/coinex_reg_tutorial'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_coinex_reg + 1).zfill(2)}.jpg'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_coinex_reg = max(
        0, min(GlobalState.getInstance().current_index_coinex_reg, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """در کادر مشخص شده آدرس ایمیل خود را وارد کنید و یک رمز دلخواه انتخاب کنید. 
روی دکمه Sign Up کلیک کنید.
""",
        """در کادر مشخص شده روی گزینه Send Code کلیک کنید. رمز 6 رقمی ارسال شده توسط صرافی به آدرس ایمیلتان را در اینجا وارد کنید و روی دکمه Confirm کلیک کنید.""",
        """در تصویر نمایش داده شده باید اشیاء مشخص شده را به ترتیب در تصویر پیدا کنید. """,
        """مانند نمونه فعالیت مورد نظر را انجام دهید و روی OK کلیک کنید.""",
        """روی آیکون حساب کاربری کلیک کنید و از منوی باز شده روی Security Settings کلیک کنید.""",
        """روبه‌روی گزینه TOTP Verification روی دکمه Set کلیک کنید.""",
        """روی گزینه Next کلیک کنید.""",
        """روی گزینه Next کلیک کنید.""",
        """روی گزینه Next کلیک کنید.""",
        """روی گزینه Next کلیک کنید.""",
        """روی گزینه Done کلیک کنید.""",
        """در کادر شماره 1 روی Send code کلیک کنید و رمز 6 رقمی ارسال شده به ایمیلتان را در این کادر وارد کنید. 
روی Next کلیک کنید.
""",
        """عبارت نمایش داده شده تحت عنوان Private key را در جای امنی ذخیره کنید.
نرم افزار Google Authenticator را از گوگل‌پلی یا اپ‌استور روی گوشی خود نصب کنید، وارد نرم افزار شوید و روی گزینه Scan a QR code کلیک کنید، سپس QR Code نمایش داده شده را با گوشی اسکن کنید.
روی دکمه Next کلیک کنید.
""",
        """وارد نرم افزار Google Authenticator شوید و کد 6 رفمی تولید شده برای اکانت CoinEx خود را در کادر روبه‌رو وارد کنید و روی Next کلیک کنید.""",
        """روی Done کلیک کنید.""",
        """مجدداً به صفحه Security Settings برگردید و روی Set مقابل Anti-Phishing Code کلیک کنید. """,
        """روی Send code کلیک کنید و رمز 6 رقمی ارسال شده به ایمیلتان را در این کادر وارد کنید. 
روی Next کلیک کنید.
""",
        """یک کلمه 8 تا 20 کاراکتری انتخاب کنید. 
این کلمه در ایمیل ارسال شده از سمت صرافی برای شما نمایش داده می‌شود. به این ترتیب ایمیل‌های مشابه که به قصد سرقت اطلاعات شخصی شما ارسال شده‌اند قابل شناسایی خواهند بود. 
این کلمه باید نزد خودتان محفوظ بماند.
روی Next کلیک کنید.
""",
        """روی Done کلیک کنید.""",
        """نمونه ایمیل ارسال شده با Anti-Phishing Code"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_coinex_reg]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_coinex_reg == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_reg + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی کوینکس  🏠⬅️ ", callback_data="exchange_coinex_menu")]
        ]
    elif GlobalState.getInstance().current_index_coinex_reg == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_coinex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_reg - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_reg - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_reg + 1))]
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
            protect_content=protect_content
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

    return GlobalState.getInstance().EXCHANGE_COINEX_REG
