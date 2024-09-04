import json
import os


def carregar_dados_player():
    '''
    Carrega os dados do arquivo 'player.json' e retorna como um dicionário Python.
    
    Returns:
        dict: Um dicionário Python contendo os dados do arquivo 'player.json'.
    
    Raises:
        FileNotFoundError: Se o arquivo 'player.json' não for encontrado.
        json.JSONDecodeError: Se houver um erro de decodificação JSON ao carregar os dados.
        Exception: Se ocorrer qualquer outro erro durante o processo de carregamento.
    '''
    try:
        with open('../data/player.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('O arquivo "player.json" não foi encontrado.')
    except json.JSONDecodeError as exc:
        raise json.JSONDecodeError('Houve um erro de decodificação JSON ao carregar os dados.') from exc
    except Exception as exc:
        raise Exception(f'Ocorreu um erro ao carregar os dados do jogador: {exc}') from exc


def guardar_dados_player(dados: dict):
    """
    Guarda os dados do jogador em um arquivo JSON.

    Args:
        dados (dict): Um dicionário contendo os dados do jogador a serem salvos.

    Raises:
        TypeError: Se os dados não forem fornecidos como um dicionário ou são nulos.
        FileNotFoundError: Se o arquivo 'player.json' não puder ser encontrado.
        json.JSONDecodeError: Se houver um erro de decodificação JSON ao salvar os dados.
        Exception: Se ocorrer qualquer outro erro não previsto.
    """
    if not isinstance(dados, dict) or dados is None:
        raise TypeError('Os dados devem ser fornecidos como um dicionário não nulo.')

    try:
        os.makedirs('data', exist_ok=True)
        with open('../data/player.json', 'wb') as f:
            json.dump(dados, f, ensure_ascii=False, separators=(',', ':'))
    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(f'O arquivo "player.json" não pôde ser encontrado: {fnf_error}') from fnf_error
