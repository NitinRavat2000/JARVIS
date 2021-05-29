import pyttsx3
from tkinter import *
import PIL.Image, PIL.ImageTk
import datetime
import wikipedia
import speech_recognition as sr
import os
import smtplib
from PIL import Image


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
    with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 2048) as source:

        #var.set("Listening...")
        #window.update()
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
                    
    try:
        #var.set("Recognizing...")
        #window.update()
        print("Recognizing...")
        query = r.recognize_google(audio)
    
    except Exception as e:
        return "None"
    #var1.set(query)
    #window.update()
    return query

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

if __name__=="__main__" :
    #mic_list = sr.Microphone.list_microphone_names()
    wishme()
    while True:

        query = takeCommand().lower()

        print(query)
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

            elif 'open window' in query:
                window = Tk()
               # global var
               # global var1

                var = StringVar()
                var1 = StringVar()
                label2 = Label(window, textvariable = var1, bg = '#FAB60C')
                label2.config(font=("Courier", 20))
                var1.set('User Said:')
                label2.pack()

                label1 = Label(window, textvariable = var, bg = '#ADD8E6')
                label1.config(font=("Courier", 20))
                var.set('Welcome')
                label1.pack()


                frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
                window.title('JARVIS')

                label = Label(window, width = 500, height = 500)
                label.pack()
                window.after(0, update, 0) 

                def update(ind):
                    ind += 1
                    label.configure(image=frame)
                    frame = frames[(ind)%100]
                    window.after(100, update, ind)

                window.mainloop()

            else:
                speak("sorry i dont know that one!")















