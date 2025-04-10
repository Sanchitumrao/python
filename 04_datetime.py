import datetime as dt 

#strftime() is a method in the datetime module that formats a datetime object into a string representation based on a specified format.

today_date = dt.datetime.now().date() 
current_time = dt.datetime.now().time()
print("Today date:", today_date) 
print("Formatted date:", today_date.strftime("%d-%m-%Y")) # Formatting the date as "DD-MM-YYYY"
print("current year:", today_date.strftime("%Y"))
print("current month:", today_date.strftime("%m"))
print("current day:", today_date.strftime("%d"))
print("current day:", today_date.strftime("%A")) 
print("current month:", today_date.strftime("%B")) 
print("current week of the year:", today_date.strftime("%W"))
print("current day of the year:", today_date.strftime("%j"))

print("current time:", current_time)
print("Formatted time:", current_time.strftime("%H:%M:%S")) 
print("current hour:", current_time.strftime("%H"))
print("AM/PM:", current_time.strftime("%p"))

#strptime() is a method in the datetime module that formats a string representation of a date and time into a datetime object based on a specified format.

date_string = dt.datetime.now().strftime("%d-%m-%Y") # Formatting the date as "DD-MM-YYYY"
print("Date string:", date_string,type(date_string))
date_object = dt.datetime.now().strptime(date_string, "%d-%m-%Y") #converting string to datetime object
print("Date object:", date_object,type(date_object))

