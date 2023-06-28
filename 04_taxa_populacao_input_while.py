populacaoBrasil = int(input("Digite quantos habitantes o Brasil tem agora: "))
while populacaoBrasil <= 0:
    populacaoBrasil = int(input('A população tem de ser maior que zero, digite novamente: '))

taxaBrasil = int(input('Informe a taxa percentual de crescimento populacional do Brasil: '))
while taxaBrasil <= 0:
    taxaBrasil = int(input('A taxa tem de ser maior que zero, digite novamente: '))
    
populacaoArgentina = int(input("Digite quantos habitantes a Argentina tem agora: "))
while populacaoArgentina <= 0:
    populacaoArgentina = int(input('A população tem de ser maior que zero, digite novamente: '))

taxaArgentina = int(input('Informe a taxa percentual de crescimento populacional do Argentina: '))
while taxaArgentina <= 0:
    taxaArgentina = int(input('A taxa tem de ser maior que zero, digite novamente: '))

while populacaoBrasil < populacaoArgentina:
    populacaoBrasil = int(input(f'A população do Brasil tem que maior a do que a da Argentina que hojé é de {populacaoArgentina}, digite outro numero: '))
    
while taxaBrasil > taxaArgentina:
    taxaArgentina = int(input(f'A taxa populacional da Argentina tem de ser maior que a do Brasil que hoje é de {taxaBrasil}, digite uma taxa maior: '))

#transformando em %
taxaBrasil = taxaBrasil / 100
taxaArgentina = taxaArgentina / 100
anos = 0

while populacaoArgentina < populacaoBrasil:
    populacaoArgentina = populacaoArgentina + populacaoArgentina * taxaArgentina
    populacaoBrasil = populacaoBrasil + populacaoBrasil * taxaBrasil
    anos += 1
    
print(f'A Argentina levara {anos} anos para ultrapassar o Brasil em população!')