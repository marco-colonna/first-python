# print(type('7')) # <class 'str'>
# print(type(7)) # <class 'int'>
# print(type(7.1)) # <class 'float'>

print(isinstance('7', str)) # True
print(isinstance(7, int)) # True
print(isinstance(7.1, float)) # True

print(isinstance(7, str)) # False
print(isinstance('7', int)) # False
print(isinstance('7.1', float)) # False
