import speech_recognition
import pyttsx3
from gtts import gTTS
import os

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi đang nghe bạn nói")
        audio =robot_ear.record(mic, duration=3)
        
    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio,language='vi-VN')
    except:
        you = ""
    print("You: " + you)
            
    if  you == "":
        robot_brain = "Tôi không nghe bạn nói gì cả, hãy thử lại"
    elif "Xin chào" in you:
        robot_brain = "Chào Lê Long"
    elif "Tạm biệt" in you:
        robot_brain = "Tạm biệt bạn, hẹn gặp lại"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Tôi không hiểu bạn đang nói gì!"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    tts = gTTS(robot_brain,lang='vi')
    tts.save("pcvoice.mp3")
