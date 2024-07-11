import platform
import os


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
