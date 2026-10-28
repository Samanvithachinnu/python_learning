import speech_recognition as sr
import pyttsx3
import webbrowser 
from datetime import datetime

# initialise 
recognizer = sr.Recognizer() 
engine = pyttsx3.init() 

# speak function 
def speak(text):
    print('Assistant: ', text) 
    engine.say(text) 
    engine.runAndWait() 

# listen function 
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        # This is important for noisy background - Hyderabad traffic etc
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print('You: ', text)
            return text.lower()
        except sr.UnknownValueError:
            speak('I am unable to understand, please speak again')
            return ''
        except sr.RequestError:
            speak('I am unable to connect to the service, check your internet')
            return ''

print('Hi welcome to voice assistant, how can i help you')
speak('Hi welcome to voice assistant, how can i help you')

while True:
    command = listen() 
    
    if not command:
        continue

    # saying HI 
    if 'hello' in command:
        speak('Hi, how can I help you?') 
        
    elif 'time' in command: 
        curtime = datetime.now().strftime('%I:%M %p') 
        speak('Current time is ' + curtime)  
        
    elif 'open google' in command: 
        speak('Opening google')
        webbrowser.open('https://www.google.com') 
        
    elif 'open youtube' in command:
        speak('Opening youtube')
        webbrowser.open('https://www.youtube.com') 
        
    elif 'search' in command:
        query = command.replace('search', '', 1).strip()
        if query:
            speak('Searching for ' + query)
            webbrowser.open('https://www.google.com/search?q=' + query)
        else:
            speak('What should I search for?')
            
    elif 'exit' in command or 'stop' in command or 'bye' in command:
        speak('Goodbye, have a nice day')
        break