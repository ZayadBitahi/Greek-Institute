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

#exercice7
import random

def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring":
        return random.randint(5, 23)
    elif season == "summer":
        return random.randint(20, 40)
    elif season in ["autumn", "fall"]:
        return random.randint(5, 20)

def main():
    valid_seasons = ["winter", "spring", "summer", "autumn", "fall"]
    
    season = input("Enter the season (winter, spring, summer, autumn/fall): ").lower()
    while season not in valid_seasons:
        print("Please enter a valid season.")
        season = input("Enter the season (winter, spring, summer, autumn/fall): ").lower()
    
    temp = get_random_temp(season)
    print("The temperature right now is", temp, "degrees Celsius.")
    
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp <= 23:
        print("Mild weather — perfect for a walk.")
    elif temp <= 32:
        print("Warm and pleasant outside.")
    elif temp <= 40:
        print("It's hot outside, stay hydrated!")

main()

#exercice 8

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ").strip()
        
        if user_answer.lower() == item["answer"].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! The correct answer was: {item['answer']}")
            incorrect += 1
            wrong_answers.append({"question": item["question"], "your_answer": user_answer, "correct_answer": item["answer"]})
    
    return correct, incorrect, wrong_answers

def show_results(correct, incorrect, wrong_answers):
    print("\nQuiz Results ")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    
    if correct == len(data):
        print("Perfect score!")
    elif correct >= len(data) // 2:
        print("Not bad!.")
    else:
        print("Keep training, Padawan.")
    
    if wrong_answers:
        print("\nQuestions you got wrong:")
        for w in wrong_answers:
            print(f"Q: {w['question']}")
            print(f"   Your answer: {w['your_answer']}")
            print(f"   Correct answer: {w['correct_answer']}\n")

correct, incorrect, wrong_answers = ask_questions()
show_results(correct, incorrect, wrong_answers)