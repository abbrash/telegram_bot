import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

from globals_mod import GlobalState

### <<<-------------------------------------------- MetaMask Wallet Menu -------------------------------------------->>> ###
async def wallet_metamask_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    GlobalState.getInstance().current_index_wallet_metamask_create = 0
    GlobalState.getInstance().first_time_loop_wallet_metamask_create = True

    keyboard = [
        [InlineKeyboardButton("ساخت کیف پول متامسک", callback_data="wallet_metamask_create")],
        [InlineKeyboardButton("وارد کردن (Import) کیف پول از پیش ساخته شده", callback_data="wallet_metamask_import")],
        [InlineKeyboardButton("ساخت حساب جدید (Add a New Account)", callback_data="wallet_metamask_add_acc")],
        [InlineKeyboardButton("اضافه‌کردن حساب از پیش ساخته شده (Import Account)", callback_data="wallet_metamask_import_acc")],
        [InlineKeyboardButton("ذخیره‌کردن عبارت بازیابی (Secret Recovery Phrase)", callback_data="wallet_metamask_save_srp")],
        [InlineKeyboardButton("ذخیره‌کردن کلید خصوصی (Private Key)", callback_data="wallet_metamask_save_pk")],
        [InlineKeyboardButton("اضافه‌کردن شبکه (Add Network)", callback_data="wallet_metamask_add_network")],
        # [InlineKeyboardButton("اضافه‌کردن توکن (Import Token)", callback_data="wallet_metamask_import_token")],
        # [InlineKeyboardButton("ارسال (Send) رمزارز از کیف پول", callback_data="wallet_metamask_send")],
        # [InlineKeyboardButton("دریافت (Receive) رمزارز در کیف پول", callback_data="wallet_metamask_receive")],
        # [InlineKeyboardButton("تبدیل رمزارز (Swap)", callback_data="wallet_metamask_swap")],
        # [InlineKeyboardButton("انتقال رمزارز میان شبکه‌ای (Bridge) درون کیف پول", callback_data="wallet_metamask_bridge")],
        # [InlineKeyboardButton("سپرده‌گذاری رمزارز (Stake)", callback_data="wallet_metamask_stake")],
        [InlineKeyboardButton("بازگشت به منوی کیف پول‌", callback_data="wallets_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = """لطفاً برای دیدن بخش‌های مختلف روی گزینه‌های زیر کلیک کنید.

Page: MetaMask_Menu"""

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

    return GlobalState.getInstance().WALLET_METAMASK_MENU


### <<<-------------------------------------------- MetaMask Wallet - Create -------------------------------------------->>> ###
async def wallet_metamask_create(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_create:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_create = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_create = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_create = int(query.data)
    elif query.data == "wallet_metamask_create":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_create = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_create = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/create'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_create + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_create = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_create, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
   """وارد سایت <a href="https://metamask.io/">متامسک</a> شوید.
روی گزینه Download for کلیک کنید.

01_Page: MetaMask_Create""",
"""تیک مربوط به موافقت با قوانین را زده و روی گزینه Create a new wallet کلیک کنید.

02_Page: MetaMask_Create""",
"""روی گزینه I agree کلیک کنید.

03_Page: MetaMask_Create""",
"""در مرحله باید یک رمز عبور (حداقل 8 کاراکتری) برای کیف پول خود ایجاد کنید.
رمز عبور خود را در کادر اول وارد کرده و دوباره در کادر پایین تکرار کنید.
گزینه مشخص شده را فعال کنید و روی Create a new wallet کلیک کنید.

04_Page: MetaMask_Create""",
"""روی گزینه Secure my wallet (recommended) کلیک کنید.

05_Page: MetaMask_Create""",
"""در این مرحله 12 واژه انگلیسی برای شما نمایش داده می‌شود.
این کلمات را به صورت صحیح و با ترتیب نشان داده شده در جای امنی ذخیره کنید.
دقت کنید هر شخصی با استفاده از این 12 کلمه روی هر دستگاهی می‌تواند به کیف پول شما دسترسی داشته باشد.
به هیچ عنوان این کلمات نباید با کسی به اشتراک گذاشته شود. در صورت مفقود شدن کلمات بازیابی، کیف پول شما غیرقابل استفاده خواهد بود.
روی گزینه Reveal Secret Recovery Phrase کلیک کنید.

06_Page: MetaMask_Create""",
"""در این بخش کلمات بازیابی کیف پول شما نمایش داده می‌شود.
روی Copy to clipboard کلیک کنید و در جای امنی ذخیره کنید. (برای اطمینان بیشتر می‌توانید کلمات بازیابی را روی کاغذ نوشته و بصورت فیزیکی این اطلاعات را نگهداری کنید.)
روی Next کلیک کنید.

07_Page: MetaMask_Create""",
"""با استفاده از کلماتی که در اختیار دارید، جاهای خالی را پر کنید و روی Confirm کلیک کنید.

08_Page: MetaMask_Create""",
"""کیف پول شما با موفقیت ساخته شد.
روی Got it! کلیک کنید.

09_Page: MetaMask_Create""",
"""برای دسترسی راحت‌تر به کیف پولتان، می‌توانید extension آن را در مرورگر خود فعال کنید.
در اینجا توضیحات مربوط مورد نیاز نمایش داده شده است.
روی Next کلیک کنید.

10_Page: MetaMask_Create""",
"""در این مرحله extension کیف پول شما با موفقیت به مرورگر اضافه شده است.
روی Done کلیک کنید.

11_Page: MetaMask_Create""",
"""برای دسترسی به کیف پولتان روی extension آن در نوار بالا و سمت راست مرورگر خود کلیک کنید.

12_Page: MetaMask_Create""",
"""پس از وارد کردن رمزعبور، کیف پول شما آماده استفاده است
 
❌❌❌توضیحات امنیتی:
پس از ساخت کیف پول‌های غیرحضانتی، عبارت بازیابی 12 تا 24 کلمه‌ای برای شما تولید می‌شود.
دقت کنید هر شخصی در هر جای دنیا می‌تواند با استفاده از عبارت بازیابی، به کیف پول شما دسترسی داشته باشد.
پس هیچ وقت و تحت هیچ شرایطی نباید عبارت بازیابی کیف پول خود را با کسی به اشتراک بگذارید.
برای دسترسی به کیف پولتان و برای امنیت بیشتر، باید برای آن یک رمزعبور ایجاد کنید و برای ورود به کیف‌پولتان به این رمزعبور نیاز خواهید داشت.
 
دقت کنید شما برای بازیابی کیف‌پولتان تنها به عبارت بازیابی نیاز دارید. می‌توانید کیف پول خود را روی چند دستگاه بصورت همزمان استفاده کنید. مثلاً برای ساخت کیف‌پول از لپ‌تاپ استفاده کنید و با نصب اپلیکیشن آن روی گوشی همراه، کیف‌پول خود را روی گوشی خود نیز بازیابی کنید. در این حالت در اپلیکیشن گوشی، عبارت بازیابی از شما درخواست می‌شود. پس از آن شما باید یک رمزعبور برای دسترسی به کیف پول خود روی گوشی ایجاد کنید. این رمزعبور می‌تواند کاملاً متفاوت با رمزعبور کیف‌پول شما که روی لپ‌تاپ نصب شده باشد.

13_Page: MetaMask_Create"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_wallet_metamask_create]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_create == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_create + 1))],
            [InlineKeyboardButton("بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_create == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_create - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_create - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_create + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_CREATE


### <<<-------------------------------------------- Metamask - Import  -------------------------------------------->>> ###
async def wallet_metamask_import(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_import:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_import = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_import = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_import = int(query.data)
    elif query.data == "wallet_metamask_import":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_import = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_import = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/import'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_import + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_import = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_import, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد سایت <a href="https://metamask.io/">متامسک</a> شوید.
روی گزینه Download for کلیک کنید.

01_Page: MetaMask_Import""",
"""تیک مربوط به موافقت با قوانین را زده و روی گزینه Import an existing wallet کلیک کنید.

02_Page: MetaMask_Import""",
"""روی گزینه I agree کلیک کنید.

03_Page: MetaMask_Import""",
"""عبارت بازیابی کیف پول خود را وارد کنید.
روی دکمه Confirm Secret Recovery Phrase کلیک کنید.

04_Page: MetaMask_Import""",
"""در این مرحله باید یک رمز عبور (حداقل 8 کاراکتری) برای کیف پول خود ایجاد کنید.
رمز عبور خود را در کادر اول وارد کرده و دوباره در کادر پایین تکرار کنید.
گزینه مشخص شده را فعال کنید و روی Import my wallet کلیک کنید.

05_Page: MetaMask_Import""",
"""روی دکمه Got it! کلیک کنید.

06_Page: MetaMask_Import""",
"""برای دسترسی راحت‌تر به کیف پولتان، می‌توانید extension آن را در مرورگر خود فعال کنید.
در اینجا توضیحات مربوط مورد نیاز نمایش داده شده است.
روی Next کلیک کنید.

07_Page: MetaMask_Import""",
"""در این مرحله extension کیف پول شما با موفقیت به مرورگر اضافه شده است.
روی Done کلیک کنید.

08_Page: MetaMask_Import""",
                     """کیف پول شما با موفقیت به مرورگرتان اضافه شده است.

09_Page: MetaMask_Import"""

    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_import]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_import == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import + 1))],
            [InlineKeyboardButton("بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_import == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_IMPORT


### <<<-------------------------------------------- Metamask - Add a New Account  -------------------------------------------->>> ###
async def wallet_metamask_add_acc(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_add_acc:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_add_acc = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_add_acc = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_add_acc = int(query.data)
    elif query.data == "wallet_metamask_add_acc":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_add_acc = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_add_acc = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/add_acc'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_add_acc + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_add_acc = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_add_acc, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد کیف پول متامسک شوید.
روی Account 1 کلیک کنید.

01_Page: MetaMask_Add_New_Acc""",
"""روی دکمه Add account or hardware wallet کلیک کنید.

02_Page: MetaMask_Add_New_Acc""",
"""روی گزینه Add a new account کلیک کنید.

03_Page: MetaMask_Add_New_Acc""",
"""یک اسم برای حساب جدید خود وارد کنید.
روی دکمه Create کلیک کنید.

04_Page: MetaMask_Add_New_Acc""",
                     """اکانت جدید شما در کیف پول با موفقیت ساخته شده است.
 
⚠️⚠️⚠️
عبارت بازیابی مخفی (Secret Recovery Phrase “SRP”)
عبارت بازیابی مخفی، یک عبارت 12 کلمه‌ای منحصر به فرد است که در زمان ساخت کیف پول متامسک شما ایجاد می‌شود.
آن را به عنوان کلید اصلی خود در نظر بگیرید. تمام حساب‌های (Accounts) شما از نظر ریاضی از این عبارت مشتق شده‌اند.
برای بازیابی کیف پول متامسک خود به عبارت بازیابی مخفی (SRP) نیاز دارید.
عبارت بازیابی مخفی (SRP) کیف پول خود را در جای امنی نزد خود نگه دارید و تحت هیچ شرایطی آن را با کسی به اشتراک نگذارید. هر کسی که به عبارت بازیابی مخفی شما دسترسی داشته باشد می‌تواند به دارایی‌های موجود در کیف پول شما نیز دسترسی داشته باشد.
 
⚠️⚠️⚠️
کلیدهای خصوصی (Private Keys)
هر حساب (Account) در کیف پول متامسک شما کلید خصوصی مخصوص خود را دارد.
این کلیدها مانند کلیدهای جداگانه برای درهای خاص (حساب) در کیف پول شما هستند.
اگر می خواهید حسابی را به کیف پول دیگری وارد کنید، از کلید خصوصی آن استفاده کنید.
کلیدهای خصوصی کیف پول خود را در جای امنی نزد خود نگهدارید و تحت هیچ شرایطی آن‌ها را با کسی به اشتراک نگذارید.
 
❌❌❌
شما نیازی به ذخیره کلیدهای خصوصی برای حساب های ایجاد شده در متامسک ندارید، اما باید به طور ایمن عبارت بازیابی مخفی (SRP) خود را ذخیره کنید. برای هر حسابی که از یک کیف پول دیگر با عبارت بازیابی مخفی (SRP) متفاوت تولید شده است و در کیف پول شما اضافه (Import) شده است، باید کلیدهای خصوصی آن حساب را نزد خود نگهداری کنید.

05_Page: MetaMask_Add_New_Acc"""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_add_acc]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_add_acc == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_add_acc + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_add_acc == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_add_acc - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_add_acc - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_add_acc + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_ADD_ACC


### <<<-------------------------------------------- Metamask - Import Account -------------------------------------------->>> ###
async def wallet_metamask_import_acc(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_import_acc:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_import_acc = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_import_acc = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_import_acc = int(query.data)
    elif query.data == "wallet_metamask_add_acc":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_import_acc = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_import_acc = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/add_acc'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_import_acc + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_import_acc = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_import_acc, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد کیف پول متامسک شوید.
روی Account 1 کلیک کنید.

01_Page: MetaMask_Import_Acc""",
"""روی دکمه Add account or hardware wallet کلیک کنید.

02_Page: MetaMask_Import_Acc""",
"""روی گزینه Import account کلیک کنید.

03_Page: MetaMask_Import_Acc""",
"""کلید خصوصی (Private Key) اکانت خود را وارد کنید. 
روی دکمه Import کلیک کنید.

04_Page: MetaMask_Import_Acc""",
"""اکانت شما با موفقیت به کیف پول اضافه شده است.
 
⚠️⚠️⚠️
در نظر داشته باشید، کیف پول متامسک اصطلاحاً یک کیف پول قطعی (Deterministic) است. به این معنی که از عبارت بازیابی مخفی (SRP) شما، همیشه همان حساب‌ها با همان آدرس‌ها و کلیدهای خصوصی و با ترتیب مشابه ایجاد می‌شود.
 
متامسک با بررسی حساب‌های (Accounts) قبلی شما به ترتیب صعودی (یعنی Account 2 و سپس Account 3 و غیره) در صورت امکان (با فرض اینکه قبلاً این حساب‌ها را وارد (Import) نکرده باشید) حساب‌های بعدی شما را اضافه می‌کند. اگر موجودی ETH غیرصفر باشد، حساب‌ها به‌طور خودکار دوباره اضافه می‌شوند. با این حال، این فرآیند زمانی پایان می‌یابد که متامسک با یک حساب با موجودی ETH صفر روبه‌رو شود؛ بنابراین اولین حساب با موجودی ETH صفر (و هر حسابی بعد از آن) دیگر به کیف پول اضافه نخواهد شد.
 
به خاطر داشته باشید که این فرآیند فقط موجودی ETH را در شبکه اصلی اتریوم (Ethereum Mainnet) بررسی می‌کند، بنابراین سایر رمزارزها یا توکن‌ها در شبکه‌های دیگر منجر به اضافه‌شدن خودکار حساب شما نمی‌شوند.
 
برای حساب‌هایی که به طور خودکار مجدداً اضافه نمی‌شوند، باید حساب را به روش استاندارد اضافه کنید. به عنوان مثال، اگر تعدادی رمزارز در Account 4 دارید، اما Account 4 به طور خودکار اضافه نمی‌شود زیرا رمزارزهای موجود، ETH روی شبکه اصلی نیستند، تنها کاری که باید انجام دهید این است که به صورت دستی حساب‌ها را اضافه کنید تا زمانی که به Account 4 برسید. Account 4 قبل از بازیابی با Account 4 بعد از بازیابی، صرف نظر از هر نامی که قبلاً انتخاب کرده‌اید، مطابقت دارد.
 
اگر نیاز به اضافه‌کردن مجدد حساب‌ها به این روش دارید، نگران متفاوت بودن آدرس حساب نباشید. آدرس‌ها از نظر رمزنگاری به صورت قطعی از کلید خصوصی شما مشتق می شوند، به این معنی که آن‌ها همیشه یکسان خواهند بود و از آنجایی که یک حساب اتریوم، پس از ایجاد، به طور دائم وجود دارد، می‌توانید فعالیت‌ خود را در ادامه تراکنش‌های گذشته با حساب‌های وارد شده از سر بگیرید.

05_Page: MetaMask_Import_Acc"""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_import_acc]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_import_acc == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_import_acc + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_import_acc == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_import_acc - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import_acc - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import_acc + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_IMPORT_ACC


### <<<-------------------------------------------- Metamask - Save SRP -------------------------------------------->>> ###
async def wallet_metamask_save_srp(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_save_srp:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_save_srp = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_save_srp = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_save_srp = int(query.data)
    elif query.data == "wallet_metamask_save_srp":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_save_srp = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_save_srp = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/save_srp'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_save_srp + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_save_srp = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_save_srp, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد کیف پول متامسک شوید.
روی علامت سه‌نقطه و سپس روی گزینه Settings کلیک کنید.

01_Page: MetaMask_Save_SRP""",
"""روی گزینه Security & privacy کلیک کنید.

02_Page: MetaMask_Save_SRP""",
"""روی دکمه Reveal Secret Recovery Phrase کلیک کنید.

03_Page: MetaMask_Save_SRP""",
"""روی دکمه Get started کلیک کنید.

04_Page: MetaMask_Save_SRP""",
"""روی گزینه Can’t help you کلیک کنید.

05_Page: MetaMask_Save_SRP""",
"""روی دکمه Continue کلیک کنید.

06_Page: MetaMask_Save_SRP""",
"""روی گزینه You’re being scammed کلیک کنید.

07_Page: MetaMask_Save_SRP""",
"""روی دکمه Continue کلیک کنید.

08_Page: MetaMask_Save_SRP""",
"""رمزعبور کیف پول خود را وارد کرده و روی دکمه Next کلیک کنید.

09_Page: MetaMask_Save_SRP""",
"""روی دکمه Hold to reveal SRP کلیک کنید و نگه‌دارید.

10_Page: MetaMask_Save_SRP""",
"""در این بخش عبارت بازیابی مخفی (SRP) کیف پول شما نمایش داده شده است. روی دکمه Copy to clipboard کلیک کنید و آن را در جای امنی ذخیره کنید.

11_Page: MetaMask_Save_SRP"""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_save_srp]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_save_srp == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_save_srp + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_save_srp == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_save_srp - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_save_srp - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_save_srp + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_SAVE_SRP


### <<<-------------------------------------------- Metamask - Save PK -------------------------------------------->>> ###
async def wallet_metamask_save_pk(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_save_pk:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_save_pk = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_save_pk = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_save_pk = int(query.data)
    elif query.data == "wallet_metamask_save_pk":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_save_pk = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_save_pk = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/save_pk'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_save_pk + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_save_pk = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_save_pk, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد کیف پول متامسک شوید.
روی Account 1 کلیک کنید.

01_Page: MetaMask_Save_PK""",
"""روی علامت سه‌نقطه روبه‌روی اکانتی که می‌خواهید کلید خصوصی آن را ذخیره کنید، کلیک کنید.
روی گزینه Account details کلیک کنید.

02_Page: MetaMask_Save_PK""",
"""روی دکمه Show private key کلیک کنید.

03_Page: MetaMask_Save_PK""",
"""رمزعبور کیف پول خود را وارد کرده و روی دکمه Confirm کلیک کنید.

04_Page: MetaMask_Save_PK""",
"""روی دکمه Hold to reveal Private Key کلیک کنید و نگه‌دارید.

05_Page: MetaMask_Save_PK""",
"""در این بخش کلید خصوصی حساب موردنظر نمایش داده می‌شود.
آن را در جای امنی ذخیره کنید.
روی دکمه Done کلیک کنید.

06_Page: MetaMask_Save_PK"""
                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_save_pk]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_save_pk == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_save_pk + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_save_pk == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_save_pk - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_save_pk - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_save_pk + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_SAVE_PK


### <<<-------------------------------------------- Metamask - Add Network -------------------------------------------->>> ###
async def wallet_metamask_add_network(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_add_network:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_add_network = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_add_network = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_add_network = int(query.data)
    elif query.data == "wallet_metamask_add_network":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_add_network = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_add_network = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/add_network'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_add_network + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_add_network = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_add_network, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = ["""وارد کیف پول متامسک شوید.
روی گزینه مشخص شده در بالا سمت چپ کلیک کنید.

01_Page: MetaMask_Add_Network""",
"""روی دکمه Add network کلیک کنید.

02_Page: MetaMask_Add_Network""",
"""روی گزینه Add روبه‌روی شبکه‌ای که می‌خواهید به کیف پولتان اضافه شود کلیک کنید.
(به عنوان مثال در اینجا شبکه Arbitrum One انتخاب شده است.)

03_Page: MetaMask_Add_Network""",
"""روی دکمه Approve کلیک کنید.

04_Page: MetaMask_Add_Network""",
"""شبکه مورد نظر با موفقیت به کیف پول شما اضافه شد.
برای انتخاب شبکه جدید روی Switch to “Arbitrum one” کلیک کنید.

05_Page: MetaMask_Add_Network"""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_add_network]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_add_network == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_add_network + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_add_network == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_add_network - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_add_network - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_add_network + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_ADD_NETWORK


### <<<-------------------------------------------- Metamask - Import Token -------------------------------------------->>> ###
async def wallet_metamask_import_token(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_import_token:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_import_token = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_import_token = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_import_token = int(query.data)
    elif query.data == "wallet_metamask_import_token":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_import_token = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_import_token = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/import_token'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_import_token + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_import_token = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_import_token, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_import_token]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_import_token == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_import_token + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_import_token == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_import_token - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import_token - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_import_token + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_IMPORT_TOKEN



### <<<-------------------------------------------- Metamask - Send -------------------------------------------->>> ###
async def wallet_metamask_send(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_send:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_send = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_send = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_send = int(query.data)
    elif query.data == "wallet_metamask_send":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_send = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_send = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/send'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_send + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_send = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_send, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_send]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_send == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_send + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_send == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_send - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_send - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_send + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_SEND


### <<<-------------------------------------------- Metamask - Receive -------------------------------------------->>> ###
async def wallet_metamask_receive(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_receive:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_receive = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_receive = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_receive = int(query.data)
    elif query.data == "wallet_metamask_receive":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_receive = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_receive = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/receive'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_receive + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_receive = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_receive, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_receive]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_receive == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_receive + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_receive == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_receive - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_receive - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_receive + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_RECEIVE


### <<<-------------------------------------------- Metamask - Swap -------------------------------------------->>> ###
async def wallet_metamask_swap(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_swap:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_swap = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_swap = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_swap = int(query.data)
    elif query.data == "wallet_metamask_swap":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_swap = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_swap = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/swap'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_swap + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_swap = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_swap, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_swap]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_swap == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_swap + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_swap == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_swap - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_swap - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_swap + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_SWAP


### <<<-------------------------------------------- Metamask - Bridge -------------------------------------------->>> ###
async def wallet_metamask_bridge(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_bridge:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_bridge = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_bridge = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_bridge = int(query.data)
    elif query.data == "wallet_metamask_bridge":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_bridge = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_bridge = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/bridge'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_bridge + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_bridge = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_bridge, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_bridge]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_bridge == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_bridge + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_bridge == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_bridge - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_bridge - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_bridge + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_BRIDGE


### <<<-------------------------------------------- Metamask - Stake -------------------------------------------->>> ###
async def wallet_metamask_stake(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    await query.answer()

    # Check if query.data is a digit
    if query.data.isdigit():
        if GlobalState.getInstance().first_time_loop_wallet_metamask_stake:
            await query.delete_message()
            GlobalState.getInstance().current_index_wallet_metamask_stake = 0
            GlobalState.getInstance().first_time_loop_wallet_metamask_stake = False
        else:
            GlobalState.getInstance().current_index_wallet_metamask_stake = int(query.data)
    elif query.data == "wallet_metamask_bridge":
        # Reset current_index when "air_drop_01" is clicked
        await query.delete_message()
        GlobalState.getInstance().current_index_wallet_metamask_stake = 0
        GlobalState.getInstance().first_time_loop_wallet_metamask_stake = False

    # Use img_add to dynamically generate the image filename based on the current index
    image_directory = 'img/wallet/metamask/bridge'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_wallet_metamask_stake + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_wallet_metamask_stake = max(
        0, min(GlobalState.getInstance().current_index_wallet_metamask_stake, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [""""""

                     ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance(
    ).current_index_wallet_metamask_stake]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_wallet_metamask_stake == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_stake + 1))],
            [InlineKeyboardButton(
                "بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="wallet_metamask_menu")]
        ]
    elif GlobalState.getInstance().current_index_wallet_metamask_stake == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton(
                "🎉🥳 تامام!", callback_data="wallet_metamask_menu")],
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(
                GlobalState.getInstance().current_index_wallet_metamask_stake - 1))]
        ]
    else:
        buttons = [
            [InlineKeyboardButton("قبلی ⬅️", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_stake - 1)),
             InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_wallet_metamask_stake + 1))]
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

    return GlobalState.getInstance().WALLET_METAMASK_STAKE
