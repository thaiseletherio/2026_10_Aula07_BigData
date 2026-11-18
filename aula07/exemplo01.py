#contador = 1
#while contador <= 10:
    #print(contador)
    # contador = contador + 1
    #contador += 1
    # Aumenta o valor em 1 a cada repetição. Esse recurso (+= 1) é chamado de operador de atribuição aumentada (ou incremento) e serve para deixar o código mais curto e fácil de ler.
#Como funciona na prática
#O uso mais comum dessa sintaxe é dentro de estruturas de repetição (como o while), para controlar quantas vezes um código já rodou. 
# contador += 1  # Aumenta o valor em 1 a cada repetição

contador = 1
soma = 0
while contador <= 5:
    n = float (input('Digite um valor: '))
    soma = soma + n

    contador += 1

    print(f'Total: {soma}') #atualiza a cada interação

#print(f'Total: {soma}') #só printa quando sai do while, por isso só mostra no final.