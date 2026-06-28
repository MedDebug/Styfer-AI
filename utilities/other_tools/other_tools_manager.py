import random
import string


# ---------------- Helper Functions ----------------

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")


def get_non_zero_float(prompt, name):
    while True:
        number = get_float(prompt)
        if number == 0:
            print(f"{name} cannot be 0.")
            continue
        return number


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")


# ---------------- Mini Tools ----------------

def random_number_generator():
    print("--------------- Random Number Generator ----------------")

    start = get_int("Enter starting number: ")
    end = get_int("Enter ending number: ")

    if start > end:
        print("Starting number cannot be greater than ending number.")
        return

    print("Result:", random.randint(start, end))


def dice_roller():
    print("--------------- Dice Roller ----------------")

    sides = get_int("Enter number of sides: ")

    if sides <= 0:
        print("Number of sides must be greater than 0.")
        return

    print("You rolled:", random.randint(1, sides))


def coin_flip():
    print("--------------- Coin Flip ----------------")
    print("Result:", random.choice(["Heads", "Tails"]))


def password_generator():
    print("--------------- Password Generator ----------------")

    length = get_int("Enter password length: ")

    if length <= 0:
        print("Password length must be greater than 0.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated password:", password)


def percentage_calculator():
    while True:
        print("""---------------- Percentage Calculator ----------------
1 - Find X% of Y
2 - Find What Percentage X is of Y
3 - Percentage Increase
4 - Percentage Decrease
5 - Exit""")

        try:
            answer = int(input("Please enter a number from 1 to 5: "))
        except ValueError:
            print("Please enter a valid integer from 1 to 5")
            continue

        if answer == 1:
            x = get_float("Please enter X: ")
            y = get_float("Please enter Y: ")
            print("Resultant:", (x / 100) * y)

        elif answer == 2:
            x = get_float("Please enter X: ")
            y = get_non_zero_float("Please enter Y: ", "Y")
            result = (x / y) * 100
            print(f"{x} is {result}% of {y}")

        elif answer == 3:
            old = get_non_zero_float("Please enter old value: ", "Old value")
            new = get_float("Please enter new value: ")
            increase = ((new - old) / old) * 100
            print("Increase:", increase, "%")

        elif answer == 4:
            old = get_non_zero_float("Please enter old value: ", "Old value")
            new = get_float("Please enter new value: ")
            decrease = ((old - new) / old) * 100
            print("Decrease:", decrease, "%")

        elif answer == 5:
            print("Thank you for using Styfer AI Percentage Calculator")
            break

        else:
            print("Please enter a valid number from 1 to 5")


def bmi_calculator():
    print("--------------- BMI Calculator ----------------")

    height = get_non_zero_float("Enter height in metres: ", "Height")
    weight = get_non_zero_float("Enter weight in kilograms: ", "Weight")

    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal Weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")