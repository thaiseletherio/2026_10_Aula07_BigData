while True:
    numero = int(input('Informe um número: '))

    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2


    print (f'\nDobro: {dobro}')
    print (f'Triplo: {triplo}')
    print (f'Quadrado: {quadrado}')

    resposta = input ('\n Quer continuar [S/N]? ').upper()

    if resposta == 'N':
        break


