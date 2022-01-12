# Найдите сумму и произведение элементов списка. Результаты вывести на экран
numbers = [1, 2, 3, 4, 5, 6]
sum_result = numbers[0]
mult_result = numbers[0]
counter = 1
list_len = len(numbers)

while counter < list_len:
    sum_result += numbers[counter]
    mult_result *= numbers[counter]
    counter += 1

print(sum_result)
print(mult_result)
