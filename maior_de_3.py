'''
Faça um Programa que leia três números e mostre o maior deles. 
'''
n1 = input('Diga um numero: ')
n2 = input('Diga outro numero: ')
n3 = input('Diga outro numero: ')

if n1 > n2 > n3:
    print('O numero {} é o maior'.format(n1))
elif n2 > n3 > n1:
    print('O numero {} é o maior'.format(n2))
else:
    print('O numero {} é o maior'.format(n3))