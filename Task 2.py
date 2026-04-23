import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Take voice command
def take_command():
    listener = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command

    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except Exception as e:
        print("Error:", e)
        speak("Microphone not working.")
        return ""

# Main assistant logic
def run_assistant():
    command = take_command()

    if command == "":
        return

    print("You said:", command)

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak("Today's date is " + date)

    elif "search" in command:
        try:
            topic = command.replace("search", "")
            info = wikipedia.summary(topic, 1)
            speak(info)
        except:
            speak("Sorry, I couldn't find information.")

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "hello" in command:
        speak("Hello! How can I help you?")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Please say the command again.")

# Run assistant
while True:
    run_assistant()