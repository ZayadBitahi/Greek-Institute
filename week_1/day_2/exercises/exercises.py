from functools import reduce
#exercice 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

#exercice 2
family = {
    "rick": {
        "name": "rick",
        "age": 43
    },
    "beth": {
        "name": "beth",
        "age": 13
    },
    "morty": {
        "name": "morty",
        "age": 5
    },
    "summer": {
        "name": "summer",
        "age": 8
    }   
}


for person in family: 
    age = family[person]["age"]  

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(family[person]['name'].title(), "has to pay $", price)

total_price = reduce(lambda x, y: x + y, [0 if family[person]["age"] < 3 else 10 if family[person]["age"] <= 12 else 15 for person in family])
print("Total price for the family is $", total_price)

#exercice 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
client = brand["type_of_clothes"]
print("Zara's clients are:", client[0] + ", "+ client[1]+ " and", client[2])
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print("The last Zara's competitor is", brand["international_competitors"][-1])
print("The major colors in the US are", brand["major_color"]["US"][0], "and", brand["major_color"]["US"][1])
print("The amount of key value pairs in this dictionary is", len(brand))
print("The keys of the brand dictionary are::", brand.keys())
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print("The number_of_stores value became", brand["number_stores"] , ", it was updated when we merged the dictionaries.") 

#exercice 4
def describe_city(city, country="Noxus"):
    print(city +" is in " + country + ".")

describe_city("The Immortal Bastion")
    

#exercice 5



import random
def enter_number(number):
    number = int(input("Enter a number between 1 and 100: "))
    correct_number = random.randint(1, 100)
    while number < 1 or number > 100:
        number = int(input("Please enter a number between 1 and 100: "))
    if number != correct_number:
        print(number , "is the wrong number, the correct number is", correct_number , ".")
    else:
        print("Congratulations! You guessed the number", correct_number, "!")

enter_number(0)

#exercice 6

#Questions 1-2
def make_shirt(size="L", message="I love Python"):
    print(f"The shirt size is {size} and the message on it is: '{message}'.")

make_shirt("XXXL", "I am a fitness model, the before picture.")
#Questions 3-4
def make_shirt(size="L", message="I love Python"):
    print(f"The shirt size is {size} and the message on it is: '{message}'.")

make_shirt()
#Question 5
def make_shirt(size="M", message="I love Python"):
    print(f"The shirt size is {size} and the message on it is: '{message}'.")
#Question 6
def make_shirt(size, message="I love D&D"):
    print(f"The shirt size is {size} and the message on it is: '{message}'.")
