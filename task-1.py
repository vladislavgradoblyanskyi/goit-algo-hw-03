from datetime import datetime

def get_days_from_today(date):
    now = datetime.today().toordinal()
    try:

        date=datetime.strptime(date,"%Y-%m-%d").toordinal()
        datediff=date-now
        return datediff

    except ValueError:
        return"bad format"
    except TypeError:
        return"bad type"

print(get_days_from_today("2021-10-09"))
print(get_days_from_today(12))
print(get_days_from_today("2026-10-09"))
