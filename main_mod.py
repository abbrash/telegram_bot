from decouple import config
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters

from main_menu_mod import *
from airdrop_phantom_mod import *
from airdrop_linea_surge_mod import *
from register_mod import *
from wallets_menu_mod import *
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
                CallbackQueryHandler(wallets_menu, pattern="^" + "wallets_menu" + "$"),
                CallbackQueryHandler(support_menu, pattern="^" + "support_menu" + "$"),
                CallbackQueryHandler(submit_email, pattern="^" + "submit_email" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
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
            GlobalState.getInstance().AIRDROPS_MENU: [
                CallbackQueryHandler(airdrop_phantom_menu, pattern="^" + "airdrop_phantom_menu" + "$"),
                CallbackQueryHandler(airdrop_linea_surge_menu, pattern="^" + "airdrop_linea_surge_menu" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_PHANTOM_MENU: [  
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
            GlobalState.getInstance().AIRDROP_LINEA_SURGE_MENU: [
                CallbackQueryHandler(airdrop_linea_surge_stake, pattern="^" + "airdrop_linea_surge_stake" + "$"),
                CallbackQueryHandler(airdrop_linea_surge_unstake, pattern="^" + "airdrop_linea_surge_unstake" + "$"),
                CallbackQueryHandler(airdrops_menu, pattern="^" + "airdrops_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_LINEA_SURGE_STAKE: [
                CallbackQueryHandler(airdrop_linea_surge_stake, pattern="^(\d+)$"),
                CallbackQueryHandler(airdrop_linea_surge_menu, pattern="^" + "airdrop_linea_surge_menu" + "$")
            ],
            GlobalState.getInstance().AIRDROP_LINEA_SURGE_UNSTAKE: [
                CallbackQueryHandler(airdrop_linea_surge_unstake, pattern="^(\d+)$"),
                CallbackQueryHandler(airdrop_linea_surge_menu, pattern="^" + "airdrop_linea_surge_menu" + "$")
            ],
            GlobalState.getInstance().WALLETS_MENU: [  
                CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "wallet_metamask_menu" + "$"),
                # CallbackQueryHandler(wallet_phantom_menu, pattern="^" + "wallet_phantom_menu" + "$"),
                # CallbackQueryHandler(wallet_rainbow_menu, pattern="^" + "wallet_rainbow_menu" + "$"),
                # CallbackQueryHandler(wallet_pontem_menu, pattern="^" + "wallet_pontem_menu" + "$"),
                # CallbackQueryHandler(wallet_unisat_menu, pattern="^" + "wallet_unisat_menu" + "$"),
                # CallbackQueryHandler(wallet_trust_menu, pattern="^" + "wallet_trust_menu" + "$"),
                CallbackQueryHandler(main_menu, pattern="^" + "main_menu" + "$")
            ],
            GlobalState.getInstance().WALLET_METAMASK_MENU: [  
                CallbackQueryHandler(wallet_metamask_create, pattern="^" + "wallet_metamask_create" + "$"),
                # CallbackQueryHandler(wallet_metamask_restore, pattern="^" + "wallet_metamask_restore" + "$"),
                # CallbackQueryHandler(wallet_metamask_send, pattern="^" + "wallet_metamask_send" + "$"),
                # CallbackQueryHandler(wallet_metamask_receive, pattern="^" + "wallet_metamask_receive" + "$"),
                # CallbackQueryHandler(wallet_metamask_swap, pattern="^" + "wallet_metamask_swap" + "$"),
                # CallbackQueryHandler(wallet_metamask_bridge, pattern="^" + "wallet_metamask_bridge" + "$"),
                # CallbackQueryHandler(wallet_metamask_stake, pattern="^" + "wallet_metamask_stake" + "$"),
                CallbackQueryHandler(wallets_menu, pattern="^" + "wallets_menu" + "$")
            ],
            GlobalState.getInstance().WALLET_METAMASK_CREATE: [  
                CallbackQueryHandler(wallet_metamask_create, pattern="^(\d+)$"),
                CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            ],
            # GlobalState.getInstance().WALLET_METAMASK_RESTORE: [  
            #     CallbackQueryHandler(wallet_metamask_restore, pattern="^(\d+)$"),
            #     CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            # ],
            # GlobalState.getInstance().WALLET_METAMASK_SEND: [  
            #     CallbackQueryHandler(wallet_metamask_send, pattern="^(\d+)$"),
            #     CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            # ],
            # GlobalState.getInstance().WALLET_METAMASK_RECEIVE: [  
            #     CallbackQueryHandler(wallet_metamask_receive, pattern="^(\d+)$"),
            #     CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            # ],
            # GlobalState.getInstance().WALLET_METAMASK_SWAP: [  
            #     CallbackQueryHandler(wallet_metamask_swap, pattern="^(\d+)$"),
            #     CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            # ],
            # GlobalState.getInstance().WALLET_METAMASK_BRIDGE: [  
            #     CallbackQueryHandler(wallet_metamask_bridge, pattern="^(\d+)$"),
            #     CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            # ],
            # GlobalState.getInstance().WALLET_METAMASK_STAKE: [  
            #     CallbackQueryHandler(wallet_metamask_stake, pattern="^(\d+)$"),
            #     CallbackQueryHandler(wallet_metamask_menu, pattern="^" + "metamask_menu" + "$")
            # ],
            # GlobalState.getInstance().SUPPORT_MENU: [
            #     CallbackQueryHandler(support_callback, pattern='^support$'),
            # ],
            # GlobalState.getInstance().SUPPORT_MENU: [
            #     CallbackQueryHandler(collect_messages, pattern='^collect_messages$'),
            #     CallbackQueryHandler(handle_support_message, pattern='^submit_support$'),
            # ],
            # GlobalState.getInstance().SUPPORT_MENU: [
            #     MessageHandler(filters.TEXT | filters.PHOTO, receive_support_message),
            #     CallbackQueryHandler(submit_support, pattern="^" + "submit_support" + "$"),
            #     CallbackQueryHandler(confirm_support, pattern='^confirm_support:'),
            #     CallbackQueryHandler(cancel_support, pattern='^cancel_support:')
            # ],
            # GlobalState.getInstance().SUPPORT_MENU_2: [
            #     MessageHandler(filters.TEXT | filters.PHOTO, receive_support_message)
            # ],
            GlobalState.getInstance().SUPPORT_MENU: [
                CallbackQueryHandler(collect_messages, pattern='^collect_messages$'),
            ],
            GlobalState.getInstance().COLLECTING_SUPPORT_MESSAGES: [
                MessageHandler(filters.TEXT | filters.PHOTO, collect_support_message),
                CallbackQueryHandler(handle_support_message, pattern='^submit_support$'),
            ],
            # GlobalState.getInstance().COLLECTING_SUPPORT_MESSAGES: [
            #     MessageHandler(filters.TEXT | filters.PHOTO, collect_support_message),
            # ],
            GlobalState.getInstance().AWAITING_SUPPORT_MESSAGE: [
                MessageHandler(filters.TEXT | filters.PHOTO, handle_support_message)
            ],
            GlobalState.getInstance().AWAITING_ADMIN_REPLY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_admin_reply)
            ],
            # GlobalState.getInstance().HANDLE: [
            #     CallbackQueryHandler(admin_response, pattern='^accept')
            # ],
            GlobalState.getInstance().END_ROUTES: [  
                CallbackQueryHandler(start_over, pattern="^" + "main_menu" + "$")
            ],
            GlobalState.getInstance().EMAIL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, confirm_email)
            ]
        },
        fallbacks=[CommandHandler("start", start),
                   CommandHandler('cancel', cancel)
                   ]
        # per_message=True
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)





    application.add_handler(CallbackQueryHandler(admin_response, pattern='^(accept|reject)_'))






    # Run the bot until the user presses Ctrl-C
    application.run_polling(
        allowed_updates=Update.ALL_TYPES, poll_interval=3, timeout=60
    )

### <<<-------------------------------------------- Initiation The Bot -------------------------------------------->>> ###

# Load the email_ids dictionary when the bot starts
GlobalState.getInstance().data_base = load_data_base()

print('Starting up bot...')

Tk = config('token')

if __name__ == "__main__":
    main()
