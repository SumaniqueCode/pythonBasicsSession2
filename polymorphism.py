# polymorphism in python
class A:
    def displayName():
        print("This is class A")
            
    def displayHello():
        print("Hello")
        
class B(A):
    # overriding the method of class A
    def displayName():
        print("This is class B")
        
class C(B):
    # overriding the method of class B
    def displayName():
        print("This is class C")
        
    def sum(num1, num2=0, num3=0):
        return num1 + num2 + num3
    
    # using args
    def add(*args):
        sum = 0
        for num in args:
            sum = sum + num
        return sum

obj = A
obj.displayName()

obj1 = B
obj1.displayName()

obj3 = C
obj3.displayName()
obj3.displayHello()
result = obj3.sum(10)
print("The sum is ", result)
result1 = obj3.sum(10,20,30)
print("The sum is ",result1)

# using args
result2 = obj3.add(10,20,30,40,50)
print("The sum is ", result2)