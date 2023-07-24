'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('Diga a sua altura: ').replace(',','.'))

peso_idealH = (72.7 * altura) - 58
peso_idealM = (62.1 * altura) - 44.7

print('O peso ideal para os homens é de {:.2f}kilos e o peso ideal para as mulheres é de {:.2f} kilos'.format(peso_idealH, peso_idealM))