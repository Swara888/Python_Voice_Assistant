import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys
import time

# ---------- INITIALIZE VOICE ENGINE ----------
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # default system voice

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)  # allow buffer flush

# ---------- SPEECH RECOGNITION ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Internet connection problem.")
        return ""

# ---------- COMMAND HANDLER ----------
def process_command(command):
    if command == "":
        return

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            speak("Searching Google")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        sys.exit()

    else:
        speak("Sorry, I cannot do that yet.")

# ---------- MAIN ----------
def main():
    speak("Voice assistant started.")
    speak("Say hello to begin.")

    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()
