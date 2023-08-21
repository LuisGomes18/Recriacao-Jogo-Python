'''
Modulo para manusear ficheiros .json (l.5)
Modulo importar moduloda fase de bebe (l.6)
'''
from json import loads
import sys
from ficheiro_fase_bebe import fase_bebe
from ficheiro_fase_crianca import fase_crianca
from ficheiro_fase_adolecente import fase_adolecente

with open("Data/Dados.json", 'r', encoding='utf-8') as dados:
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

felicidade_atual = dados_player['felicidade']
vida = dados_player['vida']

fase_bebe(dados_player, felicidade_atual, vida) # type: ignore

if dados_player['fase_bebe_terminada'] is True:
    fase_crianca(dados_player, felicidade_atual, vida)
elif dados_player['fase_bebe_terminada'] is False:
    sys.exit('Fase Bebe não foi completada a 100%')
else:
    sys.exit('Erro ao executar a Fase Criança')

if dados_player['fase_adolecente_terminada'] is True:
    fase_adolecente(dados_player, felicidade_atual, vida)

#! ERRO 29 BAIXO
# elif dados_player['fase_adolecente_terminada'] is False:
#    sys.exit('Fase Adolecente não foi completada a 100%')
# else:
#    sys.exit('Erro ao executar a Fase Adolecente')
