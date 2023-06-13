#Receba F para feminino e M para masculino e exiba o sexo da pessoa.

sexo =  str(input('Qual seu sexo digite (F) para feminino e (M) para masculino.')).upper() #esse .upper() foi usado para deixar tudo do input em letras maiusculas

if sexo == 'F':
    print('A pessoa é do sexo FEMININO!')
    
elif sexo == 'M':
    print('A pessoa é do sexo MASCULINO!')
    
else:
    print('Escolha uma das 2 opçoes F ou M.')