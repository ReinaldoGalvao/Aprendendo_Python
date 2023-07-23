'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
'''

n1 = float(input('Diga um numero: '))

if n1 > 0 :
    print('O numero {} é positivo.'.format(n1))
elif n1 == 0:
    print('O numero {:.0f} é neutro.'.format(n1))
else:
    print('O numero {} é negativo.'.format(n1))