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

def mensagem(qtd_notas, valor_nota):
    qtd_notas = int(qtd_notas)
    if(qtd_notas == 1):
        if(valor_nota > 1):
            print('     ', int(qtd_notas), ' nota de ', valor_nota, ' reais')
        else:
            print('     ', int(qtd_notas), ' moeda de ', valor_nota, ' real')
    else:
        if(valor_nota > 1):
            print('     ', int(qtd_notas), ' notas de ', valor_nota, ' reais')
        else:
            print('     ', int(qtd_notas), ' moedas de ', valor_nota, ' real')


def numNotas(valor, valor_nota):
    if(valor >= valor_nota):
        notas = valor - (valor%valor_nota)
        notas = notas/valor_nota
        mensagem(notas, valor_nota)
        novo_valor = valor%valor_nota
        return novo_valor
    else:
        return valor


contador = 0
notas = [100,50,20,10,5,2,1]
while(contador < len(lista_de_valores)):
    result = lista_de_valores[contador]
    print('Trocando ', result, ' em:')
    for nota in notas:
        if(result is not None):
            result = numNotas(result, nota)
    contador += 1

print('')
print('################################## FIM ##########################################')
print('')
