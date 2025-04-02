from datetime import datetime

def get_days_from_today(date: str) -> int:
  try:
      parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
      today_date = datetime.today().date()
      return (parsed_date - today_date).days
  except ValueError:
      print("Неправильний формат дати. Очікуваний формат 'YYYY-MM-DD'.")
