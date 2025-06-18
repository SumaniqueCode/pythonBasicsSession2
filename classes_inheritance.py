# Class in python
class A:
    def displayClassA():
        print("This is class A")

# Inheritance in Python
class B(A):
    def displayClassB():
        print("This is class B")
        
class C(B):
    def displayClassC():
        print("This is class C")

# Creating an instance of class A
obj = A
# obj.displayClassA()
obj2 = B
# obj2.displayClassB() # Output: This is class B
# obj2.displayClassA() # Output: This is class A inherited by class B
obj3 = C
obj3.displayClassC()
obj3.displayClassB()
obj3.displayClassA() # Output: This is class A inherited by class B inherited by class C
