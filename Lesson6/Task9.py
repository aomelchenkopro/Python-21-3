# Поменять местами самый большой и самый маленький элементы списка
# Please, make sure that numbers which is in the list are not duplicated
numbers = [1, 2, 3, -1, 55, 4, 5, 6, 1000, 33, 44, 46, 57]
max_element = numbers[0]
min_element = numbers[0]

for i in numbers:
    if i > max_element:
        max_element = i
    if i < min_element:
        min_element = i
    max_index = numbers.index(max_element)
    min_index = numbers.index(min_element)

print(numbers)
numbers.pop(max_index)
numbers.pop(min_index)
numbers.insert(max_index-1, min_element)
numbers.insert(min_index, max_element)

print(numbers)
