'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima
isto é, considere latas cheias. 
'''
import math

def calcular_quantidade_tinta(area):
    # Considerando 10% de folga
    area_com_folga = area * 1.1
    # Cada litro de tinta cobre 6 metros quadrados
    litros_tinta = area_com_folga / 6
    return litros_tinta

def calcular_preco_latas(litros_tinta):
    # Cada lata possui 18 litros de tinta
    latas = math.ceil(litros_tinta / 18)
    preco_total = latas * 80
    return latas, preco_total

def calcular_preco_galoes(litros_tinta):
    # Cada galão possui 3,6 litros de tinta
    galoes = math.ceil(litros_tinta / 3.6)
    preco_total = galoes * 25
    return galoes, preco_total

def calcular_preco_combinado(litros_tinta):
    # Calcula a combinação de latas e galões que minimize o desperdício
    latas = math.floor(litros_tinta / 18)
    restante = litros_tinta % 18
    galoes = math.ceil(restante / 3.6)
    preco_total = (latas * 80) + (galoes * 25)
    return latas, galoes, preco_total

# Solicita o tamanho da área a ser pintada
area_a_ser_pintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# Calcula a quantidade total de tinta necessária
litros_necessarios = calcular_quantidade_tinta(area_a_ser_pintada)

# Calcula a quantidade e o preço ao comprar apenas latas de 18 litros
latas, preco_latas = calcular_preco_latas(litros_necessarios)

# Calcula a quantidade e o preço ao comprar apenas galões de 3,6 litros
galoes, preco_galoes = calcular_preco_galoes(litros_necessarios)

# Calcula a quantidade e o preço ao combinar latas e galões
latas_combinadas, galoes_combinados, preco_combinado = calcular_preco_combinado(litros_necessarios)

# Exibe os resultados
print(f"\nQuantidade de tinta a ser comprada: {litros_necessarios:.2f} litros")
print(f"\nOpção 1 - Comprar apenas latas de 18 litros:")
print(f"Quantidade de latas: {latas}")
print(f"Preço total: R$ {preco_latas:.2f}")
print(f"\nOpção 2 - Comprar apenas galões de 3,6 litros:")
print(f"Quantidade de galões: {galoes}")
print(f"Preço total: R$ {preco_galoes:.2f}")
print(f"\nOpção 3 - Combinar latas e galões:")
print(f"Quantidade de latas: {latas_combinadas}")
print(f"Quantidade de galões: {galoes_combinados}")
print(f"Preço total: R$ {preco_combinado:.2f}")
