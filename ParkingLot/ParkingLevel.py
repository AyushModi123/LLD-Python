from ParkingSpot import ParkingSpot
from VehicleType import VehicleType
from Vehicle import Vehicle
from typing import List, Dict

class ParkingLevel:
    def __init__(self, floor: int, spot_type_map: Dict[VehicleType, int]) -> None:
        self._floor = floor
        self._parking_spots: List[ParkingSpot] = []
        spot_number = 1
        for key, value in spot_type_map.items():
            for i in range(value):
                self._parking_spots.append(ParkingSpot(spot_number, key, self))
                spot_number+=1
    
    def park_vehicle(self, vehicle: Vehicle):
        for spot in self._parking_spots:
            if spot.is_available() and spot.get_spot_type()==vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        for spot in self._parking_spots:
            if (not spot.is_available()) and spot.get_parked_vehicle()==vehicle:
                return spot.unpark_vehicle()                
        return 0

    def display_availability(self):
        print("Floor:", self._floor)
        print("Availability:")
        for spot in self._parking_spots:
            print("Spot ", spot.get_spot_id(), ": ", spot.get_spot_type(), "->", spot.is_available(), )
        
