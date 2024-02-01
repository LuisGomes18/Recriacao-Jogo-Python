import json
import os

diretorio_atual = os.getcwd()

with open(rf'{diretorio_atual}\test\data\ing.json', 'r', encoding='utf-8') as fl_ing:
    ing_language = json.load(fl_ing)

with open(rf'{diretorio_atual}\test\data\pt-pt.json', 'r', encoding='utf-8') as fl_pt_pt:
    pt_pt_language = json.load(fl_pt_pt)

print(ing_language, pt_pt_language)
