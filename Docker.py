import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os



engine = pyttsx3.init('sapi5')    # we used it to take voices
voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)     # time will be casted in int
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:  
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")

    speak("Hello! I am Docker. Please tell me how may I help you")    


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() # 'Recognizer' class helps to recognize audio
    with sr.Microphone() as source:   # used as source microphone
        print("Listening...")
        r.pause_threshold = 1     # seconds of non-speaking audio before a phrase is considered complete(means it user is taking 1 second of gap, then the program will nit complete the phase)
        #r.energy_threshold = 500   # increase energy_threshold value, if I want that my program will not listen any other voices
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed. "User said" means whatever user have said

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned that noting has been listen
    return query  

if __name__ == "__main__":
    #speak("Aj disha code kar rahi hai") 
    wishMe()
    while True:
     #if 1:
        query = takeCommand().lower() #Converting user query into lower case, and hence query will me match correctly

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")    # 'wikipedia' will be replced by blank ""
            results = wikipedia.summary(query, sentences=1)     # it will return two sentences from the wikipedia of input query
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I am Awesome")     

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  

        elif 'open google' in query:
            webbrowser.open("google.com")      

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")    

        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)    # 'listdir' make list of all the music files and stores in 'music_dir' directory
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")  

        elif 'favourite sweet of Disha' in query:
            speak("Disha's favourite sweet is Radsmalai")    


        elif 'who is Disha' in query:
            speak("Disha is a sweet girl") 

        elif 'open code' in query:
            codePath = "E:\\Visual Studio\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    