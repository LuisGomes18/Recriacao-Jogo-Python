from json import load


with open("Dados.json", encoding='utf-8') as dt:
    dados = load(dt)
amarelo = '\033[33m'
cor_original = '\033[0;0m'
negrito = '\033[1m'


def Pontuacao():
    print(f'''\n\n{amarelo}{negrito}Pntuação:{cor_original}
Vida: {dados["vida"]}
Felicidade: {dados["felicidade"]}
\n\n''')
