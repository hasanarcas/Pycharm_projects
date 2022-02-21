import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0])
engine.setProperty("rate", 120)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def listen_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "hey":
                command = command.replace("hey", "")
            if "bob" in command:
                command = command.replace("bob", "")
    except:
        pass
    if not command:
        engine.runAndWait()
    return command


def run_Bob():
    command = listen_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        kit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        talk("It is " + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    else:
        talk("English          motherfucker,                                                                                                            do you speak it?")

while(True):
    run_Bob()