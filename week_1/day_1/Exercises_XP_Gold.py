#exercise 1

month = int(input("Enter a month number (1-12): "))

if month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Autumn"
elif month == 12 or month == 1 or month == 2:
    season = "Winter"
else:
    season = "Come on man, there are only 12 months in a year!"

print("Season:", season)

#exercise 2

#first part
for number in range(1, 21):
    print(number)

#second part
for even_number in range(1, 21):
    if even_number % 2 == 0:
        print(even_number)


#exercise 3

while True:
    name = input("Enter your name: ")
    if name == "Zayad":
        break

#exercise 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name(2): ")

if user_name in names:
    index = names.index(user_name)
    print(index)
else:
    print("Name not found.")

#exercise 5


num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

greatest = num1
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3

print("The greatest number is:", greatest)


#exercise 6

import random

while True:
    guess = input("Guess a number between 1 and 9, or type quit to stop: ")

    if guess == "quit":
        break

    guess = int(guess)
    random_number = random.randint(1, 9)

    if guess == random_number:
        print("Winner")
    else:
        print("Better luck next time.")