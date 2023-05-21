from Erros import Json_Inicio

from json import load
from json import dump


Json_Inicio()
dados_js = Json_Inicio()
dados = dados_js

amarelo = '\033[33m'
cor_original = '\033[0;0m'
negrito = '\033[1m'
vida = 0
felicidade = 0


def Salvar_Dados():
    global dt
    global dados
    with open("Dados.json", "w") as dt:
        dump(dados, dt)


def Sexo():
    sexo = str(input('''Insira o sexo da personagem (F - Feminino, M - Masculino, NB - Não Binario)
-> '''))
    sexo = sexo.lower()
    if sexo == "f":
        dados["sexo"] = sexo
    elif sexo == "m":
        dados["sexo"] = sexo
    elif sexo == "nb":
        dados["sexo"] = sexo
    Salvar_Dados()


def Pontuacao():
    with open("Dados.json", encoding='utf-8') as dt:
        dados = load(dt)
    print(f'''\n\n{amarelo}{negrito}Pntuação:{cor_original}
Vida: {dados["vida"]}
Felicidade: {dados["felicidade"]}
\n\n''')
