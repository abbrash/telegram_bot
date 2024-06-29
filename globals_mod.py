class GlobalState:
    _instance = None

    def __init__(self):
        if GlobalState._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GlobalState._instance = self

        # Initialize constants
        self.START_ROUTES, self.END_ROUTES, self.EMAIL, _ = range(4)
        self.EXCHANGES_MENU, self.AIRDROPS_MENU, self.WALLETS_MENU, self.SUPPORT_MENU, _, _ = range(4, 10)

        self.EXCHANGE_BINGX_MENU, self.EXCHANGE_COINEX_MENU, self.EXCHANGE_NOBITEX_MENU, self.EXCHANGE_BITPIN_MENU = range(20, 24)
        self.EXCHANGE_NOBITEX_DEPOSIT_RIALS, self.EXCHANGE_NOBITEX_WITHDRAW_RIALS, self.EXCHANGE_NOBITEX_DEPOSIT, self.EXCHANGE_NOBITEX_WITHDRAW, self.EXCHANGE_NOBITEX_TRADE_SPOT = range(24, 29)
        self.EXCHANGE_BITPIN_DEPOSIT_RIALS, self.EXCHANGE_BITPIN_WITHDRAW_RIALS, self.EXCHANGE_BITPIN_DEPOSIT, self.EXCHANGE_BITPIN_WITHDRAW, self.EXCHANGE_BITPIN_TRADE_SPOT = range(29, 34)
        self.EXCHANGE_BINGX_REG, self.EXCHANGE_BINGX_DEPOSIT, self.EXCHANGE_BINGX_WITHDRAW,  self.EXCHANGE_BINGX_TRADE_SPOT, self.EXCHANGE_BINGX_TRADE_FUTURES = range(34, 39)
        self.EXCHANGE_COINEX_REG, self.EXCHANGE_COINEX_DEPOSIT, self.EXCHANGE_COINEX_WITHDRAW,  self.EXCHANGE_COINEX_TRADE_SPOT, self.EXCHANGE_COINEX_TRADE_FUTURES = range(39, 44)

        self.AIRDROP_PHANTOM_MENU, self.AIRDROP_PHANTOM_SWAP, self.AIRDROP_PHANTOM_STAKE, self.AIRDROP_PHANTOM_UNSTAKE = range(100, 104)
        self.AIRDROP_LINEA_SURGE_MENU, self.AIRDROP_LINEA_SURGE_STAKE, self.AIRDROP_LINEA_SURGE_UNSTAKE, _ = range(104, 108)
        self.WALLET_METAMASK_MENU, self.WALLET_METAMASK_CREATE, self.WALLET_METAMASK_IMPORT, self.WALLET_METAMASK_ADD_ACC = range(108, 112)
        self.WALLET_METAMASK_IMPORT_ACC, self.WALLET_METAMASK_SAVE_SRP, self.WALLET_METAMASK_SAVE_PK, self.WALLET_METAMASK_ADD_NETWORK = range(112, 116)
        self.WALLET_METAMASK_IMPORT_TOKEN, self.WALLET_METAMASK_SEND, self.WALLET_METAMASK_RECEIVE, self.WALLET_METAMASK_SWAP = range(116, 120)
        self.WALLET_METAMASK_BRIDGE, self.WALLET_METAMASK_STAKE, _, _ = range(120, 124)

        self. AWAITING_SUPPORT_MESSAGE, self.AWAITING_ADMIN_REPLY = range(800,802)
        self.COLLECTING_SUPPORT_MESSAGES = 900

        # Initialize variables
        self.first_time_loop_phantom_swap = True
        self.first_time_loop_phantom_stake = True
        self.first_time_loop_phantom_unstake = True
        self.current_index_phantom_swap = 0
        self.current_index_phantom_stake = 0
        self.current_index_phantom_unstake = 0

        self.first_time_loop_linea_surge_stake = True
        self.first_time_loop_linea_surge_unstake = True
        self.current_index_linea_surge_stake = 0
        self.current_index_linea_surge_unstake = 0

        self.first_time_loop_nobitex_deposit_rials = True
        self.first_time_loop_nobitex_withdraw_rials = True
        self.first_time_loop_nobitex_deposit = True
        self.first_time_loop_nobitex_withdraw = True
        self.first_time_loop_nobitex_trade_spot = True
        self.first_time_loop_bitpin_deposit_rials = True
        self.first_time_loop_bitpin_withdraw_rials = True
        self.first_time_loop_bitpin_deposit = True
        self.first_time_loop_bitpin_withdraw = True
        self.first_time_loop_bitpin_trade_spot = True
        self.first_time_loop_bingx_reg = True
        self.first_time_loop_bingx_deposit = True
        self.first_time_loop_bingx_withdraw = True
        self.first_time_loop_bingx_trade_spot = True
        self.first_time_loop_bingx_trade_futures = True
        self.first_time_loop_coinex_reg = True
        self.first_time_loop_coinex_deposit = True
        self.first_time_loop_coinex_withdraw = True
        self.first_time_loop_coinex_trade_spot = True
        self.first_time_loop_coinex_trade_futures = True
        self.current_index_nobitex_deposit_rials = 0
        self.current_index_nobitex_withdraw_rials = 0
        self.current_index_nobitex_deposit = 0
        self.current_index_nobitex_withdraw = 0
        self.current_index_nobitex_trade_spot = 0
        self.current_index_bitpin_deposit_rials = 0
        self.current_index_bitpin_withdraw_rials = 0
        self.current_index_bitpin_deposit = 0
        self.current_index_bitpin_withdraw = 0
        self.current_index_bitpin_trade_spot = 0
        self.current_index_bingx_reg = 0 
        self.current_index_bingx_deposit = 0
        self.current_index_bingx_withdraw = 0
        self.current_index_bingx_trade_spot = 0
        self.current_index_bingx_trade_futures = 0
        self.current_index_coinex_reg = 0
        self.current_index_coinex_deposit = 0
        self.current_index_coinex_withdraw = 0
        self.current_index_coinex_trade_spot = 0
        self.current_index_coinex_trade_futures = 0

        self.first_time_loop_wallet_metamask_create = True
        self.first_time_loop_wallet_metamask_import = True
        self.first_time_loop_wallet_metamask_add_acc = True
        self.first_time_loop_wallet_metamask_import_acc = True
        self.first_time_loop_wallet_metamask_save_srp = True
        self.first_time_loop_wallet_metamask_save_pk = True
        self.first_time_loop_wallet_metamask_add_network = True
        self.first_time_loop_wallet_metamask_import_token = True
        self.first_time_loop_wallet_metamask_send = True
        self.first_time_loop_wallet_metamask_receive = True
        self.first_time_loop_wallet_metamask_swap = True
        self.first_time_loop_wallet_metamask_bridge = True
        self.first_time_loop_wallet_metamask_stake = True
        self.current_index_wallet_metamask_create = 0
        self.current_index_wallet_metamask_import = 0
        self.current_index_wallet_metamask_add_acc = 0
        self.current_index_wallet_metamask_import_acc = 0
        self.current_index_wallet_metamask_save_srp = 0
        self.current_index_wallet_metamask_save_pk = 0
        self.current_index_wallet_metamask_add_network = 0
        self.current_index_wallet_metamask_import_token = 0
        self.current_index_wallet_metamask_send = 0
        self.current_index_wallet_metamask_receive = 0
        self.current_index_wallet_metamask_swap = 0
        self.current_index_wallet_metamask_bridge = 0
        self.current_index_wallet_metamask_stake = 0


        # Initialize message IDs dictionary
        self.message_ids = {}
        self.chat_id = None
        self.data_base = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


### Accessing Constants and Variables
### from globals import GlobalState
### def some_function():
    ## Accessing constants
    # stage_constant = GlobalState.getInstance().START_ROUTES

    # # Accessing variables
    # first_time_swap = GlobalState.getInstance().first_time_loop_ph_swap
    # current_index_swap = GlobalState.getInstance().current_index_ph_swap

    # # Example of setting a variable
    # GlobalState.getInstance().first_time_loop_ph_swap = False