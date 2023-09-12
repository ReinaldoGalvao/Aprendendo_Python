'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

numeros = (int(input('Diga um numero: ')),
            int(input('Diga outro numero: ')),
            int(input('Diga mais um numero: ')),
            int(input('Fale um numero: ')),
            int(input('Diga mais uma vez numero: ')),
            int(input('Diga um numero novamente: ')),
            int(input('Diga outro numero: ')),
            int(input('Diga mais um numero: ')),
            int(input('Fale um numero: ')),
            int(input('Diga mais uma vez numero: ')),)

"""i = len(numeros) -1
while i >=0:
    print(numeros[i])
    i -= 1
"""

for i in reversed(numeros):
    print(i, end=' ')