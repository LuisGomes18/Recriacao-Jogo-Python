'''
Random: Para gerar numeros pseudoaleatorios
Extras: Para carregar diferentes parte do codigo
'''
#! pylint: disable=redefined-outer-name
from random import randint

from extras import carregar_dados
from extras import guardar_dados
from extras import pontuacao


DEBUG = 1
dados = carregar_dados()

def fase_crianca(dados):
    '''
    Fase Criança 
    '''
    felicidade = dados['felicidade']

    lampada = randint(1, 9)
    pintura = randint(1, 3)
    bebes = randint(1 , 3)
    felicidade_media = (lampada + pintura + bebes) // 3 #* TMP
    felicidade += felicidade_media

    dados['felicidade'] = felicidade
    dados['lampada'] = lampada
    dados['pintura'] = pintura
    dados['bebes'] = bebes

    match lampada:
        case 9:
            print('\033[32m' + f'\n\nLampadas: {lampada}' + '\033[0m')
        case _:
            print(f'\n\nLampadas: {lampada}')
    match pintura:
        case 3:
            print('\033[32m' + f'Pintura: {pintura}' + '\033[0m')
        case _:
            print(f'Pintura: {pintura}')
    match bebes:
        case 3:
            print('\033[32m' + f'Bebes: {bebes}' + '\033[0m')
        case _:
            print(f'Bebes: {bebes}')

    guardar_dados(dados)
    pontuacao(dados)
    print('\n')

    dados['fase_crianca_terminada'] = True

    guardar_dados(dados)


match DEBUG:
    case 1:
        fase_crianca(dados)
    case 0:
        pass
    case _:
        print('Valor Invalido')
        exit(1)
