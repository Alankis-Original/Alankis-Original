import pyttsx3
engine = pyttsx3.init()
while True:
    say = input("What do want AI to say?: ")
    engine.setProperty('rate', 125)
    engine.say(say)
    engine.runAndWait()