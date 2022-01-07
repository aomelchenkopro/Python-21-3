# Определить четверть координатной плоскости, которой принадлежит точка.
# Координаты точки ввести с клавиатуры

x = int(input('Enter x: '))
y = int(input('Enter y: '))
if x > 0 and y > 0:
    print('1')
elif x < 0 < y:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 > y:
    print('4')
