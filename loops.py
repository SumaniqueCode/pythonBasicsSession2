# loops in python: while, for, nested loops
# requirements in loops: initialization, condition, increment/decrement

# while loop
i = 1
while i <= 10:
    print(i, end=" ")
    i = i + 1
print("")

# for loop
for j in range(10):
    print(j, end=" ")
print("")

# nested loop
for k in range(1, 6):
    for l in range(1, 6):
        print(l, end=" ")
    print("")
