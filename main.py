import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui

engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak('the current date is')
    speak(day)
    speak(month)
    speak(year)
def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good morning sir!")
    elif hour>=12 and hour <18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("good evening")
    else:
        speak("good night")
    speak("Ultron at your service Please tell me how can i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio =r.listen(source)
    try:
        print("Recognizning..")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com','xyz')
    server.sendmail('xyz@gmail.com',to,content)
    server.close()
    
def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/abhis/JARVIS/ss.png')
    
    
    
if __name__=="__main__":
    wishme()
    while True:
        query =takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'search' in query:
            speak('Searching...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("To whom should I send the email?")
                to = takeCommand()
                speak('what should i say?')
                content =takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email!")
        elif 'web search' in query:
            speak("what should i search?")
            chromepath = "C:/Users/abhis/AppData/Local/Programs/Opera GX\launcher.exe"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
        elif 'play songs' in query:
            songs_dir=''
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'remember that' in query:
            speak('what should i remember')
            data=takeCommand()
            speak("You said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak('you said me to remember'+remember.read())
        
        elif 'offline'in query:
            quit()
            
            
    
  