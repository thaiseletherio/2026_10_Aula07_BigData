#meta 2000 para cada vendedor
#registrar os valores de venda dos vendedores
#solicitar o valor vendido e calcular o atingimento da meta
# para quando o usuário não quiser mais cadastrar os valores de outro vendedor
#calculo de atingimento: atingimento = (vendas / meta) * 100

# resposta = 'S'
# meta = 2000

# while resposta == 'S':
#     venda = float(input('Quanto você vendeu? '))
#     atingimento = (venda / meta) * 100
#     print (f'Atingimento da meta: {atingimento}')
    
#     resposta = input ('\nVocê quer adicionar outra venda? [S/N] ').upper()


#correção

META = 2000 
vendedor = 1
resposta = 'S'

while resposta == 'S':
    vendas = float(input('\nValor das vendas: '))
    atingimento = (vendas / META) * 100

    print (f'VENDEDOR {vendedor}')
    print(f'Total das vendas R$ {vendas}')
    print(f'Atingimento {atingimento} %')
    vendedor += 1

    resposta = input('\nQuer continuar? [S/N]: ').upper()

print ('Programa encerrado')
