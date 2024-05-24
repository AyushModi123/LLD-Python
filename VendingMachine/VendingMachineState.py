from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    @abstractmethod
    def select_product(self, product):
        pass

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def insert_note(self, note):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def return_change(self):
        pass