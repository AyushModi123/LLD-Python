from  Vehicle import Vehicle, VehicleType

class Car(Vehicle):
    def __init__(self, license_plate) -> None:
        super().__init__(VehicleType.CAR, license_plate)
    
    def get_type(self) -> VehicleType:
        return self._type
    
    def get_license_plate(self) -> str:
        return self._license_plate