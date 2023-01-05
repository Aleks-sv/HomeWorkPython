# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число '))
lengthNumber = len(str(number)) - 1
while number != int(number):
    number = round(number * 10, lengthNumber)
print(number)
sum = 0
while number > 0:
    result = number % 10
    sum += result
    number //= 10
print(round(sum))
