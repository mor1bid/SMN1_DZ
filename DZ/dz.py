work = range(1,5)
holiday = range(6,7)
myday = int(input('Введите номер дня недели: \n'))
for i in work:
    if myday == i:
        print('Сегодня будний день.')
        exit()
for i in holiday:
    if myday == i:
        print('Сегодня выходной день.')
    else:
        print('Задано неверное значение!')