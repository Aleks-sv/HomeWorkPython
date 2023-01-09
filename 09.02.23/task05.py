# Задайте число. 
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input('Введите число '))

def positiveFib(num):
    posiveList = [0, 1]
    for i in range(num - 1):
        posiveList.append(posiveList[-2] + posiveList[-1])
    return posiveList

def negativeFib(num):
    negativeList = [0, 1]
    for i in range(num-1):
        negativeList.append(negativeList[-2] - negativeList[-1])
    return negativeList

print(negativeFib(number)[::-1] + positiveFib(number)[1:])