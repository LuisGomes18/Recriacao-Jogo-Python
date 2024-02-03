from random import randint

from extras import carregar_dados
from extras import guardar_dados
from extras import pontuacao


DEBUG = 1
dados = carregar_dados()


def fase_adulto_parte_2(dados):
    felicidade = dados["felicidade"]
    vida = dados["vida"]
    moedas = dados["dinheiro"]

    pontuacao(dados)

    escolha_flores = int(
        input("Escolha as flores (Grande mas caras-> 1, Pequenas mas bratas -> 2): ")
    )
    while escolha_flores not in [1, 2]:
        escolha_flores = int(input("Escolha as flores (Grande mas caras-> 1, Pequenas mas bratas -> 2): "))

    match escolha_flores:
        case 1:
            moedas -= 20
            dados["flores"] = {"flores_grandes": True, "flores_pequenas": False}
        case 2:
            moedas -= 10
            dados["flores"] = {"flores_grandes": False, "flores_pequenas": True}
        case _:
            print("Valor Invalido")
            exit(1)
    dados["dinheiro"] = moedas

    pontuacao(dados)
    guardar_dados(dados)

    escolha_carros = int(input("Escolha o carro (Moderno mas caro -> 1, Mais ou menos -> 2, Chaço mas barato -> 3): "))
    while escolha_carros not in [1, 2, 3]:
        escolha_carros = int(input("Escolha o carro (Moderno mas caro -> 1, Mais ou menos -> 2, Chaço mas barato -> 3): "))

    match escolha_carros:
        case 1:
            moedas -= 800
            dados["carros"] = {
                "carros_modernos": True,
                "carros_mais_ou_menos": False,
                "carros_antigos": False,
            }
        case 2:
            moedas -= 400
            dados["carros"] = {
                "carros_modernos": False,
                "carros_mais_ou_menos": True,
                "carros_antigos": False,
            }
        case 3:
            moedas -= 200
            dados["carros"] = {
                "carros_modernos": False,
                "carros_mais_ou_menos": False,
                "carros_antigos": True,
            }
        case _:
            print("Valor Invalido")
            exit(1)
    dados["dinheiro"] = moedas

    pontuacao(dados)
    guardar_dados(dados)

    namorada_1 = str(input("Pretende namorar como a primeira rapariga (s/n): "))
    chance_aceitar = randint(0, 100)
    if namorada_1.lower() == "s" and chance_aceitar <= 25:
        print("Ela aceitou")
        dados["namorada_1"] = True
        felicidade += 5  #! TMP
    elif namorada_1.lower() == "n" or chance_aceitar > 25:
        print("Voçe não quis namorar ou ela não eceitou")
        dados["namorada_1"] = False
        felicidade -= 5  #! TMP
    else:
        print("Valor Invalido")
        dados["namorada_1"] = None
        exit(1)

    pontuacao(dados)
    guardar_dados(dados)

    namorada_1_aceitou = dados["namorada_1"]
    if not namorada_1_aceitou:
        namorada_2 = str(input("Pretende namorar com a segunda rapariga (s/n): "))
        chance_aceitar = randint(0, 100)
        if namorada_2.lower() == "s" and chance_aceitar >= 50:
            print("Ela aceitou")
            dados["namorada_2"] = True
            felicidade += 5  #! TMP
        elif namorada_2.lower() == "n" or chance_aceitar < 50:
            print("Voçe não quis namorar ou ela não aceitou")
            dados["namorada_2"] = False
            felicidade -= 5  #! TMP
        else:
            print("Valor Invalido")
            dados["namorada_2"] = None
            exit(1)
    elif namorada_1_aceitou:
        namorada_2 = None
        dados["namorada_2"] = None
    else:
        print("Valor Invalido")
        dados["namorada_2"] = None
        exit(1)

    pontuacao(dados)
    guardar_dados(dados)


match DEBUG:
    case 1:
        fase_adulto_parte_2(dados)
    case 0:
        pass
    case _:
        print("Valor Invalido")
        exit(1)
