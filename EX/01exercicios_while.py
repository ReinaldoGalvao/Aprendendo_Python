#Faça um programa que peça uma nota, entre zero e dez
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    
    if nota < 0 or nota > 10:
        print('ta de sacanagem')
        continue
    else:
        print('acertou, mizeravi')
        break

    
    
""""    
while nota < 0 or nota > 10:
    nota = int(input('Ditite uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Ta d+ né cara')
print('Acertou!!!!!!!!!!!!!!!!')
print(f'Parabens, você digitou a nota {nota}')"""