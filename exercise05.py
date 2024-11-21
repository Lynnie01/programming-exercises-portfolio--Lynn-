###5.Days of the month

# Create a dictionary where the keys are month numbers (1-12) and the values are the number of days in each month
days_in_month = {
    1: 31,  # January
    2: 28,  # February 
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31  # December
}

# Tell the user to put the month number
month = int(input("Enter the month number (1-12): "))

# Check if the input is a valid month number
if month < 1 or month > 12:
    print("Invalid month number! Please enter a number between 1 and 12.")
else:
    # If the month is February, check for a leap year
    if month == 2:
        # Ask the user if it's a leap year
        leap_year = input("Is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        # Mkae the output  the number of days in the corresponding month
        print(f"The month has {days_in_month[month]} days.")
