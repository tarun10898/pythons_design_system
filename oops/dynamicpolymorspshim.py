from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, name: str, brand: str):
        self.name: str = name
        self.brand: str = brand
        self.current_speed: int = 0
        self._is_engine_on:bool = False

    def start_engine(self) -> None:
        self._is_engine_on = True
        print(f"{self.name} engine started.")

    def stop_engine(self) -> None:
        self._is_engine_on = False
        self.current_speed = 0
        print(f"{self.name} engine stopped.")

    @abstractmethod
    def accelerate(self):
        pass             

    @abstractmethod
    def brake(self):
        pass

class ManualCar(Car):
    def __init__(self, name:str, brand:str):
        super().__init__(name,brand)
        self.current_gear: int = 0

    def shift_gear(self, gear:int) -> None:
        if 0<= gear <=6:
            self.current_gear  = gear
            self.current_speed =  gear*2    
            print(f"{self.name} shifted to gear {gear} and the speed is now {self.current_speed}.")
    
    def accelerate(self):
        if not self._is_engine_on:
            print(f"{self.name} engine is off. Please start the engine first.")    
        else:
            self.current_speed += self.current_gear * 5
            print(f"{self.name} accelerate to {self.current_speed} km/h.")

    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 10
            print(f"{self.name} is braking so speed reduced to {self.current_speed}.")
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.name} slowed down to {self.current_speed} km/h.")      

if __name__ == "__main__":
    my_manual_car = ManualCar("Mustang", "Ford")
    my_manual_car.start_engine()
    my_manual_car.shift_gear(3)
    my_manual_car.accelerate()
    my_manual_car.brake()           