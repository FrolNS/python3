# Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# (максимальное значение у числа 1.2 , минимальное у 10.01)

listFromUser = list(input("Введите список чисел через пробел: ").split())
listFloat = list(map(float, listFromUser))
print(listFloat)
newList = list()
for i in range(len(listFloat)):
    newList.append(round(listFloat[i] % 1, 2))
print(newList)
print(max(newList) - min(newList))
