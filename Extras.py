#!/usr/bin/python
# -*- coding: utf-8 -*-
from json import load
from sys import exit as ext

try:
    with open("Dados.json", encoding='utf-8') as dados_jg:
        dados = load(dados_jg)
except FileNotFoundError as e:
    print(f'Erro: Arquivo Dados.json não encontrado')
    ext()

def Escolher_sexo_personagem():
    global Sexo_Personagem
    Sexo_Personagem = int(input('Escolha o sexo do seu personagem:\n 1 - Masculino\n 2 - Feminino\n 3- Não-Binarie\n--> '))
    dados["dados"][0]["Sexo_Personagem"] = Sexo_Personagem

def Pontuacao():
    print('\033[33m' + f'\n\nFelicidade: {dados["dados"][0]["Felicidade"]}\nVida: {dados["dados"][0]["Vida"]}\n\n' + '\033[0m')
