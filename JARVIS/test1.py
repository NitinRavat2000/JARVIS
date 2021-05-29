import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import os
import smtplib


import webbrowser


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello Nitin Ravat,i am alexa. please tell me how may i help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index = 1, sample_rate = 48000, 
                        chunk_size = 2048) as source:
        
        print("Listening...")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        #query = r.recognize_google(audio)
        #audio=r.record(source,duration=5)
        
        query =  r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
       print('Did not get you try again....')
    
   
    return query



if __name__=="__main__" :
    #mic_list = sr.Microphone.list_microphone_names()
    wishme()
    while True:

        query = takeCommand().lower()


        if 'alexa' in query:
            if 'open youtube' in query:
                webbrowser.open("youtube.com")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ravat nitin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'E:\\songs\\nitin best songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        else:
            speak("sorry i dont know that one!")






    
