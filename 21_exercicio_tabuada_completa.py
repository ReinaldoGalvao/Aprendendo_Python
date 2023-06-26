#Mostra a tabuada completa de todos os numeros entre 1 e 10

for i in range(1, 11):
    print(F"======== [TABAUADA {i}] ========")
    for j in range(1, 11):
        print(f"{i} X {j} == {i*j}")