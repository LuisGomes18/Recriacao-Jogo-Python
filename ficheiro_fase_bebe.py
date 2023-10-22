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
    match sexo:
        case 'F' | 'f':
            print("\nIt's a girl!")
        case 'M' | 'm':
            print("\nIt's a boy!")
        case _:
            print('Valor Invalido')
            exit(1)
    dados['sexo'] = sexo

    guardar_dados(dados)

    opcao_1 = str(input('Quer ir com seus pais (s/n)\n-> '))
    match opcao_1:
        case 'S' | 's' | 'y' | 'Y':
            felicidade += 2
            print('Voçe foi com seus pais')
        case 'n' | 'N':
            felicidade -= 2
            print('Voçe nao foi com seus pais')
        case _:
            print('Valor Invalido')
            exit(1)

    dados['felicidade'] = felicidade
    guardar_dados(dados)

    pontuacao(dados)

    print('\nAgora é a parte em que o jogador deveria pegar os biberões, mas como não há interface gráfica, será feito de forma aleatória. :)\n')
    sleep(2)

    match opcao_1:
        case 'n' | 'N':
            biberoes = randint(4, 9)
        case 's' | 'S':
            biberoes = randint(5, 9)
        case _:
            print('Valor Invalido')
            exit(1)

    dados['biberoes'] = biberoes
    print(f'Voce pegou {biberoes} biberoes')

    felicidade = int(biberoes // 2) #* TMP
    dados['felicidade'] = felicidade
    guardar_dados(dados)

    pontuacao(dados)

    opcao_2 = str(input('Quer ir no baloiço (s/n)\n-> '))
    match opcao_2:
        case "s" | "S" | "y" | "Y":
            felicidade += 1
            print('Voçe foi no baloiço')
        case "n" | "N":
            felicidade -= 1
            print('Voçe não foi no baloiço')
        case _:
            print('Valor Invalido')
            exit(1)

    dados['felicidade'] = felicidade
    dados['fase_bebe_terminada'] = True
    guardar_dados(dados)

    pontuacao(dados)

match DEBUG:
    case 1:
        fase_bebe(dados)
    case 0:
        pass
    case _:
        print('Valor Invalido')
        exit(1)
