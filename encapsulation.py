class SportsCar:
    def __init__(self, name:str, brand: str) -> None:
        self.name: str = name
        self.brand: str = brand
        self.__is_engine_on: bool = False
        self.__current_speed: int = 0
        self.__current_gear: int = 0
        self.__type_comp : str|None =  "standard turbocharger pro max ultra"

    def get_type_comp(self) -> str|None:
        return self.__type_comp
    
    def set_type_comp (self, comp: str|None) -> str|None:
        self.__type_comp = comp
        return self.__type_comp
    
    def start_engine(self) -> None:
        self.__is_engine_on = True
        print(f"{self.name} engine started.")

    def shift_gear(self, gear:int) -> None:
        if 0 <= gear <= 6:
            self.__current_gear = gear
            print(f"{self.name} shifted to gear {gear}.")
        else:
            print("Invalid gear. Please select a gear between 0 and 6.")

    def accelerate(self, speed_increase:int) -> None:
        if not self.__is_engine_on:
            print(f"{self.name} engine is off. Please start the engine first.")
        else:
            self.__current_speed += speed_increase * self.__current_gear + 10  
            print(f"{self.name} accelerate to {self.__current_speed} km/h.")    
    
    def brake(self) -> None:
        if self.__current_speed > 0:
            self.__current_speed -= 10
            print(f"{self.name} is braking so speed reduced to {self.__current_speed}.")
        if self.__current_speed < 0:
            self.__current_speed = 0
        print(f"{self.name} slowed down to {self.__current_speed} km/h.")

    def stop_engine(self) -> None:
        self.__is_engine_on = False
        self.__current_speed = 0
        self.__current_gear = 0
        print(f"{self.name} engine stopped.")

if __name__ == "__main__":
    my_car = SportsCar("Mustang", "Ford")
    my_car.start_engine()
    my_car.shift_gear(1)
    my_car.accelerate(20)
    my_car.shift_gear(2)
    my_car.accelerate(30)
    my_car.brake()
    my_car.stop_engine()

    print("Type of component:", my_car.get_type_comp())
    print("Setting type of component to 'Turbocharger'")
    my_car.set_type_comp("Turbocharger")      
                 