# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
#  Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число '))

def decToBin(num, result = ""):
    if num == 0:
        return result[::-1]
    result += str(num%2)
    return decToBin(num//2, result)
print(decToBin(number))