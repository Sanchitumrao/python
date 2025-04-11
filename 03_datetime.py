import datetime as dt 
 
#time delta() is a class in the datetime module that represents a duration, the difference between two dates or times.

current_date = dt.datetime.now().date() # Getting the current date
new_date = current_date + dt.timedelta(days=5) # Adding 5 days to the current date
print("Current date:", current_date)
print("New date (after adding 5 days):", new_date) 
print("Difference in days:", (new_date - current_date).days) 

new2_date = current_date + dt.timedelta(weeks=2) # Adding 2 weeks to the current date
print("New date (after adding 2 weeks):", new2_date)

for i in range(5):
    new_date = current_date + dt.timedelta(days=i) # Adding i days to the current date
    print("New date (after adding", i, "days):", new_date)
