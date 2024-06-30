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
        [InlineKeyboardButton("نوبیتکس (Nobitex) 🇮🇷🇮🇷", callback_data="exchange_nobitex_menu")],
        [InlineKeyboardButton("بیت‌پین (BitPin) 🇮🇷🇮🇷", callback_data="exchange_bitpin_menu")],
        [InlineKeyboardButton("بینگ‌اکس (BingX) 🇪🇺🇺🇸", callback_data="exchange_bingx_menu")],
        [InlineKeyboardButton("کوینکس (CoinEx) 🇪🇺🇺🇸", callback_data="exchange_coinex_menu")],
        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠 ", callback_data="main_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """با استفاده از لینک‌های قرارداده شده در این بخش می‌توانید در صرافی‌های پیشنهادی ثبت‌نام کنید. 
برای صرافی‌های داخلی (نوبیتکس و بیت‌پین) طبق دستورالعمل وبسایت صرافی مورد نظر عمل کنید. 
آموزش ثبت‌نام در صرافی‌های خارجی (کوینکس و بینگ‌اکس) نیز بصورت جداگانه فراهم شده است.

Page: Exchanges_Menu"""

# # Select an image to send
#     image_filename = os.path.join('img', 'exchange', 'exchanges_logo.jpg').replace('\\', '/')

#     # Send the image along with the text and buttons
#     if query.message and query.message.text:
#         try:
#             await query.delete_message()
#             await context.bot.send_photo(
#                 chat_id=update._effective_user.id,
#                 photo=open(image_filename, 'rb'),
#                 caption=text,
#                 reply_markup=key_markup,
#                 parse_mode="HTML",
#                 protect_content=protect_content
#             )

#         except BadRequest:
#             await context.bot.send_message(chat_id=update._effective_user.id,
#                                            text=text,
#                                            reply_markup=key_markup,
#                                            protect_content=protect_content
#                                            )

#     else:
#         await context.bot.send_photo(
#             chat_id=update._effective_user.id,
#             photo=open(image_filename, 'rb'),
#             caption=text,
#             reply_markup=key_markup,
#             parse_mode="HTML",
#             protect_content=protect_content
#         )

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

    return GlobalState.getInstance().EXCHANGES_MENU

### <<<-------------------------------------------- Nobitex Exchange Menu -------------------------------------------->>> ###
async def exchange_nobitex_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        [InlineKeyboardButton("لینک ثبت‌نام در صرافی نوبیتکس", url='https://nobitex.ir/signup/?refcode=1557073')],
        [InlineKeyboardButton("واریز ریالی به صرافی", callback_data="exchange_nobitex_deposit_rials")],
        [InlineKeyboardButton("برداشت ریالی از صرافی", callback_data="exchange_nobitex_withdraw_rials")],
        [InlineKeyboardButton("واریز رمزارز به صرافی", callback_data="exchange_nobitex_deposit")],
        [InlineKeyboardButton("برداشت رمزارز از صرافی", callback_data="exchange_nobitex_withdraw")],
        [InlineKeyboardButton("خرید و فروش در صرافی", callback_data="exchange_nobitex_trade_spot")],
        [InlineKeyboardButton("بازگشت به منوی صرافی‌ها🏠⬅️ ", callback_data="exchanges_menu")]
    ]

    key_markup = InlineKeyboardMarkup(keyboard)
    text = """لطفاً برای ثبت‌نام در صرافی نوبیتکس روی دکمه "ثبت نام" کلیک کنید.
با استفاده از این لینک می‌توانید 15 درصد از کارمزد معاملات خود را به حسابتان در صرافی بازگردانید.

Page: Nobitex_Menu"""

# Select an image to send
    image_filename = os.path.join('img', 'exchange', 'local_exchange', 'nobitex', 'nobitex_logo.jpg').replace('\\', '/')

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

### <<<-------------------------------------------- Nobitex Exchange Deposit Rials -------------------------------------------->>> ###
async def exchange_nobitex_deposit_rials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_nobitex_deposit_rials:
            await query.delete_message()
            GlobalState.getInstance().current_index_nobitex_deposit_rials = 0
            GlobalState.getInstance().first_time_loop_nobitex_deposit_rials = False
        else:
            GlobalState.getInstance().current_index_nobitex_deposit_rials = int(query.data)
    elif query.data == "exchange_nobitex_deposit_rials":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_nobitex_deposit_rials = 0
        GlobalState.getInstance().first_time_loop_nobitex_deposit_rials = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/nobitex/nobitex_deposit_rials'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_nobitex_deposit_rials + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_nobitex_deposit_rials = max(
        0, min(GlobalState.getInstance().current_index_nobitex_deposit_rials, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد سایت <a href="https://nobitex.ir">نوبیتکس</a> شوید.
روی گزینه کیف پول و سپس روی "واریز" کلیک کنید.

Page: Nobitex_Deposit_Rials_01""",

"""  
از لیست کارت‌های بانکی موجود، کارتی که می‌خواهید واریز را با استفاده از آن انجام دهید را انتخاب کنید.
مبلغ واریز را وارد کنید و سپس روی گزینه "واریز شتابی" کلیک کنید.
 
⚠️ ⚠️ ⚠️ به نکاتی ذکرشده از طرف صرافی دقت کنید.

Page: Nobitex_Deposit_Rials_02"""
]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_nobitex_deposit_rials]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_nobitex_deposit_rials == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_nobitex_deposit_rials + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی نوبیتکس  🏠⬅️ ", callback_data="exchange_nobitex_menu")]
        ]
    elif GlobalState.getInstance().current_index_nobitex_deposit_rials == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_nobitex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_deposit_rials - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_deposit_rials - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_nobitex_deposit_rials + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_NOBITEX_DEPOSIT_RIALS


### <<<-------------------------------------------- Nobitex Exchange Withdraw Rials -------------------------------------------->>> ###
async def exchange_nobitex_withdraw_rials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_nobitex_withdraw_rials:
            await query.delete_message()
            GlobalState.getInstance().current_index_nobitex_withdraw_rials = 0
            GlobalState.getInstance().first_time_loop_nobitex_withdraw_rials = False
        else:
            GlobalState.getInstance().current_index_nobitex_withdraw_rials = int(query.data)
    elif query.data == "exchange_nobitex_withdraw_rials":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_nobitex_withdraw_rials = 0
        GlobalState.getInstance().first_time_loop_nobitex_withdraw_rials = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/nobitex/nobitex_withdraw_rials'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_nobitex_withdraw_rials + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_nobitex_withdraw_rials = max(
        0, min(GlobalState.getInstance().current_index_nobitex_withdraw_rials, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد سایت <a href="https://nobitex.ir">نوبیتکس</a> شوید.
روی گزینه "کیف پول" و سپس روی "برداشت" کلیک کنید.

Page: Nobitex_Withdraw_Rials_01
""",
"""
از لیست شماره شباهای موجود، شماره‌ای که می‌خواهید وجه برداشت شده به آن واریز شود را انتخاب کنید.
مبلغ برداشت را وارد کنید.
کد شناسایی دو عاملی تولید شده توسط برنامه Google Authenticator گوشی را وارد کرده و سپس روی گزینه "برداشت" کلیک کنید.
 
⚠️ ⚠️ ⚠️ به نکاتی ذکرشده از طرف صرافی دقت کنید.

Page: Nobitex_Withdraw_Rials_02"""
]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_nobitex_withdraw_rials]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_nobitex_withdraw_rials == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_nobitex_withdraw_rials + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی نوبیتکس  🏠⬅️ ", callback_data="exchange_nobitex_menu")]
        ]
    elif GlobalState.getInstance().current_index_nobitex_withdraw_rials == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_nobitex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_withdraw_rials - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_withdraw_rials - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_nobitex_withdraw_rials + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_NOBITEX_WITHDRAW_RIALS

### <<<-------------------------------------------- Nobitex Exchange Deposit -------------------------------------------->>> ###
async def exchange_nobitex_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_nobitex_deposit:
            await query.delete_message()
            GlobalState.getInstance().current_index_nobitex_deposit = 0
            GlobalState.getInstance().first_time_loop_nobitex_deposit = False
        else:
            GlobalState.getInstance().current_index_nobitex_deposit = int(query.data)
    elif query.data == "exchange_nobitex_deposit":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_nobitex_deposit = 0
        GlobalState.getInstance().first_time_loop_nobitex_deposit = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/nobitex/nobitex_deposit'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_nobitex_deposit + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_nobitex_deposit = max(
        0, min(GlobalState.getInstance().current_index_nobitex_deposit, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد سایت <a href="https://nobitex.ir">نوبیتکس</a> شوید.
روی گزینه کیف پول و سپس روی "واریز" کلیک کنید.

Page: Nobitex_Deposit_01
                     """,
                     """از بخش بالا گزینه "رمزارز" را انتخاب کنید.
در کادر مشخص شده، رمزارز خود را انتخاب کنید. (به عنوان نمونه در اینجا پالیگان (MATIC) انتخاب شده است.)
شبکه واریز را انتخاب کنید. (به عنوان نمونه در اینجا Polygon انتخاب شده است.)
دقت کنید انتقال موفق دارایی شما نیازمند تعداد مشخصی تأیید در شبکه است که این تعداد با توجه به شبکه انتخاب شده متفاوت است. (برای شبکه Polygon به حداقل 128 تأیید در شبکه نیاز است.)
آدرس واریز ارز انتخاب شده روی شبکه مورد نظر برای شما تولید شده است. آن را کپی کرده و به عنوان آدرس کیف پول مقصد استفاده کنید.
 
❌❌❌دقت کنید این آدرس تنها برای ارز و شبکه انتخاب شده قابل استفاده است. (در این مثال، فقط رمزارز پالیگان بر روی شبکه Polygon به این آدرس واریز می‌شود.) در صورتی که رمزارزی دیگر یا همین رمزارز ولی روی شبکه‌ای دیگر به این آدرس ارسال شود، دارایی ارسال شده برای همیشه از دست خواهد رفت.
 
 
⚠️ ⚠️ ⚠️به نکاتی ذکرشده از طرف صرافی دقت کنید.
 
 Page: Nobitex_Deposit_02"""
]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_nobitex_deposit]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_nobitex_deposit == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_nobitex_deposit + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی نوبیتکس  🏠⬅️ ", callback_data="exchange_nobitex_menu")]
        ]
    elif GlobalState.getInstance().current_index_nobitex_deposit == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_nobitex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_deposit - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_deposit - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_nobitex_deposit + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_NOBITEX_DEPOSIT


### <<<-------------------------------------------- Nobitex Exchange Withdraw -------------------------------------------->>> ###
async def exchange_nobitex_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_nobitex_withdraw:
            await query.delete_message()
            GlobalState.getInstance().current_index_nobitex_withdraw = 0
            GlobalState.getInstance().first_time_loop_nobitex_withdraw = False
        else:
            GlobalState.getInstance().current_index_nobitex_withdraw = int(query.data)
    elif query.data == "exchange_nobitex_withdraw":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_nobitex_withdraw = 0
        GlobalState.getInstance().first_time_loop_nobitex_withdraw = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/nobitex/nobitex_withdraw'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_nobitex_withdraw + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_nobitex_withdraw = max(
        0, min(GlobalState.getInstance().current_index_nobitex_withdraw, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد سایت <a href="https://nobitex.ir">نوبیتکس</a> شوید.
روی گزینه "کیف پول" و سپس روی "برداشت" کلیک کنید.

Page: Nobitex_Withdraw_01
""",
"""                    
رمزارز مورد نظرتان را انتخاب کنید.
شبکه‌ای که می‌خواهد رمزارز انتخاب شده روی آن منتقل شود را انتخاب کنید.
آدرس کیف‌پول مقصد روی شبکه انتخاب شده (در این مثال: شبکه پالیگان) را وارد کنید.
مقدار ارزی که می‌خواهید برداشت کنید مشخص کنید.
کد شناسایی دو عاملی تولید شده توسط برنامه Google Authenticator گوشی را وارد کرده و سپس روی گزینه "برداشت" کلیک کنید.
 
⚠️ ⚠️ ⚠️مقدار کارمزد برداشت و مقدار خالص دارایی انتقال داده شده برای شما نمایش داده می‌شود.
 
⚠️ ⚠️ ⚠️ به نکاتی ذکرشده از طرف صرافی دقت کنید.

Page: Nobitex_Withdraw_02"""
]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_nobitex_withdraw]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_nobitex_withdraw == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_nobitex_withdraw + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی نوبیتکس  🏠⬅️ ", callback_data="exchange_nobitex_menu")]
        ]
    elif GlobalState.getInstance().current_index_nobitex_withdraw == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_nobitex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_withdraw - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_withdraw - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_nobitex_withdraw + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_NOBITEX_WITHDRAW


### <<<-------------------------------------------- Nobitex Exchange Spot Trading -------------------------------------------->>> ###
async def exchange_nobitex_trade_spot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_nobitex_trade_spot:
            await query.delete_message()
            GlobalState.getInstance().current_index_nobitex_trade_spot = 0
            GlobalState.getInstance().first_time_loop_nobitex_trade_spot = False
        else:
            GlobalState.getInstance().current_index_nobitex_trade_spot = int(query.data)
    elif query.data == "exchange_nobitex_trade_spot":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_nobitex_trade_spot = 0
        GlobalState.getInstance().first_time_loop_nobitex_trade_spot = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/nobitex/nobitex_trade_spot'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_nobitex_trade_spot + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_nobitex_trade_spot = max(
        0, min(GlobalState.getInstance().current_index_nobitex_trade_spot, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد سایت <a href="https://nobitex.ir">نوبیتکس</a> شوید.
روی گزینه "معامله" و سپس روی "اسپات" کلیک کنید.

Page: Nobitex_SpotTrading_01
                     """,
                     """
مطابق با شکل، جفت ارز مورد نظرتان را انتخاب کنید.
 
گزینه "با تعیین قیمت" را انتخاب کنید.
برای خرید گزینه "خرید" و برای فروش گزینه "فروش" باید فعال باشد.
قیمت مورد نظرتان برای معامله را با توجه به لیست "سفارش‌های بازار" و قیمت کنونی مشخص کنید.
مقدار ارزی که می‌خواهید بخرید یا بفروشید را مشخص کنید.
روی دکمه خرید (در این مثال: خرید پالیگان) و یا فروش (در این مثال: فروش پالیگان) کلیک کنید.
سفارش شما در لیست "سفارش‌های بازار" قرار گرفته است. با توجه به قیمت تعیین‌شده از سوی شما، سفارش‌تان به صورت آنی یا با تأخیر انجام می‌شود.
 
قیمت مشخص شده در میانه لیست "سفارش‌های بازار" که با کادر خط‌چین مشخص شده است، قیمت کنونی رمزارز انتخابی را بر حسب "تومان" نمایش می‌دهد.
پس از انجام معامله، ارز مورد نظر به کیف پولتان واریز خواهد شد.
 
⚠️ ⚠️ ⚠️ درنظر داشته باشید که به جای واحد "ریال" از واحد "تومان" (IRT) در صرافی نوبیتکس استفاده می‌شود.

Page: Nobitex_SpotTrading_02"""
]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_nobitex_trade_spot]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_nobitex_trade_spot == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_nobitex_trade_spot + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی نوبیتکس  🏠⬅️ ", callback_data="exchange_nobitex_menu")]
        ]
    elif GlobalState.getInstance().current_index_nobitex_trade_spot == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_nobitex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_trade_spot - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_nobitex_trade_spot - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_nobitex_trade_spot + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_NOBITEX_TRADE_SPOT

### <<<-------------------------------------------- BitPin Exchange Menu -------------------------------------------->>> ###
async def exchange_bitpin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    keyboard = [
        [InlineKeyboardButton("لینک ثبت‌نام در صرافی بیت‌پین", url='https://bitpin.ir/signup/?ref=aP0DtoVG')],
        [InlineKeyboardButton("بازگشت به منوی صرافی‌ها🏠⬅️ ", callback_data="exchanges_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)
    text = """لطفاً برای ثبت‌نام در صرافی بیت‌پین روی دکمه "ثبت نام" کلیک کنید. 
با استفاده از این لینک می‌توانید 15 درصد از کارمزد معاملات خود را به حسابتان در صرافی بازگردانید. 
"""

    # Select an image to send
    image_filename = os.path.join('img', 'exchange', 'local_exchange', 'bitpin','bitpin_logo.jpg').replace('\\', '/')

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


### <<<-------------------------------------------- BitPin Exchange Deposit Rials -------------------------------------------->>> ###
async def exchange_bitpin_deposit_rials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bitpin_deposit_rials:
            await query.delete_message()
            GlobalState.getInstance().current_index_bitpin_deposit_rials = 0
            GlobalState.getInstance().first_time_loop_bitpin_deposit_rials = False
        else:
            GlobalState.getInstance().current_index_bitpin_deposit_rials = int(query.data)
    elif query.data == "exchange_bitpin_deposit_rials":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bitpin_deposit_rials = 0
        GlobalState.getInstance().first_time_loop_bitpin_deposit_rials = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/bitpin/bitpin_deposit_rials'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bitpin_deposit_rials + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bitpin_deposit_rials = max(
        0, min(GlobalState.getInstance().current_index_bitpin_deposit_rials, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bitpin_deposit_rials]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bitpin_deposit_rials == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_deposit_rials + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بیت‌پین  🏠⬅️ ", callback_data="exchange_bitpin_menu")]
        ]
    elif GlobalState.getInstance().current_index_bitpin_deposit_rials == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bitpin_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_deposit_rials - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bitpin_deposit_rials - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bitpin_deposit_rials + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BITPIN_DEPOSIT_RIALS


### <<<-------------------------------------------- BitPin Exchange Withdraw Rials -------------------------------------------->>> ###
async def exchange_bitpin_withdraw_rials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bitpin_withdraw_rials:
            await query.delete_message()
            GlobalState.getInstance().current_index_bitpin_withdraw_rials = 0
            GlobalState.getInstance().first_time_loop_bitpin_withdraw_rials = False
        else:
            GlobalState.getInstance().current_index_bitpin_withdraw_rials = int(query.data)
    elif query.data == "exchange_bitpin_withdraw_rials":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bitpin_withdraw_rials = 0
        GlobalState.getInstance().first_time_loop_bitpin_withdraw_rials = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/bitpin/bitpin_withdraw_rials'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bitpin_withdraw_rials + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bitpin_withdraw_rials = max(
        0, min(GlobalState.getInstance().current_index_bitpin_withdraw_rials, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bitpin_withdraw_rials]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bitpin_withdraw_rials == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_withdraw_rials + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بیت‌پین  🏠⬅️ ", callback_data="exchange_bitpin_menu")]
        ]
    elif GlobalState.getInstance().current_index_bitpin_withdraw_rials == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bitpin_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_withdraw_rials - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bitpin_withdraw_rials - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bitpin_withdraw_rials + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BITPIN_WITHDRAW_RIALS

### <<<-------------------------------------------- BitPin Exchange Deposit -------------------------------------------->>> ###
async def exchange_bitpin_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bitpin_deposit:
            await query.delete_message()
            GlobalState.getInstance().current_index_bitpin_deposit = 0
            GlobalState.getInstance().first_time_loop_bitpin_deposit = False
        else:
            GlobalState.getInstance().current_index_bitpin_deposit = int(query.data)
    elif query.data == "exchange_bitpin_deposit":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bitpin_deposit = 0
        GlobalState.getInstance().first_time_loop_bitpin_deposit = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/bitpin/bitpin_deposit'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bitpin_deposit + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bitpin_deposit = max(
        0, min(GlobalState.getInstance().current_index_bitpin_deposit, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bitpin_deposit]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bitpin_deposit == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_deposit + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بیت‌پین  🏠⬅️ ", callback_data="exchange_bitpin_menu")]
        ]
    elif GlobalState.getInstance().current_index_bitpin_deposit == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bitpin_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_deposit - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bitpin_deposit - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bitpin_deposit + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BITPIN_DEPOSIT


### <<<-------------------------------------------- BitPin Exchange Withdraw -------------------------------------------->>> ###
async def exchange_bitpin_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bitpin_withdraw:
            await query.delete_message()
            GlobalState.getInstance().current_index_bitpin_withdraw = 0
            GlobalState.getInstance().first_time_loop_bitpin_withdraw = False
        else:
            GlobalState.getInstance().current_index_bitpin_withdraw = int(query.data)
    elif query.data == "exchange_bitpin_withdraw":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bitpin_withdraw = 0
        GlobalState.getInstance().first_time_loop_bitpin_withdraw = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/bitpin/bitpin_withdraw'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bitpin_withdraw + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bitpin_withdraw = max(
        0, min(GlobalState.getInstance().current_index_bitpin_withdraw, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bitpin_withdraw]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bitpin_withdraw == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_withdraw + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بیت‌پین  🏠⬅️ ", callback_data="exchange_bitpin_menu")]
        ]
    elif GlobalState.getInstance().current_index_bitpin_withdraw == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bitpin_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_withdraw - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bitpin_withdraw - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bitpin_withdraw + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BITPIN_WITHDRAW


### <<<-------------------------------------------- BitPin Exchange Spot Trading -------------------------------------------->>> ###
async def exchange_bitpin_trade_spot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bitpin_trade_spot:
            await query.delete_message()
            GlobalState.getInstance().current_index_bitpin_trade_spot = 0
            GlobalState.getInstance().first_time_loop_bitpin_trade_spot = False
        else:
            GlobalState.getInstance().current_index_bitpin_trade_spot = int(query.data)
    elif query.data == "exchange_bitpin_trade_spot":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bitpin_trade_spot = 0
        GlobalState.getInstance().first_time_loop_bitpin_trade_spot = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/local_exchange/bitpin/bitpin_trade_spot'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bitpin_trade_spot + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bitpin_trade_spot = max(
        0, min(GlobalState.getInstance().current_index_bitpin_trade_spot, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bitpin_trade_spot]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bitpin_trade_spot == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_trade_spot + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بیت‌پین  🏠⬅️ ", callback_data="exchange_bitpin_menu")]
        ]
    elif GlobalState.getInstance().current_index_bitpin_trade_spot == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bitpin_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bitpin_trade_spot - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bitpin_trade_spot - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bitpin_trade_spot + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BITPIN_TRADE_SPOT

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
    image_filename = os.path.join('img', 'exchange', 'global_exchange', 'bingx', 'bingx_logo.png').replace('\\','/')

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
    image_directory = 'img/exchange/global_exchange/bingx/bingx_reg_tutorial'
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

### <<<-------------------------------------------- BingX Exchange Deposit -------------------------------------------->>> ###
async def exchange_bingx_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bingx_deposit:
            await query.delete_message()
            GlobalState.getInstance().current_index_bingx_deposit = 0
            GlobalState.getInstance().first_time_loop_bingx_deposit = False
        else:
            GlobalState.getInstance().current_index_bingx_deposit = int(query.data)
    elif query.data == "exchange_bingx_deposit":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bingx_deposit = 0
        GlobalState.getInstance().first_time_loop_bingx_deposit = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/bingx/bingx_deposit'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bingx_deposit + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bingx_deposit = max(
        0, min(GlobalState.getInstance().current_index_bingx_deposit, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bingx_deposit]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bingx_deposit == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_deposit + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی بینگ‌اکس  🏠⬅️ ", callback_data="exchange_bingx_menu")]
        ]
    elif GlobalState.getInstance().current_index_bingx_deposit == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_bingx_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_deposit - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_deposit - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_deposit + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BINGX_DEPOSIT


### <<<-------------------------------------------- BingX Exchange Withdraw -------------------------------------------->>> ###
async def exchange_bingx_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bingx_withdraw:
            await query.delete_message()
            GlobalState.getInstance().current_index_bingx_withdraw = 0
            GlobalState.getInstance().first_time_loop_bingx_withdraw = False
        else:
            GlobalState.getInstance().current_index_bingx_withdraw = int(query.data)
    elif query.data == "exchange_bingx_withdraw":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bingx_withdraw = 0
        GlobalState.getInstance().first_time_loop_bingx_withdraw = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/bingx/bingx_withdraw'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bingx_withdraw + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bingx_withdraw = max(
        0, min(GlobalState.getInstance().current_index_bingx_withdraw, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bingx_withdraw]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bingx_withdraw == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bingx_withdraw + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بینگ‌اکس  🏠⬅️ ", callback_data="exchange_bingx_menu")]
        ]
    elif GlobalState.getInstance().current_index_bingx_withdraw == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bingx_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bingx_withdraw - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_withdraw - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_withdraw + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BINGX_WITHDRAW


### <<<-------------------------------------------- BingX Exchange Spot Trading -------------------------------------------->>> ###
async def exchange_bingx_trade_spot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bingx_trade_spot:
            await query.delete_message()
            GlobalState.getInstance().current_index_bingx_trade_spot = 0
            GlobalState.getInstance().first_time_loop_bingx_trade_spot = False
        else:
            GlobalState.getInstance().current_index_bingx_trade_spot = int(query.data)
    elif query.data == "exchange_bingx_trade_spot":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bingx_trade_spot = 0
        GlobalState.getInstance().first_time_loop_bingx_trade_spot = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/bingx/bingx_trade_spot'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bingx_trade_spot + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bingx_trade_spot = max(
        0, min(GlobalState.getInstance().current_index_bingx_trade_spot, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bingx_trade_spot]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bingx_trade_spot == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bingx_trade_spot + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بینگ‌اکس  🏠⬅️ ", callback_data="exchange_bingx_menu")]
        ]
    elif GlobalState.getInstance().current_index_bingx_trade_spot == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bingx_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bingx_trade_spot - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_trade_spot - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_trade_spot + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BINGX_TRADE_SPOT

### <<<-------------------------------------------- BingX Exchange Futures Trading -------------------------------------------->>> ###
async def exchange_bingx_trade_futures(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_bingx_trade_futures:
            await query.delete_message()
            GlobalState.getInstance().current_index_bingx_trade_futures = 0
            GlobalState.getInstance().first_time_loop_bingx_trade_futures = False
        else:
            GlobalState.getInstance().current_index_bingx_trade_futures = int(query.data)
    elif query.data == "exchange_bingx_trade_futures":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_bingx_trade_futures = 0
        GlobalState.getInstance().first_time_loop_bingx_trade_futures = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/bingx/bingx_trade_futures'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_bingx_trade_futures + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_bingx_trade_futures = max(
        0, min(GlobalState.getInstance().current_index_bingx_trade_futures, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_bingx_trade_futures]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_bingx_trade_futures == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_bingx_trade_futures + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی صرافی بینگ‌اکس  🏠⬅️ ", callback_data="exchange_bingx_menu")]
        ]
    elif GlobalState.getInstance().current_index_bingx_trade_futures == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="exchange_bingx_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_bingx_trade_futures - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_bingx_trade_futures - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_bingx_trade_futures + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_BINGX_TRADE_FUTURES


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
    image_filename = os.path.join('img', 'exchange', 'global_exchange', 'coinex', 'coinex_logo.jpg').replace('\\','/')

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
    image_directory = 'img/exchange/global_exchange/coinex/coinex_reg_tutorial'
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


### <<<-------------------------------------------- CoinEx Exchange Deposit -------------------------------------------->>> ###
async def exchange_coinex_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_coinex_deposit:
            await query.delete_message()
            GlobalState.getInstance().current_index_coinex_deposit = 0
            GlobalState.getInstance().first_time_loop_coinex_deposit = False
        else:
            GlobalState.getInstance().current_index_coinex_deposit = int(query.data)
    elif query.data == "exchange_coinex_deposit":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_coinex_deposit = 0
        GlobalState.getInstance().first_time_loop_coinex_deposit = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/coinex/coinex_deposit'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_coinex_deposit + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_coinex_deposit = max(
        0, min(GlobalState.getInstance().current_index_coinex_deposit, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_coinex_deposit]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_coinex_deposit == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_deposit + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی کوینکس  🏠⬅️ ", callback_data="exchange_coinex_menu")]
        ]
    elif GlobalState.getInstance().current_index_coinex_deposit == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_coinex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_deposit - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_deposit - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_deposit + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_COINEX_DEPOSIT


### <<<-------------------------------------------- CoinEx Exchange Withdraw -------------------------------------------->>> ###
async def exchange_coinex_withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_coinex_withdraw:
            await query.delete_message()
            GlobalState.getInstance().current_index_coinex_withdraw = 0
            GlobalState.getInstance().first_time_loop_coinex_withdraw = False
        else:
            GlobalState.getInstance().current_index_coinex_withdraw = int(query.data)
    elif query.data == "exchange_coinex_withdraw":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_coinex_withdraw = 0
        GlobalState.getInstance().first_time_loop_coinex_withdraw = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/coinex/coinex_withdraw'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_coinex_withdraw + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_coinex_withdraw = max(
        0, min(GlobalState.getInstance().current_index_coinex_withdraw, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_coinex_withdraw]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_coinex_withdraw == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_withdraw + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی کوینکس  🏠⬅️ ", callback_data="exchange_coinex_menu")]
        ]
    elif GlobalState.getInstance().current_index_coinex_withdraw == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_coinex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_withdraw - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_withdraw - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_withdraw + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_COINEX_WITHDRAW


### <<<-------------------------------------------- CoinEx Exchange Spot Trading -------------------------------------------->>> ###
async def exchange_coinex_trade_spot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_coinex_trade_spot:
            await query.delete_message()
            GlobalState.getInstance().current_index_coinex_trade_spot = 0
            GlobalState.getInstance().first_time_loop_coinex_trade_spot = False
        else:
            GlobalState.getInstance().current_index_coinex_trade_spot = int(query.data)
    elif query.data == "exchange_coinex_trade_spot":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_coinex_trade_spot = 0
        GlobalState.getInstance().first_time_loop_coinex_trade_spot = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/coinex/coinex_trade_spot'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_coinex_trade_spot + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_coinex_trade_spot = max(
        0, min(GlobalState.getInstance().current_index_coinex_trade_spot, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_coinex_trade_spot]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_coinex_trade_spot == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_spot + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی کوینکس  🏠⬅️ ", callback_data="exchange_coinex_menu")]
        ]
    elif GlobalState.getInstance().current_index_coinex_trade_spot == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_coinex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_spot - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_spot - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_spot + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_COINEX_TRADE_SPOT

### <<<-------------------------------------------- CoinEx Exchange Futures Trading -------------------------------------------->>> ###
async def exchange_coinex_trade_futures(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    protect_content = not is_admin(update._effective_user.id)

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_coinex_trade_futures:
            await query.delete_message()
            GlobalState.getInstance().current_index_coinex_trade_futures = 0
            GlobalState.getInstance().first_time_loop_coinex_trade_futures = False
        else:
            GlobalState.getInstance().current_index_coinex_trade_futures = int(query.data)
    elif query.data == "exchange_coinex_trade_futures":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_coinex_trade_futures = 0
        GlobalState.getInstance().first_time_loop_coinex_trade_futures = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/exchange/global_exchange/coinex/coinex_trade_futures'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_coinex_trade_futures + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_coinex_trade_futures = max(
        0, min(GlobalState.getInstance().current_index_coinex_trade_futures, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_coinex_trade_futures]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_coinex_trade_futures == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_futures + 1))],
            [InlineKeyboardButton("بازگشت به منوی صرافی کوینکس  🏠⬅️ ", callback_data="exchange_coinex_menu")]
        ]
    elif GlobalState.getInstance().current_index_coinex_trade_futures == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="exchange_coinex_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_futures - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_futures - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_coinex_trade_futures + 1))]
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
            protect_content=protect_content,
            parse_mode='HTML'  # Add this line
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

    return GlobalState.getInstance().EXCHANGE_COINEX_TRADE_FUTURES