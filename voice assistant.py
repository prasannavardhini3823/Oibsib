import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning buddy!")
    elif 12 <= hour < 18:
        speak("Good Afternoon buddy!")
    else:
        speak("Good Evening buddy!")
    speak("I am JARVIS your voice Assistant. How can I help you today?")

def take_command():
    # It takes microphone input from the user and returns string output
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service; check your network connection.")
            return "None"
        except Exception as e:
            print(f"Error: {e}")
            return "None"
        return query
    except OSError as e:
        print(f"Error: {e}")
        speak("No microphone found. Please check your microphone settings and try again.")
        return "None"

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")

def tell_date():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Today's date is {today}")

def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

def search_web(query):
    speak("Searching the web...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if query == "none":
            continue
        elif 'hello' in query:
            speak("Hello! How can I assist you?")
        elif 'time' in query:
            tell_time()
        elif 'date' in query:
            tell_date()
        elif 'wikipedia' in query:
            search_wikipedia(query)
        elif 'search' in query:
            search_web(query)
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day!")
            break