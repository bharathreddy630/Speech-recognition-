import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    return query.lower()
def respond_to_query(query):
    if "hello" in query:
        speak("Hello! How can I assist you today?")
    elif "time" in query:
        time_str = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {time_str}")
    elif "date" in query:
        date_str = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date_str}")
    elif "search" in query:
        speak("What do you want to search for?")
        search_query = take_command()
        if search_query != "None":
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Searching for {search_query}")
        else:
            speak("Sorry, I didn't catch that.")
    elif "stop" in query or "exit" in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I can only do basic tasks like telling the time or searching the web.")
if __name__ == "__main__":
    speak("Initializing voice assistant. How can I help you?")
    while True:
        query = take_command()
        if query != "None":
            respond_to_query(query)