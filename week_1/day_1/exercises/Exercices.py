#exercice 1
print ("Hello World"+"\n" * 4)

#exercice 2
print((99**3)*8)

#exercice 3
your_name = input("Enter your name: ")
my_name = "Zayad"
if your_name == my_name:
    print("STOP! YOU CAN'T HAVE IT! IT'S MINE AND ONLY MINE!")
else:
    print("Hello " + your_name + "! I wish you had a better name like mine!")

#Exercice 4
your_height = int(input("Enter your height in cm: "))
if your_height >145:
    print("You can ride the roller coaster!")
else:
    print("Sorry you cannot ride, go drink some milk, good luck next year!")

#Exercice 5
my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(11)
my_fav_numbers.add(12)
my_fav_numbers.remove(12)
friend_fav_numbers = {6, 7, 8, 9, 10}
our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print("Our favorite numbers are: ", our_fav_numbers)

#Exercice 6
my_tuple = (1, 2, 3, 4, 5)
#It is not possible to add elements to a tuple.

#Exercice 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()
print(basket)

#Exercice 8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
print("The following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print("I made your" + sandwich)


