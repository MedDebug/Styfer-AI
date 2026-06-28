from utilities.other_tools.other_tools_menu import other_tools_menu
from utilities.other_tools.other_tools_manager import (
    random_number_generator,
    dice_roller,
    coin_flip,
    password_generator,
    percentage_calculator,
    bmi_calculator
)

def run_other_tools():
    while True:
        other_tools_menu()
        try:
            answer = int(input("Please enter a number from 1 to 7 (inclusive): "))
        except ValueError:
            print("Please enter a valid integer from 1 to 7 (inclusive)")
            continue
        
        if answer == 1:
            random_number_generator()
        elif answer == 2:
            dice_roller()
        elif answer == 3:
            coin_flip()
        elif answer == 4:
            password_generator()
        elif answer == 5:
            bmi_calculator()
        elif answer == 6:
            percentage_calculator()
        elif answer == 7:
            print("Thank you for using Styfer AI Basic Toolkit")
            break
        else:
            print("Please enter a valid number from 1 to 7 (inclusive) ")
            continue
