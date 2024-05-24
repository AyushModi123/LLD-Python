from abc import ABC, abstractmethod, ABCMeta
from VehicleType import VehicleType

class Vehicle(metaclass=ABCMeta):
    def __init__(self, type: VehicleType, license_plate: str) -> None:
        self._type = type
        self._license_plate = license_plate

    @abstractmethod
    def get_type(self) -> VehicleType:
        pass
    
    @abstractmethod
    def get_license_plate(self) -> str:
        pass
    
