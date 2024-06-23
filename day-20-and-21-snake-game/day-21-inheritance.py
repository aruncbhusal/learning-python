# We can set a class to inherit from another class
# The class to inherit from is called the super class
# We need to call the init for the super class to use
# its init in our new class, so that it can inherit its
# attributes and methods

class Car:
    def __init__(self):
        self.wheels = 4
    
    def whatisthis(self):
        print("This is a car.")
    
    def canitrun(self):
        print("Ofcourse it can run")
        
class ToyotaCorolla(Car):
    def __init__(self):
        super().__init__()
        
    def whatisthis(self):
        super().whatisthis()
        print("Model: The Toyota Corolla")
        
    def price(self):
        print("Nah it's cheap")
        
my_toyota = ToyotaCorolla()
my_toyota.whatisthis()
my_toyota.price()
print(f"And it's got the wheels: {my_toyota.wheels}")
my_toyota.canitrun()


# Next thing to learn today is slicing of list and tuple
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
cities = ('Amsterdam', 'Berlin', 'Canberra', 'Dublin', 'Edinburgh', 'Frankfurt'
          , 'Genoa', 'Hawai', 'Idaho', 'Jakarta', 'Kansas')

print(alphabet)
# This prints the whole list
print(alphabet[2:6])
# From index 2 to 5 i.e. c to f
print(alphabet[4:])
# From index 4 i.e. e to the end
print(alphabet[:7])
# Upto index 6 i.e. g
# These also work with tuples the same way
print(cities[1:8:2])
# The third value sets increment, i.e. index 1 3 5 7 will be printed
print(cities[::-1])
# leaving all other as empty and increment as -1 will reverse the list/tuple