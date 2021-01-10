import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib, ssl

#from time import ctime

from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

p = 'E:\\MOVIES\\SRK MOVIES & SHOWS\\FAN.mp4'

def speak(audio):
    print(audio)
    engine.say(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    engine.runAndWait()

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You : " +data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def start():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Pragyansh Nigam")
    
    elif hour>=12 and hour<=15:
        speak("Good Afternoon Pragyansh Nigam")

    elif hour>=16 and hour<23:
        speak("Good Evening Pragyansh Nigam")
    
    else:
        speak("Good Night Pragyansh Nigam")

    speak("I am your new friend, what can I do for you?")

def sendEmail(receiver_email, message):
	port = 465
	smtp_server = "smtp.gmail.com"
	sender_email = "en17cs301180@medicaps.ac.in"
	password = input("Type your password and press enter : ") 
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

if __name__ == "__main__":
    start()
    while True:
        data = recordAudio().lower()

        if 'open gmail' in data:
            speak("opening gmail")
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open('gmail.com')

        elif 'open youtube' in data:
            speak("opening youtube")
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new("youtube.com")

        elif 'open google' in data:
            speak("opening google ")
            chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab("google.com")

        elif 'play music' in data:
            speak("playing music")
            music_dir = 'E:\\django\\mymusic\\assets\\audio'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what time is it' in data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is "+strTime)

        elif 'good job' in data:
            speak("Thank you, what else can I do for you?")

        elif 'who are you' in data:
        	speak("I am Just A Rather Very Intelligent System")

        elif 'how are you' in data:
            speak("I am fine, what about you?")

        elif "what is your name" in data:
            speak("My name is jarvis")

        elif "who is your favourite actor" in data:
        	speak("Shah Rukh Khan is my all time favourite actor.")

        elif 'send an email' in data:
            try:
            	receiver_email = "nigampragyansh@gmail.com"
            	message = "Hi there! This email is sent to you using python."
            	sendEmail(receiver_email, message)
            	speak("email has been sent!")  
            except Exception as e:
                print(e)
                speak("email NOT sent!")

        elif 'open teamviewer' in data:
            speak("opening team viewer")
            path = 'C:\\Program Files\\TeamViewer\\TeamViewer.exe'
            os.startfile(path)

        elif 'open github' in data:
            speak("opening Github")
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab("github.com")
            
        elif 'open projects' in data:
            speak("opening projects")
            path = 'E:\\django'
            os.startfile(path)
        
        elif 'watch movie' in data:
            speak("Now watching fan!")
            path = p
            os.startfile(path)

        elif 'open game' in data:
        	speak("opening game")
        	path = 'E:\\GAMES\\MAX PAYNE 2 THE FALL OF MAX PAYNE\\Max Payne 2\\MaxPayne2.exe'
        	os.startfile(path)

        elif 'open git' in data:
        	speak('opening git')
        	path = 'C:\\Program Files\\Git\\git-cmd.exe'
        	os.startfile(path)

        elif 'open sublime text' in data:
        	speak('opening sublime text')
        	path = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
        	os.startfile(path)
        
        elif 'exit' in data:
            break
       