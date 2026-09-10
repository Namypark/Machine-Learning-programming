from parking_lot import Car, ParkingLot


def main():
    print("Hello from machine-learning-programming!")


if __name__ == "__main__":
    main()


# 1. Create independent Car instances
car1 = Car(license_plate="ABC-123", model="Tesla Model 3")
car2 = Car(license_plate="XYZ-789", model="Toyota Camry")
car3 = Car(license_plate="LMN-456", model="Ford Mustang")

# 2. Instantiate a ParkingLot with capacity for 2 cars
lot = ParkingLot(capacity=2)

# 3. Park cars into the lot
lot.park_car(car1)
lot.park_car(car2)

# Attempt to park when full
lot.park_car(car3)

# Display current parking state
lot.display_stat()

# A car leaves, freeing up a space
lot.leave_parking("ABC-123")

# Now the third car can park
lot.park_car(car3)
lot.display_stat()
