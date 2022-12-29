import speech_recognition
import pyttsx3
import webbrowser
import time

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
print("Chào mừng bạn đến chương trình mở web bằng giọng nói.")
print("Hiện tại chưa có bản tiếng Việt ad sẽ sớm bổ xung sớm nhất có thể.")
print("Đây chỉ là bản thử nghiệm nên chỉ hỗ trợ mở các web nổi tiếng như Youtube, Facebook, Gmail,...")
print("Để mở web hãy nói tên web khi ô cửa sổ xuất hiện dòng chữ I'm Listening.")
print("*Note: muốn mở Gmail thì nói Mail nhé!")
print("")
input("Bấm Enter để tiếp tục.")
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print("3")
time.sleep(1)

Not_Supported = ['Discord', 'Instagram', 'Messenger', 'Pinterest', 'Tik-Tok', 'Zalo']
the_end = ['thanks', 'thank you', 'bye']

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
    elif "YouTube" in you:
        robot_brain = webbrowser.open('https://www.youtube.com/')
        robot_brain = "Your YouTube is open"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "Facebook" in you:
        robot_brain = webbrowser.open('https://www.facebook.com/')
        robot_brain = "Your Facebook is open"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "Mail" in you:
        robot_brain = webbrowser.open('https://mail.google.com')
        robot_brain = "Your Gmail is open"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif you in Not_Supported:
        robot_brain = "This web is not supported!"
    elif you in the_end:
        robot_brain = "Goodbye, see you later!"
        print("Robot: " + str(robot_brain))
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I don't understand what you're saying"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()