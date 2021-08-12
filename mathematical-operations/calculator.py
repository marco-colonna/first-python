# Build a simple calculator that accepts a first number, an operation, and a second number.
# Make sure that you implement logic for the following results:
#   Sum, Difference, Product, Quotient, Exponent, Modulus
# If users fail to enter a numeric value or enter an operation that isn't recognized,
# tell them that there's a problem and exit.

print('Simple calculator!')

first_value = input('First number? ')
operation = input('Operation? ')
second_value = input('Second number? ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Please input a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

if operation == '+':
    total = first_value + second_value
    operation_name = 'Sum'
elif operation == '-':
    total = first_value - second_value
    operation_name = 'Difference'
elif operation == '*':
    total = first_value * second_value
    operation_name = 'Product'
elif operation == '/':
    total = first_value / second_value
    operation_name = 'Quotient'
elif operation == '**':
    total = first_value ** second_value
    operation_name = 'Exponent'
elif operation == '%':
    total = first_value % second_value
    operation_name = 'Modulus'
else:
    print('Operation not recognized.')
    exit()

print(operation_name + ' of ' + str(first_value) + ' ' + operation + ' ' + str(second_value) + ' equals ' + str(total))
