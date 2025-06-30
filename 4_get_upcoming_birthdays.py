from datetime import datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users):
  today = datetime.now().date()
  upcoming_birthdays = []

  for user in users:
    try:
      birthday = datetime.strptime(user.get("birthday"), DATE_FORMAT).date()
    except ValueError:
      print(f"Неправильний формат дати для {user.get("name")}. Очікуваний формат 'YYYY.MM.DD'. Отримано: {user.get("birthday")}.")
      continue
    
    birthday_current = birthday.replace(year=today.year)

    if birthday_current < today:
      birthday_current = birthday.replace(year=today.year + 1)

    if today <= birthday_current <= today + timedelta(days=6):
      weekday = birthday_current.weekday()
      if weekday in [5, 6]:  # Saturday (5) or Sunday (6)
        birthday_current += timedelta(days=(7 - weekday))

      upcoming_birthdays.append({
        "name": user.get("name"),
        "congratulation_date": birthday_current.strftime(DATE_FORMAT)
      })

  return upcoming_birthdays
