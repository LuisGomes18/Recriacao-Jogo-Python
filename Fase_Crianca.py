#!/usr/bin/python
# -*- coding: utf-8 -*-
from Extras import *
from random import randint
from time import sleep
from json import load
from sys import exit as ext
import os

try:
    with open("Dados.json", encoding='utf-8') as dados_jg:
        dados = load(dados_jg)
except FileNotFoundError:
    print('Erro: Arquivo Dados.json não encontrado')
    ext()

def Fase_Crianca():
    lampadas = randint(1, 9)
    pintar = randint(1, 3)
    bebes = randint(1, 3)
    if lampadas == 9:
        print('\033[32m' + f'Lampadas: {lampadas}' + '\033[0m')
    elif pintar == 3:
        print('\033[32m' + f'Pintar: {pintar}' + '\033[0m')
    elif bebes == 3:
        print('\033[32m' + f'Bebes: {bebes}' + '\033[0m')
    
    if lampadas in [1, 2, 3, 4, 5, 6, 7, 8]:
        print(f'Lampadas: {lampadas}')
    if pintar in [1, 2]:
        print(f'Pintar: {pintar}')
    if bebes in [1, 2]:
        print(f'Bebes: {bebes}')

    
    media = (lampadas + pintar + bebes) // 3
    dados["dados"][0]["Felicidade"] = dados["dados"][0]["Felicidade"] + media
    Pontuacao()

Fase_Crianca()