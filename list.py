# list in python
# list are mutable , i.e., they can be modified after creation.

list1 = ["Hello", "World", "Python", "Programming", 1, 2.4, True, None, "Hello", 2.4]
list2= [5,8,11,20,34,49,1]
print(list1) #printing whole list
print(list1[1]) #printing through index
print(list1[2:5]) #printing through index range
print(list1[ :5]) #printing through index range from start to 5
print(list1[5: ]) #printing from index 5 to end
list1.append('Appended string') #appending element at the end
print(list1)
print(len(list1))
list1.reverse()  # reversing the list
print(list1)  # printing reversed list
list1.remove(2.4)
print(list1)
list1.pop()
print(list1)
list2.sort()
print("Sorted list: ", list2)  # sorting the list in ascending order

list2.sort(reverse=True)
print("Sorted list: ", list2)  # sorting the list in descending order

list2.insert(2, 10) # inserting element at index 2
print(list2)

#for clearing list
list2.clear()
print(list2)


# Printing using len function
for i in range (len(list1)):
    print(list1[i], end= " ")

#printing every items in list using for loop
for item in list1:
    print(item, end=" ")

print(list1+list2)
