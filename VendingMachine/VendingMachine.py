from Inventory import Inventory
from Product import Product
from VendingMachineState import VendingMachineState
from ReadyState import ReadyState
from PaymentState import PaymentState
from ReturnChangeState import ReturnChangeState
from DispenseProductState import DispenseProductState
from Coin import Coin
from Note import Note

class VendingMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VendingMachine, cls).__new__(cls)
            cls._instance.__initialise_machine()
        return cls._instance
    
    def __initialise_machine(self):
        self.inventory = Inventory()
        self.__ready_state = ReadyState(self)
        self.__payment_state = PaymentState(self)
        self.__return_change_state = ReturnChangeState(self)
        self.__dispense_product_state = DispenseProductState(self)
        self.__current_state: VendingMachineState = self.__ready_state
        self.__selected_product: Product = None
        self.__total_payment = 0.0

    def update_state(self, state: VendingMachineState):
        self.__current_state = state

    def select_product(self, product: Product):
        self.__current_state.select_product(product)

    def insert_coin(self, coin: Coin):
        self.__current_state.insert_coin(coin)

    def insert_note(self, note: Note):
        self.__current_state.insert_note(note)

    def dispense_product(self):
        self.__current_state.dispense_product()

    def return_change(self):
        self.__current_state.return_change()

    def add_coin(self, coin: Coin):
        self.__total_payment+=coin.value
    
    def add_note(self, note: Note):
        self.__total_payment+=note.value

    def set_selected_product(self, product: Product):
        self.__selected_product = product

    def get_ready_state(self):
        return self.__ready_state

    def get_payment_state(self):
        return self.__payment_state
    
    def get_dispense_state(self):
        return self.__dispense_product_state
    
    def get_return_change_state(self):
        return self.__return_change_state
    
    def get_total_payment(self):
        return self.__total_payment

    def get_selected_product(self):
        return self.__selected_product
        
    def reset_payment(self):
        self.__total_payment = 0.0
    
    def reset_selected_product(self):
        self.__selected_product = None