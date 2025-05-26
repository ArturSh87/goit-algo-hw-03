from datetime import datetime, date, timedelta 

def get_days_from_today(date_string):
    try:
        user_date = datetime.strptime(date_string, "%Y-%m-%d").date()
        current_date = date.today()
        delta = user_date - current_date  
        return delta.days 
    except ValueError:
        return("Неправильний формат дати")
print(get_days_from_today("2025-05-26"))