import calendar

def display_calendar():

    year = int(input("enter year"))
    month = int(input("enter month(1-12):"))

    cal = calendar.TextCalendar(calendar.SUNDAY)

    month_calendar = cal.formatmonth(year,month)
    print(month_calendar)

display_calendar()
