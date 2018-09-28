import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice',b'brazil')
engine.say('Joao vai se fuder')
engine.runAndWait()