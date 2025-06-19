#constructor in python

class ConstructorDemo:
    def __init__(self):
        print("This is a constructor in python")

class AddNumbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def sum(self):
        return self.num1 + self.num2
    
    def __call__(self, num1, num2):
        return num1 + num2
        
        
obj = ConstructorDemo()
add = AddNumbers(10,20) # initializing the constructor with arguments
print(add.sum())
print(add(20,30)) # calling class