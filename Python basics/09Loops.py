# Loops in python

# Loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.

# Python has two primitive looping statements:
# 1. for loop
# 2. while loop

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# The for loop can also iterate over a string

for letter in "banana":
    print(letter)

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# The range() function is often used to loop through a set of code a specified number of times.

#range function
for i in range(6):
    print(i)
    # The above code will print numbers from 0 to 5

# The range() function can also take two arguments: start and end.
for i in range(2, 6):
    print(i)
    

# The range() function can also take three arguments: start, end, and step.
for i in range(2, 30, 3):
    print(i)

# Nested for loop
# A nested loop is a loop inside another loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop".
# The "inner loop" and the outer loop can be any type of loop (for loop, while loop, etc.)
for i in range(2, 6):
    for j in range(1, 4):
        print(i, j)

# while loop
# The while loop will continue to execute as long as the condition is true.
# The while loop is generally used when the number of iterations is not known beforehand.
i = 1
while i < 6:
    print(i)
    i += 1


#break statement

# The break statement is used to exit a loop.
# When the break statement is executed, the loop is terminated and the program control resumes at the next statement following the loop.
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#continue statement
# The continue statement is used to skip the current iteration of a loop and continue with the next iteration.
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

#pass statement
# The pass statement is a null operation; nothing happens when it executes.
# It is used when a statement is syntactically required but you do not want any command or code to execute.
for i in range(1, 10):
    if i == 5:
        pass
    print(i)



