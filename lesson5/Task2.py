# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

a = int(input('Please, enter the first number: '))
b = int(input('Please, enter the second number: '))
c = int(input('Please, enter the third number: '))
message = None

if (c > a > b) or (b > a > c):
    message = f'The first number {a} is average'
elif (c > b > a) or (a > b > c):
    message = f'The second number {b} is average'
elif (a > c > b) or (b > c > a):
    message = f'The third number {c} is average'
else:
    message = "There aren't any average numbers"

print(message)
