import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(command):
    engine.say(command)
    engine.runAndWait()

def takecom():
    command = ''
    try:
       with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)  #api
        command = command.lower()
        if 'whats' in command:
            print(command)
    except:
     pass
     return command

def run():
    comman = takecom()
    if 'play' in comman:
        song = comman.replace('play', '')
        talk('playing'+song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in comman:
         time = datetime.datetime.now().strftime('%H:%M %p')
         talk('Current time is'+time)
    elif 'tell about' in comman:
         person = comman.replace('tell about','')
         info = wikipedia.summary(person,1)
         print(info)
         talk(info)
    elif 'date' in comman:
        talk('Sorry,') 
    elif 'are u single' in comman:
        talk('i am in relationship with wifi')
    elif 'joke' in comman:
        talk('everyday is not sunday')
    else:
        talk('please say the command again.')                       
while True:
  run()           