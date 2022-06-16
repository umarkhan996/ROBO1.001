import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voices',voices[0].id)


def speak(audio):
    pass
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("GOOD MORNING")
    elif hour >=12 and hour <6:
        speak('Good Evening')
    else:
        speak('Good Night')

    greet = 'HI Sir, I am Jarvis. Kaam Bata Aur Chal Pahli Fursat me nikal'
    print(greet)
    speak(greet)
    


def takeCommand():
    # '''It Takes input via voice from the user'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.........')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")
    
    except Exception as e:
        print("Say that again please......")
        return 'none'
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',567)
    server.ehlo()
    server.starttls()
    server.login("ABC@gmail.com","PASSWORD")
    server.sendmail('ABC@gmail.con',to ,content)
    server.close()



if __name__== "__main__":
    wishMe()

    
    # speak("HI SHAHBAZ BAHI. HOW ARE YOU ? ")
    # speak("HI AKAML . HOW ARE YOU ? ")

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.......')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open-Youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open-Instagram' in query:
            webbrowser.open("Instagram.com")
            
        elif 'open-Facebook' in query:
            webbrowser.open("Facebook.com")

        elif 'open-Google' in query:
            webbrowser.open("Google.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%m:%S')
            speak(f' Sir, The time is{strTime}')

        elif 'Email to umarkhan' in query:
            try:
                speak('What should i say')
                content=takeCommand()
                to='mdumarkhan996@gamil.com'
                sendEmail(to,content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak("Sorry i could not sent your email")

    

  
    
