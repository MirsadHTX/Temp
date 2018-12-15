import pyttsx3
import datetime

var = str(datetime.datetime.now())
#print(var)

tekstVariable = "Hello Mirsad"
engine = pyttsx3.init()
engine.say(tekstVariable)
engine.runAndWait()

engine.say("time is")
engine.runAndWait()


time = var[11:13]
min = var[14:16]
print(time)
print(min)

engine.say(time)
engine.runAndWait()

engine.say(min)
engine.runAndWait()