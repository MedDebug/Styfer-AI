import win32com.client


# ---------------- Voice Setup ----------------

speaker = win32com.client.Dispatch("SAPI.SpVoice")


# ---------------- Voice Functions ----------------

def speak(text):
    speaker.Speak(str(text))

def say(text):
    print(text)
    speak(text)

def ask(text):
    speak(text)
    return input(text)


def set_rate(rate):
    speaker.Rate = rate


def set_volume(volume):
    speaker.Volume = volume


def show_available_voices():
    voices = speaker.GetVoices()

    for i in range(voices.Count):
        voice = voices.Item(i)
        print(f"{i} - {voice.GetDescription()}")


def change_voice():
    voices = speaker.GetVoices()

    while True:
        index = get_int("Please enter a voice index: ")

        if 0 <= index < voices.Count:
            speaker.Voice = voices.Item(index)
            say("Voice changed successfully.")
            break
        else:
            say("Please enter a valid index starting from 0.")


# ---------------- Input Helper Functions ----------------

def get_int(prompt):
    while True:
        try:
            return int(ask(prompt))
        except ValueError:
            speak("Please enter a valid number.")


def get_float(prompt):
    while True:
        try:
            return float(ask(prompt))
        except ValueError:
            speak("Please enter a valid number.")


def get_non_zero_float(prompt, name):
    while True:
        number = get_float(prompt)

        if number == 0:
            speak(f"{name} cannot be zero.")
            continue

        return number