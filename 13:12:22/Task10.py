# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


pointFirstX = int(input('Введите координаты первой точки по оси X = '))
pointFirstY = int(input('Введите координаты первой точки по оси Y = '))
pointSecondX = int(input('Введите координаты второй точки по оси X = '))
pointSecondY = int(input('Введите координаты второй точки по оси Y = '))

result = ((pointSecondX - pointFirstX)**2 + (pointSecondY - pointFirstY)**2)**0.5
print(f'Расстояние между двумя точками = {round(result, 3)}')