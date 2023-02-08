#!/usr/bin/python
# -*- coding: utf-8 -*-
from Extras import *
from random import randint
from time import sleep
from json import load

with open("Dados.json", encoding='utf-8') as dados_jg:
    dados = load(dados_jg)