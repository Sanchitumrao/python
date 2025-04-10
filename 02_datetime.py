#built-in modules

#datetime and time modules
import datetime as dt # Importing the built-in datetime module with an alias 'dt'
import time as t # Importing the built-in time module with an alias 't'

# dt.datetime()# The datetime module supplies classes for manipulating dates and times.

print("Current date and time:", dt.datetime.now()) # Getting the current date and time
print("Current date:", dt.datetime.now().date()) # Getting the current date
print("Current time:", dt.datetime.now().time()) # Getting the current time
print("Current year:", dt.datetime.now().year) # Getting the current year
print("Current month:", dt.datetime.now().month) # Getting the current month
print("Current day:", dt.datetime.now().day) # Getting the current day
print("Current hour:", dt.datetime.now().hour) # Getting the current hour
print("Current minute:", dt.datetime.now().minute) # Getting the current minute
print("Current second:", dt.datetime.now().second) # Getting the current second

#t.sleep() is a function that suspends the execution of the current thread for a specified number of seconds.
print("Sleeping for 5 seconds...")
t.sleep(5) # Sleep for 5 seconds
print("Awake now!")

print("Current time ",t.time()) # Getting the current time in seconds



