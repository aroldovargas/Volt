#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reconhecimento_voz.py
#  
#  Copyright 2018 Aroldo <AroldoAROLDO-NOT>


def leArq():
	dic = {}
	lstchaves =[]
	lstconteudos = []
	conteudo = []
	chave = ""
	i = 1

	#Lendo o arquivo de texto e construindo o dicionário, a chave é o vocabulário e o conteúdo é uma lista de palavras relacionadas ao vocabulário 

	with open("Arq.txt", "r") as arq:
		linhas = arq.read().splitlines()
		chave = linhas[0][1:] 

		while i < len(linhas):
			if (linhas[i][0] == "*"):
				if (i != 0):
					dic[chave] = conteudo
					chave = linhas[i][1:]
					conteudo = []
					i = i + 1

			conteudo.append(linhas[i])
			i = i + 1

		dic[chave] = conteudo

	#Lista de todas as chaves do dic
	for c in dic:
		lstchaves.append(c)
		lstconteudos.append(dic[c])

	return dic,lstchaves,lstconteudos
	

leArq()