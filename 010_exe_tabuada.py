#tabuada

"""n1 = int(input('Fale um numero: '))
n2 = 0
print(f'Tabuada de {n1}')
for n2 in range(10):
    n2 += 1
    print(f'{n1} x {n2} = {n1*n2}')
    
"""
   
tabuada=int(input("Tabuada do numero: "))
for count in range(10):
    print("%s x %s = %s" % (tabuada, count+1, tabuada*(count+1)) )