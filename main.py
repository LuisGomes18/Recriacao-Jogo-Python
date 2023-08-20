'''
Modulo para manusear ficheiros .json (l.5)
Modulo importar moduloda fase de bebe (l.6)
'''
from json import loads
from ficheiro_fase_bebe import fase_bebe
from ficheiro_fase_crianca import fase_crianca

with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

felicidade_atual = dados_player['felicidade']
vida = dados_player['vida']

felicidade_atual = fase_bebe(felicidade_atual)

if dados_player['fase_bebe_terminada'] is True:
    fase_crianca(vida, felicidade_atual)
elif dados_player['fase_bebe_terminada'] is False:
    exit('Fase Bebe não foi completada a 100%')
else:
    exit('Erro ao executar a Fase Criança')
