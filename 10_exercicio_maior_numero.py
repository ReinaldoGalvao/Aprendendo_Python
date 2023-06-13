#Receba 3 numeros inteiros e exiba o maior deles

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

if n1 > n2 and n1 > n3: #aqui usei um operador operacional ( < ) e um eperador logico ( and )
    print(f"O numero {n1} é o maior!")

elif n2 > n1 and n2 > n3:
    print(f"O numero {n2} é o maior!")

else:
    print(f"O numero {n3} é o maior!")