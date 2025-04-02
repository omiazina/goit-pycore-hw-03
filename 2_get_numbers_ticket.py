import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
  MIN_NUMBER = 1
  MAX_NUMBER = 1000
  
  if not (MIN_NUMBER <= min <= max <= MAX_NUMBER):
      raise ValueError(f"Некоректний діапазон: min має бути ≥ {MIN_NUMBER}, max ≤ {MAX_NUMBER} та min < max.")
  
  if not (min <= quantity <= max):
      raise ValueError(f"Некоректна кількість чисел: quantity має бути в межах [{min}, {max}].")
  
  numbers = range(min, max + 1)
  random_numbers = random.sample(numbers, quantity)
  return sorted(random_numbers)
