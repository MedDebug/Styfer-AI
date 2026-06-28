
from main.main_menu import main_menu
from file_system.file_main import run_file_manager
from memory_system.memory_main import run_memory_manager
from utilities.utilities_main import run_utilities
import pyttsx3 as ts

engine = ts.init()

while True:
    main_menu()
    engine.say("Please enter a number from 1 to 4 (inclusive): ")
    engine.runAndWait()
    try:
        answer = int(input("Please enter a number from 1 to 4 (inclusive): "))
    except ValueError:
        print("Please enter a number from 1 to 4 (inclusive) ")
        continue
    
    if answer == 1:
        run_file_manager()
    elif answer == 2:
        run_memory_manager()
    elif answer == 3:
        run_utilities()
    elif answer == 4:
        print("Thank you for using Styfer AI")
        break
    else:
        print("Please enter a valid number")
        continue