#Receba um numero e exiba se ele é positivo ou negativo.

numero = float(input('Digite um numero: '))

if numero > 0:
    print(f'O numero {numero} é positivo.')
    
elif numero < 0:
    print(f'O numero {numero} é negativo.')
    
elif numero == 0:
    print(f'O numero {numero} é neutro.')
    
'''
no ultimo elif poderia usar só o else: e dar um print

'''