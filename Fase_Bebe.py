from json import load
from Extras import Salvar_Dados
from Extras import Sexo
from Extras import Pontuacao
from time import sleep
from random import randint
from json import dump


DEBUG = 1
try:
    with open("Dados.json", encoding='utf-8') as dt:
        dados = load(dt)
except FileNotFoundError:
    exit('Ficheiro não encontrado ou corrompido')  # ! Usar Anti-cheat para não poder existir este erro
felicidade = dados["felicidade_inicial"]


def Fase_Bebe():
    global felicidade
    Sexo()
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
