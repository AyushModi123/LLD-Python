from VendingMachineState import VendingMachineState
from Inventory import Inventory
from Coin import Coin
from Note import Note
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VendingMachine import VendingMachine
else:
    VendingMachine = None


class PaymentState(VendingMachineState):

    def __init__(self, vending_machine: VendingMachine) -> None:
        self.vending_machine = vending_machine

    def __check_payment_status(self):
        if self.vending_machine.get_total_payment() >= self.vending_machine.get_selected_product().get_price():
            self.vending_machine.update_state(self.vending_machine.get_dispense_state())

    def select_product(self, product):
        print("Product already Selected")
        
    def insert_coin(self, coin: Coin):
        self.vending_machine.add_coin(coin)
        print("Coin Inserted: ", coin.value)
        self.__check_payment_status()

    def insert_note(self, note: Note):
        self.vending_machine.add_note(note)
        print("Note Inserted: ", note.value)
        self.__check_payment_status()

    def dispense_product(self):
        print("Please complete payment first")
    
    def return_change(self):
        print("Please complete payment first")