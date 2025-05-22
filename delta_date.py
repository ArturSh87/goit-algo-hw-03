from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = user_date - current_date
        return delta.days
    except ValueError:
        return("Неправильний формат дати")
print(get_days_from_today("2020-10-12"))