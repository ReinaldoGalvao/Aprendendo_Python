'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = (int(input('Diga a 1ª nota: ')),
         int(input('Diga a 2ª nota: ')),
         int(input('Diga a 3ª nota: ')),
         int(input('Diga a 4ª nota: ')),)

media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4


print(f'A média das 4 notas é {media:.2f}')