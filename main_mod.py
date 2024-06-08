from decouple import config
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters

from main_menu_mod import *
from airdrop_phantom_mod import *
from airdrop_linea_surge_mod import *
from register_mod import *
from wallet_menu_mod import *
from exchanges_menu_mod import *
from wallet_metamask_mod import *
from support_menu_mod import *

### <<<-------------------------------------------- Main Function -------------------------------------------->>> ###
def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(
        '7029020592:AAGYmkIiqRPL99oGfIW0vvyTIhSJYKDbl9U').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            GlobalState.getInstance().START_ROUTES: [   
                CallbackQueryHandler(exchanges_menu, pattern="^" + "exchanges_menu" + "$"),
                CallbackQueryHandler(airdrops_menu, pattern="^" + "airdrops_menu" + "$"),
                CallbackQueryHandler(exchanges_menu, pattern="^" + "exchanges_menu" + "$"),
                CallbackQueryHandler(support_menu, pattern="^" + "support_menu" + "$"),
                CallbackQueryHandler(submit_email, pattern="^" + "submit_email" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$"),
                CallbackQueryHandler(wallet_menu, pattern="^" + "wallet_menu" + "$"),
                CallbackQueryHandler(airdrop_phantom_menu, pattern="^" + "airdrop_phantom_menu" + "$"),
                CallbackQueryHandler(air_drop_linea_surge_menu, pattern="^" + "air_drop_linea_surge_menu" + "$")
            ],
            GlobalState.getInstance().EXCHANGES_MENU: [  
                CallbackQueryHandler(exchange_nobitex_menu, pattern="^" + "exchange_nobitex_menu" + "$"),
                CallbackQueryHandler(exchange_bitpin_menu, pattern="^" + "exchange_bitpin_menu" + "$"),
                CallbackQueryHandler(exchange_bingx_menu, pattern="^" + "exchange_bingx_menu" + "$"),
                CallbackQueryHandler(exchange_coinex_menu, pattern="^" + "exchange_coinex_menu" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            # GlobalState.getInstance().EXCHANGE_NOBITEX_MENU: [  
            #     CallbackQueryHandler(exchange_nobitex_reg_tutorial, pattern="^" + "exchange_nobitex_reg_tutorial" + "$"),
            #     CallbackQueryHandler(exchanges_menu, pattern="^" + "exchanges_menu" + "$")
            # ],
            # GlobalState.getInstance().EXCHANGE_BITPIN_MENU: [  
            #     CallbackQueryHandler(exchange_bitpin_reg_tutorial, pattern="^" + "exchange_bitpin_reg_tutorial" + "$"),
            #     CallbackQueryHandler(exchanges_menu, pattern="^" + "exchanges_menu" + "$")
            # ],
            # GlobalState.getInstance().EXCHANGE_BINGX_MENU: [  
            #     CallbackQueryHandler(exchange_bingx_reg_tutorial, pattern="^" + "exchange_bingx_reg_tutorial" + "$"),
            #     CallbackQueryHandler(exchanges_menu, pattern="^" + "exchanges_menu" + "$")
            # ],
            # GlobalState.getInstance().EXCHANGE_COINEX_MENU: [  
            #     CallbackQueryHandler(exchange_coinex_reg_tutorial, pattern="^" + "exchange_coinex_reg_tutorial" + "$"),
            #     CallbackQueryHandler(exchanges_menu, pattern="^" + "exchanges_menu" + "$")
            # ],
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
            # GlobalState.getInstance().SEND_IMG: [
            #     CallbackQueryHandler(airdrop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
            # ],
            GlobalState.getInstance().AIRDROPS_MENU: [
                CallbackQueryHandler(airdrop_phantom_menu, pattern="^" + "airdrop_phantom_menu" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_PHANTOM_MENU: [  # The buttons callbacks of the "Phantom Airdrop Menu"
                CallbackQueryHandler(airdrop_phantom_swap, pattern="^" + "airdrop_phantom_swap" + "$"),
                CallbackQueryHandler(airdrop_phantom_stake, pattern="^" + "airdrop_phantom_stake" + "$"),
                CallbackQueryHandler(airdrop_phantom_unstake, pattern="^" + "airdrop_phantom_unstake" + "$"),
                CallbackQueryHandler(airdrops_menu, pattern="^" + "airdrops_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_PHANTOM_SWAP: [
                CallbackQueryHandler(airdrop_phantom_swap, pattern="^(\d+)$"),
                CallbackQueryHandler(airdrop_phantom_menu, pattern="^" + "airdrop_phantom_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_PHANTOM_STAKE: [
                CallbackQueryHandler(airdrop_phantom_stake, pattern="^(\d+)$"),
                CallbackQueryHandler(airdrop_phantom_menu, pattern="^" + "airdrop_phantom_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_PHANTOM_UNSTAKE: [
                CallbackQueryHandler(airdrop_phantom_unstake, pattern="^(\d+)$"),
                CallbackQueryHandler(airdrop_phantom_menu, pattern="^" + "airdrop_phantom_menu" + "$")
            ],
            GlobalState.getInstance().LINEA_SURGE_AIRDROP: [
                CallbackQueryHandler(air_drop_linea_surge_stake, pattern="^" + "linea_surge_stake" + "$"),
                CallbackQueryHandler(air_drop_linea_surge_unstake, pattern="^" + "linea_surge_unstake" + "$"),
                # CallbackQueryHandler(air_drop_menu, pattern="^" + "back_to_air_drop_menu" + "$")
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
