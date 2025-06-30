import re

COUNTRY_CODE = "380"

def normalize_phone(phone_number: str) -> str:
  digits = re.sub(r"\D", "", phone_number)

  if digits.startswith(COUNTRY_CODE):
    formatted_number = f"+{digits}"
  elif digits.startswith("0"):
    formatted_number = f"+{COUNTRY_CODE}{digits[1:]}"
  else:
    formatted_number = f"+{COUNTRY_CODE}{digits}"

  return formatted_number
