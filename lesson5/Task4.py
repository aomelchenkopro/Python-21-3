# Вводятся три целых числа. Определить какое из них наибольшее.

a = int(input('Please, enter the first number: '))
b = int(input('Please, enter the second number: '))
c = int(input('Please, enter the third number: '))

if (c > a > b) or (c > b > a):
    message = f'{c} is the biggest number'
elif (b > c > a) or (b > a > c):
    message = f'{b} is the biggest number'
elif (a > b > c) or (a > c > b):
    message = f'{a} is the biggest number'
else:
    message = "There aren't any average numbers"

print(message)
