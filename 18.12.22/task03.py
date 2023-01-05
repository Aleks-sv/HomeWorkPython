# Задайте список из n чисел последовательности 
# (1+1\n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

number = int(input('Введите число '))
dictNum = {}
sumNum = 0
for i in range(1, number+1):
    dictNum[i] = round((1+1/i)**i, 2)
print(dictNum)
for i in dictNum.values():
    sumNum += i
print(sumNum)