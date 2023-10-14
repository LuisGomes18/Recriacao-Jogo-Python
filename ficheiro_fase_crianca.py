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

    if lampada == 9:
        print('\033[32m' + f'\n\nLampadas: {lampada}' + '\033[0m')
    else:
        print(f'\n\nLampadas: {lampada}')
    if pintura == 3:
        print('\033[32m' + f'Pintura: {pintura}' + '\033[0m')
    else:
        print(f'Pintura: {pintura}')
    if bebes == 3:
        print('\033[32m' + f'Bebes: {bebes}' + '\033[0m')
    else:
        print(f'Bebes: {bebes}')

    guardar_dados(dados)
    pontuacao(dados)
    print('\n')

    dados['fase_crianca_terminada'] = True

    guardar_dados(dados)


if DEBUG == 1:
    fase_crianca(dados)
elif DEBUG == 0:
    pass
else:
    print('VALOR INVALIDO')
