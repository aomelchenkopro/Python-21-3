# Имееться два списка. Проверить все ли элементи
# втрого списка присутствуют в первом списке.
a = [1, 2, 3, 4, "a", "b", "c", [9, 8, 7]]
b = [1, "a", "b"]
is_accepted = True
for e in b:
    if e not in a:
        print("Not all elements exist in the first list")
        is_accepted = False
        break

if is_accepted:
    print("All elements exist in the first list")
