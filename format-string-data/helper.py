# message = str.capitalize('first message') # member of the str class
# print(message)

# message = 'second message'.capitalize() # member of the literal string
# print(message)

# message = 'third message'
# print(message.capitalize()) # member of a variable

# message = 'hello world'
# print(message.lower())
# print(message.upper())

# message = message.title()
# print(message)
# print(message.swapcase())

# location = 'Mississippi'
# print(location.count('s'))

# print(len('how many characters in this string?'))

# message = 'racecar'
# print(message.startswith('r')) # True
# print(message.startswith('a')) # False
# print(message.startswith('ra')) # True

# print(message.endswith('r')) # True
# print(message.endswith('a')) # False
# print(message.endswith('ar')) # True

# message = 'The quick brown fox jumps over the lazy dog'
# print(message.find('q'))

# print(message.find('t'))
# print(message.find('T'))

# message = '    middle     '
# print('.' + message.lstrip() + '.')
# print('.' + message.rstrip() + '.')
# print('.' + message.strip() + '.')

# message = 'brevity is the essence of wit'
# message = message.replace('essence', 'soul')
# print(message)

message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))
