# -*- coding: utf-8 -*-

from Erros import Json_Inicio
from json import load
from Extras import Salvar_Dados
from Extras import Sexo
from Extras import Pontuacao
from time import sleep
from random import randint
from json import dump

# 0 - nao debug // 1 - para debug 
DEBUG = 1
Json_Inicio()
dados_js = Json_Inicio()
dados = dados_js
felicidade = dados["felicidade"]
print(felicidade)


def Fase_Bebe():
    global felicidade
    Sexo()
    sexo_atual = Sexo()
    dados["sexo"] = sexo_atual
    with open("Dados.json", "w") as dt:
        dump(dados, dt)
    opcao_1 = str(input('\nQuer ir com os pais? (S/N)\n'))
    if opcao_1.lower() == "s":
        print('Voce foi com seu pais')
        felicidade += 2  # ! TMP
        dados["felicidade"] = felicidade
        with open("Dados.json", "w") as dt:
            dump(dados, dt)
    elif opcao_1.lower() == "n":
        print('Voce não foi com seu pais')
    else:
        print('Opção invalida')
    sleep(2)
    with open("Dados.json", "w") as dt:
        dump(dados, dt)

    biberoes_apanhados = randint(0, 6)
    dados["biberoes_apanhados"] = biberoes_apanhados
    felicidade = biberoes_apanhados / 6  # ** Verificar este (6)
    with open("Dados.json", "w") as dt:
        dump(dados, dt)
    print('\n')

    opcao_2 = str(input('Quer andar de boloiço? (S/N)\n'))
    if opcao_2.lower() == "s":
        print('Voce foi com no boloiço')
        felicidade += 1  # ? 1 Mais ou menos
        with open("Dados.json", "w") as dt:
            dump(dados, dt)
    elif opcao_2.lower() == "n":
        print('Voce não foi com no baloiço')
    else:
        print('Opção invalida')

    with open("Dados.json", "w") as dt:
        dump(dados, dt)
    Pontuacao()
    sleep(2)


if DEBUG == 1:
    Fase_Bebe()
elif DEBUG == 0:
    print(' ')
else:
    print('Numero Invalido')
