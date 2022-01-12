# Найти наибольший элемент списка и вывести его на экран
numbers = [1, 2, 3, -1, 55, 4, 5, 6]
max_element = numbers[0]

for i in numbers:
    if i > max_element:
        max_element = i

print(f"The max element is {max_element}")
