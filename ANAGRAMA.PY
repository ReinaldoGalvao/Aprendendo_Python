s = input('Diga a primeira palavra: ').upper()
t = input('Diga a segunda palavra: ').upper()

# Verificar se as strings têm o mesmo tamanho
if len(s) != len(t):
    print("False")
    quit()

# Ordenar as strings e compará-las
if sorted(s) == sorted(t):
    print("As palavras são um anagrama")
else:
    print("As palavras não são um anagrama")
