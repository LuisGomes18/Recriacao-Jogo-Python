'''
JSON: Módulo utilizado para lidar com a serialização e desserialização de objetos JSON 
(JavaScript Object Notation). Ele fornece funções como loads para carregar ficheiros JSON 
com informações do jogo e dump para salvar as informações do Python em JSON num ficheiro.
'''
from json import loads, dump
from random import randint
import sys

AMARELO = '\033[33m'
ORIGINAL = '\033[0;0m'

with open("Data/Dados.json", 'r', encoding='utf-8') as dados: # type: ignore
    conteudo_json = dados.read()
    dados_player = loads(conteudo_json)

vida = dados_player["vida"]
felicidade_atual = dados_player["felicidade"]

def pontuacao(felicidade_atual, vida, dinheiro):# pylint: disable=redefined-outer-name
    '''
    Mostra a pontuação atual do jogador.

    Parâmetros:
    felicidade_atual (int): A quantidade atual de felicidade do jogador.
    vida (int): A quantidade atual de vida do jogador.

    Esta função imprime a pontuação atual do jogador, incluindo a felicidade e a vida.
    Utiliza cores para destacar as informações na saída.
    '''
    print(f'\n{AMARELO}Felicidade: {felicidade_atual}')
    print(f'Vida: {vida}')
    print(f'Dinheiro: {dinheiro} {ORIGINAL}\n')


def artes(dados_player, felicidade_atual): # pylint: disable=redefined-outer-name
    """
    Realiza uma série de interações relacionadas a 
    eventos artísticos e atualiza as informações do jogador.

    Parâmetros:
    - dados_player (dict): Um dicionário contendo os dados do jogador.
    - felicidade_atual (int): O nível atual de felicidade do jogador.

    Retorna:
    Nenhum valor de retorno explícito, mas atualiza os dados do jogador e sua felicidade.

    Eventos realizados:
    - Geração de dinheiro com base em uma moeda aleatória.
    - Opção de ajudar ou não uma colega em sua peça de arte, com impacto na felicidade.
    - Atualização da felicidade do jogador com base nas escolhas feitas.
    - Geração aleatória de valores para comida, fumo e atividade de ginásio.
    - Opção de fazer uma apresentação de peça de arte, com impacto na felicidade.
    - Atualização final da felicidade do jogador com base nas escolhas e atividades.
    """

    moeda = randint(10, 80)
    dinheiro = moeda * 20
    dados_player['dinheiro'] = dinheiro

    with open("Data/Dados.json", 'w', encoding='utf-8') as dados: # pylint: disable=redefined-outer-name
        dump(dados_player, dados, ensure_ascii=False, indent=4)

    ajuda_1 = str(input('Quer ajudar sua colega na peça de arte dela: (S/N)\n-> ')) # type: ignore
    chance_ajuda_1 = randint(0, 100)
    if ajuda_1.lower() == "s" and chance_ajuda_1 > 50:
        print('Ela aceitou sua ajuda')
        felicidade_atual += 2
    elif ajuda_1.lower() == "n" and chance_ajuda_1 < 50:
        print('Ela não quis sua ajuda')
        felicidade_atual -= 2
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    comida = randint(0, 6)
    fumar = randint(0 , 4)
    ginasio = randint(0, 4)
    dados_player['comida_adulto'] = comida
    dados_player['fumar_adulto'] = fumar
    dados_player['ginasio_adulto'] = ginasio

    print(f'''\nComida: {comida}
Fumar: {fumar}
Ginásio: {ginasio}\n
''')

    ajuda_2 = str(input('Fazer apresentação de peça de arte(S/N)\n-> '))
    chance_apresentacao = randint(0, 100)
    if ajuda_2.lower() == "s" and chance_apresentacao < 30:
        print('Voçe foi na apresentação e correu bem')
        felicidade_atual += 3
    elif ajuda_2.lower() == "s" and chance_apresentacao > 30:
        print('Voce foi na apresentação e correu mal')
        felicidade_atual -= 2
    elif ajuda_2.lower() == "n":
        print('Voce não foi a apresentação')
        felicidade_atual -= 3
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    felicidade_atual += int(comida / 3)
    felicidade_atual -= int(fumar / 3)
    dinheiro -= int(fumar / 2)
    felicidade_atual += int(ginasio / 3)


def medicina(dados_player, felicidade_atual): # pylint: disable=redefined-outer-name
    """
    Realiza uma série de interações relacionadas a
    eventos médicos e atualiza as informações do jogador.

    Parâmetros:
    - dados_player (dict): Um dicionário contendo os dados do jogador.
    - felicidade_atual (int): O nível atual de felicidade do jogador.

    Retorna:
    Nenhum valor de retorno explícito, mas atualiza os dados do jogador e sua felicidade.

    Eventos realizados:
    - Geração de dinheiro com base em uma moeda aleatória.
    - Opção de ajudar ou não um colega a fazer um curativo, com impacto na felicidade.
    - Atualização da felicidade do jogador com base nas escolhas feitas.
    - Geração aleatória de valores para comida, fumo e atividade de ginásio.
    - Opção de fazer uma operação médica, com impacto na felicidade.
    - Atualização final da felicidade do jogador com base nas escolhas e atividades.
    """

    moeda = randint(10, 80)
    dinheiro = moeda * 20
    dados_player['dinheiro'] = dinheiro

    with open("Data/Dados.json", 'w', encoding='utf-8') as dados: # pylint: disable=redefined-outer-name
        dump(dados_player, dados, ensure_ascii=False, indent=4)

    ajuda_1 = str(input('Quer ajudar seu colega a fazer um curativo: (S/N)->\n '))
    chance_ajuda_1 = randint(0, 100)
    if ajuda_1.lower() == "s" and chance_ajuda_1 > 50:
        print('Ela aceitou sua ajuda')
        felicidade_atual += 2
    elif ajuda_1.lower() == "n" and chance_ajuda_1 < 50:
        print('Ela não quis sua ajuda')
        felicidade_atual -= 2
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    comida = randint(0, 6)
    fumar = randint(0 , 4)
    ginasio = randint(0, 4)
    dados_player['comida_adulto'] = comida
    dados_player['fumar_adulto'] = fumar
    dados_player['ginasio_adulto'] = ginasio

    print(f'''\nComida: {comida}
Fumar: {fumar}
Ginásio: {ginasio}\n
''')

    ajuda_2 = str(input('Quer fazer uma operação: (S/N)\n-> '))
    chance_operacao = randint(0, 100)
    if ajuda_2.lower() == "s" and chance_operacao < 30:
        print('Voçe vez a operação e correu bem')
        felicidade_atual += 3
    elif ajuda_2.lower() == "s" and chance_operacao > 30:
        print('Voce vez a operação e correu mal')
        felicidade_atual -= 2
    elif ajuda_2.lower() == "n":
        print('Voce vez a operação')
        felicidade_atual -= 3
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    felicidade_atual += int(comida / 3)
    felicidade_atual -= int(fumar / 3)
    dinheiro -= int(fumar / 2)
    felicidade_atual += int(ginasio / 3)


def musica(dados_player, felicidade_atual): # pylint: disable=redefined-outer-name
    """
    Realiza uma série de interações relacionadas a
    eventos musicais e atualiza as informações do jogador.

    Parâmetros:
    - dados_player (dict): Um dicionário contendo os dados do jogador.
    - felicidade_atual (int): O nível atual de felicidade do jogador.

    Retorna:
    Nenhum valor de retorno explícito, mas atualiza os dados do jogador e sua felicidade.

    Eventos realizados:
    - Geração de dinheiro com base em uma moeda aleatória.
    - Opção de ajudar ou não um colega a afinar a guitarra, com impacto na felicidade.
    - Atualização da felicidade do jogador com base nas escolhas feitas.
    - Geração aleatória de valores para comida, fumo e atividade de ginásio.
    - Opção de ajudar um colega a decorar a letra de uma música, com impacto na felicidade.
    - Atualização final da felicidade do jogador com base nas escolhas e atividades.
    """

    moeda = randint(10, 80)
    dinheiro = moeda * 20
    dados_player['dinheiro'] = dinheiro

    with open("Data/Dados.json", 'w', encoding='utf-8') as dados: # pylint: disable=redefined-outer-name
        dump(dados_player, dados, ensure_ascii=False, indent=4)

    ajuda_1 = str(input('Quer ajudar seu colega a afinar a guitarra: (S/N)->\n '))
    chance_ajuda_1 = randint(0, 100)
    if ajuda_1.lower() == "s" and chance_ajuda_1 > 50:
        print('Ela aceitou sua ajuda')
        felicidade_atual += 2
    elif ajuda_1.lower() == "n" and chance_ajuda_1 < 50:
        print('Ela não quis sua ajuda')
        felicidade_atual -= 2
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    comida = randint(0, 6)
    fumar = randint(0 , 4)
    ginasio = randint(0, 4)
    dados_player['comida_adulto'] = comida
    dados_player['fumar_adulto'] = fumar
    dados_player['ginasio_adulto'] = ginasio

    print(f'''\nComida: {comida}
Fumar: {fumar}
Ginásio: {ginasio}\n
''')

    ajuda_2 = str(input('Sua colega pediu sua ajuda para decorar a letra da musica \n-> '))
    chance_operacao = randint(0, 100)
    if ajuda_2.lower() == "s" and chance_operacao < 30:
        print('Voçe ajudou e ela decorou a musica')
        felicidade_atual += 3
    elif ajuda_2.lower() == "s" and chance_operacao > 30:
        print('Voçe ajudou ela mas ela nao decorou muito bem os acordes')
        felicidade_atual -= 2
    elif ajuda_2.lower() == "n":
        print('Voce quis ajudar')
        felicidade_atual -= 3
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    felicidade_atual += int(comida / 3)
    felicidade_atual -= int(fumar / 3)
    dinheiro -= int(fumar / 2)
    felicidade_atual += int(ginasio / 3)


def desporto(dados_player, felicidade_atual): # pylint: disable=redefined-outer-name
    """
    Realiza uma série de interações relacionadas a 
    eventos desportivos e atualiza as informações do jogador.

    Parâmetros:
    - dados_player (dict): Um dicionário contendo os dados do jogador.
    - felicidade_atual (int): O nível atual de felicidade do jogador.

    Retorna:
    Nenhum valor de retorno explícito, mas atualiza os dados do jogador e sua felicidade.

    Eventos realizados:
    - Geração de dinheiro com base em uma moeda aleatória.
    - Opção de ajudar ou não uma colega a fazer o aquecimento, com impacto na felicidade.
    - Atualização da felicidade do jogador com base nas escolhas feitas.
    - Geração aleatória de valores para comida, fumo e atividade de ginásio.
    - Opção de ajudar um colega a aprender um novo desporto, com impacto na felicidade.
    - Atualização final da felicidade do jogador com base nas escolhas e atividades.
    """

    moeda = randint(10, 80)
    dinheiro = moeda * 20
    dados_player['dinheiro'] = dinheiro

    with open("Data/Dados.json", 'w', encoding='utf-8') as dados: # pylint: disable=redefined-outer-name
        dump(dados_player, dados, ensure_ascii=False, indent=4)

    ajuda_1 = str(input('Sua colega quer ajuda a fazer o aquecimento: (S/N)\n-> ')) # type: ignore
    chance_ajuda_1 = randint(0, 100)
    if ajuda_1.lower() == "s" and chance_ajuda_1 > 50:
        print('Ela aceitou sua ajuda')
        felicidade_atual += 2
    elif ajuda_1.lower() == "n" and chance_ajuda_1 < 50:
        print('Ela não quis sua ajuda')
        felicidade_atual -= 2
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    comida = randint(0, 6)
    fumar = randint(0 , 4)
    ginasio = randint(0, 4)
    dados_player['comida_adulto'] = comida
    dados_player['fumar_adulto'] = fumar
    dados_player['ginasio_adulto'] = ginasio

    print(f'''\nComida: {comida}
Fumar: {fumar}
Ginásio: {ginasio}\n
''')

    ajuda_2 = str(input('Um colega pediu-te ajuda para aprender um novo desporto(S/N)\n-> '))
    chance_apresentacao = randint(0, 100)
    if ajuda_2.lower() == "s" and chance_apresentacao < 30:
        print('Voce aaceitou e seu colega aprendeu')
        felicidade_atual += 3
    elif ajuda_2.lower() == "s" and chance_apresentacao > 30:
        print('Voce aceitou mas seu colega não aprendeu muito bem')
        felicidade_atual -= 2
    elif ajuda_2.lower() == "n":
        print('Voce não ajudou seu colega')
        felicidade_atual -= 3
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    felicidade_atual += int(comida / 3)
    felicidade_atual -= int(fumar / 3)
    dinheiro -= int(fumar / 2)
    felicidade_atual += int(ginasio / 3)


def escritorio(dados_player, felicidade_atual): # pylint: disable=redefined-outer-name
    """
    Realiza uma série de interações relacionadas a 
    eventos desportivos e atualiza as informações do jogador.

    Parâmetros:
    - dados_player (dict): Um dicionário contendo os dados do jogador.
    - felicidade_atual (int): O nível atual de felicidade do jogador.

    Retorna:
    Nenhum valor de retorno explícito, mas atualiza os dados do jogador e sua felicidade.

    Eventos realizados:
    - Geração de dinheiro com base em uma moeda aleatória.
    - Opção de ajudar ou não uma colega a fazer o aquecimento, com impacto na felicidade.
    - Atualização da felicidade do jogador com base nas escolhas feitas.
    - Geração aleatória de valores para comida, fumo e atividade de ginásio.
    - Opção de ajudar um colega a aprender um novo desporto, com impacto na felicidade.
    - Atualização final da felicidade do jogador com base nas escolhas e atividades.
    """

    moeda = randint(10, 80)
    dinheiro = moeda * 20
    dados_player['dinheiro'] = dinheiro

    with open("Data/Dados.json", 'w', encoding='utf-8') as dados: # pylint: disable=redefined-outer-name
        dump(dados_player, dados, ensure_ascii=False, indent=4)

    ajuda_1 = str(input('Sua colega quer ajuda arrumar papeis: (S/N)\n-> ')) # type: ignore
    chance_ajuda_1 = randint(0, 100)
    if ajuda_1.lower() == "s" and chance_ajuda_1 > 50:
        print('Ela aceitou sua ajuda')
        felicidade_atual += 2
    elif ajuda_1.lower() == "n" and chance_ajuda_1 < 50:
        print('Ela não quis sua ajuda')
        felicidade_atual -= 2
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    comida = randint(0, 6)
    fumar = randint(0 , 4)
    ginasio = randint(0, 4)
    dados_player['comida_adulto'] = comida
    dados_player['fumar_adulto'] = fumar
    dados_player['ginasio_adulto'] = ginasio

    print(f'''\nComida: {comida}
Fumar: {fumar}
Ginásio: {ginasio}\n
''')

    ajuda_2 = str(input('Vai haver uma reunião pretende ir(S/N)\n-> '))
    chance_apresentacao = randint(0, 100)
    if ajuda_2.lower() == "s" and chance_apresentacao < 30:
        print('Voce foi a reunião correu bem')
        felicidade_atual += 3
    elif ajuda_2.lower() == "s" and chance_apresentacao > 30:
        print('Voce foi a reunião e correu mal')
        felicidade_atual -= 2
    elif ajuda_2.lower() == "n":
        print('Voce não foi a reunião')
        felicidade_atual -= 3
    else:
        print('Valor invalido')
        sys.exit(1)

    dados_player['felicidade'] = felicidade_atual

    with open("Data/Dados.json", 'w', encoding='utf-8') as arquivo_json: # type: ignore
        dump(dados_player, arquivo_json, ensure_ascii=False, indent=4)
    pontuacao(felicidade_atual, vida, dinheiro)

    felicidade_atual += int(comida / 3)
    felicidade_atual -= int(fumar / 3)
    dinheiro -= int(fumar / 2)
    felicidade_atual += int(ginasio / 3)
