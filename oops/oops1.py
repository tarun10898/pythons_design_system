
#  class and objects in python


# class Student:
#     subjec: str = "Python"
#     collage: str = "ABC"
#     year: int = 2024

# s1 = Student()
# s2 = Student()

# print(s1.subjec, s1.collage, s1.year  )
# print(s2.subjec, s2.collage, s2.year  )



#  default constructor

# class Student:
#     def __init__(self, name):
#         self.name = name

# stu1 = Student("Rahul")
# stu2 = Student("Harshita")

# print(stu1.name, stu2.name)

# parameterized constructor

# class Student:
#     def __init__(self,subject:str,college:str, year:int):
#         self.subject = subject
#         self.college = college
#         self.year = year


# s1 = Student("Python","ABC",2024)
# s2 = Student("Java","XYZ",2023)       
# print(s1.subject, s1.college, s1.year  )
# print(s2.subject, s2.college, s2.year  )

#attributes

# class Student:
#     collage: str = "ABC"
#     def __init__(self,name:str, subject:str,year:int):
#         self.name = name
#         self.subject = subject
#         self.year = year

# s1 = Student("Rahul", "Python", 2024)

# print(s1.name, s1.subject, s1.year, s1.collage)

#  clsass attributs can also be accessed using class name
# print(Student.collage)

# methods in class 

# class Laptop:

#     name: str = "dell"

#     def __init__ (self, rame:int ,processor: str):
#         self.ram = rame
#         self.processor = processor
    
#     def display(self):
#         return f"Laptop Name is with ram {self.ram} and processor {self.processor}"

#     @classmethod
#     def get_info(cls):
#         cls.name = "hp"
#         return f"Laptop Name is {cls.name} "    
#     @staticmethod
#     def info():
#         return "This is laptop class"   
    

# l1 = Laptop(8,"i5")
# print(Laptop.get_info()  ) 
# print(l1.display())
# print(l1.info())


#encapsulation

# class Car:
#     def __init__(self,name:str, model: str, price:int, secret_code: str):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.__secret_code = secret_code
#     def info_of_car(self):
#         return f"Car Name is {self.name} , model is {self.model} and price is {self.price}"

#     def get_secret_code(self):
#         return self.__secret_code
    
#     def set_secret_code(self, code):
#         self.__secret_code = code
#         return print(f"secret code is updaed to {self.__secret_code}")
    
# c1= Car("BMW","X5", 5000000, "XYZ123")
# print(c1.info_of_car())

# print(c1.get_secret_code())

# c1.set_secret_code("ABC987")

