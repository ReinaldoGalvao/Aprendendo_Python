'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
usando a seguinte fórmula: (72.7*altura) - 58
'''
altura = float(input('Diga a sua altura: ').replace(',','.'))

peso_ideal = (72.7 * altura) - 58

print('Sua peso ideal é {:.2f}'.format(peso_ideal))