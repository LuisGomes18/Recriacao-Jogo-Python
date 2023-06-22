'''
Modulo para manusear ficheiros .json (l.6 e 7)
Modulo para fazer pausas entre codigos (l.8)
Modulo para randomizar numeros (l.9)
'''
from json import loads
from json import dump
from time import sleep
from random import randint
from extras import pontuacao


DEBUG = 0
FASE_BEBE_TERMINADA = 'false'


def fase_bebe(felicidade_atual):
    ''' Definição da fase de bebê '''

    opcao_sexo = str(input('''Insira o sexo da personagem
(F - Feminino, M - Masculino, NB - Não Binário)\n-> '''))
    dados_player['sexo'] = opcao_sexo

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    opcao_1 = str(input('\nQuer ir com seus pais (s/n)\n-> '))
    # pylint: disable=W0621
    if opcao_1.lower() == 's':
        felicidade_atual += 2
        dados_player['felicidade'] = felicidade_atual
        with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
            dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
        print('Você foi com seus pais')
    elif opcao_1.lower() == 'n':
        print('Você não foi com seus pais')
    else:
        print('Opção inválida')
    pontuacao(felicidade_atual, vida)

    sleep(1)
    print('''\nAgora é a parte em que o jogador deveria pegar os biberões,
mas como não há interface gráfica, será feito de forma aleatória.\n''')
    sleep(1)

    biberoes = 0
    if opcao_1.lower() == "n":
        biberoes = randint(4, 9)
    elif opcao_1.lower() == "s":
        biberoes = randint(5, 9)
    dados_player['biberoes_apanhados'] = biberoes
    print(f'\nVocê pegou {biberoes} biberões')
    felicidade_atual += int(biberoes / 3) #* TMP
    dados_player['felicidade'] = felicidade_atual
    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida)

    opcao_2 = str(input('\nQuer ir no baloiço (s/n)\n-> '))
    if opcao_2.lower() == "n":
        print('Você não foi no baloiço')
    elif opcao_2.lower() == "s":
        print('Você foi no baloiço')
        felicidade_atual += 1
        dados_player['felicidade'] = felicidade_atual
        with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
            dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    else:
        print('Opção inválida')
    pontuacao(felicidade_atual, vida)

    FASE_BEBE_TERMINADA = 'true'  # pylint: disable=C0103
    dados_player['fase_bebe_terminada'] = FASE_BEBE_TERMINADA
    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    return felicidade_atual


if DEBUG == 1:
    with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
        conteudo_json = dados.read()
        dados_player = loads(conteudo_json)
    felicidade_atual = dados_player['felicidade']
    vida = dados_player['vida']
    felicidade_atual = fase_bebe(felicidade_atual)
elif DEBUG == 0:
    pass
else:
    print('Valor Incorreto')
