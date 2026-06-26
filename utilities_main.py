from styfer_calculator_main import run_styfer_calculator
from physics_main import run_physics_manager
from utilities_menu import utilities_menu



def run_utilities():
    while True:
        utilities_menu()
        try:
            answer = int(input("Please enter a number from 1 to 4 (inclusive): "))
        except ValueError:
            print("Please enter a valid integer from 1 to 4 (inclusive)")
            continue
        
        if answer == 1:
            run_styfer_calculator()
        elif answer == 2:
            run_physics_manager()
        elif answer == 3:
            print("Coming soon")
        elif answer == 4:
            print("Thank you for using Styfer AI Utilities")
            break
        else:
            print("Please enter a valid integer from 1 to 4 (inclusive)")
            continue
        
        