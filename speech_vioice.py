import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate',150)
engine.setProperty('volume',0.9)

text = "hey how are yash , i love you yash so much"

engine.say(text)

engine.runAndWait()
