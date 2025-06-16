# operators in python
# 1. Arithmetic operators +, -, *, /, %, **, //

num1 = 10
num2 = 15

sum = num1+num2
print("Sum of two numbers is:", sum)

rem = num2 % num1
print(rem)

pow = num1**2
print(pow)

div = num2//2
print(div)

#2. Comparison operators ==, !=, >, <, >=, <=
print(num1>num2)
print(num1!=num2)
print(num1==num2)
print(num1<=num2)

#3 logical operators and, or, not
#and operator
print(num1>=num2 and num2<=num1)
print(num1<=num2 and num2>=num1)

#or operator
print(num1>=num2 or num2<=num1)
print(num1<=num2 or num2<=num1)
print (not num1>num2)

# assignment operator = , +=, -=, *=, /=, %=, **=

num1 = num1 + 1
print(num1)

num1 += 1
print(num1)

num1 **= 2
print(num1)
