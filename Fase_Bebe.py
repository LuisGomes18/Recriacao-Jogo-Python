from json import load
from Extras import Sexo
from Extras import Pontuacao
from json import dump
from time import sleep

DEBUG = 1
try:
    with open("Dados.json", encoding='utf-8') as dt:
        dados = load(dt)
        print('Dados Carregados')  #! tmp
except FileNotFoundError:
    exit('Ficheiro não encontrado ou corrompido')
felicidade = dados["felicidade_inicial"]

def Fase_Bebe():
    global felicidade
    Sexo()
    opcao_1 = str(input('\nQuer ir com os pais? (s/n)\n'))
    if opcao_1.lower() == "y":
        print('Voce foi com seu pais')
        felicidade = felicidade + 2
        dados["felicidade"] = felicidade
        with open("Dados.json", "w") as dt:
            dump(dados, dt)
        Pontuacao()
    elif opcao_1.lower() == "n":
        print('Voce não foi com seu pais')
        Pontuacao()
    else:
        print('Opção invalida')
    sleep(2)

if DEBUG == 1:
    Fase_Bebe()
elif DEBUG == 0:
    print(' ')
