from random import randint
from time import sleep
from sys import exit
from os import system


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
moedas = 0
vida_b = 0
vida_c = 0
vida_adc_r = 0
vida_adc_nb = 0

def pontuacao():
    print('\033[93m' + f'\nVida - {vida}')
    print(f'Felicidade - {felicidade}\n' + '\033[0m')

def game_over():
    if felicidade == 0:
        print('Game Over')
        print('Lembra-te suicídio nao e a melhor opção caso tenhas esses pensamentos liga para\n 122 ou https://prevenirsuicidio.pt/contactos-e-servicos-disponiveis/ (Portugal) 188 (Brasil) ')
        exit('Tua vida tva tão mal que suicidas-te')
    elif vida == 0:
        print('Game Over')
        exit('Perdes-te :)')

def amizades():
    global felicidade
    global level_amz
    global chance_amz
    chance_amz = randint(0 ,2)
    if chance_amz == 0:
        opcao_amz = str(input('Tentar fazer uma nova amiga? '))
        opcao_pess = randint(0, 100)
        if opcao_amz == "sim" or opcao_amz == "SIM" and opcao_pess > 50:
            print('Voce fez um nova amiga')
            pontuacao()
            felicidade += 1
            if felicidade > 15:
                resto_amizade_1 = felicidade - 15
                felicidade = felicidade - resto_amizade_1
                pontuacao()
                level_amz += 1
        elif opcao_amz == "sim" or opcao_amz == "SIM" and opcao_pess < 50:
            print('Ela não quer ser tua amiga')
            felicidade -= 1
            pontuacao()
        elif opcao_amz == "nao" or opcao_amz == "NAO" or opcao_amz == "não" or opcao_amz == "NÃO":
            print('Voce nao quis ser amigo dela')
            pontuacao()

    elif chance_amz == 1:
        opcao_amz = str(input('Tentar fazer uma nova amigo? '))
        opcao_pess = randint(0, 100)
        if opcao_amz == "sim" or opcao_amz == "SIM" and opcao_pess > 50:
            print('Voce fez um novo amigo')
            felicidade += 1
            pontuacao()
            if felicidade > 15:
                resto_amizade_1 = felicidade - 15
                felicidade = felicidade - resto_amizade_1
                pontuacao()
                level_amz += 1
        elif opcao_amz == "sim" or opcao_amz == "SIM" and opcao_pess < 50:
            print('Ela não quer ser tua amigo')
            felicidade -= 1
            ajuda_felicidade()
            game_over()
            pontuacao()
        elif opcao_amz == "nao" or opcao_amz == "NAO" or opcao_amz == "não" or opcao_amz == "NÃO":
            print('Voce nao quis ser amigo dele')
            pontuacao()

    elif chance_amz == 3:
        opcao_amz = str(input('Tentar fazer uma nova amigo? '))
        opcao_pess = randint(0, 100)

def escolhas_adulto1():
    global felicidade
    reuniao = str(input('Ir a reunião '))
    if reuniao == "sim":
        felicidade -= 2
        ajuda_felicidade()
        pontuacao()
        game_over()
    escadl = randint(0, 1)
    if escadl == 1:
        escadl2 = str(input('Ajudar colega com trabalho '))
        if escadl2 == "sim" or escadl2 == "SIM":
            felicidade = felicidade + 2
            pontuacao()
        elif escadl2 == "nao" or escadl2 == "NAO" or escadl2 == "não" or escadl2 == "NÃO":
            felicidade = felicidade - 2
            ajuda_felicidade()
            pontuacao()
            game_over()
    elif escadl == 2:
        escadl3 = str(input('Ajudar colega com a fotocopiadora '))
        if escadl3 == "sim" or escadl3 == "SIM":
            felicidade += 2
            pontuacao()
        elif escadl3 == "nao" or escadl3 == "NAO" or escadl3 == "não" or escadl3 == "NÃO":
            felicidade -= 2
            ajuda_felicidade()
            pontuacao()
            game_over()

def ajuda_felicidade():
    global ajuda
    global metade
    global felicidade
    global vida
    metade = felicidade /2
    if felicidade <= metade:
        chance_ajuda = randint(1, 3)
        if chance_ajuda == 1:
            ajuda = str(input('Ir com os amigos? '))
            metade = felicidade /16 # Procurar qual o maximo de felicidade (papeis)
            if ajuda == "sim":
                felicidade += 5
                ajuda_felicidade()
                pontuacao()
                game_over()
        elif chance_ajuda == 2:
            ajuda = str(input('Quer fazer alguma atividade? '))
            if ajuda == "sim":
                felicidade += 5
                ajuda_felicidade()
                pontuacao()
                game_over()
        elif chance_ajuda == 3:
            ajuda = str(input('Quer fazer alguma atividade? '))
            if ajuda == "sim":
                felicidade += 5
                ajuda_felicidade()
                pontuacao()
                game_over()

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
    print('COMEÇO DA FASE BÉBÉ')
    global vida
    global felicidade
    global biberao
    global resto
    global vida_b
    vida = 12
    felicidade = 6
    sexo()
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
    biberaochao = randint(1, 2)
    biberao = randint(biberaochao, 9)
    felicidade += biberao  # biberao = 1
    if felicidade > 15:
        resto = felicidade - 15
        felicidade = felicidade - resto
        pontuacao()
    elif felicidade < 15:
        pontuacao()
    vida_b = 1
    print('ACABA FASE BÉBÉ')

def vida_crianca():
    print('COMEÇO DA FASE CRIANÇA')
    global felicidade
    global bebe
    global lampada
    global pintura
    global chance
    global brinquedo
    global resto_bebe
    global resto_lampada
    global resto_pintura
    global vida_c
    bebe = randint(0, 4)
    lampada = randint(0, 14)
    pintura = randint(0, 4)
    chance = randint(0, 100)

    #* Chance para saber se o brinquedo ira aparecer ou não
    if chance > 50:
        brinquedo = randint(0, 1)
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
    pontuacao()  #* So para a pessoa saber
    vida_c = 1
    print('ACABA FASE CRIANÇA')

def vida_adolecente_masculino_hetero():
    print('COMEÇO DA FASE ADOLECENTE MASCULINO')
    global felicidade
    global Futebol
    global Musica
    global Artes
    global Medicina
    global Literacia
    global Fumar
    global media
    global profisao
    global media
    global media_fumar
    global opcao_2
    global opcao_3
    global opcao_4
    global opcao_5
    global opcao_6
    global chance_5
    global chance_2
    global chance_3
    global chance_4
    global chance_5
    global resto_amizade_1
    global resto_amizade_2
    global resto_amizade_3
    global vida_adc_r
    opcao_2 = int(input('1 - Futebol \n2 - Musica \n3 - Artes\n4 - Medicina\n5 - Literacia\n --> '))
    if opcao_2 == 1:
        Futebol = 1
    elif opcao_2 == 2:
        Musica = randint(0, 13)
    elif opcao_2 == 3:
        Artes = 1
    elif opcao_2 == 4:
        Medicina = 1
    elif opcao_2 == 5:
        Literacia = 1
    profisao = opcao_2
    opcao_3 = str(input('Tentar fazer uma nova amiga? '))
    chance_2 = randint(0, 100)
    if opcao_3 == "sim":
        if chance_2 > 50:
            print('Voce fez uma nova amiga : ')
            felicidade += 5
            ajuda_felicidade()
            pontuacao()
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
            pontuacao()
            game_over()

    opcao_4 = str(input('Tentar fazer um novo amigo? '))
    chance_3 = randint(0, 100)
    if opcao_4 == "sim":
        if chance_3 > 50:
            print('Voce fez um novo amigo : ')
            felicidade += 5
            pontuacao()
            game_over()
            if felicidade > 15:
                resto_amizade_2 = felicidade - 15
                felicidade = felicidade - resto_amizade_2
                pontuacao()

    opcao_5 = str(input('Tentar fazer uma novo amigo? '))
    chance_4 = randint(0, 100)
    if opcao_5 == "sim":
        if chance_4 > 50:
            print('Voce fez uma nova amigo : ')
            felicidade += 5
            ajuda_felicidade()
            pontuacao()
            game_over()
            if felicidade > 15:
                resto_amizade_3 = felicidade - 15
                felicidade = felicidade - resto_amizade_3
                pontuacao()

    # Atividades que a pessoa ir a fazer

    Futebol = randint(0, 20)
    Musica = randint(0, 20)
    Artes = randint(0, 20)
    Medicina = randint(0, 20)
    Literacia = randint(0, 20)
    Fumar = randint(0, 20)
    media_fumar = int(Fumar / 15)
    if opcao_2 == 1:
        media = int((Musica + Artes + Medicina + Literacia) / 4)
        felicidade -= media
        felicidade -= media_fumar
        ajuda_felicidade()
        pontuacao()
        game_over()
    elif opcao_2 == 2:
        media = int((Futebol + Artes + Medicina + Literacia) / 4)
        felicidade -= media
        felicidade -= media_fumar
        ajuda_felicidade()
        pontuacao()
        game_over()
    elif opcao_2 == 3:
        media = int((Futebol + Musica + Medicina + Literacia) / 4)
        felicidade -= media
        felicidade -= media_fumar
        ajuda_felicidade()
        pontuacao()
        game_over()
    elif opcao_2 == 4:
        media = int((Futebol + Musica + Artes + Literacia) / 4)
        felicidade -= media
        felicidade -= media_fumar
        ajuda_felicidade()
        pontuacao()
        game_over()
    elif opcao_2 == 5:
        media = int((Futebol + Musica + Artes + Literacia) / 4)
        felicidade -= media
        felicidade -= media_fumar
        ajuda_felicidade()
        pontuacao()
        game_over()
    opcao_6 = str(input('Tentar fazer uma novo amigo? ')) #? Mudar depois para brincar , ler com amigos e etc
    chance_5 = randint(0, 100)
    if opcao_6 == "sim":
        if chance_5 > 50:
            print('Voce fez uma nova amigo : ')  #? Mudar depois para brincar , ler com amigos e etc
            felicidade -= 1
            ajuda_felicidade()
            game_over()
            if felicidade > 15:
                resto_amizade_3 = felicidade - 15
                felicidade = felicidade - resto_amizade_3
                pontuacao()

    vida_adc_r = 1
    print('ACABA FASE ADOLECENTE MASCULINO')

def vida_adulto_masculino_hetero():
    print('COMEÇO DA FASE ADULTO MASCULINO')
    global felicidade
    global moedas
    global dinheiro
    global comida
    global fumar
    global ginasio
    global ramo_pq
    global ramo_md
    global ramo_gr
    global carro_barato
    global carro_medio
    global carro_caro
    global nv_chance_casar
    global nv_chance_carro
    moedas = randint(0, 33)
    dinheiro = moedas
    comida = randint(0, 5)
    fumar = randint(0, 1)
    ginasio = randint(0, 1)
    felicidade = felicidade - comida
    felicidade = felicidade -  fumar
    felicidade = felicidade - ginasio
    escolhas_adulto1()
    ajudar_pobre = str(input('Ajudar pobre '))
    if ajudar_pobre == "sim":
        dinheiro -= 2
        print(dinheiro)
        pontuacao()
    elif ajudar_pobre == "nao":
        felicidade -= 1
        ajuda_felicidade()
        print(dinheiro)
        pontuacao()
        game_over()
    #! Parte do casamento
    ramo_pq = 10 #! TMP
    ramo_md = 20 #! TMP
    ramo_gr = 30 #! TMP
    nv_chance_casar = 0
    print('Escolha do ramo de flores')
    escflores = str(input('grande, media ou pequeno '))
    if escflores == "grande" and dinheiro >= ramo_gr:
        print('Voçe comprou o ramo grande')
        nv_chance_casar = 1
    elif escflores == "grande" and dinheiro < ramo_gr:
        print('Voce não tem dinhero')
        if dinheiro >= ramo_md:
            print('Voce comprou o ramo medio')
            nv_chance_casar = 2
        elif dinheiro < ramo_md:
            print('Voce comprou o ramo pequeno')
            nv_chance_casar = 3
    carro_barato = 10 #! TMP
    carro_medio = 20 #! TMP
    carro_caro = 30 #! TMP
    nv_chance_carro = 0
    esccarro = str(input('Caro, Medio ou barato '))
    if esccarro == "caro" and dinheiro >= carro_caro:
        print('Voce comprou o carro caro')
        nv_chance_carro = 1
    elif esccarro == "grande" and dinheiro < carro_caro:
        print('Voce não tem dinhero')
        if dinheiro >= carro_medio:
            print('Voce comprou o carro medio')
            nv_chance_carro = 2
        elif dinheiro < carro_medio:
            print('Voce comprou o carro barato')
            nv_chance_carro = 3

    casar = int(input('1 para primeiro 2 para o segundo 3 para o terceiro'))
    if casar == 1:
        print('a')
    print('ACABA FASE ADULTO MASCULINO')

system('cls')
comecar = str(input('Start? '))
if comecar == "sim" or comecar == "Sim" or comecar == "SIM":
    print('A começar')
    vida_bebe()
    if vida_b == 1:
        vida_crianca()
        sleep(2)
        if sexopg == 0 and vida_b == 1:
            vida_adolecente_masculino_hetero()
            sleep(2)
            if vida_adc_r == 1:
                vida_adulto_masculino_hetero()
                sleep(2)

        else:
            print('\033[31m' + 'Erro Critico' + '\033[0m')
            print('\033[31m' + 'Bug Maximo' + '\033[0m')