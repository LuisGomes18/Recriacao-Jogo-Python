import json
import os

diretorio_atual = os.getcwd()


lingua = str(input('Lingua: (pt-pt ou ing) -> '))
lingua.lower()
match lingua:
    case 'pt-pt':
        with open(rf'{diretorio_atual}\test\data\pt-pt.json', 'r', encoding='utf-8') as fl_lingua:
            language = json.load(fl_lingua)
    case 'ing':
        with open(rf'{diretorio_atual}\test\data\ing.json', 'r', encoding='utf-8') as fl_lingua:
            language = json.load(fl_lingua)
    case _:
        print('Valor Invalido')
        exit(1)


print('\n' + language['Phase_1'][0]['phrase_1'])
print(language['Phase_1'][0]['phrase_2'])
print(language['Phase_1'][0]['phrase_3'])
