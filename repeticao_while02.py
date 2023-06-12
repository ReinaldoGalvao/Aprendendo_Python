from random import randint

cartas = 0
while cartas < 21:
    cartas += randint(1,10)
    print(f'Você tem {cartas} pontos')