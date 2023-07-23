'''Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo. '''

n1 = int(input('Diga um número: '))
n2 = int(input('Diga outro número: '))
nr3 = float(input('Diga um número real: ').replace(',','.'))
metade2 = n2 / 2
n1x2 = n1 * 2
calculo1 = (2 * n1) * (n2 / 2)
print('o produto do dobro do primeiro é {} com metade do segundo que é {} será de {}.'.format(n1x2, metade2, calculo1))
print('A soma do triplo de {} com {} é {}'.format(n1, nr3, 3*n1+nr3))
print('O número {} elevado ao cubo é {:.2f}'.format(nr3, nr3**2))
