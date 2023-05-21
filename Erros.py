# -*- coding: utf-8 -*-

from json import load
from json import dump
import os

nome_arquivo = "Dados.json"
dados_json = {
    "vida": 12,
    "felicidade": 6,
    "vida_inicial": 12,
    "felicidade_inicial": 6,  # Anti-Cheat
    "sexo": "ND",
    "biberoes_apanhados": 0
}


def Json_Inicio():
    global dados
    dados = dados_json

    if os.path.exists(nome_arquivo):
        with open('Dados.json', 'r') as file:
            dados = load(file)
    else:
        with open('Dados.json', 'w') as file:
            dump(dados_json, file)
    return dados
