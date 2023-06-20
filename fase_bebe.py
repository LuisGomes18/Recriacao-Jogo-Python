'''
Modulo para manusear ficheiros .json
'''
from json import loads
from json import dump
from time import sleep


with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

DEBUG = 1
felicidade_atual = dados_player['felicidade']
vida = dados_player['vida']

def fase_bebe():
    ''' Definição da fase de bebê '''

    opcao_sexo = str(input('''Insira o sexo da personagem
(F - Feminino, M - Masculino, NB - Não Binário)\n-> '''))
    dados_player['sexo'] = opcao_sexo

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)

    opcao_1 = str(input('Quer ir com seus pias (s/n)\n-> '))
    # pylint: disable=W0621
    if opcao_1.lower() == 's':
        felicidade_atual += 2
        with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json:
            dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
        print('Voce foi com seus pais')
    elif opcao_1.lower() == 'n':
        print('Voce nao foi com seus pais')
    else:
        print('Opção invalida')

    sleep(1)
    print('''\nAgora e parte em que o player deveria apanhar os biberoes
mas como nao tem interface grafica sera feito randomizado\n''')
    sleep(1)

    opcao_2 = str('Quer ir no baloiço\n-> ')

if DEBUG == 1:
    fase_bebe()
elif DEBUG != 0:
    print('Número introduzido incorreto')
