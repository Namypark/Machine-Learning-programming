class Car:
    def __init__(self, license_plate: str, model: str):

        self.license_plate = license_plate
        self.model = model

    def __str__(self):
        return f"{self.model} ({self.license_plate})"


class ParkingLot:
    def __init__(self, capacity: int):

        # Attributes managing the parking lot capacity
        self.capacity = capacity
        self.parked_cars: list[Car] = []

    def park_car(self, car: Car) -> bool:

        if len(self.parked_cars) >= self.capacity:
            print("---------------------------parking full ---------------------------")
            return False

        self.parked_cars.append(car)
        print(f"{car} has been parked")
        return True

    def leave_parking(self, license_plate: str):
        for car in self.parked_cars:
            if car.license_plate == license_plate:
                self.parked_cars.remove(car)
                print(f"{car} left parking")
                return car

        print(f"{license_plate} - Car not found")
        return None

    def display_stat(self):
        print("---------------------------parking status ---------------------------")
        print(f"{len(self.parked_cars)} / {self.capacity}")

        for i, car in enumerate(self.parked_cars, start=1):
            print(f"spot{i}:{car}")
        if not self.parked_cars:
            print("empty")
