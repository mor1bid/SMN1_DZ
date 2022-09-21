# print('hello world')
# int, float, boolean, str, list, None
value = None
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12334
s = 'hi bob'

print (s)
# интерполяция
print(a, ' - ',b, ' - ', s)
print('{} - {} - {}'.format(a, b, s)) 
print(f'{a} - {b} - {s}')
# bool
f = True
print (f)

list = ['1', '2', '3', 'hello',]
print (list)
# аккуратнее с пробелами

a = int(input())
b = int(input())
print(a, '+', b, '=', a+b)
a = float(input()) #дробные числа ввод
b = float(input())
print(a, '+', b, '=', a+b)

a = 123
b = 321
c = a/b # дробное число
c = a//b # целая часть дробного числа
с = a*b
c = a**b # возведение в степень
print(c)
d = 1.2
e = 12
de = round(d*e) # то же, что и Math.Round

a = 1 > 4 and 5 > 2
print(a)
func = 1
T = 4
x = 123
print(func<T>x)
f = 1>2 or 4<6
print(f)
f = [1,2,3,4]
print(2 in f)

# чётное\нечётное?
is_odd = f[0] % 2 == 0
print(is_odd)

#  ЦИКЛЫ

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

orig = int(input())
inv = 0
while orig != 0:
    inv = inv * 10 + (orig % 10)
    orig //= 10
else:
    print('ты волшебник гарри')
print(inv)

list = range[11]
for i in list:
    print(i)
for i in range[1, 11, 2]:
    print(i)

# списки
nums = [1,2,3,4,5]
rain = range(1,6)
print(type(rain))
nums = list(rain) # приведение типа range к типу list
print(f'{len(nums)} len') # длина массива
print(nums)
nums[0] = 10
print(nums)
for i in nums:
    i*=2
    print(i)
print(nums)

# ФУНКЦИЯ

#x = int(input())
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = x
print(f(arg))
print(type(f(arg))) # пишет тип