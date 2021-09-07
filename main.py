import datetime
import random
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import  smtplib
import pyjokes
import  wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('Your email here', 'Your password')
    server.sendmail('mukulsingla1234@gmail.com', to, content)
    server.close()


def wishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour>=5 and hour <12:
        speak("Good morning!")
    elif hour>=12 and hour<16:
        speak("Good afternoon")
    else:
        speak("Good evening!")
    speak("Hello Mukul. My name is Tinku. How may i help you? ")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said {query} \n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2);
            print(results)
            speak("According to Wikipedia, " + results)

        elif'who are you' in  query:
            speak("I am Jarvis. I can play songs,open youtube videos,tell time, send emails and do many more things for you sir.")

        elif 'hi' in query or 'hello' in query:
            speak("Hello!")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)


        elif 'email to mukul' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = "mukulsingla1234@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent|")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email at moment")

        elif 'spotify' in query:
            codePath = "C:\\Users\\MUKUL\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\MUKUL\\OneDrive\\Desktop\\MP3'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'quit' in query:
            exit()

        else:
            app_id = "Your wolframalpha app id"
            client = wolframalpha.Client(app_id)
            res = client.query(query)

            try:
                ans = next(res.results).text
                print(ans)
                speak(ans)
            except Exception as e:
                print("Sorry, I am unable to find results for you. Try to say that again please...")
