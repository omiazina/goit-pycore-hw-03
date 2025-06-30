from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def get_days_from_today(date: str) -> int:
  try:
    parsed_date = datetime.strptime(date, DATE_FORMAT)
  except ValueError:
    print("Неправильний формат дати. Очікуваний формат 'YYYY-MM-DD'.")
    return
  
  now = datetime.now()
  days_diff = (now - parsed_date).days
  return days_diff
