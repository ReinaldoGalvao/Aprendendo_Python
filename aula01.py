nota1 = int(input('Qaul a primeira nota: '))
nota2 = int(input('Qual a segunda nota: '))
nota3 = int(input('Qua a terceira nota: '))
nota4 = int(input('Qual a quarta nota: '))
nota5 = int(input('Qual a quinta nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(media)

if media >= 9:
    print(f'Você está aprovado com a media de {media} e mensão SS')
    
elif media > 7 and media < 9 :
    print(f'Você está aprovado com a media de {media} e mensão MS')

elif media > 5 and media < 7 :
    print(f'Você está aprovado com a media de {media} e mensão MM')
    
else:
    print(f'Você está reprovado com a media de {media} e mensão MI')