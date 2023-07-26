'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

preco_gasolina = 2.50
preco_alcool = 1.90

litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

if tipo_combustivel == 'A':
    if litros_vendidos <= 20:
        valor_total = litros_vendidos * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_total = litros_vendidos * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel == 'G':
    if litros_vendidos <= 20:
        valor_total = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_total = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.06))
else:
    print("Tipo de combustível inválido.")
    valor_total = 0

print(f"O valor total a ser pago pelo cliente é: R$ {valor_total:.2f}")

