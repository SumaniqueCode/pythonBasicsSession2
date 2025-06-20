# regex in python

import re

# pattern for regex
# pattern = "This"
# string = "This is test string"

# # matching the pattern in the string
# if re.match(pattern, string):  
#     print("String found by match method")

# #search
# if re.search(pattern, string):
#     print("String found search method")
    

# pattern = r'[A-Z]+[a-z]+\d'
# string = input("Enter string: ")

# if re.match(pattern, string):
#     print("Pattern matched")
# else:
#     print("Pattern not matched")

pattern = r'[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]'
string = input("Enter your email: ")
if re.match(pattern, string):
    print("Valid email")
    print("Signed up successfully")
else:
    print("Invalid email")