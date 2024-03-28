from random import randint
from extras import escolha_sexo
from json_defs import carregar_json
from json_defs import guardar_json

DEBUG = 0


def fase_bebe():
    """
    Definiçao que contem fase bebe e todos os suas definicoes
    """
    dados = carregar_json()
    input('\nDe enter para começar o jogo\n')
    escolha_sexo()

    opcao_1 = str(input('\n\nQuer ir com os pais? (s ou n)\n-> '))
    opcao_1.lower()
    print('\n')

    while opcao_1 not in ["s", "n"]:
        opcao_1 = str(input('\n\nQuer ir com os pais? (s ou n)\n-> '))
        opcao_1.lower()

    match opcao_1:
        case "s":
            print('Voçe foi com os pais')
            dados["FASE_BEBE"]["pais"] = True
        case "n":
            print('Voçe nao foi com seu pais')
            dados["FASE_BEBE"]["pais"] = False
        case _:
            print('Valor Invalido')
            dados["FASE_BEBE"]["pais"] = None
    print('\n')
    guardar_json(dados)

    match opcao_1:
        case "s":
            biberoes = randint(5, 9)
        case "n":
            biberoes = randint(1, 9)
    dados["FASE_BEBE"]["biberoes"] = biberoes
    guardar_json(dados)

    opcao_2 = str(input('\n\nQuer ir no baloiço? (s ou n)\n-> '))
    opcao_2.lower()
    print('\n')

    while opcao_2 not in ["s", "n"]:
        opcao_2 = str(input('\n\nQuer ir no baloiço? (s ou n)\n-> '))
        opcao_2.lower()

    match opcao_2:
        case "s":
            print('Voçe foi no baloiço')
        case "n":
            print('Voçe não foi no baloiço')
        case _:
            print('Valor Invalido')
    print('\n')


match DEBUG:
    case 0:
        fase_bebe()
    case 1:
        pass
    case _:
        print('Valor Invalido')
