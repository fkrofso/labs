numbers_tuple = tuple(
    map(int, input("Введіть числа для кортежу через пробіл: ").split())
)
x = int(input("Введіть число x: "))

if x in numbers_tuple:
  print("Число належить кортежу")
else:
  print("Число не належить кортежу")
