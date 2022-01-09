# Повторить все методы строковых объектов

# capitalize
print('pYtHoN'.capitalize())

# casefold
print('pYtHoN'.casefold())

# center
print('pYtHoN'.center(20, '*'))

# count
print('pYtHoN'.count('YtH'))

# encode
print('Кириллица'.encode())

# endswith
print('pYtHoN'.endswith('HoN'))

# expandtabs
print('pYtH	oN'.expandtabs())

# find
# Поиск подстроки в строке
print('Python'.find('th'))

# format
print('Hello {} {}'.format('world', 'python'))

# format_map
point = {'x': 4, 'y': -5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

# index
animals = ['cat', 'dog', 'rabbit', 'horse']
index = animals.index('dog')
print(index)

# isalnum
print('abc'.isalnum())
print('123'.isalnum())

# isalpha
txt = "CompanyX"
x = txt.isalpha()
print(x)

# isascii
'w z'.isascii()

# isdecimal
s = "28212"
print(s.isdecimal())

# isdigit
txt = "50800"
x = txt.isdigit()
print(x)

# isidentifier
str = 'Py thon'
print(str.isidentifier())

# islower
txt = "hello world!"
x = txt.islower()
print(x)

# 'isnumeric
print('10'.isnumeric())

# isprintable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

# isspace
txt = "   "
x = txt.isspace()
print(x)

# istitle
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

# isupper
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# join
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# ljust
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# lower
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# lstrip
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

# maketrans
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# partition
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# removeprefix
line = 'BaseTestCase'
print(line.removeprefix('Base'))

# removesuffix
line = 'BaseTestCase'
print(line.removesuffix('Case'))

# replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# rfind
my_str = 'barbarian'
print(my_str.rfind('bar'))

# rindex
my_str = 'barbarian'
print(my_str.rindex('bar'))

# rjust
str = "это строковый пример....wow!!!"
print(str.rjust(50, '*'))

# rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

# rsplit
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# rstrip
txt = "     banana     "
x = txt.rstrip()
print(x)

# split
txt = "welcome to the jungle"
x = txt.split()
print(x)

# splitlines
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# startswith
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# strip
txt = "     banana     "
x = txt.strip()
print(x)

# swapcase
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# title
txt = "Welcome to my world"
x = txt.title()
print(x)

# translate
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# upper
txt = "Hello my friends"
x = txt.upper()
print(x)

# zfill
txt = "50"
x = txt.zfill(10)
print(x)
