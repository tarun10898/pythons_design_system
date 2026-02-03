class Car():
    def __init__(self, name:str, brand:str) -> None:
        self.name: str = name
        self.brand: str = brand
        self._is_engine_on: bool = False
        self.current_speed: int = 0
        self.current_gear: int = 0

    def start_engine(self) -> None:
        self._is_engine_on = True
        print(f"{self.name} engine started.")

    def accelerate(self) -> None:
        if not self._is_engine_on:
            print(f"{self.name} engine is off. Please start the engine first.")    
        else:
            self.current_speed += 10
            print(f"{self.name} accelerate to {self.current_speed} km/h.")

    def brake(self) -> None:
        if self.current_speed > 0:
            self.current_speed -= 10
            print(f"{self.name} is braking so speed reduced to {self.current_speed}.")
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.name} slowed down to {self.current_speed} km/h.")                 

class ManualCar(Car):
    def __init__(self, name: str, brand: str) -> None:
        super().__init__(name, brand)

    def shift_gear(self, gear:int) -> None:
        if 0 <= gear <= 6:
            self.current_gear = gear
            self.current_speed = gear * 2
            print(f"{self.name} shifted to gear {gear}.")
        else:
            print("Invalid gear. Please select a gear between 0 and 6.")   

    def accelerate(self) -> None:
        if not self._is_engine_on:
            print(f"{self.name} engine is off. Please start the engine first.")    
        else:
            self.current_speed += self.current_gear * 5
            print(f"{self.name} accelerate to {self.current_speed} km/h.")         


class ElectricCar(Car):
    def __init__(self, name: str, brand: str, battery_capacity: int) -> None:
        super().__init__(name, brand)
        self.battery_capacity: int = battery_capacity

    def accelerate(self) -> None:
        if not self._is_engine_on:
            print(f"{self.name} engine is off. Please start the engine first.")    
        else:
            self.current_speed += 15
            print(f"{self.name} accelerate to {self.current_speed} km/h.")

if __name__ == "__main__":

    my_manual_car = ManualCar("Mustang", "Ford")
    my_manual_car.start_engine()
    my_manual_car.shift_gear(3)
    my_manual_car.accelerate()
    my_manual_car.brake()

    my_electric_car = ElectricCar("Model S", "Tesla", 100)
    my_electric_car.start_engine()
    my_electric_car.accelerate()
    my_electric_car.brake()

