import platform
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extras.json_def import carregar_dados_player, guardar_dados_player


def limpar_terminal():
    os.system("cls" if platform.system() == "Windows" else "clear")


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
    dados = carregar_dados_player()["recursos"][0]

    vida, dinheiro, felicidade = (dados.get(i) for i in ("vida", "dinheiro", "felicidade"))

    if any(i is None for i in (vida, dinheiro, felicidade)):
        raise Exception("Dados do player incorretos, corrija para prosseguir no jogo")

    print(f'\n\nVida: {vida}\nFelicidade: {felicidade}\nDinheiro: {dinheiro}\n\n')


def escolha_sexo():
    """
    Fun o que permite ao jogador escolher o sexo da personagem.
    """

    # Carrega os dados do jogador
    dados = carregar_dados_player()

    # Solicita ao jogador que escolha o sexo da personagem
    while True:
        sexo = input('Escolha o sexo da personagem (F- Feminino, M - Masculino): ').strip().lower()
        if sexo in ("f", "m"):
            break

    # Adiciona o sexo escolhido aos dados do jogador
    dados["recursos"][0]["sexo"] = sexo

    # Salva os dados do jogador
    guardar_dados_player(dados)
