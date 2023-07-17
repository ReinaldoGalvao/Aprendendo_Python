#Receba um numero e mostre todos os numeros pares de 0 ate o numero digitado.
n2 = int(input('Digite um numero: '))

i = 1
while i <= n2:
    if i % 2 == 0:
        print(i)
    i += 1