from json import load
from json import JSONDecodeError
from extras import guardar_dados


def language_choice(dados):
    """
    This function prompts the user to choose a language and loads the corresponding language file. 
    It handles exceptions related to JSON decoding and file loading, and returns the chosen language.
    """
    try:
        language = int(
            """Choice your language:
(1 - Portugal - Portuguese)
(2 - English)
-> """)

        match language:
            case 1:
                with open("language/pt-pt.json", "r", encoding="utf-8") as fl_lingua:
                    language = load(fl_lingua)
                    dados['lang'] = 'pt-pt'
                    guardar_dados(dados)
            case _:
                print("Valor Invalido")
                exit(1)
    except JSONDecodeError:
        print("Error to load the file language")
        exit(1)
    except Exception as erro:
        print("Error to load the language", erro)
        exit(1)
    else:
        return language
