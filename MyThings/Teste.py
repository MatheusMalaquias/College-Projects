nomes = []
numeros = []
#Adicione nomes e números e digite "fim" para terminar
print('Escreva fim para terminar')
nome = input('Nome: ')
nomes.append(nome)
numero = input('Número: ')
numeros.append(numero)
print('--------------------')
while nome and numero != 'fim':
    nome = input('Nome: ')
    numero = input('Numero: ')
    print('--------------------')
    if nome and numero != 'fim':
        nomes.append(nome)
        numeros.append(numero)
else:
    print('Os seus contatos são:')
    for nome in nomes:
        print(f'{nome} - {numero}')