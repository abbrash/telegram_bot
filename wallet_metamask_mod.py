import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

from globals_mod import GlobalState

### <<<-------------------------------------------- Metamask Wallet Menu -------------------------------------------->>> ###
async def wallet_metamask_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

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
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="wallet_menu")]
    ]
    key_markup = InlineKeyboardMarkup(keyboard)

    text = "لطفاً برای دیدن آموزش هر بخش روی دکمه مورد نظر کلیک کنید:"

    # Select an image to send
    # Replace with the actual path to your image
    image_filename = os.path.join('img', 'wallet', 'metamask', 'metamask_wallet_img.jpg')

    # Send the image along with the text and buttons
    sent_message = await context.bot.send_photo(
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

    return GlobalState.getInstance().METAMASK_WALLET


### <<<-------------------------------------------- Metamask - Create -------------------------------------------->>> ###

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
    image_directory = 'img/wallet/metamask/create'
    img_add = image_directory
    image_filename = f'{image_directory}/{str(GlobalState.getInstance().current_index_metamask_create_wallet + 1).zfill(2)}.png'

    # Ensure current_index stays within the bounds of available images
    GlobalState.getInstance().current_index_metamask_create_wallet = max(
        0, min(GlobalState.getInstance().current_index_metamask_create_wallet, len(os.listdir(img_add)) - 1))

    # Define your list of captions here
    captions_list = [
        """ابتدا وارد سایت MetaMask شوید.
روی گزینه Download for کلیک کنید.
""",
        """تیک مربوط به موافقت با قوانین را زده و روی گزینه Create a new wallet کلیک کنید.""",
        """روی گزینه I agree کلیک کنید. """,
        """در مرحله باید یک رمز عبور (حداقل 8 کاراکتری) برای کیف پول خود ایجاد کنید. 
رمز عبور خود را در کادر اول وارد کرده و دوباره در کادر پایین تکرار کنید. 
گزینه مشخص شده را فعال کنید و روی Create a new wallet کلیک کنید.
""",
        """روی گزینه Secure my wallet (recommended) کلیک کنید.""",
        """در این مرحله 12 واژه انگلیسی برای شما نمایش داده می‌شود. 
این کلمات را به صورت صحیح و با ترتیب نشان داده شده در جای امنی ذخیره کنید.
دقت کنید هر شخصی با استفاده از این 12 کلمه روی هر دستگاهی می‌تواند به کیف پول شما دسترسی داشته باشد.
به هیچ عنوان این کلمات نباید با کسی به اشتراک گذاشته شود. 
در صورت مفقود شدن کلمات بازیابی، کیف پول شما غیرقابل استفاده خواهد بود. 
روی گزینه Reveal Secret Recovery Phrase کلیک کنید.
""",
        """در این بخش کلمات بازیابی کیف پول شما نمایش داده می‌شود. 
روی Copy to clipboard کلیک کنید و در جای امنی ذخیره کنید. (برای اطمینان بیشتر می‌توانید کلمات بازیابی را روی کاغذ نوشته و بصورت فیزیکی این اطلاعات را نگهداری کنید.)
روی Next کلیک کنید.
""",
        """با استفاده از کلماتی که در اختیار دارید، جاهای خالی را پر کنید و  روی Confirm کلیک کنید.""",
        """کیف پول شما با موفقیت ساخته شد.
روی Got it! کلیک کنید.
""",
        """برای دسترسی راحت‌تر به کیف پولتان، می‌توانید extension آن را در مرورگر خود فعال کنید.
در اینجا توضیحات مربوط مورد نیاز نمایش داده شده است.
روی Next کلیک کنید
""",
        """در این مرحله extension کیف پول شما با موفقیت به مرورگر اضافه شده است.
روی Done کلیک کنید.
""",
        """برای دسترسی به کیف پولتان روی extension آن در نوار بالا و سمت راست مرورگر خود کلیک کنید.""",
        """پس از وارد کردن رمزعبور، کیف پول شما آماده استفاده است.
        ❌❌❌توضیحات امنیتی:
پس از ساخت کیف پول‌های غیرمتمرکز، عبارت بازیابی 12 تا 24 کلمه‌ای برای شما تولید می‌شود. 
دقت کنید هر شخصی در هر جای دنیا می‌تواند با استفاده از عبارت بازیابی، به کیف پول شما دسترسی داشته باشد.
پس هیچ وقت و تحت هیچ شرایطی نباید عبارت بازیابی کیف پول خود را با کسی به اشتراک بگذارید. 

برای دسترسی به کیف پولتان و برای امنیت بیشتر، باید برای آن یک رمزعبور ایجاد کنید و برای ورود به کیف‌پولتان به این رمزعبور نیاز خواهید داشت. 

دقت کنید شما برای بازیابی کیف‌پولتان تنها به عبارت بازیابی نیاز دارید. می‌توانید کیف پول خود را روی چند دستگاه بصورت همزمان استفاده کنید. مثلاً برای ساخت کیف‌پول از لپ‌تاپ استفاده کنید و با نصب اپلیکیشن آن روی گوشی همراه، کیف‌پول خود را روی گوشی خود نیز بازیابی کنید. در این حالت در اپلیکیشن گوشی، عبارت بازیابی از شما درخواست می‌شود. پس از آن شما باید یک رمزعبور برای دسترسی به کیف پول خود روی گوشی ایجاد کنید. این رمزعبور می‌تواند کاملاً متفاوت با رمزعبور کیف‌پول شما که روی لپ‌تاپ نصب شده باشد. 
"""
    ]

    # Construct caption with current index and total number of photos
    caption = captions_list[GlobalState.getInstance().current_index_metamask_create_wallet]

    # Construct InlineKeyboardMarkup based on current message index
    buttons = []
    if GlobalState.getInstance().current_index_metamask_create_wallet == 0:
        buttons = [
            [InlineKeyboardButton("➡️ بعدی", callback_data=str(GlobalState.getInstance().current_index_metamask_create_wallet + 1))],
            [InlineKeyboardButton("بازگشت به منوی کیف پول متامسک 🏠⬅️ ", callback_data="metamask_menu_over")]
        ]
    elif GlobalState.getInstance().current_index_metamask_create_wallet == len(os.listdir(img_add)) - 1:
        buttons = [
            [InlineKeyboardButton("🎉🥳 تامام!", callback_data="metamask_menu_over")],
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

    return GlobalState.getInstance().METAMASK_WALLET_CREATE


### <<<-------------------------------------------- Metamask - Restore  -------------------------------------------->>> ###
### <<<-------------------------------------------- Metamask - Send -------------------------------------------->>> ###
### <<<-------------------------------------------- Metamask - Receive -------------------------------------------->>> ###
### <<<-------------------------------------------- Metamask - Swap -------------------------------------------->>> ###
### <<<-------------------------------------------- Metamask - Bridge -------------------------------------------->>> ###
### <<<-------------------------------------------- Metamask - Stake -------------------------------------------->>> ###
