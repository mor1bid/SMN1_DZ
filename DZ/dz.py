# # 1. Напишите программу, которая принимает на вход цифру, 
# # обозначающую день недели, и проверяет, 
# # является ли этот день выходным.

myday = int(input('1. Введите номер дня недели: \n'))
for i in range(1,6):
    if myday == i:
        print('Сегодня будний день.')
for i in range(6,8):
    if myday == i:
        print('Сегодня выходной день.')
if (myday>7):
    print('Задано неверное значение!')


# # 2. Напишите программу, которая принимает на вход 
# # координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# # и выдаёт номер четверти плоскости, 
# # в которой находится эта точка (или на какой оси она находится).

print('2. Введите значения координат:')
X = float(input('X: '))
Y = float(input('Y: '))
if X == 0 or Y == 0:
    print('Данная точка лежит ни в одной из плоскостей.')
if X > 0 and Y > 0:
    print('Данная точка лежит в I четверти.')
if X < 0 and Y > 0:
    print('Данная точка лежит во II четверти.')
if X < 0 and Y < 0:
    print('Данная точка лежит в III четверти.')
if X > 0 and Y < 0:
    print('Данная точка лежит в IV четверти.')

# # 3. Напишите программу, которая по заданному номеру четверти, 
# # показывает диапазон возможных координат точек 
# # в этой четверти (x и y).

import random
num = int(input('3. Введите значение четвери координат: \n'))
if num>4 or num<=0:
    print('Заданно некорректное значение.')
else:
    print('В данной четверти лежат координаты: ')
    for i in range(11):
        if (num==1):
            X = round(random.uniform(1, 11.5), 2)
            Y = round(random.uniform(1, 11.5), 2)
        elif (num==2):
            X = round(random.uniform(-1, -11.5), 2)
            Y = round(random.uniform(1, 11.5), 2)
        elif (num==3):
            X = round(random.uniform(-1, -11.5), 2)
            Y = round(random.uniform(-1, -11.5), 2)
        elif (num==4):
            X = round(random.uniform(1, 11.5), 2)
            Y = round(random.uniform(-1, -11.5), 2)
        print('(', X, ',', Y, ')')

# # 4. Напишите программу, которая принимает на вход координаты двух точек 
# # и находит расстояние между ними в 2D пространстве.

import math
print('4. Введите значения координат 1-й точки:')
X1 = float(input('X: '))
Y1 = float(input('Y: '))
print('Введите значения координат 2-й точки:')
X2 = float(input('X: '))
Y2 = float(input('Y: '))
distance = round(math.sqrt((X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1)), 3)
print('Расстояние между точками А(', X1, ',', Y1, ') и Б(', X2, ',', Y2, ') =', distance)

# # 5. Напишите программу для. проверки истинности утверждения 
# # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('5. Введите значения 3-х предикат:')
for i in range(999):
    X=int(input('X: '))
    if X == 1: 
        X = bool(True)
    elif X == 0: 
        X = bool(False)
    else: 
        print('Задано некорректное значение.')
        exit()
    Y=int(input('Y: '))
    if Y == 1: 
        Y = bool(True)
    elif Y == 0: 
        Y = bool(False)
    else: 
        print('Задано некорректное значение.')
        exit()
    Z=int(input('Z: '))
    if Z == 1: 
        Z = bool(True)
    elif Z == 0: 
        Z = bool(False)
    else: 
        print('Задано некорректное значение.')
        exit()
    res = not(X or Y or Z) == (not X and not Y and not Z)
    print(res)
    print('Введите значения 3-х предикат:')
