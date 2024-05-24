from VendingMachineState import VendingMachineState
from Inventory import Inventory
from Product import Product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VendingMachine import VendingMachine
else:
    VendingMachine = None


class ReadyState(VendingMachineState):

    def __init__(self, vending_machine: VendingMachine) -> None:
        self.vending_machine = vending_machine

    def select_product(self, product: Product):
        # print("Product already Selected")
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.set_selected_product(product)
            self.vending_machine.update_state(self.vending_machine.get_payment_state())
            print("Product Selected: ", product.get_name())
        else:
            print("Product not available")

    def insert_coin(self, coin):
        print('Select product first')

    def insert_note(self, note):
        print('Select product first')

    def dispense_product(self):
        print("Please select product and complete payment")
    
    def return_change(self):
        print("Make the payment first")