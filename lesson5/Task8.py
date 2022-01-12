str1 = '''  File "leveleUp.py", line 34
    tem = 5 if current_temperature >= 5
                                      ^
SyntaxError: invalid syntax ”””'''

str2 = '''Traceback (most recent call last):
  File "leveleUp.py", line 18, in <module>
    print("current_temperature: ---------", current_temperature, f"Type is: ----- {type(current_temperature)}")
NameError: name 'current_temperature' is not defined
'''

elements = [str1, str2]
rows = None
for e in elements:
    rows = e
    if str1.find('SyntaxError: '):
        rows = str1.split('\n')
        rows[len(rows)-1] = 'Hello world'
print('\n'.join(rows))
