from utilities.calculator.styfer_calculator_menu import show_styfer_calculator_menu
from voice_hub import ask,say,speak
from utilities.calculator.styfer_calculator_manager import basic_calculation, square_root, squaring, cube_root, cubing, quadratic_equations, power, distance_formula

def run_styfer_calculator():
    while True:
        show_styfer_calculator_menu()
        print()
        try:
            answer = int(ask("Please enter a number from 1 to 9 (inclusive): "))
        except ValueError:
            print()
            say("Invalid, please try again")
            continue
        
        if answer == 1:
            basic_calculation()
        elif answer == 2:
            squaring()
        elif answer == 3:
            square_root()
        elif answer == 4:
            cubing()
        elif answer == 5:
            cube_root()
        elif answer == 6:
            quadratic_equations()
        elif answer == 7:
            power()
        elif answer == 8:
            distance_formula()
        elif answer == 9:
            say("Thank you for using Styfer AI Utilities")
            break
        else:
            say("Please enter a valid integer")
            continue

