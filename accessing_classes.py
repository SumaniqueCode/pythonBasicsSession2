#impoting classes and function
from encapsulation import Vehicle

class Car(Vehicle):
    def displayCarDetails():
        print("This is car Car Details")
        
car = Car
car.displayCarDetails()
print(car.displayDetails())