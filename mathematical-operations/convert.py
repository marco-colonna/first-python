# numeric_value = '7'
# print(numeric_value.isnumeric()) # True

# string_value = 'Bob'
# print(string_value.isnumeric()) # False

first_value = input('First Number: ')
second_value = input('Second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Please enter numbers only.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))