'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
letras =  (input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           input('Diga uma letra: ').lower(), 
           )

consoantes = [] #aqui criei uma lista para guardar as consoantes
vogais = []
for p in letras : #criei uma repetição em cima das letras
    if p not in 'aeiou': #criei um if que verifica se a letra digitada nao faz parete de aeiou
        consoantes.append(p) #se atender acima ele dar uma append (adiciona) na lista consoantes
    if p in 'aeiou':#criei um if que verifica se a letra digitada faz parete de aeiou
        vogais.append(p)#se atender acima ele dar uma append (adiciona) na lista vogais
print(f'Foram {len(consoantes)} consoantes digitadas.') #aqui dei um len para contar qts registros tem na lista consoantes
print(f'e foram elas {", ".join(consoantes)}') #aqui o join junta tudo que esta dentro da cosoante separados por uma virgula + espaço
print(f'Foram {len(vogais)} vogais digitadas.') #aqui dei um len para contar qts registros tem na lista consoantes
print(f'e foram elas {", ".join(vogais)}') #aqui o join junta tudo que esta dentro da vogais separados por uma virgula + espaço
