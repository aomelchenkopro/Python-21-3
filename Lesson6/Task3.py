# Заполнить список ста нулями, кроме первого и последнего элементов,
# которые должны быть равны единице
zeros = []

for i in range(100):
    zeros.append(1 if i == 0 or i == 99 else 0)

print(zeros)
