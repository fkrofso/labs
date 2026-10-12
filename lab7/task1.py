car_mileage = {"AA1234BB": 45000, "BC5678EE": 12000, "KA9999OK": 85000}
print("Початковий словник:", car_mileage)

car_mileage["AA1234BB"] = 48000
car_mileage["BI7777AX"] = 5000

print("Оновлений словник:", car_mileage)

limit = int(input("Введіть поріг пробігу для пошуку: "))
print(f"Автомобілі з пробігом понад {limit}:")
for car, mileage in car_mileage.items():
  if mileage > limit:
    print(f"- {car}: {mileage} км")
