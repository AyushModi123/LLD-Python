from VehicleType import VehicleType
from Car import Car
from Truck import Truck
from ParkingSpot import ParkingSpot
from ParkingLevel import ParkingLevel
from ParkingLot import ParkingLot

car_obj = Car("UP0000")
print(car_obj.get_type())
print(car_obj.get_license_plate())

truck_obj = Truck("UP1111")
print(truck_obj.get_type())
print(truck_obj.get_license_plate())

my_lot = ParkingLot()
my_lot.add_level({
    VehicleType.CAR: 10,
    VehicleType.TRUCK: 3,
    VehicleType.Motorcycle: 10
})
my_lot.show_levels()

my_lot.park_vehicle(car_obj)
my_lot.park_vehicle(truck_obj)

my_lot.add_level({
    VehicleType.CAR: 5,
    VehicleType.TRUCK: 2,
    VehicleType.Motorcycle: 3
})

import time
time.sleep(5)
print("Total Fee: ", round(my_lot.unpark_vehicle(truck_obj), 2))
my_lot.display_availability()