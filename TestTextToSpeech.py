import pyttsx3
engine = pyttsx3.init()

Navn = input("Hvad hedder du?")

engine.say(Navn + "you are very nice")












alder = input ("How old are you?")

engine.say ("I can see you are" + alder + "years old" )

engine.runAndWait()