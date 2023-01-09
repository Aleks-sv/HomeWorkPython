# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

listNum = []
for i in range(random.randint(0, 10)):
    listNum.append(random.randint(0, 20))
print(listNum)

resultList = []
middleElem = len(listNum)//2 + len(listNum)%2
for i in range(middleElem):
    resultList.append(listNum[i] * listNum[len(listNum) - i - 1])
print(resultList)