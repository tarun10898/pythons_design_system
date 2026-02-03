from abc import ABC, abstractmethod

# Base Car class
class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0

    # Common methods for all cars
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")

    # Abstract methods for dynamic polymorphism
    @abstractmethod
    def accelerate(self, speed=None):
        pass

    @abstractmethod
    def brake(self):
        pass


class ManualCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.current_gear = 0

    # Specialized method for Manual Car
    def shift_gear(self, gear):
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")

    # Overriding accelerate - supports both dynamic and "static" polymorphism
    def accelerate(self, speed=None):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return
        if speed is None:  # Default accelerate (dynamic polymorphism)
            self.current_speed += 20
        else:              # Accelerate with given speed (simulating static polymorphism)
            self.current_speed += speed
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    # Overriding brake
    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery_level = 100

    # Specialized method for Electric Car
    def charge_battery(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} : Battery fully charged!")

    # Overriding accelerate - supports both dynamic and "static" polymorphism
    def accelerate(self, speed=None):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return
        if self.battery_level <= 0:
            print(f"{self.brand} {self.model} : Battery dead! Cannot accelerate.")
            return

        if speed is None:  # Default accelerate
            self.battery_level -= 10
            self.current_speed += 15
        else:              # Accelerate with given speed
            self.battery_level -= (10 + speed)
            self.current_speed += speed

        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h. "
              f"Battery at {self.battery_level}%.")

    # Overriding brake
    def brake(self):
        self.current_speed -= 15
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Regenerative braking! Speed is now {self.current_speed} km/h. "
              f"Battery at {self.battery_level}%.")


# Main function
def main():
    my_manual_car = ManualCar("Ford", "Mustang")
    my_manual_car.start_engine()
    my_manual_car.accelerate()          # Dynamic polymorphism
    my_manual_car.accelerate(30)        # Simulated static polymorphism
    my_manual_car.brake()
    my_manual_car.stop_engine()

    print("----------------------")

    my_electric_car = ElectricCar("Tesla", "Model S")
    my_electric_car.start_engine()
    my_electric_car.accelerate()        # Dynamic polymorphism
    my_electric_car.accelerate(40)      # Simulated static polymorphism
    my_electric_car.brake()
    my_electric_car.stop_engine()


if __name__ == "__main__":
    main()
