#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reconhecimento_voz.py
#  
#  Copyright 2018 Aroldo <AroldoAROLDO-NOT>

import speech_recognition as sr
import sys
import Fala_volt
import Lib_Lervoz
import pyttsx3
import TAD_dic


def main():
	while True:
		frase = Lib_Lervoz.getAudio()
		print("EU: ",frase)
		lst_frase = frase.split()
		
		#Inicio Dialogo
		if (("dia") and ("hoje")) in lst_frase:
				hj = Fala_volt.getData()
				Fala_volt.Voz_alta(hj)
		if "Volt" in lst_frase:
			dialogo()		
			break
		#Aprendizado
		else:
			if (("seu") and ("nome")) in lst_frase:
				Fala_volt.Voz_alta("Meu nome é Volt")
			else:
				Fala_volt.Voz_alta(frase)
				print(frase)
		
		frase = ""
		lst_frase = []


def dialogo():

	Fala_volt.Voz_alta("Estou a sua disposição mestre")
	
	return None
'''
	vocabulario = ""
	while True:
		frase = Lib_Lervoz.getAudio()
		frase = frase.split()

		for palavra in frase:
			dic,lstchaves,lstconteudos = TAD_dic.leArq()
			i = 0
			for chave in lstconteudos:
				for conteudo in chave:
					if palavra == conteudo:
						vocabulario = lstchaves[i]
				i = i + 1
'''
	

main()