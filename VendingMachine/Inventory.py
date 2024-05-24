from Product import Product
from typing import Dict

class Inventory:
    _instance = None
    __products: Dict[Product, int] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Inventory, cls).__new__(cls)                                
        return cls._instance  
    
    def add_product(self, product: Product, quantity: int) -> None:
        self.__products[product] = quantity

    def remove_product(self, product: Product) -> None:
        self.__products.pop(product)

    def get_quantity(self, product: Product) -> int:
        return self.__products.get(product, 0)
    
    def update_quantity(self, product: Product, quantity: int) -> None:
        self.__products[product] = quantity
    
    def is_available(self, product: Product) -> bool:
        return True if self.__products.get(product, 0)>0 else False
    


        