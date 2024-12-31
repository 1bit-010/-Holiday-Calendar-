import holidays
import calendar

def display_indian_holiday_calendar(year):
    # Define Indian holidays using the holidays library
    indian_holidays = holidays.India(years=year)
    
    # Display the year calendar
    print(f"\n{calendar.TextCalendar().formatyear(year)}")
    
    # Print the list of holidays
    print(f"Holidays in India for the year {year}:\n")
    for date, name in sorted(indian_holidays.items()):
        print(f"{date}: {name}")

# User input for the year
try:
    year = int(input("Enter the year for the holiday calendar (e.g., 2025): "))
    display_indian_holiday_calendar(year)
except ValueError:
    print("Invalid year! Please enter a valid numeric year.")
