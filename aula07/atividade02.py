#registre os valores gastos
#apresente o acumulado no final
#solicita a despesa
#soma as despesas 
#continua até o usuário querer encerrar os registros
#ao final, quantidade de despesas registradas e total das despesas


despesa = 0
soma = 0
while True:  
    valor = float(input(f'Insira a despesa: R$ '))
    #print (f'Despesa: {despesa}') - isso aqui não faz sentido, porque ele fica maluco e printa a despesa errada.
    despesa += 1 
    soma = soma + valor
    #print (f'SOMA = {soma}')

    resposta = input('\nDeseja continuar [S/N]?').upper()

    if resposta == 'N':
        break
print (f'\nNúmero de despesas: {despesa}')
print (f'Total das despesas: {soma}')


