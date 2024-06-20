class GlobalState:
    _instance = None

    def __init__(self):
        if GlobalState._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GlobalState._instance = self

        # Initialize constants
        self.START_ROUTES, self.END_ROUTES, self.EMAIL, _ = range(4)
        self.EXCHANGES_MENU, self.AIRDROPS_MENU, self.WALLETS_MENU, self.SUPPORT_MENU = range(4, 8)
        self.AIRDROP_PHANTOM_MENU, self.AIRDROP_PHANTOM_SWAP, self.AIRDROP_PHANTOM_STAKE, self.AIRDROP_PHANTOM_UNSTAKE = range(8, 12)
        self.AIRDROP_LINEA_SURGE_MENU, self.AIRDROP_LINEA_SURGE_STAKE, self.AIRDROP_LINEA_SURGE_UNSTAKE, _ = range(12, 16)
        self.WALLET_METAMASK_MENU, self.WALLET_METAMASK_CREATE, _, _ = range(16, 20)
        self.EXCHANGE_BINGX_MENU, self.EXCHANGE_COINEX_MENU, self.EXCHANGE_BINGX_REG, self.EXCHANGE_COINEX_REG = range(20, 24)

        self. AWAITING_SUPPORT_MESSAGE, self.AWAITING_ADMIN_REPLY = range(30,32)
        self.COLLECTING_SUPPORT_MESSAGES = 40

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

        self.first_time_loop_metamask_create_wallet = True
        self.current_index_metamask_create_wallet = 0

        self.first_time_loop_bingx_reg = True
        self.first_time_loop_coinex_reg = True
        self.current_index_bingx_reg = 0 
        self.current_index_coinex_reg = 0

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