from utilities.calculator.styfer_calculator_menu import show_styfer_calculator_menu
from utilities.calculator.styfer_calculator_manager import basic_calculation, square_root, squaring, cube_root, cubing, quadratic_equations, power, distance_formula

def run_styfer_calculator():
    while True:
        show_styfer_calculator_menu()
        try:
            answer = int(input("Please enter a number from 1 to 9 (inclusive): "))
        except ValueError:
            print("Please enter a valid integer from 1 to 9 (inclusive)")
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
            print("Thank you for using Styfer AI Utilities")
            break
        else:
            print("Please enter a valid integer from 1 to 9 (inclusive)")
            continue

