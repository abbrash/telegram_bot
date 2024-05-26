class GlobalState:
    _instance = None

    def __init__(self):
        if GlobalState._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GlobalState._instance = self

        # Initialize constants
        self.START_ROUTES, self.END_ROUTES, self.SEND_IMG, self.EMAIL = range(4)
        self.PH_AIRDROP, self.PH_AIRDROP_SWAP, self.PH_AIRDROP_STAKE, self.PH_AIRDROP_UNSTAKE = range(4,8)
        self.LINEA_SURGE_AIRDROP, self.LINEA_SURGE_AIRDROP_STAKE, self.LINEA_SURGE_AIRDROP_UNSTAKE = range(8,11)

        # Initialize variables
        self.first_time_loop_ph_swap = True
        self.first_time_loop_ph_stake = True
        self.first_time_loop_ph_unstake = True
        self.current_index_ph_swap = 0
        self.current_index_ph_stake = 0
        self.current_index_ph_unstake = 0

        self.first_time_loop_linea_surge_stake = True
        self.first_time_loop_linea_surge_unstake = True
        self.current_index_linea_surge_stake = 0
        self.current_index_linea_surge_unstake = 0

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