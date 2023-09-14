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
    if i % 2 == 0:
        par.append(i)
        npar +=1
    else:
        impar.append(i)
        nimpar +=1
        
print(f'Os números digitados foram {" ".join(map(str, numeros))}')
print(f'Os números pares digitados são: {" ".join(map(str, par))}')
print(f'Os números ímpares digitados são: {" ".join(map(str, impar))}')