# # Error handling in python

# try: # implement the main logic here
#     result = 5/0
#     print(result)

# except ZeroDivisionError as e: # handle the specific error
#     print(e) # prints the default message provided by the class


# try:
#     result = 15/0
#     print(result)

# except ZeroDivisionError as e:
#     print("Error: Division by zero is not allowed") # prints the custom message
    

# try: 
#     num = int(input("Enter a number: "))
#     print(num)

# except (ValueError, TypeError) as e: # handle multiple exceptions
#     print(e)

class EvenNumberError(Exception): # custom error
    pass

try:
    num1 = int(input("Enter an odd number: "))
    if num1%2 ==0:
        raise EvenNumberError("Error: Number is even") # raise a custom error
    else:
        print(num1)
except EvenNumberError as e:
    print(e) # prints the custom error message

else:
    print("Program executed succesfully")

finally:
    print("Finall block executed") # this block will always execute, regardless of whether an
    