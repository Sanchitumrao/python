#match case statement
# The match case statement is a new feature in Python 3.10 that allows for more readable and concise code when dealing with multiple conditions.
# It is similar to switch case statements in other programming languages.

day = "Monday"
match day:
    case "Monday":
        print("Start of the workweek!")
    case "Friday":
        print("Weekend is near!")
    case "Saturday":
        print("It's the weekend!")
    case "Sunday":
        print("It's the weekend!")


# The match case statement can also be used with patterns, allowing for more complex matching.

# For example, we can match against a tuple of values:
coordinates = (2, 4)
match coordinates:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")




