#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reconhecimento_voz.py
#  
#  Copyright 2018 Aroldo <AroldoAROLDO-NOT>

import speech_recognition as sr
import sys
import pyttsx3
from datetime import date

engine = pyttsx3.init()
engine.setProperty('voice',b'brazil')

#Fala em voz alta o parametro do tipo string 
def Voz_alta(frase):
	engine.say(frase)
	engine.runAndWait()

def diaExtenso(dia):
	dia = int(dia)
	pos = 0

	dias = ["primeiro","dois","três","quatro","cinco","seis","sete","oito", "nove","dez",
	"onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
	"vinte","vinte e um","vinte e dois","vinte e três","vinte e quatro","vinte e cinco","vinte e seis",
	"vinte e sete","vinte e oito","vinte e nove","trinta","trinta e um"]

	if dia < 10:
		pos = dia[1]
		extenso = dias[pos-1]

	else:
		pos = dia
		extenso = dias[pos-1]

	return extenso

def getData():
	hj = date.today()
	diaAtual = hj.day
	mesAtual = hj.month
	anoAtual = hj.year

	dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
	meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']


	diaSemana = dias[hj.weekday()]
	mes = meses[int(mesAtual)-1]
	dia = diaExtenso(diaAtual)

	dataExtenso = ("Hoje é",diaSemana,"dia",dia,"de",mes)

	return dataExtenso

#def horaExtenso(hora):
#def getHora():


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
