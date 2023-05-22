# -*- coding: utf-8 -*-
from Erros import Json_Inicio
from json import load
from json import dump


Json_Inicio()
dados_js = Json_Inicio()
dados = dados_js

amarelo = '\033[33m'
cor_original = '\033[0;0m'
negrito = '\033[1m'
vida = 0
felicidade = 0


def Salvar_Dados():
    global dt
    global dados
    with open("Dados.json", "w") as dt:
        dump(dados, dt)


def Sexo():
    global sexo
    sexo = str(input('''Insira o sexo da personagem (F - Feminino, M - Masculino, NB - Não Binario)
-> '''))
    sexo = sexo.lower()
    dados["sexo"] = sexo
    return sexo


def Pontuacao():
    dados_js = Json_Inicio()
    dados = dados_js
    print(f'\n\n{amarelo}{negrito}Pntuação:{cor_original} Vida: {dados["vida"]}\n Felicidade: {dados["felicidade"]}\n\n')
