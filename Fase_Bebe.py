from json import load
from Extras import Pontuacao

DEBUG = 1

try:
    with open("Dados.json", encoding='utf-8') as dt:
        dados = load(dt)
        print('Dados Carregados')  #! tmp
except FileNotFoundError:
    exit('Ficheiro não encontrado ou corrompido')
felicidade = dados["felicidade"]

def Fase_Bebe():
    opcao_1 = str(input('Quer ir com os pais? (y/n)\n'))
    if opcao_1 == "y":
        print('Voce foi com seu pais')
        felicidade =+ 2
        dados["felicidade"] = felicidade
        with open("Dados.json", "w") as dt:
            json.dump(dados, dt)
        Pontuacao()
    elif opcao_1 == "n":
        print('Voce não foi com seu pais')
        Pontuacao()
    else:
        print('Opção invalida')

if DEBUG == 1:
    Fase_Bebe()
elif DEBUG == 0:
    PRINT('FUNÇÃO DEBUG ESTA DESATIVADO')
