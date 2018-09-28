import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice',b'brazil')
engine.say('Junin vai se fuder')
engine.runAndWait()