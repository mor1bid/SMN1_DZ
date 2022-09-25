# # 1. Напишите программу, которая принимает на вход цифру, 
# # обозначающую день недели, и проверяет, 
# # является ли этот день выходным.

# myday = int(input('1. Введите номер дня недели: \n'))
# for i in range(1,6):
#     if myday == i:
#         print('Сегодня будний день.')
# for i in range(6,8):
#     if myday == i:
#         print('Сегодня выходной день.')
# if (myday>7):
#     print('Задано неверное значение!')


# #2. Напишите программу, которая принимает на вход 
# # координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# # и выдаёт номер четверти плоскости, 
# # в которой находится эта точка (или на какой оси она находится).

# print('2. Введите значения координат:')
# X = float(input('X: '))
# Y = float(input('Y: '))
# if X == 0 or Y == 0:
#     print('Данная точка лежит ни в одной из плоскостей.')
# if X > 0 and Y > 0:
#     print('Данная точка лежит в I четверти.')
# if X < 0 and Y > 0:
#     print('Данная точка лежит во II четверти.')
# if X < 0 and Y < 0:
#     print('Данная точка лежит в III четверти.')
# if X > 0 and Y < 0:
#     print('Данная точка лежит в IV четверти.')

# #3. Напишите программу, которая по заданному номеру четверти, 
# # показывает диапазон возможных координат точек 
# # в этой четверти (x и y).

from multiprocessing.resource_sharer import stop
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