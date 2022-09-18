import random as rd

vida = 0
felicidade = 0
biberaochao = 0
biberao = 0

def vida_bebe():
    global vida
    global felicidade
    global biberao
    global resto
    vida = 12
    felicidade = 6
    print(f'Vida - {vida}')
    print(f'Felicidade - {felicidade}')    
    pais = str(input('Vai querer com seus pais? '))
    if pais == "sim":
        print('Voçe foi com os pais')
        if felicidade > 12:
            felicidade += 0
            print(f'Vida - {vida}')
            print(f'Felicidade - {felicidade}')
        elif felicidade < 12:    
            felicidade += 2
            print(f'Vida - {vida}')
            print(f'Felicidade - {felicidade}')
    elif pais == "não":
        print('Não foste com os pais')
        felicidade += 0
        print(f'Vida - {vida}')
        print(f'Felicidade - {felicidade}')
    else:
        print('Resposta incorreta') 
        felicidade += 0    
        print(f'Vida - {vida}')
        print(f'Felicidade - {felicidade}') 

    print('Apanhar os biberões')
    print('OBS: Neste caso ja que não tem interface e tudo gerado de forma random')
    biberaochao = rd.randint(1, 2)
    biberao = rd.randint(biberaochao, 9)
    felicidade += biberao # biberao = 1
    if felicidade > 15:
        resto = felicidade - 15
        felicidade = felicidade - resto
        print(f'Vida - {vida}')
        print(f'Felicidade - {felicidade}')
    elif felicidade < 15:
        print(f'Vida - {vida}')
        print(f'Felicidade - {felicidade}')

def vida_crianca():
    print('')  #TEMP       

comecar = str(input('Bora começar: '))
if comecar == "sim":
    print('Bora\n')
    vida_bebe()