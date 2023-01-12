# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

path = 'file05_1.txt'
data = open(path, 'r')
for lineOne in data:
    print(lineOne)
data.close()

path = 'file05_2.txt'
data = open(path, 'r')
for lineTwo in data:
    print(lineTwo)
data.close()

lineListOne = lineOne.split(' ')
#lineSet = set(lineListOne)
print(lineListOne)
numListOne = []
num = ''
for i in lineOne:
    if i.isdigit():
        num += i
    else:
        if num != '':
            numListOne.append(int(num))
            num = ''
if num != '':
    numListOne.append(int(num))
print(numListOne)

#print(lineSet)
#print(lineListOne[0][3])
#for i in lineListOne:
    











    
# temp = 'x**3 + 2x**2 + 27 = 0'
# temp1 = '3*x**3 + 4*x**1 + 2 = 0'
# data = open('file05_1.txt', 'w')
# data.writelines(temp)
# data.close

# data = open('file05_2.txt', 'w')
# data.writelines(temp1)
# data.close