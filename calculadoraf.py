# Python Program to convert temperature in fahrenheit to celsius


# Python Program to convert temperature in celsius to fahrenheit
celsius = int(input('Diga a temperatura: '))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32

print('%0.1f graus Celsius é igual a %0.1f graus Fahrenheit' % (celsius,fahrenheit))





fahrenheit = int(input('Diga a temperatura: '))

# calculate celsius
celsius = (fahrenheit - 32) / 1.8

print('%0.1f graus Fahrenheit é igual a %0.1f graus Celsius' % (fahrenheit,celsius))
