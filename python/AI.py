import speech_recognition
import pyttsx3
import webbrowser
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio =robot_ear.record(mic, duration=3)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)
        
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hey Siri" in you:
        robot_brain = "I'm here"
    elif "hello" in you:
        robot_brain = "Hello Le Long"
    elif "English" in you:
        robot_brain = "Yes, I can speak English"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "your name" in you:
        robot_brain = "My name is Siri"
    elif "my name" in you:
        robot_brain = "Your name is Le Long" 
    elif "Facebook profile" in you:
        robot_brain = webbrowser.open('https://www.facebook.com/Longpogba06')
        robot_brain = "Your Facebook profile is open"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "YouTube" in you:
        robot_brain = webbrowser.open('https://www.youtube.com/')
        robot_brain = "Your YouTube is open"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "bye" in you:
        robot_brain = "Bye Le Long"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I don't understand what you're saying"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()