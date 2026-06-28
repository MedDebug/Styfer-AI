from utilities.calculator.styfer_calculator_main import run_styfer_calculator
from utilities.physics.physics_main import run_physics_manager
from utilities.utilities_menu import utilities_menu
from utilities.unit_conversions.unit_conversion_main import run_unit_converter
from utilities.currency_converter_manager import currency_conversions
from utilities.other_tools.other_tools_main import run_other_tools


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
            run_unit_converter()
        elif answer == 4:
            currency_conversions()
        elif answer == 5:
            run_other_tools()
        elif answer == 5:
            print("Thank you for using Styfer AI Utilities")
            break
        else:
            print("Please enter a valid integer from 1 to 4 (inclusive)")
            continue
        
        