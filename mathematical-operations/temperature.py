# Build a program that prompts users for a temperature in Fahrenheit,
# performs conversion to Celsius, and then displays the Celsius temperature.
# If users enter a bad value, the program should
# tell them that there's a problem and then exit.

temperature = input('What is the temperature in Fahrenheit? ')

if temperature.isnumeric() == False:
    print('Input is not a number.')
    exit()

temperature = int(temperature)

temperature = int((temperature - 32) * 5 / 9)

print('Temperature in Celsius is ' + str(temperature) + '.')
