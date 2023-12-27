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
    match escolha_flores:
        case 1:
            moedas -= 20
            dados["flores"] = {
                "flores_grandes": True, 
                "flores_pequenas": False
            }
        case 2:
            moedas -= 10
            dados["flores"] = {
                "flores_grandes": False, 
                "flores_pequenas": True
            }
        case _:
            print("Valor Invalido")
            exit(1)
    dados["dinheiro"] = moedas

    pontuacao(dados)
    guardar_dados(dados)

    escolha_carros = int(
        input(
            "Escolha o carro (Moderno mas caro -> 1, Mais ou menos -> 2, Chaço mas barato -> 3): "
        )
    )
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

match DEBUG:
    case 1:
        fase_adulto_parte_2(dados)
    case 0:
        pass
    case _:
        print("Valor Invalido")
        exit(1)
