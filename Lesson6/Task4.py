# Сформировать возрастающий список из чётных чисел (количество элементов 45)


inter_counter = 0
even = 0
even_number = []

while inter_counter < 45:
    even_number.append(even)
    even += 2
    inter_counter += 1

print(even_number)
