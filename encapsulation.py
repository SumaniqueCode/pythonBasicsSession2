# encapsulation in python
class Vehicle:
    # public function
    def displayName():
        return "Ford"
    
    #protected function
    def _displayModel():
        return "Mustang"
    
    #private function
    def __engine():
        return "V8"
    
    # public function to display private and protected data
    def displayDetails():
        name = Vehicle.displayName()
        model = Vehicle._displayModel()
        engine = Vehicle.__engine()
        return f"Name: {name}, Model: {model}, Engine: {engine}"

vehicle = Vehicle
print(vehicle.displayName()) # accessing public function
print(vehicle._displayModel()) # accessing protected function
print(vehicle.displayDetails()) # accessing public function to display private and protected data