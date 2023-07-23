'''
Faça um Programa que peça dois números e imprima o maior deles. 
'''

n1 = int(input('Diaga um numero: '))
n2 = int(input('Diaga outro numero: '))

if n1 > n2 :
    print('O numero maior é {}'.format(n1))
elif n1 == n2:
    print('Os números são iguais')
else:
    print('O numero maior é {}'.format(n2))