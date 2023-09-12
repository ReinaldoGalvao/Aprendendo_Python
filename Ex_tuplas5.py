'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''

numeros = (
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    (int(input('Diga um numero: '))),
    )
par = []
impar = []
npar = 0
nimpar = 0
for i in numeros:
    if i % 2 != 0:
        impar.append(i)
        nimpar +=1
    else:
        par.append(i)
        
print(f'Os números digitados foram {numeros}')
print(f'Os números pares digitados são: {" ".join(map(str, par))}')
print(f'Os números ímpares digitados são: {" ".join(map(str, impar))}')