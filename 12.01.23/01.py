# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

number = int(input('Задайте точность: '))
print(math.pi)
print(f'Число pi c точностью {number} = {(round(math.pi * 10**number)) / 10**number}')