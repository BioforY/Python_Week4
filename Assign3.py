#Create a python class named Person:
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and {self.gender}.")
        
intro = Person("Ian", 27, "male")
intro.introduce()