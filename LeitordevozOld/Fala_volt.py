#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reconhecimento_voz.py
#  
#  Copyright 2018 Aroldo <AroldoAROLDO-NOT>

import speech_recognition as sr
import sys
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('voice',b'brazil')

def Voz_alta(frase):
	engine.say(frase)
	engine.runAndWait()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
