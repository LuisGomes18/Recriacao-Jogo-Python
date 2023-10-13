from json import loads
from json import dump

def carregar_dados():
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
    with open('Data/Dados.json', 'w', encoding='utf-8') as dados_player:
        dump(dados_player, dados, ensure_ascii=False, indent=4)

def pontuacao(dados):
    felicidade = dados['felicidade']
    vida = dados['vida']
    dinheiro = dados['dinheiro']
    print('\033[33m' + f'\nFelicidade: {felicidade}')
    print(f'Vida: {vida}')
    print(f'Dinheiro: {dinheiro}\n' + '\033[0;0m')
