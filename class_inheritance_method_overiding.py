# Class Inheritance

## Relationships in Object Oriented Programming
## 1. Has-a:
##    A robot HAS A battery.
##
## 2. Is-a:
##    A robot cat IS A robot.
##
## 3. Inheritance:
##     Base class (parent) -> Devied Clase 1 (child), Devied Clase 1 (child)

class Robot:  # Parent Class constructor
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New Position:', self.position)

    def eat(self): # Method overriding, Child class first
        print("I am hungry!")

class Robot_Dog(Robot): # Child Class constructor, inheriing the parent class
    def make_noise(self):
        print('Woof Woof!')

    def eat(self): # Method overriding, Child class first
        super().eat() # super method called the parent class
        print('I like bacon!')

# Main program
my_robot_dog = Robot_Dog('Bud') # create a Robot_Dog object by calling the constructor
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()

