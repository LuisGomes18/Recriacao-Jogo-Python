'''
Modulo para manusiar ficheiros json
'''
from json import loads
from json import dump


DEBUG = 0

def fase_adolecente(vida, felicidade_atual):
    ''' Definicao da fase de adolecente '''
    print('aaa')

    return vida, felicidade_atual

if DEBUG == 1:
    with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
        conteudo_json = dados.read()
        dados_player = loads(conteudo_json)
    felicidade_atual = dados_player['felicidade']
    vida = dados_player['vida']
    vida, felicidade_atual = fase_adolecente(vida, felicidade_atual)
elif DEBUG == 0:
    pass
else:
    print('Valor Incorreto')
