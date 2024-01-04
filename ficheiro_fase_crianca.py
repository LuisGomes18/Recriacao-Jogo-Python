from random import randint

from extras import carregar_dados
from extras import guardar_dados
from extras import pontuacao


DEBUG = 0
dados = carregar_dados()


def fase_crianca(dados):
    felicidade = dados["DADOS_IMPORTANTES"]["felicidade"]

    lampada = randint(1, 9)
    pintura = randint(1, 3)
    bebes = randint(1, 3)
    felicidade_media = (lampada + pintura + bebes) // 3  # * TMP
    felicidade += felicidade_media

    dados["DADOS_IMPORTANTES"]["felicidade"] = felicidade
    dados["FASE_CRIANCA"]["lampada"] = lampada
    dados["FASE_CRIANCA"]["pintura"] = pintura
    dados["FASE_CRIANCA"]["bebes"] = bebes

    match lampada:
        case 9:
            print("\033[32m" + f"\n\nLampadas: {lampada}" + "\033[0m")
        case _:
            print(f"\n\nLampadas: {lampada}")
    match pintura:
        case 3:
            print("\033[32m" + f"Pintura: {pintura}" + "\033[0m")
        case _:
            print(f"Pintura: {pintura}")
    match bebes:
        case 3:
            print("\033[32m" + f"Bebes: {bebes}" + "\033[0m")
        case _:
            print(f"Bebes: {bebes}")

    guardar_dados(dados)
    pontuacao(dados)
    print("\n")

    dados["FASE_CRIANCA"]["fase_crianca_terminada"] = True
    guardar_dados(dados)


match DEBUG:
    case 1:
        fase_crianca(dados)
    case 0:
        pass
    case _:
        print("Valor Invalido")
        exit(1)
