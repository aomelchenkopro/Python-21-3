# Из двух случайных чисел, одно из которых четное, а другое нечетное,
# определить и вывести на экран нечетное число.

a = 11
b = 12
message = None

if b % 2 == 0 and a % 2 == 0:
    message = 'Both numbers are even'
elif b % 2 == 0:
    message = f'{b} is even'
elif a % 2 == 0:
    message = f'{a} is even'
else:
    message = "There aren't any even numbers"
print(message)
