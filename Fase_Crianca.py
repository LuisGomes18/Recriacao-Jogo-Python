#!/usr/bin/python
# -*- coding: utf-8 -*-
from Extras import *
from random import randint
from time import sleep
from json import load
from sys import exit as ext

try:
    with open("Dados.json", encoding='utf-8') as dados_jg:
        dados = load(dados_jg)
except FileNotFoundError:
    print("Erro: Arquivo Dados.json não encontrado.")
    ext()