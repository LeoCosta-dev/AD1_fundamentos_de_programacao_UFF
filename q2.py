print('')
print('#################################################################################')
print('------------Questão 2 da AD1-1 de Fundamentos de programação!--------------------')
print('#################################################################################')
print('')

qtd_testes = input('Quantos teste serão realizados? ')
while(not qtd_testes.isnumeric()):
    print('Valor inválido! Esta aplicação aceita apenas números como valor de entrada!')
    qtd_testes = input('Quantos testes serão realizados?')

qtd_valores = input('Quantas entradas de valores terão cada teste? ')
while(not qtd_valores.isnumeric()):
    print('Valor inválido! Esta aplicação aceita apenas números como valor de entrada!')
    qtd_valores = input('Quantas entradas de valores terão cada teste? ')

valor_min = input('Qual será o valor mínimo do intervalo considerado? ')
while(not valor_min.replace('.','',1).isdigit() and not valor_min.isnumeric):
    print('Valor inválido! Esta aplicação aceita apenas números como valor de entrada!')
    valor_min = input('Qual será o valor mínimo do intervalo considerado? ')

valor_max = input('E o valor máximo desse intervalo? ')
while(not valor_max.replace('.','',1).isdigit() and not valor_min.isnumeric):
    print('Valor inválido! Esta aplicação aceita apenas números como valor de entrada!')
    valor_max = input('E o valor máximo desse intervalo? ')

qtd_testes = int(qtd_testes)
qtd_valores = int(qtd_valores)
valor_max = float(valor_max)
valor_min = float(valor_min)

contador_1 = 0

while(contador_1 < qtd_testes):
    lista = []
    contador_2 = 0
    while(contador_2 < qtd_valores):
        valor = input('Digite o {}º valor: '.format(contador_2 + 1))
        if(valor.isnumeric()):
            lista.append(int(valor))
        elif(valor.replace('.','',1).isdigit() or float(valor) < 0):
            lista.append(float(valor))
        else:
            print('Valor inválido! Esta aplicação aceita apenas números como valor de entrada!')
            valor = input('Digite o {}º valor: '.format(contador_2 + 1))
        contador_2 += 1
    
    contador_3 = 0
    soma_interval = 0
    abaixo_interval = 0
    acima_interval = 0
    dentro_interval = 0

    while(contador_3 < len(lista)):
        if(lista[contador_3] < valor_min):
            abaixo_interval += 1
        elif(lista[contador_3] > valor_max):
            acima_interval += 1
        else:
            dentro_interval += 1
            soma_interval += lista[contador_3]
        contador_3 += 1
    print('Teste ', contador_1 + 1)
    print('     intervalo: ', [valor_min, valor_max])
    print('     Abaixo do intervalo: ', abaixo_interval, ', ', 'No intervalo: ', dentro_interval, ',', 'Acima do intervalo: ', acima_interval)
    print('     Soma dos valores dentro do intervalo: ', soma_interval)
    contador_1 += 1

print('')
print('################################## FIM ##########################################')
print('')