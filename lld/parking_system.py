import datetime
import math


class Vehicle:
    def __init__(self, parking_spots: int):
        self._parking_spots = parking_spots

    @property
    def parking_spots(self) -> int:
        return self._parking_spots


class Car(Vehicle):
    def __init__(self):
        super().__init__(1)


class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)


class SemiTruck(Vehicle):
    def __init__(self):
        super().__init__(3)


class Driver:
    def __init__(self, driver_id: str, vehicle: Vehicle):
        self._id = driver_id
        self._vehicle = vehicle
        self._balance = 0.0

    @property
    def id(self) -> str:
        return self._id

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float):
        self._balance = amount


class ParkingFloor:
    def __init__(self, spot_count: int):
        self._parking_spots = [0] * spot_count
        self._vehicle_map = {}

    def assign_spots(self, vehicle: Vehicle) -> bool:
        vehicle_size = vehicle.parking_spots
        l = 0

        for r in range(len(self._parking_spots)):
            if self._parking_spots[r] != 0:
                l = r + 1
            elif r - l + 1 == vehicle_size:
                self._vehicle_map[vehicle] = (l, r)
                for k in range(l, r + 1):
                    self._parking_spots[k] = 1
                return True

        return False

    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        if vehicle not in self._vehicle_map:
            return False

        start, end = self._vehicle_map[vehicle]
        for i in range(start, end + 1):
            self._parking_spots[i] = 0

        del self._vehicle_map[vehicle]
        return True

    @property
    def parking_spots(self) -> list:
        return self._parking_spots

    def get_vehicle_spots(self, vehicle: Vehicle):
        return self._vehicle_map.get(vehicle, None)


class ParkingGarage:
    def __init__(self, number_of_floors: int, spots_per_floor: int):
        self._number_of_floors = number_of_floors
        self._spots_per_floor = spots_per_floor
        self._parking_floors = [
            ParkingFloor(self._spots_per_floor) for _ in range(self._number_of_floors)
        ]

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for floor in self._parking_floors:
            if floor.assign_spots(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        for floor in self._parking_floors:
            if floor.remove_vehicle(vehicle):
                return True
        return False


class ParkingSystem:
    def __init__(self, parking_garage: ParkingGarage, hourly_rate: float):
        self._parking_garage = parking_garage
        self._hourly_rate = hourly_rate
        self._time_parked = {}

    def park_vehicle(self, driver: Driver) -> bool:
        is_parked = self._parking_garage.park_vehicle(driver.vehicle)
        if is_parked:
            # Store full timestamp, not just the integer hour
            self._time_parked[driver.id] = datetime.datetime.now()
        return is_parked

    def remove_vehicle(self, driver: Driver) -> bool:
        if driver.id not in self._time_parked:
            return False

        start_time = self._time_parked[driver.id]
        now = datetime.datetime.now()

        # Calculate difference using datetime objects
        duration_seconds = (now - start_time).total_seconds()
        duration_hours = duration_seconds / 3600

        # Bill at least 1 hour minimum
        billable_hours = math.ceil(max(duration_hours, 1.0))
        charge = billable_hours * self._hourly_rate

        driver.balance += charge
        del self._time_parked[driver.id]

        return self._parking_garage.remove_vehicle(driver.vehicle)

parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 10)
driver1 = Driver(1, Car())
driver2 = Driver(2, Limo())
driver3 = Driver(3, SemiTruck())
print(parkingSystem.park_vehicle(driver1))
print(parkingSystem.park_vehicle(driver2))
print(parkingSystem.park_vehicle(driver3))

print(parkingSystem.remove_vehicle(driver1))
print(parkingSystem.remove_vehicle(driver2))
print(parkingSystem.remove_vehicle(driver3))

print(driver1.balance)