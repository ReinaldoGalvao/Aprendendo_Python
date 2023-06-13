#Receba uma temperatura em farenheit e exiba em graus celsius
Fahrenheit = float(input('Fale quantos graus Fahrenheit esta gora: '))

grausC = 5 * ((Fahrenheit - 32)  /9) #calculo para graus Celsios para Fahrenheit - (graus Celsios*1.8)+32

print(f'Agora nesse momento a temperatura em Fahrenheit é {grausC}')