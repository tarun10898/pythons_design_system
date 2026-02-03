from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        pass

    @abstractmethod
    def accerate(self) -> None:
        pass

    @abstractmethod
    def brake(self) -> None:
        pass

    @abstractmethod
    def shift_grear(self, gear: int) -> None:
        pass


class SportsCar(Car):
    def __init__(self, brand:str, model:str) -> None:
        self.brand: str = brand
        self.model: str = model
        self.is_engine_on: bool = False
        self.current_gear:int = 0
        self.current_speed:int = 0

    def start_engine(self) -> None:
        self.is_engine_on = True
        print(f"{self.brand} {self.model} engine started.")

    def shift_grear(self, gear:int) -> None:
        self.current_gear = gear
        print(f"{self.brand} {self.model} shifed to gear {self.current_gear}.")

    def accerate(self) -> None:
        if self.is_engine_on:
            self.current_speed += 10 * self.current_gear
            print(f"{self.brand} {self.model} accelerated to {self.current_speed} km/hr.")
        else:
            print(f"Can't accelerate. {self.brand} {self.model} engine is off.")

    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 10
            print(f"{self.brand} {self.model} slowed down to {self.current_speed} km/hr.")
        else:
            print(f"{self.brand} {self.model} is already stationary.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        self.current_gear = 0
        print(f"{self.brand} {self.model} engine stopped.")


def main():
    my_car = SportsCar("Porsche", "911")
    my_car.start_engine()
    my_car.shift_grear(1)
    my_car.accerate()
    my_car.shift_grear(2)
    my_car.accerate()
    my_car.brake()
    my_car.stop_engine()

if __name__ == "__main__":
    main()                


