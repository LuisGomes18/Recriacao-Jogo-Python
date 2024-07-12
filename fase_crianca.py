from json_def import carregar_dados_player, guardar_dados_player
from random import randint


def fase_bebe():
    dados = carregar_dados_player()

    pais = input('Quer ir com os pais (s/n)? ').strip().lower()
    while pais not in ["s", "n"]:
        pais = input('Quer ir com os pais (s/n)? ').strip().lower()

    if pais == "s":
        print('Foste com os pais')
        dados["fase_crianca"][0]["pais"] = "S"
    elif pais == "n":
        print('Foste sem os pais')
        dados["fase_crianca"][0]["pais"] = "N"

    guardar_dados_player(dados)

    biberao = randint(1, 0)
    dados["fase_crianca"][0]["biberoes"] = biberao

fase_bebe()
