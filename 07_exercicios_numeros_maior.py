# Inicializa a variável do maior número com um valor inicial baixo
maior_numero = float('-inf')
soma = 0

# Loop para ler os números e calcular a soma
for i in range(5):
    numero = float(input("Digite um número: "))
    
    # Verifica se o número lido é maior que o maior número atual
    if numero > maior_numero:
        maior_numero = numero
    
    soma += numero

# Calcula a média dos números
media = soma / 5

# Exibe o maior número, a soma e a média
print("O maior número é:", maior_numero)
print("A soma dos números é:", soma)
print("A média dos números é:", media)