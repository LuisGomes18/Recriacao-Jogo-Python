import platform
import os
from json_def import  carregar_dados_player, guardar_dados_player


def limpar_terminal():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def welcome():
    limpar_terminal()
    print("""


    ██╗     ██╗███████╗███████╗    ██╗███████╗     █████╗      ██████╗  █████╗ ███╗   ███╗███████╗
    ██║     ██║██╔════╝██╔════╝    ██║██╔════╝    ██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██║     ██║█████╗  █████╗      ██║███████╗    ███████║    ██║  ███╗███████║██╔████╔██║█████╗  
    ██║     ██║██╔══╝  ██╔══╝      ██║╚════██║    ██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ███████╗██║██║     ███████╗    ██║███████║    ██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚══════╝╚═╝╚═╝     ╚══════╝    ╚═╝╚══════╝    ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                                                                
    
Projeto Criado por: Luís Gomes
Repositorio do Projeto: https://github.com/LuisGomes18/Recriacao-Jogo-Python
Linguagem de Programação Usadas: Python


""")


def pontuacao():
    dados = carregar_dados_player()

    vida = dados["recursos"][0]["vida"]
    dinheiro = dados["recursos"][0]["dinheiro"]
    felicidade = dados["recursos"][0]["felicidade"]

    if vida is None or dinheiro is None or felicidade is None:
        raise Exception("Dados do player incorretos, corrija para prosseguir no jogo")

    print(f'\n\nVida: {vida}\nFelicidade: {felicidade}\nDinheiro: {dinheiro}\n\n')


def escolha_sexo():
    """
    Fun o que permite ao jogador escolher o sexo da personagem.
    """

    # Carrega os dados do jogador
    dados = carregar_dados_player()

    # Solicita ao jogador que escolha o sexo da personagem
    sexo = str(input('Escolha o sexo da personagem (F- Feminino, M - Masculino): ')).strip().lower()

    # Verifica se o sexo escolhido   valido
    while sexo not in ["f", "m"]:
        # Se n o for, solicita novamente
        sexo = str(input('Escolha o sexo da personagem (F- Feminino, M - Masculino): ')).strip().lower()

    # Se o sexo for feminino, imprime uma mensagem de confirma o
    if sexo == "f":
        print('E uma menina\n')
    # Se o sexo for masculino, imprime uma mensagem de confirma o
    else:
        print('E um menino\n')

    # Adiciona o sexo escolhido aos dados do jogador
    dados["recursos"][0]["sexo"] = sexo

    # Salva os dados do jogador
    guardar_dados_player(dados)
