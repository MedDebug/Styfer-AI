import random
import string
from voice_hub import say,ask,speak,get_float,get_int,get_non_zero_float

def random_number_generator():
    print("--------------- Random Number Generator ----------------")
    print()
    start = get_int("Enter starting number: ")
    end = get_int("Enter ending number: ")

    if start > end:
        say("Starting number cannot be greater than ending number.")
        return

    say(f"Result: {random.randint(start, end)}")

def dice_roller():
    print("--------------- Dice Roller ----------------")
    print()
    sides = get_int("Enter number of sides: ")

    if sides <= 0:
        say("Number of sides must be greater than 0.")
        return

    say(f"You rolled: {random.randint(1, sides)}")

def coin_flip():
    print("--------------- Coin Flip ----------------")
    print()
    say(f"Result: {random.choice(['Heads', 'Tails'])}") 

def password_generator():
    print("--------------- Password Generator ----------------")
    print()
    length = get_int("Enter password length: ")

    if length <= 0:
        say("Password length must be greater than 0.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)

    say(f"Generated password: {password}")


def percentage_calculator():
    while True:
        print("""---------------- Percentage Calculator ----------------
    1 - Find X% of Y
    2 - Find What Percentage X is of Y
    3 - Percentage Increase
    4 - Percentage Decrease
    5 - Exit""")
        print()
        answer = get_int(("Please enter a number from 1 to 5: "))

        if answer == 1:
            x = get_float("Please enter X: ")
            y = get_float("Please enter Y: ")
            say(f"Resultant:  {(x / 100) * y}")

        elif answer == 2:
            x = get_float("Please enter X: ")
            y = get_non_zero_float("Please enter Y: ", "Y")
            result = (x / y) * 100
            say(f"{x} is {result}% of {y}")

        elif answer == 3:
            old = get_non_zero_float("Please enter old value: ", "Old value")
            new = get_float("Please enter new value: ")
            increase = ((new - old) / old) * 100
            say(f"Increase: {increase}%")

        elif answer == 4:
            old = get_non_zero_float("Please enter old value: ", "Old value")
            new = get_float("Please enter new value: ")
            decrease = ((old - new) / old) * 100
            say(f"Decrease: {decrease}%")

        elif answer == 5:
            say("Thank you for using Styfer AI Percentage Calculator")
            break

        else:
            say("Please enter a valid number from 1 to 5")
            continue

def bmi_calculator():
    print("--------------- BMI Calculator ----------------")

    height = get_non_zero_float("Enter height in metres: ", "Height")
    weight = get_non_zero_float("Enter weight in kilograms: ", "Weight")

    bmi = weight / (height ** 2)

    say(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        say("Category: Underweight")
    elif bmi < 25:
        say("Category: Normal Weight")
    elif bmi < 30:
        say("Category: Overweight")
    else:
        say("Category: Obese")