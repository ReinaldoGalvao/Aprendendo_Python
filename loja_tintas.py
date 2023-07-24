'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

metros_paredes = int(input('Diga em metros o tamanho da parede: '))

total_pint_lata18 = 3 * 18
valor_lata18 = 80

qts_latas = metros_paredes / total_pint_lata18
total_pago = qts_latas * valor_lata18

print('Você usar {0:.2f} latas de tinta.'.format(qts_latas))
print('O valor pago será de R${0:.2f}.'.format(total_pago))
