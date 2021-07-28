import os

def calculate_leave(input_hours):
    from datetime import datetime, time
    today = datetime.today()
    leave_amt = 6.769
    weeks = input_hours / leave_amt * 2
    days = (weeks * 7)
    days = int(days)
    while days > 0:
        try:
            today = datetime(today.year, today.month, today.day + 1)
            days = days - 1
            continue
        except ValueError:
            try:
                today = datetime(today.year, today.month + 1, 1)
                continue
            except ValueError:
                today = datetime(today.year + 1, 1, 1)
                continue
    print("So, you want to save up ", input_hours, "additional hours... ")
    print()       
    print("You will have enough vacation hours in ", round(weeks, 2), " weeks")
    print()
    print("This means, you will have to save vacation from now until roughly", today.strftime("%B %d, %Y"))
    print()
   
    

user_choice = "y"
while user_choice.lower() == "y":
    
    input_hours = int(input("How many vacation hours do you need? "))
   

    if input_hours > 0 and input_hours < 500:
        calculate_leave(input_hours)
        user_choice = input("Would you like to try another amount? (y/n): ")
        
        
    elif input_hours < 0:
        print("Please enter a number greater than 0.")
    
    elif input_hours > 500:
        print("Please enter a number less than 500.")

while user_choice.lower() == "n":
    print("Googerboogerye")
    break
