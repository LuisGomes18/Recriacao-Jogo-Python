from random import randint

from extras import carregar_dados
from extras import guardar_dados


DEBUG = 0
dados = carregar_dados()
# dinheiro - felicidade
# comida + felicidade (+7 obeso)
# fumar +felicidade (7 die)
# exercicio + saude  (vida)


def fase_adulto(dados):
    felicidade = dados["felicidade"]
    vida = dados["vida"]

    moedas = randint(25, 31)
    felicidade -= moedas / 2
    dados["moedas"] = moedas
    dados["felicidade"] = felicidade

    comida = randint(3, 10)
    if comida >= 7:
        dados["obeso"] = True
    felicidade += comida / 2
    vida -= comida / 2
    dados["comida"] = comida
    dados["felicidade"] = felicidade
    dados["vida"] = vida

    fumar = randint(3, 10)
    dados["fumar"] = fumar
    if fumar >= 7:
        print("Die")
        dados["morto"] = True
        exit(0)
    else:
        dados["morto"] = False

    exercicio = randint(3, 8)
    vida += exercicio / 2
    dados["exercicio"] = exercicio
    dados["vida"] = vida


    dados["felicidade"] = felicidade
    dados["fase_adulto_terminada"] = True
    guardar_dados(dados)


match DEBUG:
    case 1:
        fase_adulto(dados)
    case 0:
        pass
    case _:
        print("Valor Invalido")
        exit(1)
