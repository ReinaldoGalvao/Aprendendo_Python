#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    login = input('Login: ')
    senha = input('Senha: ')
    if login == senha:
        print('Login e Senha não pode ser iguais')
        continue
    else:
        break