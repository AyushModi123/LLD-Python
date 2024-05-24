from ParkingLevel import ParkingLevel
from VehicleType import VehicleType
from Vehicle import Vehicle
from typing import Dict

class ParkingLot:
    _instance = None
    level_number = 0
    levels: ParkingLevel = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)                    
        return cls._instance    
    
    def add_level(self, spot_type_map: Dict[VehicleType, int]) -> None:
        ParkingLot.levels.append(ParkingLevel(ParkingLot.level_number, spot_type_map))
        ParkingLot.level_number+=1

    def show_levels(self):
        print(ParkingLot._instance.levels)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in ParkingLot.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in ParkingLot.levels:
            return level.unpark_vehicle(vehicle)               
        return 0
    
    def display_availability(self):
        for level in ParkingLot.levels:
            level.display_availability()


#Testing singleton design in multi-threaded environment
#Won't truly multithread because of GIL

# import threading
# def test_function():
#     ab = ParkingLot()
#     ab.add_level({
#     VehicleType.CAR: 10,
#     VehicleType.TRUCK: 3,
#     VehicleType.Motorcycle: 10
#     })
#     ab.show_levels()

# t1 = threading.Thread(target=test_function, group=None)
# t2 = threading.Thread(target=test_function, group=None)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
