# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

listNum = []
for i in range(random.randint(0, 10)):
    listNum.append(random.randint(0, 20))
print(listNum)

sumElem = 0
for i in range(1, len(listNum), 2):
    sumElem += listNum[i]
print(sumElem)