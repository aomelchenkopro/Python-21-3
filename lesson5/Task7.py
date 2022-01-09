# Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на
# экран сообщение об этом, а также остаток (если он есть) и частное
# (в любом случае).

a = int(input('a = '))
b = int(input('b = '))
c = a/b
d = a % b
if d == 0:
    print(f'The first number is divisible by the second. \nThe Result\
 of the division is {c}')
else:
    print(f"The first number isn't divisible by the second without a reminder\
\nThe result of the division is {c}, {d}")