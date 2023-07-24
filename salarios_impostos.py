'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
Sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
valor_horas = float(input('Diga qual o valor da hora trabalhadas: ').replace(',', '.'))
horas_trab = int(input('Diga quantas horas foram trabalhadas no mês: '))
salario_bruto = valor_horas * horas_trab

imposto_renda = (11 /100) * salario_bruto
pagou_renda = salario_bruto - imposto_renda

inss = (8 / 100) * salario_bruto
pagou_inss = salario_bruto - inss

sind = (5 / 100) * salario_bruto
pagou_inss = salario_bruto - sind

salario_liq = salario_bruto - imposto_renda - inss - sind


print('+ Salário Bruto: \033[32mR${0:.2f}\033[m'.format(salario_bruto))
print('- IR (11%): \033[31mR${0:.2f}\033[m'.format(imposto_renda))
print('- INSS (8%) : \033[31mR${0:.2f}\033[m'.format(inss))
print('- SINDICATO (5%) : \033[31mR${0:.2f}\033[m'.format(sind))
print('= Salário Liquido : \033[32mR${0:.2f}\033[m'.format(salario_liq))





