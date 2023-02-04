# Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

def square(a,b):
    if b == 1:
        return a
    else:
        return a*square(a,b-1)

print(square(first_number,second_number))