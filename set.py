# sets in python

set1 = {"hello", "Python", 2, 99, 5.4, "hello", 2}
set2 = {"hello", 6, 3.4, "test", 99}

# print(set1)

# adding data to set
set1.add(551)
# print(set1)

# union in set
print("Union: ", set1.union(set2))
print("Union: ", set1 | set2)

# intersection in set
print("Intersection: ", set1.intersection(set2))
print("Intersection: ", set1 & set2)

#difference in set
print("Difference: ", set1.difference(set2))
print("Difference: ", set1 - set2)

#symmetric difference
print("Symmetric Difference: ", set1.symmetric_difference(set2))