import json 
import os

def create_memory_file():
    user_details = {
        "User_name": "Medhansh",
        "Age": 19,
        "Home_directory": "C:\\Users\\Medhansh\\Desktop",
        "Current_project": "Styfer AI"
        }
            
    with open("memory.json", "w") as starter_data:
        json.dump(user_details,starter_data)
        
def load_memory():
    with open("memory.json", "r") as starter_data:
        memory = json.load(starter_data)
    return memory
        
if os.path.isfile("memory.json"):
    loaded_memory = load_memory()
else:
    create_memory_file()
    loaded_memory = load_memory()
    print(loaded_memory)
    

