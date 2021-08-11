# In this challenge, you build a calorie counter that prompts the user for:
#   The current date (in any format)
#   Breakfast calories eaten
#   Lunch calories eaten
#   Dinner calories eaten
#   Snack calories eaten
# The program will then sum up all of the calories and format them into a message.

print("Today's date?")
date = input()
print("Breakfast calories?")
breakfast = int(input())
print("Lunch calories?")
lunch = int(input())
print("Dinner calories?")
dinner = int(input())
print("Snack calories?")
snack = int(input())
sum = breakfast + lunch + dinner + snack
print("Calorie content for " + date + ": " + str(sum))
