peso_max = 50

peso_pescado = float(input('Diga quantos kilos foram pescado: ').replace(',', '.'))

if peso_max < peso_pescado:
    sobre_peso = peso_pescado - peso_max 
    multa = 4 * sobre_peso
    print('Foram pescado {} e o máximo permitido é de {} então você tera que pagar R$4.00 para cada kilo acima do máximo\nEntão você terá que pagar a multa de R${:.2f}'.format(peso_pescado, peso_max, multa))
