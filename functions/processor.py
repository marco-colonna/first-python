# The process_numbers() function must select all numeric values, even those values that are strings,
# and return them as a list. The values must be converted to numbers and included in the returned list.
# The list must be sorted. The function must handle the possibility that the input parameter isn't
# formatted as a list. In that case, it must return an empty list.

def process_numbers(my_list):
    numbers = []

    if isinstance(my_list, list) == False:
        return numbers

    for number in my_list:
        if str(number).isnumeric():
            numbers.append(int(number))

    numbers.sort()

    return numbers

# The process_names() function must select all string values that aren't numeric and return them as a list.
# The list must be sorted. The function must handle the possibility that the input parameter isn't
# formatted as a list. In that case, it must return an empty list.

def process_names(my_list):
    names = []

    if isinstance(my_list, list) == False:
        return names
    
    for name in my_list:
        if str(name).isnumeric() == False:
            names.append(str(name))

    names.sort()
    
    return names
