'''
JSON: Módulo utilizado para lidar com a serialização e desserialização de objetos JSON 
(JavaScript Object Notation). Ele fornece funções como loads para carregar ficheiros JSON 
com informações do jogo e dump para salvar as informações do Python em JSON num ficheiro.
'''
from json import loads
from random import randint

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


def artes():
    '''Docytype'''
    moeda = randint(0, 10)
    moedas = moeda * 20
