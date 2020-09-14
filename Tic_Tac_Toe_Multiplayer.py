def display(campos):
    print(f'{campos[1]:^3}|{campos[2]:^3}|{campos[3]:^3}\n'
          f'{"-" * 11}\n'
          f'{campos[4]:^3}|{campos[5]:^3}|{campos[6]:^3}\n'
          f'{"-" * 11}\n'
          f'{campos[7]:^3}|{campos[8]:^3}|{campos[9]:^3}')


def check_play(msg):
    while True:
        player = input(msg)
        if player.isdigit():
            if int(player) in range(1, 10):
                break
            else:
                print('Número digitado não está entre 1 e 9')
        else:
            print('Tecla pressionada não é um digito')
    return int(player)


def check_position(mark):
    while True:
        jogada = check_play(f'{mark}, escolha uma posição entre 1 e 9 disponível: ')
        if campos[jogada] == ' ':
            break
        else:
            print('Posição ja marcada por algum dos jogadores!')
    return jogada


def entrada():
    while True:
        marcador = input('Qual você quer ser? [O / X]: ').upper()
        if marcador in 'OX':
            break
        else:
            print('Opção Inválida! Tente novamente.')
    return marcador


def limpar_tabuleiro():
    campos = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return campos


def escolhe_mark():
    # ESCOLHENDO UM MARCADOR PARA CADA JOGADOR
    marcador = entrada()
    if marcador == 'X':
        marcador1 = 'X'
        marcador2 = 'O'
        print(f'Você escolheu {marcador}, então você começa primeiro!')
    else:
        marcador1 = 'X'
        marcador2 = 'O'
        print(f'Você escolheu {marcador}, então seu adversário começa primeiro!')
    return [marcador1, marcador2]


def check_jogo(mark1, mark2):
    # CRIANDO UM LOOP PARA AS JOGADAS QUE SÓ QUEBRA CASO DE ALGUMA VITÓRIA OU VELHA
    cont = 0
    while True:
        jogador1 = check_position(mark1)
        campos[jogador1] = mark1
        display(campos)
        if checker(mark1):
            print(f'\n{mark1} GANHOU!')
            break
        cont += 1
        if cont == 9:
            print('\nDEU VELHA!')
            break
        jogador2 = check_position(mark2)
        campos[jogador2] = mark2
        display(campos)
        if checker(mark2):
            print(f'\n{mark2} GANHOU')
            break
        cont += 1


def checker(m):
    l_inicio = 1
    l_fim = 4
    ganhou = 0

    for c in range(0, 3):
        varC = ''.join([campos[1 + c], campos[4 + c], campos[7 + c]])
        varL = ''.join(campos[l_inicio:l_fim])
        l_inicio += 3
        l_fim += 3
        if varC == str(m * 3) or varL == str(m * 3):
            ganhou = 1
            break

    varD1 = ''.join([campos[1], campos[5], campos[9]])
    varD2 = ''.join([campos[3], campos[5], campos[7]])
    if ganhou == 0 and varD1 == str(m * 3) or varD2 == str(m * 3):
        ganhou = 1

    if ganhou == 1:
        return True
    else:
        return False


# _______PROGRAMA PRINCIPAL_______
campos = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

print('=' * 31)
print(f'{"BEM-VINDO AO JOGO DA VELHA!":^31}')
print('=' * 31)

# CRIANDO UM LOOP QUE SO QUEBRA SE O USUÁRIO NÃO QUISER JOGAR NOVAMENTE
while True:
    marcador1, marcador2 = map(str, escolhe_mark())
    display(campos)
    check_jogo(marcador1, marcador2)
    campos = limpar_tabuleiro()

    while True:
        opcao = input('Deseja continuar? [S/N]: ').upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('Fim de Jogo!')
