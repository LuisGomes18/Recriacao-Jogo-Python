import random as rd


vida = 0
felicidade = 0
sexopg = 0
biberaochao = 0
biberao = 0
Futebol = 0
Musica = 0
Artes = 0
Medicina = 0
Literacia = 0

def pontuacao():
    print('\033[93m' + f'\nVida - {vida}')
    print(f'Felicidade - {felicidade}\n' + '\033[0m')

def sexo():
    global sexo_personagem
    global sexopg
    sexo_personagem = str(input('Qual sexo do personagem (Masculino ou Femenino)?  '))
    if sexo_personagem == "Masculino" or sexo_personagem == "masculino":
        sexopg = 0
    if sexo_personagem == "Femenino" or sexo_personagem == "femenino":
        sexopg = 1    

def vida_bebe():
    global vida
    global felicidade
    global biberao
    global resto
    vida = 12
    felicidade = 6
    pontuacao()
    pais = str(input('Vai querer com seus pais? '))
    if pais == "sim":
        print('Voçe foi com os pais')
        if felicidade > 12:
            felicidade += 0
            pontuacao()
        elif felicidade < 12:
            felicidade += 2
            pontuacao()
    elif pais == "não":
        print('Não foste com os pais')
        felicidade += 0
        pontuacao()
    else:
        print('Resposta incorreta')
        felicidade += 0
        pontuacao()

    print('Apanhar os biberões')
    print('OBS: Neste caso ja que não tem interface e tudo gerado de forma random')
    biberaochao = rd.randint(1, 2)
    biberao = rd.randint(biberaochao, 9)
    felicidade += biberao  # biberao = 1
    if felicidade > 15:
        resto = felicidade - 15
        felicidade = felicidade - resto
        pontuacao()
    elif felicidade < 15:
        pontuacao()

def vida_crianca():
    global bebe
    global lampada
    global pintura
    global chance
    global brinquedo
    global resto_bebe
    global resto_lampada
    global resto_pintura
    bebe = rd.randint(0, 4)
    lampada = rd.randint(0, 14)
    pintura = rd.randint(0, 4)
    chance = rd.randint(0, 100)

    # Chance para saber se o brinquedo ira aparecer ou não
    if chance > 50:
        brinquedo = rd.randint(0, 1)
    if bebe > 3:
        resto_bebe = bebe - 3
        bebe = bebe - resto_bebe
    if lampada > 9:
        resto_lampada = lampada - 9
        lampada = lampada - resto_lampada
    if pintura > 3:
        resto_pintura = pintura - 3
        pintura = pintura - resto_pintura

    if bebe == 3:
        print('\033[32m' + 'bebes 3/3')
    if lampada == 9:
        print('\033[32m' + 'lampada 9/9')
    if pintura == 3:
        print('\033[32m' + 'pintura 3/3')
    if chance > 50:
        print('\033[32m' + 'brinquedo 1/1')

    elif bebe < 3:
        print(f'bebes {bebe}/3')
    elif lampada < 9:
        print(f'lampada {lampada}/9')
    elif pintura < 3:
        print(f'pintura {pintura}/3')
    pontuacao()  # So para a pessoa saber

def vida_adolecente_rapaz():
    global opcao_2
    global Futebol
    global Musica
    global Artes
    global Medicina
    global Literacia
    global profisao
    global opcao_3
    global chance_2
    global resto_amizade_1
    opcao_2 = int(input('1 - Futebol \n2 - Musica \n3 - Artes\n4 - Medicina\n5 - Literacia\n --> '))
    if opcao_2 == 1:
        Futebol = 1
    elif opcao_2 == 2:
        Musica = rd.randint(0, 13)
    elif opcao_2 == 3:
        Artes = 1
    elif opcao_2 == 4:
        Medicina = 1
    elif opcao_2 == 5:
        Literacia = 1                     
    profisao = opcao_2
    opcao_3 = str(input('Tentar fazer uma nova amiga? '))
    chance_2 = rd.randint(0, 100)
    if opcao_3 == "sim":
        if chance_2 > 50:
            print('Voce fez uma nova amiga : ')
            felicidade += 1
            if felicidade > 15:
                resto_amizade_1 = felicidade - 15
                felicidade = felicidade - resto_amizade_1
                pontuacao()
    elif opcao_3 == "sim":
        if chance_2 < 50:
            print('Ela não quer ser sua amiga')
            felicidade -= 1

comecar = str(input('Bora começar: '))
if comecar == "sim":
    print('Bora\n')
    vida_bebe()
    vida_crianca()
    if sexopg == 0:
        vida_adolecente_rapaz()
    elif sexopg == 1:
        print('fdg')  # TMP 

#Anotações: Forma binaria para decisoes
#           Diferente sexos (Masculino, Femenino)
#           Comunidade LGBTQ+