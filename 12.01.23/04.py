# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Задайте натуральную степень: '))

coef = list(range(0, 101))
str = []
temp = ''
for i in range(0, k):
    str.append(f'{random.choice(coef)}*X**{k}')
    k -= 1
    if k == 0:
        str.append(f'{random.choice(coef)}')
#print(str)
for i in range(0,len(str)-1):
    temp += str[i] + ' + '
temp += str[-1] + ' = 0'
print(temp)

data = open('file04.txt', 'w')
data.writelines(temp)
data.close

