#!/usr/bin/python
# -*- coding: utf-8 -*-
from Extras import *
from random import randint
from time import sleep
from json import load

with open("Dados.json", encoding='utf-8') as dados_jg:
    dados = load(dados_jg)

def Fase_Bebe():
    global Felicidade
    Escolher_sexo_personagem()

    sleep(5)
    Ir_com_pais = str(input('\n\nVoçe que ir com seus pais? \n--> '))
    if Ir_com_pais.lower() == 'sim':
        print('Voçe foi com seu pais')
        dados["dados"][0]["Felicidade"] += 2
    elif Ir_com_pais.lower() not in ['nao', 'não']:
        print('Voçe não foi com seu pais')
        dados["dados"][0]["Felicidade"] += 0
    Pontuacao()

    sleep(5)
    print('Esta parte do código é feito por forma random já que não existe formato visual')
    sleep(2)
    Biberoes = randint(1, 9)
    dados["dados"][0]["Felicidade"] += int(Biberoes / 6)
    print(f'Voçe consegiu "apanhar": {Biberoes} biberões')
    Pontuacao()

    sleep(5)
    Ir_no_escorrega = str(input('Voçe quer ir no escorrega? \n--> '))
    if Ir_no_escorrega.lower() == 'sim':
        print('Voçe foi no escorrega')
        dados["dados"][0]["Felicidade"] += 2
    elif Ir_no_escorrega.lower() not in ['nao', 'não']:
        print('Voçe não foi no escorrega')
        dados["dados"][0]["Felicidade"] += 0
    Pontuacao()
    dados["dados"][0]["Final_fase_bebe"] = 1

Fase_Bebe()
