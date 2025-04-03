#conditional statements
# Conditional statements are used to perform different actions based on different conditions.
# if, if-elif-else, if-else,nested if, match-case

# if condition:
# code to execute if condition is true
age = 18
if age >= 18:
    print("You are eligible to vote.")


# if-else statement
# if-else statement is used when you have two conditions to check.
age2=17
if age2>= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# if-elif-else statement
# if-elif-else statement is used when you have multiple conditions to check.
age3 = 20
if age3 < 13:
    print("You are a child.")
elif age3 < 20:
    print("You are a teenager.")
elif age3 < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# nested if statement

# nested if statement is used when you have a condition inside another condition.
age4 = 20
if age4 >= 18:
    print("You are eligible to vote.")
    if age4 >= 21:
        print("You are eligible to drink alcohol.")
    else:
        print("You are not eligible to drink alcohol.")


