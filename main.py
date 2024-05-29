from decouple import config
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters

from main_menu_mod import *
from phantom_airdrop import *
from linea_surge_airdrop import *
from register import *
from wallet_menu_mod import *
from exchange import *
from metamask_wallet_mod import *


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(
        '6264022397:AAF0AfVhD1YvP-Mqk8qwEAi_awRhC8XQxQw').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            GlobalState.getInstance().START_ROUTES: [   # The buttons callbacks of the "Main Menu"
                CallbackQueryHandler(submit_email, pattern="^" + "submit_email" + "$"),
                CallbackQueryHandler(local_exchange, pattern="^" + "local_exchange" + "$"),
                CallbackQueryHandler(global_exchange, pattern="^" + "global_exchange" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$"),
                CallbackQueryHandler(air_drop_menu, pattern="^" + "air_drops" + "$"),
                CallbackQueryHandler(wallet_menu, pattern="^" + "wallet_menu" + "$"),
                CallbackQueryHandler(air_drop_phantom_menu, pattern="^" + "air_drop_phantom_menu" + "$"),
                CallbackQueryHandler(air_drop_linea_surge_menu, pattern="^" + "air_drop_linea_surge_menu" + "$"),
                CallbackQueryHandler(wallet_menu, pattern="^" + "wallet_menu" + "$")
            ],
            GlobalState.getInstance().WALLET: [  # The buttons callbacks of the "Wallet Menu"
                CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$"),
                # CallbackQueryHandler(wallet_phantom_menu, pattern="^" + "phantom_menu" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            GlobalState.getInstance().METAMASK_WALLET: [  # The buttons callbacks of the "MetaMask Menu"
                CallbackQueryHandler(wallet_metamask_create, pattern="^" + "metamask_wallet_create" + "$"),
                # CallbackQueryHandler(wallet_metamask_restore, pattern="^" + "metamask_wallet_restore" + "$"),
                # CallbackQueryHandler(wallet_metamask_send, pattern="^" + "metamask_wallet_send" + "$"),
                # CallbackQueryHandler(wallet_metamask_receive, pattern="^" + "metamask_wallet_receive" + "$"),
                # CallbackQueryHandler(wallet_metamask_swap, pattern="^" + "metamask_wallet_swap" + "$"),
                # CallbackQueryHandler(wallet_metamask_bridge, pattern="^" + "metamask_wallet_bridge" + "$"),
                # CallbackQueryHandler(wallet_metamask_stake, pattern="^" + "metamask_wallet_stake" + "$"),
                CallbackQueryHandler(wallet_menu, pattern="^" + "wallet_menu" + "$")
            ],
                GlobalState.getInstance().METAMASK_WALLET_CREATE: [  # The buttons callbacks of the ... 
                CallbackQueryHandler(wallet_metamask_create, pattern="^(\d+)$"),
                CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu_over" + "$")
            ],
            GlobalState.getInstance().END_ROUTES: [  # The buttons callbacks of the ... 
                CallbackQueryHandler(start_over, pattern="^" + "main_menu" + "$")
            ],
            GlobalState.getInstance().SEND_IMG: [
                CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            ],
            GlobalState.getInstance().PH_AIRDROP: [  # The buttons callbacks of the "Phantom Airdrop Menu"
                CallbackQueryHandler(air_drop_phantom_swap, pattern="^" + "phantom_swap" + "$"),
                CallbackQueryHandler(air_drop_phantom_stake, pattern="^" + "phantom_stake" + "$"),
                CallbackQueryHandler(air_drop_phantom_unstake, pattern="^" + "phantom_unstake" + "$"),
                CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            ],
            GlobalState.getInstance().PH_AIRDROP_SWAP: [
                CallbackQueryHandler(air_drop_phantom_swap, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_phantom_menu_over, pattern="^" + "air_drop_phantom_menu_over" + "$")
            ],
            GlobalState.getInstance().PH_AIRDROP_STAKE: [
                CallbackQueryHandler(air_drop_phantom_stake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_phantom_menu_over, pattern="^" + "air_drop_phantom_menu_over" + "$")
            ],
            GlobalState.getInstance().PH_AIRDROP_UNSTAKE: [
                CallbackQueryHandler(air_drop_phantom_unstake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_phantom_menu_over, pattern="^" + "air_drop_phantom_menu_over" + "$")
            ],
            GlobalState.getInstance().LINEA_SURGE_AIRDROP: [
                CallbackQueryHandler(air_drop_linea_surge_stake, pattern="^" + "linea_surge_stake" + "$"),
                CallbackQueryHandler(air_drop_linea_surge_unstake, pattern="^" + "linea_surge_unstake" + "$"),
                CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            ],
            GlobalState.getInstance().LINEA_SURGE_AIRDROP_STAKE: [
                CallbackQueryHandler(air_drop_linea_surge_stake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_linea_surge_menu_over, pattern="^" + "air_drop_linea_surge_menu_over" + "$")
            ],
            GlobalState.getInstance().LINEA_SURGE_AIRDROP_UNSTAKE: [
                CallbackQueryHandler(air_drop_linea_surge_unstake, pattern="^(\d+)$"),
                CallbackQueryHandler(air_drop_linea_surge_menu_over, pattern="^" + "air_drop_linea_surge_menu_over" + "$")
            ],
            GlobalState.getInstance().EMAIL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_email)
            ]
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(
        allowed_updates=Update.ALL_TYPES, poll_interval=3, timeout=60
    )

### <<<------------------------------------------------------------------------------------------------------------>>> ###
### <<<------------------------------------------------------------------------------------------------------------>>> ###
### <<<-------------------------------------------- Initiation The Bot -------------------------------------------->>> ###
### <<<------------------------------------------------------------------------------------------------------------>>> ###
### <<<------------------------------------------------------------------------------------------------------------>>> ###


# Load the email_ids dictionary when the bot starts
GlobalState.getInstance().data_base = load_data_base()

print('Starting up bot...')

Tk = config('token')

if __name__ == "__main__":
    main()
