import pyttsx3 as ts 
engine = ts.init()

#-----------------------------HELPER FUNCTIONS-------------------------------

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")

#-----------------------------------------------------------------------------

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def set_rate(rate):
    engine.setProperty('rate', rate)

def set_volume(volume):
    engine.setProperty('volume', volume)

def show_available_voices():
    voices = engine.getProperty('voices')
    for i in range(len(voices)):
        print(f"{i} - {voices[i].name}")

def change_voice():
    voices = engine.getProperty('voices')
    while True:
        index = get_int("Please enter a valid index: ")
        try:
            engine.setProperty('voice',voices[index].id)
            print("Voice changed successfully")
            break
        except IndexError:
            print("Please enter a valid index starting from 0")
            continue


#-----------------------------HELPER FUNCTIONS--------------------

def ask(text):
    speak(text)
    return input(text)

def get_float(prompt):
    while True:
        try:
            return float(ask(prompt))
        except ValueError:
            speak("Please enter a valid number")

def get_int(prompt):
    while True:
        try:
            return int(ask(prompt))
        except ValueError:
            speak("Please enter a valid number")

def get_non_zero_float(prompt, name):
    while True:
        number = get_float(prompt)
        if number == 0:
            speak(f"{name} cannot be 0.")
            continue
        return number
    
#---------------------------------------------------------------