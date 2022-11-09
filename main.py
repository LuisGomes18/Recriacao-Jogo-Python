import random as rd
import sys


vida = 0
felicidade = 0
sexopg = 0
biberaochao = 0
biberao = 0
bebe = 0
lampada = 0
pintura = 0
chance = 0
brinquedo = 0
Futebol = 0
Musica = 0
Artes = 0
Medicina = 0
Literacia = 0
Fumar = 0

def pontuacao():
    print('\033[93m' + f'\nVida - {vida}')
    print(f'Felicidade - {felicidade}\n' + '\033[0m')

def game_over():
    if felicidade == 0:
        print('Game Over')
        print('Lembra-te suicídio nao e a melhor opção caso tenhas esses pensamentos liga para\n 122 ou https://prevenirsuicidio.pt/contactos-e-servicos-disponiveis/ (Portugal) 188 (Brasil) ')
        sys.exit('Tua vida tva tão mal que suisidas-te')
    elif vida == 0:
        print('Game Over')   
        #exit() 
        sys.exit('Perdes-te :)')

def ajuda_felicidade():
    global ajuda
    global metade
    global felicidade
    global vida
    metade = felicidade /2
    if felicidade <= metade:
        chance_ajuda = rd.randint(1, 3)
        if chance_ajuda == 1:
            ajuda = str(input('Ir com os amigos? '))
            metade = felicidade /16 # Procurar qual o maximo de felicidade (papeis)
            if ajuda == "sim":
                felicidade += 5
        elif chance_ajuda == 2:
            ajuda = str(input('Quer fazer alguma atividade? '))
            if ajuda == "sim":
                felicidade += 5
        elif chance_ajuda == 3:
            ajuda = str(input('Quer fazer alguma atividade? '))
            if ajuda == "sim":
                felicidade += 5

def sexo():
    global sexo_personagem
    global sexopg
    sexo_personagem = str(input('Qual sexo do personagem (Masculino, Feminino ou Nao Binarie)?  '))
    if sexo_personagem == "Masculino" or sexo_personagem == "masculino":
        sexopg = 0
    if sexo_personagem == "Feminino" or sexo_personagem == "feminino":
        sexopg = 1    
    elif sexo_personagem == "Nao-Binarie" or sexo_personagem == "nao-binarie" or sexo_personagem == "nao binarie" or sexo_personagem == "Nao Binarie":
        sexopg = 2

def vida_bebe():
    global vida
    global felicidade
    global biberao
    global resto
    vida = 12
    felicidade = 6
    pontuacao()
    pais = str(input('Vai querer com seus pais? '))
    if pais == "sim" or pais == "SIM":
        print('Voçe foi com os pais')
        if felicidade > 12:
            felicidade += 0
            pontuacao()
        elif felicidade < 12:
            felicidade += 2
            pontuacao()
    elif pais == "não" or pais == "nao" or pais == "NAO" or pais == "NÃO":
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
    global felicidade
    global Futebol
    global Musica
    global Artes
    global Medicina
    global Literacia
    global Fumar
    global profisao
    global opcao_2    
    global opcao_3
    global opcao_4
    global opcao_5
    global chance_2
    global chance_3
    global resto_amizade_1
    global resto_amizade_2
    global resto_amizade_3
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
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_1 = felicidade - 15
                felicidade = felicidade - resto_amizade_1
                pontuacao()
    elif opcao_3 == "sim":
        if chance_2 < 50:
            print('Ela não quer ser sua amiga')
            felicidade -= 1
            ajuda_felicidade()
            game_over()

    opcao_4 = str(input('Tentar fazer um novo amigo? '))
    chance_3 = rd.randint(0, 100)
    if opcao_4 == "sim":
        if chance_3 > 50:
            print('Voce fez um novo amigo : ')
            felicidade += 1
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_2 = felicidade - 15
                felicidade = felicidade - resto_amizade_2
                pontuacao()

    opcao5 = str(input('Tentar fazer uma novo amigo? '))
    chance_4 = rd.randint(0, 100)
    if opcao5 == "sim":
        if chance_4 > 50:
            print('Voce fez uma nova amigo : ')
            felicidade -= 1
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_3 = felicidade - 15
                felicidade = felicidade - resto_amizade_3
                pontuacao()

    # Atividades que a pessoa ir a fazer 

    Futebol = rd.randint(0, 20)
    Musica = rd.randint(0, 20)
    Artes = rd.randint(0, 20)
    Medicina = rd.randint(0, 20)
    Literacia = rd.randint(0, 20)
    Fumar = rd.randint(0, 20)
    if Futebol == 14 and profisao == 1:
        felicidade =- 1

def vida_adolecente_nao_binario():
    global felicidade
    global Futebol
    global Musica
    global Artes
    global Medicina
    global Literacia
    global Fumar
    global profisao
    global opcao_2    
    global opcao_3
    global opcao_4
    global opcao_5
    global opcao_6
    global chance_2
    global chance_3
    global chance_4
    global chance_5
    global resto_amizade_1
    global resto_amizade_2
    global resto_amizade_3
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
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_1 = felicidade - 15
                felicidade = felicidade - resto_amizade_1
                pontuacao()
    elif opcao_3 == "sim":
        if chance_2 < 50:
            print('Ela não quer ser sua amiga')
            felicidade -= 1
            ajuda_felicidade()
            game_over()

    opcao_4 = str(input('Tentar fazer um novo amigo? '))
    chance_3 = rd.randint(0, 100)
    if opcao_4 == "sim":
        if chance_3 > 50:
            print('Voce fez um novo amigo : ')
            felicidade += 1
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_2 = felicidade - 15
                felicidade = felicidade - resto_amizade_2
                pontuacao()

    opcao_5 = str(input('Tentar fazer uma amiga? '))
    chance_4 = rd.randint(0, 100)
    if opcao_5 == "sim":
        if chance_4 > 50:
            print('Voce fez uma amiga : ')
            felicidade -= 1
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_3 = felicidade - 15
                felicidade = felicidade - resto_amizade_3
                pontuacao()

    opcao_6 = str(input('Tentar fazer um amigo? '))
    chance_5 = rd.randint(0, 100)
    if opcao_6 == "sim":
        if chance_5 > 50:
            print('Voce fez um amigo : ')
            felicidade -= 1
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_4 = felicidade - 15
                felicidade = felicidade - resto_amizade_4
                pontuacao()

    Futebol = rd.randint(0, 20)
    Musica = rd.randint(0, 20)
    Artes = rd.randint(0, 20)
    Medicina = rd.randint(0, 20)
    Literacia = rd.randint(0, 20)
    Fumar = rd.randint(0, 20)
    if Futebol == 14 and profisao == 1:
        felicidade =- 1


def vida_adulta_rapaz():
    print('a')    

comecar = str(input('Bora começar: '))
if comecar == "sim":
    print('Bora\n')
    vida_bebe()
    vida_crianca()
    if sexopg == 0:
        vida_adolecente_rapaz()
    elif sexopg == 1:
        print('fdg')  # TMP 

