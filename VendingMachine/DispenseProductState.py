from VendingMachineState import VendingMachineState

from Inventory import Inventory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VendingMachine import VendingMachine
else:
    VendingMachine = None

class DispenseProductState(VendingMachineState):

    def __init__(self, vending_machine: VendingMachine) -> None:
        self.vending_machine = vending_machine

    def select_product(self, product):
        print("Product already Selected")

    def insert_coin(self, coin):
        print('Product already Selected')

    def insert_note(self, note):
        print('Product already Selected')

    def dispense_product(self):
        product = self.vending_machine.get_selected_product()
        current_quantity = self.vending_machine.inventory.get_quantity(product)
        self.vending_machine.inventory.update_quantity(product, current_quantity-1)
        print("Please collect the Product")
        self.vending_machine.update_state(self.vending_machine.get_return_change_state())        
    
    def return_change(self):
        print("Payment process already completed")