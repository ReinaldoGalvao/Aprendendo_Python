'''
Faça um Programa que leia três números e mostre o maior e o menor deles. 
'''

n1 = int(input('Diga um número: '))
n2 = int(input('Diga outro número: '))
n3 = int(input('Diga mais um número: '))

# Verifica o maior número
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# Verifica o menor número
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Exibe o resultado
print('O número {} é o maior.'.format(maior))
print('O número {} é o menor.'.format(menor))
