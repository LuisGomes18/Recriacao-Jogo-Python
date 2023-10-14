from os import system
from time import sleep
from random import randint

from extras import carregar_dados
from extras import guardar_dados
from extras import pontuacao


DEBUG = 1
dados = carregar_dados()

def fase_bebe(dados):
    '''Fase Bebe'''
    system('clear')
    felicidade = dados['felicidade']

    sexo = str(input('''\n\nInsira o sexo  da personagem:
(F - Femenino
M - Masculino)
-> '''))
    dados['sexo'] = sexo

    guardar_dados(dados)

    opcao_1 = str(input('\nQuer ir com seus pais (s/n)\n-> '))
    if opcao_1.lower() == 's' or opcao_1.lower() == 'y':
        felicidade += 2
        print('Voçe foi com seus pais')
    elif opcao_1.lower() == 'n':
        felicidade -= 2
        print('Voçe não foi com seus pais')
    else:
        print('Valor Invalido')

    dados['felicidade'] = felicidade
    guardar_dados(dados)

    pontuacao(dados)

    print('\nAgora é a parte em que o jogador deveria pegar os biberões, mas como não há interface gráfica, será feito de forma aleatória. :)\n')
    sleep(2)

    if opcao_1.lower() == "n":
        biberoes = randint(4, 9)
    elif opcao_1.lower() == "s" or opcao_1.lower() == "y":
        biberoes = randint(5, 9)

    dados['biberoes'] = biberoes
    print(f'Voce pegou {biberoes} biberoes')

    felicidade = int(biberoes // 2) #* TMP
    dados['felicidade'] = felicidade
    guardar_dados(dados)

    pontuacao(dados)

    opcao_2 = str(input('Quer ir no baloiço (s/n)\n-> '))
    if opcao_2.lower() == "s" or opcao_2.lower() == "y":
        felicidade += 1
        print('Voce foi no baloico')
    elif opcao_2.lower() == "n":
        felicidade -= 1
        print('Voçe não foi no baloiço')
    else:
        print('Valor Invalido')

    dados['felicidade'] = felicidade
    dados['fase_bebe_terminada'] = True
    guardar_dados(dados)

    pontuacao(dados)

if DEBUG == 1:
    fase_bebe(dados)
elif DEBUG == 0:
    pass
else:
    print('VALOR INVALIDO')

