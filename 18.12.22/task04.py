# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Введите число '))
listNumber = []
for i in range(- number, number + 1):
    listNumber.append(i)
print(listNumber)

file = open("File.txt", "r")
date = file.readlines()
for i in range(len(date)):
    date[i] = int(date[i].strip())
print(date)
resultMulty = 1
for i in range(len(date)):
    resultMulty *= listNumber[date[i]]
print(resultMulty)