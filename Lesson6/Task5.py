# Пользователь вводит число. Определить, содержит ли список данное число x.
# Вивести информационное сообщение содержит или не содержит
fl_contain = False
numbers = [1, 2, 3, 4, 5, 6, 7]

x = int(input("x = "))
if x in numbers:
    fl_contain = True

if fl_contain == True:
    print("The list contains x")
else:
    print("The list doesn't contain x")
