import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_audio import *
from jokes import *
import randfacts
from weather import *
import datetime


engine = p.init()
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("Morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("hello , good "+ wishme()  +"I am your voice assistant")
speak("today is" + today_date.strftime("%d") + "of" + today_date.strftime("%b") + "and its currently" +(today_date.strftime("%I"))+(today_date.strftime("%M"))+ (today_date.strftime("%p")))
# speak("temperature in gwalior is " + str(temp()) + "degree celcius" + "and with" + str(des()))
speak("What can I do for you")


with sr.Microphone() as source:
    r.energy_threshold = 10000
    '''by increasing the energy threshold it will catch even low voices .. default value 300'''
    r.adjust_for_ambient_noise(source, duration=1)
    '''noice cancellation'''
    print("listening")
    audio = r.listen(source)
    '''it listens to what we say and capture it in microphone and save it in variable audio'''
    text2 = r.recognize_google(audio, language='en-us')

    '''it converts the audio and sends the audio to google api engine and it converts the audio we have entered to a 
    text'''

if "How" and "are" and "you" in text2:
    speak("i am having a good day, what you want me to do")

# with sr.Microphone() as source:
#     r.energy_threshold = 10000
#     r.adjust_for_ambient_noise(source, duration=1)
#     print("listening....")
#     audio = r.listen(source)
#     text2 = r.recognize_google(audio)

elif "information" in text2:
    speak("you need information related to which topic")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))

    assist = infow()
    assist.navigate_to_wikipedia(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video ??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening....")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        speak("Playing {} on youtube".format(vid))
        print("Playing {} on youtube".format(vid))
        assist = music()
        assist.play(vid)

elif "joke" in text2:
    speak("sure sir, get ready for some chuckles")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "fact" in text2:
    print("sure sir")
    speak("sure sir")

    x = randfacts.get_fact()
    print(x)
    speak("Did you know that" + x)

elif "temperature" in text2:
    print("temperature in gwalior is " + str(temp()) + "degree celcius" + "and with" + str(des()))
    speak("temperature in gwalior is " + str(temp()) + "degree celcius" + "and with" + str(des()))

else:
    print("Sorry, I dont get it")
    speak("Sorry, I don't get it")

