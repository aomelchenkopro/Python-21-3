# Определите, есть ли в списке повторяющиеся элементы, если да, то
# вывести на экран это значение
numbers = [1, 2, 3, -1, -1, 4, 55, 4, 5, 6]
duplicates = []
for i in numbers:
    if numbers.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

print(f"The list of duplicates {duplicates}")
