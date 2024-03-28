from json_defs import carregar_json
from json_defs import guardar_json


def escolha_sexo():
    dados = carregar_json()
    sexo = input('''Escolha o sexo do personagem:
1) Masculino
2) Feminino
-> ''')
    print('\n')
    while sexo not in ["1", "2"]:
        sexo = input('''Escolha o sexo do personagem:
1) Masculino
2) Feminino
-> ''')
    sexo_fn = " "
    if sexo == "1":
        sexo_fn = "M"
    elif sexo == "2":
        sexo_fn = "F"
    else:
        print('Valor Inválido, por favor escolha um valor válido')
        sexo_fn = " "
    print('\n')

    dados["DADOS_IMPORTANTES"]["sexo"] = sexo_fn
    dados["DADOS_IMPORTANTES"]["fase_atual"] = "Fase_Bebe"
    guardar_json(dados)
