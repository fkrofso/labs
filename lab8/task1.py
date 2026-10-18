total_price = float(input("Введіть загальну ціну товару: "))
quantity = int(input("Введіть кількість одиниць товару: "))

if quantity > 0:
    unit_price = total_price / quantity
    print(f"Ціна за одну одиницю товару: {unit_price:.2f}")
else:
    print("Помилка! Кількість має бути додатною (більше 0).")
