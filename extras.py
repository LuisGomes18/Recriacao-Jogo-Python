from json import loads
from json import dump
from platform import system
import os


def apagar_terminal():
    sistema = system()
    try:
        if sistema == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    except Exception as erro:
        print('Erro ao apagar o terminal', erro)


def carregar_dados():
    """
    Loads data from a JSON file and returns the loaded data.

    Returns:
        dict: The loaded data from the JSON file.

    Raises:
        FileNotFoundError: If the file 'Data/Dados.json' is not found.
    """
    try:
        with open('Data/Dados.json', 'r', encoding='utf-8') as dados_player:
            conteudo = dados_player.read()
            dados = loads(conteudo)
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    else:
        return dados


def guardar_dados(dados):
    """
    Save the given data to a JSON file.

    Parameters:
    - dados (any): The data to be saved.

    Returns:
    - None
    """
    with open('Data/Dados.json', 'w', encoding='utf-8') as dados_player:
        dump(dados, dados_player, ensure_ascii=False, indent=2)


def pontuacao(dados):
    """
    Generates a function comment for the given function body in a markdown code block with the correct language syntax.

    :param dados: A dictionary containing important data.
    :type dados: dict

    :return: None
    :rtype: None
    """
    felicidade = dados['DADOS_IMPORTANTES']['felicidade']
    vida = dados['DADOS_IMPORTANTES']['vida']
    dinheiro = dados['DADOS_IMPORTANTES']['dinheiro']
    print(f'\nFelicidade: {felicidade}')
    print(f'Vida: {vida}')
    print(f'Dinheiro: {dinheiro}\n')
