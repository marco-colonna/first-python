# print(type('Hello world')) # <class 'str'>
# print(type(7)) # <class 'int'>

# print(type(True)) # <class 'bool'>
# print(type(False)) # <class 'bool'>

# print(type('True')) # <class 'str'>
# print(type('False')) # <class 'str'>

# print(bool('True')) # true
# print(bool('False')) # true
# print(bool('')) # false
# print(bool(' ')) # true
# print(bool('Hello world!')) # true

# print(bool(7)) # true
# print(bool(1)) # true
# print(bool(0)) # false
# print(bool(-1)) # true

# print(1 + 1 == 3) # false
# print(1 + 1 == 2) # true

# print(3 == 4) # false
# print(3 != 4) # true

# print(3 > 4) # false
# print(3 < 4) # true
# print(3 >= 4) # false
# print(3 <= 4) # true

first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')
