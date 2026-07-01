from voice_hub import ask, speak, say
from main.main_menu import main_menu
from file_system.file_main import run_file_manager
from memory_system.memory_main import run_memory_manager
from utilities.utilities_main import run_utilities

while True:
    main_menu()
    print()
    try:
        answer = int(ask("Please enter a number from 1 to 4 (inclusive): "))
    except ValueError:
        print()
        say("Invalid, Please try again ")
        continue
    
    if answer == 1:
        run_file_manager()
    elif answer == 2:
        run_memory_manager()
    elif answer == 3:
        run_utilities()
    elif answer == 4:
        say("Thank you for using Styfer Artifical Intelligence")
        break
    else:
        say("Please enter a valid number")
        continue