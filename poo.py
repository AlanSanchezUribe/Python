class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name + " and I am", self.age, "years old")

person1 = Person("John", 36)
person2 = Person("Alice", 25)

person1.greet()
person2.greet()