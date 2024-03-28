from json import load
from json import dump
from json import JSONDecodeError


def carregar_json():
    """
    Definiçao para carregar os dados para ficheiro json
    """
    try:
        with open('Data/Dados.json', 'r', encoding='utf-8') as f:
            data = load(f)
    except JSONDecodeError:
        print('Erro na decodificação do JSON')
    except FileNotFoundError:
        print('O arquivo Dados.json não foi encontrado')
    except Exception as json_error:
        print(f'Erro inesperado ao carregar o JSON: \n{json_error}')
    else:
        return data


def guardar_json(dados):
    """
    Definicao para guardar os dados para ficheiro json
    """
    try:
        with open('Data/Dados.json', 'w', encoding='utf-8') as f:
            dump(dados, f, indent=4)
    except FileNotFoundError:
        print('O arquivo Dados.json não foi encontrado')
    except Exception as json_error:
        print(f'Erro inesperado ao guardar o JSON: \n{json_error}')
