# Вводятся координаты (x; y) точки и радиус круга (r). Определить принадлежит
# ли данная точка кругу, если его центр находится в начале координат.

x = float(input('Enter x: '))
y = float(input('Enter y: '))
r = float(input('Enter r: '))
h = (x ** 2 + y ** 2) ** 0.5

if h <= r:
    message = 'The point belongs to the circle'
else:
    message = "The point doesn't belongs to the circle"

print(message)
