resposta = 'S'
while resposta == 'S':
    numero = int(input('Informe um número: '))

    dobro = numero * 2
    triplo = numero * 3
    #quadrado = numero * numero
    quadrado = numero ** 2


    print (f'\nDobro: {dobro}')
    print (f'Triplo: {triplo}')
    print (f'Quadrado: {quadrado}')

    resposta = input('\nQuer continuar: [S/N]').upper() #.upper força a resposta para letra maiuscula, 
    #senão não vai pegar o minúsculo e não vai girar o while. 