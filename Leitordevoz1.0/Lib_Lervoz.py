#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reconhecimento_voz.py
#  
#  Copyright 2018 Aroldo <AroldoAROLDO-NOT>

import speech_recognition as sr
import sys
import pyttsx3
import Fala_volt

#Retorna a frase captada do microfone, caso nao consiga sintetizar as palavras, alerta que nao foi entendido.
def getAudio():
	record = sr.Recognizer()
	with sr.Microphone() as source:
		record.adjust_for_ambient_noise(source)
		frase = ""
		while sr.UnknownValueError:
		    audio = record.listen(source)
		    try:
		        frase = record.recognize_google(audio,language='pt')
		        return frase
		    except sr.UnknownValueError:
		    	Fala_volt.Voz_alta('Não entendi o que você falou!')
	return frase


















'''


	r = sr.Recognizer()
	engine = pyttsx3.init()
	engine.setProperty('voice',b'brazil')

	with sr.Microphone() as s:
		r.adjust_for_ambient_noise(s)
		palavra = ""
		while True:
			audio = r.listen(s)
			try:
				palavra = r.recognize_google(audio,language='pt')
			except sr.UnknownValueError:
				engine.say('Não entendi o que você falou!')
				engine.runAndWait()
			print(palavra)
			if palavra == "tudo bem":
				engine.say('Tudo sim e com você?')
				engine.runAndWait()
			if palavra == "Conhece o João":
				engine.say('Sim, ele é viadinho')
				engine.runAndWait()
			if palavra == "desligar":
				engine.say('Adeus, até a próxima!')
				engine.runAndWait()
				sys.exit()
			palavra = ""


r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice',b'brazil')

with sr.Microphone() as s:
	r.adjust_for_ambient_noise(s)
	palavra = ""
	while True:
		audio = r.listen(s)
		try:
			palavra = r.recognize_google(audio,language='pt')
		except sr.UnknownValueError:
			engine.say('Não entendi o que você falou!')
			engine.runAndWait()
		print(palavra)
		if palavra == "tudo bem":
			engine.say('Tudo sim e com você?')
			engine.runAndWait()
		if palavra == "desligar":
			engine.say('Adeus, até a próxima!')
			engine.runAndWait()
			sys.exit()
		palavra = ""

'''

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
