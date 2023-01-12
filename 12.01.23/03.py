# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

import random

number = int(input('Введите длинну последовательности: '))
list = []
for i in range(number):
    list.append(random.randint(2, 5))
print(list)
print(set(list))