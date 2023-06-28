# Inicializa a variável do maior número com um valor inicial baixo
maior_numero = float('-inf')

# Loop para ler os números
for i in range(5):
    numero = float(input("Digite um número: "))
    
    # Verifica se o número lido é maior que o maior número atual
    if numero > maior_numero:
        maior_numero = numero

# Após ler todos os números, exibe o maior número encontrado
print("O maior número é:", maior_numero)