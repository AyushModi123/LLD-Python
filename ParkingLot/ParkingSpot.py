from VehicleType import VehicleType
from Vehicle import Vehicle
from datetime import datetime

class ParkingSpot:
    def __init__(self, id: int, type: VehicleType, level) -> None:
        self.__level = level
        self.__spot_id: int = id
        self.__spot_type: VehicleType = type
        self.__parked_vehicle: Vehicle = None
        self.__parked_at: datetime = None

    def is_available(self) -> bool:
        return self.__parked_vehicle == None

    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available() and vehicle.get_type()==self.__spot_type:
            self.__parked_vehicle = vehicle
            self.__parked_at = datetime.now()
        else:
            raise ValueError("Invalid vehicle type or spot already occupied.")
        
    def unpark_vehicle(self):
        if not self.is_available():
            self.__parked_vehicle = None
            return (datetime.now() - self.__parked_at).total_seconds()*0.01
        return 0

    def get_spot_type(self):
        return self.__spot_type
    
    def get_parked_vehicle(self):
        return self.__parked_vehicle
    
    def get_spot_id(self):
        return self.__spot_id
    
    def get_level(self):
        return self.__level
