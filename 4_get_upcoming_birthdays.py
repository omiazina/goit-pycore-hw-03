from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    DATE_FORMAT = "%Y.%m.%d"

    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], DATE_FORMAT).date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= today + timedelta(days=6):
            weekday = birthday_this_year.weekday()
            if weekday in [5, 6]:  # Saturday (5) or Sunday (6)
                birthday_this_year += timedelta(days=(7 - weekday))

            upcoming_birthdays.append({
                "name": user.get("name"),
                "congratulation_date": birthday_this_year.strftime(DATE_FORMAT)
            })

    return upcoming_birthdays
