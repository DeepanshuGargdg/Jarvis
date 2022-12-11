import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import os
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def jokes():
    speak(pyjokes.get_jokes('hi',category='neutral'))
def  speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe(): 
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
            
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
            
        else:
            speak("Good Evening!") 
        speak("I am jarvis sir. Please tell me how may I help you")
            
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        
        print("say that again please...")
        return "None"
    return query
        
if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    while True:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google'  in query:
            webbrowser.open("google.com")  
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open jokes' in query:
            jokes()
        elif 'open codechef'  in query:
            webbrowser.open("codechef.com")  
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open spotify'  in query:
            webbrowser.open("spotify.com")  
        elif 'play music' in query:
            n=random.randint(0,3)
            print(n)
            music_dir ='C:\\Users\\HP\\OneDrive\\Desktop\\n'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
