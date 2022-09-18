import random as rd


vida = 0
felicidade = 0
biberaochao = 0
biberao = 0
fim_bebe = 0


def pontuacao():
    print('\033[93m' + f'\nVida - {vida}')
    print(f'Felicidade - {felicidade}\n' + '\033[0m')


def vida_bebe():
    global vida
    global felicidade
    global biberao
    global resto
    global fim_bebe
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
    fim_bebe = 1


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

def vida_adolecente():
    print() # TEMP

comecar = str(input('Bora começar: '))
if comecar == "sim":
    print('Bora\n')
    vida_bebe()
    if fim_bebe == 1:
        vida_crianca()
    elif fim_bebe == 0:
        print('Erro Def vida_bebe()')
