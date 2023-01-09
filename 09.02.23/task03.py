# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def fract(num):
    return round(num%1, 2)

listNum = []
for i in range(random.randint(0, 10)):
    listNum.append(round(random.uniform(0, 20), 2))
print(listNum)

listFract = []
for i in listNum:
    if i%1!=0:
        listFract.append(fract(i))
print(listFract)
maxElem = listFract[0]
minElem = listFract[0]
for i in listFract:
    if i > maxElem:
        maxElem = i
    elif i < minElem:
        minElem = i
print(maxElem - minElem)