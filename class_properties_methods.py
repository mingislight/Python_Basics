# Object and Class
## Defining the Robot Dog class

class Robot_Dog: 
    # Initialize the properties
    def __init__(self, name_Val, breed_Val): # Let us initialize our robot's properties (self, properties1, properties2)
        self.name = name_Val
        self.breed = breed_Val

    def bark(self): # Class method like a function, but with "self" as the parameter
        print('Woof Woof!')

# Main Program
my_dog = Robot_Dog('Simba', 'Shiba Inu')
print("My Dog's name is",my_dog.name)
print("And the breed is", my_dog.breed)

my_dog.bark()