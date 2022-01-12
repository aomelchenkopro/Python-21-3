# 1. Изучить методи пространсва имен списков
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
# '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort']

# Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# Copy the fruits list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# Return the number of times the value "cherry" appears in the fruits list
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

# Add the elements to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# The index() method returns the position at the first
# occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# The insert() method inserts the specified value at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# The pop() method removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop(1))

# The remove() method removes the first occurrence of the element
# with the specified value.
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# The reverse() method reverses the sorting order of the elements.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# The sort() method sorts the list ascending by default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
