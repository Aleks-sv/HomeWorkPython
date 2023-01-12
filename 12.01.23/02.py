# Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.

number = int(input('Введите натуральное чсило: '))
list = []

while number > 1:
    if number%2 == 0:
        list.append(2)
        number /= 2
    elif number%3 == 0:
        list.append(3)
        number /= 3
    elif number%5 == 0:
        list.append(5)
        number /= 5
    elif number%7 == 0:
        list.append(7)
        number /= 7
    elif number%11 == 0:
        list.append(11)
        number /= 11
    elif number%13 == 0:
        list.append(13)
        number /= 13
    elif number%number ==0:
        list.append(number)
        number /= number
print(list)
