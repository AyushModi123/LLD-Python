from VendingMachineState import VendingMachineState
from Inventory import Inventory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VendingMachine import VendingMachine
else:
    VendingMachine = None

class ReturnChangeState(VendingMachineState):

    def __init__(self, vending_machine: VendingMachine) -> None:
        self.vending_machine = vending_machine

    def select_product(self, product):
        print("Product already Dispensed")

    def insert_coin(self, coin):
        print('Payment already completed')

    def insert_note(self, note):
        print('Payment already completed')

    def dispense_product(self):
        print("Product already dispensed")
    
    def return_change(self):
        product = self.vending_machine.get_selected_product()
        change = self.vending_machine.get_total_payment() - product.get_price()
        if change > 0:
            #Keep the change
            print("Change Returned: ", change)
        else:
            print("No change to return")
        self.vending_machine.reset_payment()
        self.vending_machine.reset_selected_product()
        self.vending_machine.update_state(self.vending_machine.get_ready_state())