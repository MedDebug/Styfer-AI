from utilities.unit_conversions.unit_conversion_menu import unit_conversion_menu
from utilities.unit_conversions.unit_conversions_manager import (
    volume_conversions,
    area_conversions,
    length_distance_conversions,
    mass_conversions,
    time_conversions,
    temperature_conversions,
    speed_conversions,
    pressure_conversions,
    energy_conversions
)
from voice_hub import ask,say,speak

def run_unit_converter():
    while True:
        unit_conversion_menu()
        print()
        try:
            answer = int(ask("Please enter an integer from 1 to 10 (inclusive): "))
        except ValueError:
            print()
            print("Invalid, please try again")
            continue
        
        if answer == 1:
            volume_conversions()
        elif answer == 2:
            area_conversions()
        elif answer == 3:
            length_distance_conversions()
        elif answer == 4:
            mass_conversions()
        elif answer == 5:
            time_conversions()
        elif answer == 6:
            temperature_conversions()
        elif answer == 7:
            speed_conversions()
        elif answer == 8:
            pressure_conversions()
        elif answer == 9:
            energy_conversions()
        elif answer == 10:
            print()
            say("Thank you for using Styfer AI Unit Converter")
            break
        else:
            say("Please enter a valid integer")
            continue
