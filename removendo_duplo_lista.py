lista = ['a', 'b', 'a', 'b', 'c', 'f', 'c']

#nova_lista = set(lista)

# nova_lista = []
# for elemento in lista:
#     if elemento not in nova_lista:
#         nova_lista.append(elemento)

nova_lista = list(dict.fromkeys(lista).keys())

print(nova_lista)