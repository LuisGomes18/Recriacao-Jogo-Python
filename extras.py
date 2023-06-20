'''
Modulos de correção de erros
E modulos para usar ficheiros json
'''
# -*- coding: utf-8 -*-
from json import dump
from Erros import Json_Inicio

Json_Inicio()
dados_js = Json_Inicio()
dados = dados_js

AMARELO = '\033[33m'
COR_ORIGINAL = '\033[0;0m'
NEGRITO = '\033[1m'
VIDA = 0
FELICIDADE = 0

with open("Dados.json", "w", encoding='utf-8') as dados_file:
    dump(dados, dados_file)

def sexo():
    ''' Definicao para desidir o sexo da personagem '''
    opcao_sexo = str(input('''Insira o sexo da personagem
(F - Feminino, M - Masculino, NB - Não Binario)
-> '''))
    opcao_sexo = opcao_sexo.lower()
    dados["sexo"] = opcao_sexo
    return opcao_sexo


def pontuacao():
    '''Definicao que mostra ao utilizador a pontuacao'''
    pontuacao_dados_js = Json_Inicio()
    dados = pontuacao_dados_js
    print('''\n\n{AMARELO}{NEGRITO}
Pntuação:{COR_ORIGINAL} Vida: {dados["vida"]}\n Felicidade: {dados["felicidade"]}\n\n''')
