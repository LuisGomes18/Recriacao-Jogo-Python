"""
Random: Para gerar numeros pseudoaleatorios
Extras: Para carregar diferentes parte do codigo
"""
#! pylint: disable=redefined-outer-name
from random import randint

from extras import carregar_dados
from extras import guardar_dados
from extras import pontuacao


DEBUG = 0
VERDE = "\033[32m"
ORIGINAL = "\033[0;0m"
dados = carregar_dados()


def fase_adolecente(dados):
    """
    Fase Adolecente
    """
    felicidade = dados["felicidade"]
    atividade_escolhida = int(
        input(
            """
1) Artes
2) Medicina
3) Musica
4) Desporto
-> """
        )
    )
    while atividade_escolhida not in [1, 2, 3, 4]:
        atividade_escolhida = int(
            input(
                """
1) Artes
2) Medicina
3) Musica
4) Desporto
-> """
            )
        )

    dados["atividade"] = atividade_escolhida
    guardar_dados(dados)

    artes = randint(3, 9)
    medicina = randint(3, 9)
    musica = randint(3, 9)
    desporto = randint(3, 9)

    dados["artes"] = artes
    dados["medicina"] = medicina
    dados["musica"] = musica
    dados["desporto"] = desporto

    guardar_dados(dados)
    pontuacao(dados)

    if atividade_escolhida == 1 and artes == 9:
        print(f"{VERDE}\nArtes: {artes}{ORIGINAL}")
    elif artes != 9:
        print(f"\nArtes: {artes}")
    else:
        print("Valor incorreto")

    if atividade_escolhida == 2 and medicina == 9:
        print(f"{VERDE}Medicina: {medicina}{ORIGINAL}")
    elif medicina != 9:
        print(f"Medicina: {medicina}")
    else:
        print("Valor incorreto")

    if atividade_escolhida == 3 and musica == 9:
        print(f"{VERDE}Musica: {musica}{ORIGINAL}")
    elif musica != 9:
        print(f"Musica: {musica}")
    else:
        print("Valor incorreto")

    if atividade_escolhida == 4 and desporto == 9:
        print(f"{VERDE}Desporto: {desporto}{ORIGINAL}")
    elif desporto != 9:
        print(f"Desporto: {desporto}")
    else:
        print("Valor incorreto")

    match atividade_escolhida:
        case 1:
            felicidade += int(artes / 2)
        case 2:
            felicidade += int(medicina / 2)
        case 3:
            felicidade += int(musica / 2)
        case 4:
            felicidade += int(desporto / 2)

    dados["felicidade"] = felicidade
    guardar_dados(dados)
    pontuacao(dados)

    chances_amizade = []
    chance_amigo = randint(0, 100)
    match chance_amigo:
        case x if x < 50:
            print("Você faz um novo amigo")
            felicidade += 2
        case _:
            print("Você não fez um novo amigo")
    chances_amizade.append(chance_amigo)

    chance_amigo_2 = randint(0, 100)
    match chance_amigo_2:
        case x if x < 50:
            print("Você faz um novo amigo")
            felicidade += 2
        case _:
            print("Você não fez um novo amigo")
    chances_amizade.append(chance_amigo_2)

    chance_amigo_3 = randint(0, 100)
    match chance_amigo_3:
        case x if x < 50:
            print("Você faz um novo amigo")
            felicidade += 2
        case _:
            print("Você não fez um novo amigo")
    chances_amizade.append(chance_amigo_3)

    dados["chance_amigos"] = chances_amizade

    guardar_dados(dados)
    pontuacao(dados)
    print("\n")

    dados["fase_adolecente_terminada"] = True

    guardar_dados(dados)


match DEBUG:
    case 1:
        fase_adolecente(dados)
    case 0:
        pass
    case _:
        print("Valor Invalido")
        exit(1)
