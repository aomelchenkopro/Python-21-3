# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли
# он разносторонним, равнобедренным или равносторонним.

a = int(input('Please, enter the first segment length: '))
b = int(input('Please, enter the second segment length: '))
c = int(input('Please, enter the third segment length: '))

triangle_exists = False
if a < (b+c) and b < (a+c) and c < (a+b):
    triangle_exists = True

if triangle_exists:
    print('Triangle exists')

    if a == b == c:
        print('Triangle is equilateral')
    elif (a == b) or (b == c) or (a == c):
        print('Triangle is isosceles')

    if a != b != c:
        print('Triangle is versatile')
else:
    print("Triangle doesn't exist")
