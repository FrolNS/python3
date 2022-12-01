# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
#  элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

listFromUser = list(input("Введите список чисел через пробел: ").split())
listInt = list(map(int, listFromUser))
print(listInt)
sum = 0
for i in range(1, len(listInt), 2):
    sum += listInt[i]
print(sum)
