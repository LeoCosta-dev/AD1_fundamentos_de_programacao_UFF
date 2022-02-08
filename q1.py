print('')
print('#################################################################################')
print('------------Questão 1 da AD1-1 de Fundamentos de programação!--------------------')
print('#################################################################################')
print('')


lista_de_valores = []
numero_digitado = input('Digite o valor: ')

while(numero_digitado != ""):
    if(numero_digitado.isnumeric()):
        numero_inteiro = int(numero_digitado)
        lista_de_valores.append(numero_inteiro)
        numero_digitado = input('Digite o valor: ')
    else:
        print('Digite um valor válido, essa aplicação aceita apenas entradas númericas!')
        numero_digitado = input('Digite o valor: ')

contador = 0
while(contador < len(lista_de_valores)):

    valor = lista_de_valores[contador]
    print('Trocando ', valor, ' em:')

    if(valor >= 100):
        notas_de_cem = valor - (valor%100)
        notas_de_cem = notas_de_cem/100
        if(notas_de_cem == 1):
            print('     ', int(notas_de_cem), ' nota de 100 reais')
        else:
            print('     ', int(notas_de_cem), ' notas de 100 reais')
        valor = valor%100

    if(valor >= 50):
        notas_de_cinquenta = valor - (valor%50)
        notas_de_cinquenta = notas_de_cinquenta/50
        if(notas_de_cinquenta == 1):
            print('     ', int(notas_de_cinquenta), ' nota de 50 reais')
        else:
            print('     ', int(notas_de_cinquenta), ' notas de 50 reais')
        valor = valor%50

    if(valor >= 20):
        notas_de_vinte = valor - (valor%20)
        notas_de_vinte = notas_de_vinte/20
        if(notas_de_vinte == 1):
            print('     ', int(notas_de_vinte), ' nota de 20 reais')
        else:
            print('     ', int(notas_de_vinte), ' notas de 20 reais')
        valor = valor%20

    if(valor >= 10):
        notas_de_dez = valor - (valor%10)
        notas_de_dez = notas_de_dez/10
        if(notas_de_dez == 1):
            print('     ', int(notas_de_dez), ' nota de 10 reais')
        else:
            print('     ', int(notas_de_dez), ' notas de 10 reais')
        valor = valor%10

    if(valor >= 5):
        notas_de_cinco = valor - (valor%5)
        notas_de_cinco = notas_de_cinco/5
        if(notas_de_cinco == 1):
            print('     ', int(notas_de_cinco), ' nota de 5 reais')
        else:
            print('     ', int(notas_de_cinco), ' notas de 5 reais')
        valor = valor%5

    if(valor >= 2):
        notas_de_dois = valor - (valor%2)
        notas_de_dois = notas_de_dois/2
        if(notas_de_dois == 1):
            print('     ', int(notas_de_dois), ' nota de 2 reais')
        else:
            print('     ', int(notas_de_dois), ' notas de 2 reais')
        valor = valor%2

    if(valor >= 1):
        moedas = valor
        if(moedas == 1):
            print('     ', int(moedas), ' moeda de 1 real')
        else:
            print('     ', int(moedas), ' moedas de 1 real')
    contador += 1

print('')
print('################################## FIM ##########################################')
print('')
