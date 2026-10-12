list1 = list(map(int, input("Введіть перший список через пробіл: ").split()))
list2 = list(map(int, input("Введіть другий список через пробіл: ").split()))

list3 = []
for i in range(len(list1)):
  list3.append(list1[i] + list2[i])

print("Третій список:", list3)
