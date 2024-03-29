'''
Json: Para manipular os ficheiros .json
'''
from json import loads
from json import dump


def carregar_dados():
    '''
    Carrega os dados do ficheiro
    '''
    try:
        with open('Data/Dados.json', 'r', encoding='utf-8') as dados_player:
            conteudo = dados_player.read()
            dados = loads(conteudo)
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    else:
        pass
    return dados

def guardar_dados(dados):
    '''
    Guardar os dados modificados
    '''
    with open('Data/Dados.json', 'w', encoding='utf-8') as dados_player:
        dump(dados, dados_player, ensure_ascii=False, indent=4)

def pontuacao(dados):
    '''
    Mostra na tela a pontuacao
    '''
    felicidade = dados['DADOS_IMPORTANTES']['felicidade']
    vida = dados['DADOS_IMPORTANTES']['vida']
    dinheiro = dados['DADOS_IMPORTANTES']['dinheiro']
    print('\033[33m' + f'\nFelicidade: {felicidade}')
    print(f'Vida: {vida}')
    print(f'Dinheiro: {dinheiro}\n' + '\033[0;0m')
