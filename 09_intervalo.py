#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

print("Números no intervalo entre", numero1, "e", numero2, ":")

inicio = min(numero1, numero2)
fim = max(numero1, numero2)

soma = 0

for numero in range(inicio, fim + 1):
    print(numero, end=' ')
    soma += numero

print("A soma dos números é:", soma)