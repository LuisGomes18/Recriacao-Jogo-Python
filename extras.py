'''
Modulo para manusear ficheiros .json (l.4)
'''
from json import loads

AMARELO = '\033[33m'
ORIGINAL = '\033[0;0m'

with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

vida = dados_player["vida"]
felicidade_atual = dados_player["felicidade"]

def pontuacao(felicidade_atual, vida):
    '''Mostra a pontuacao'''
    print(AMARELO + f'\nFelicidade: {felicidade_atual}')
    print(f'Vida: {vida}\n' + ORIGINAL)
