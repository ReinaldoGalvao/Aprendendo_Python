full_name = input('Diga seu nome completo: ')

# Capitalizar o nome completo
capitalized_full_name = ' '.join(word.capitalize() for word in full_name.split())

# Imprimir o nome completo capitalizado
print(capitalized_full_name)
