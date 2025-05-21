# create a function that takes a date as input and returns the day name of that date.

import datetime as dt

def get_day_name(date_string):
    # Convert the string to a datetime object
    date_object = dt.datetime.strptime(date_string, "%d-%m-%Y")
    # Get the day name
    day_name = date_object.strftime("%A")
    print(day_name)

prompt=("Enter a date (DD-MM-YYYY): ")
date_string = input(prompt)
get_day_name(date_string)