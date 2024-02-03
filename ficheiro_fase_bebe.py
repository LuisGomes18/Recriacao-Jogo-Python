from time import sleep
from random import randint

from extras import carregar_dados
from extras import guardar_dados
from extras import pontuacao
from extras import apagar_terminal
from language import language_choice


DEBUG = 0
current_language = " "
dados = carregar_dados()

language = language_choice() # type: ignore
current_language = dados['lang']

def fase_bebe(dados):
    apagar_terminal()
    felicidade = dados["DADOS_IMPORTANTES"]["felicidade"]

    sexo = str(input("tfd"))
    while sexo.lower() not in ["f", "m"]:
        sexo = str(input("""\n\nInsira o sexo  da personagem:
(F - Femenino
M - Masculino)
-> """
            )
        )
    match sexo.lower():
        case "f":
            print("\nIt's a girl!")
        case "m":
            print("\nIt's a boy!")
        case _:
            print("\nValor Invalido")
            exit(1)
    dados["FASE_BEBE"]["sexo"] = sexo

    guardar_dados(dados)

    opcao_1 = str(input("\nQuer ir com seus pais (s/n)\n-> "))
    while opcao_1.lower() not in ["s", "n"]:
        opcao_1 = str(input("\nQuer ir com seus pais (s/n)\n-> "))
    match opcao_1.lower():
        case "s":
            felicidade += 2
            print("\nVoçe foi com seus pais")
        case "n":
            felicidade -= 2
            print("\nVoçe nao foi com seus pais")
        case _:
            print("\nValor Invalido")
            exit(1)

    dados["DADOS_IMPORTANTES"]["felicidade"] = felicidade
    guardar_dados(dados)

    pontuacao(dados)

    print(
        "\nAgora é a parte em que o jogador deveria pegar os biberões, mas como não há"
        "interface gráfica, será feito de forma aleatória. :)\n"
    )
    sleep(2)

    match opcao_1.lower():
        case "n":
            biberoes = randint(4, 9)
        case "s":
            biberoes = randint(5, 9)
        case _:
            print("Valor Invalido")
            exit(1)

    dados["FASE_BEBE"]["biberoes"] = biberoes
    print(f"\nVoce pegou {biberoes} biberoes")

    felicidade = int(biberoes // 2)  # * TMP
    dados["DADOS_IMPORTANTES"]["felicidade"] = felicidade
    guardar_dados(dados)

    pontuacao(dados)

    opcao_2 = str(input("\nQuer ir no baloiço (s/n)\n-> "))
    while opcao_2.lower() not in ["s", "n"]:
        opcao_2 = str(input("\nQuer ir no baloiço (s/n)\n-> "))
    match opcao_2.lower():
        case "s":
            felicidade += 1
            print("Voçe foi no baloiço")
        case "n":
            felicidade -= 1
            print("Voçe não foi no baloiço")
        case _:
            print("Valor Invalido")
            exit(1)

    dados["DADOS_IMPORTANTES"]["felicidade"] = felicidade
    dados["FASE_BEBE"]["fase_bebe_terminada"] = True
    guardar_dados(dados)

    pontuacao(dados)


match DEBUG:
    case 1:
        fase_bebe(dados)
    case 0:
        pass
    case _:
        print("Valor Invalido")
        exit(1)
