#Defina um usuario e senha depois verifique se o login do usuario é valido
usuario = 'xipos'
senha = '123456'

while True:
    usuarioLogin = input('Digite seu login: ')
    usuarioSenha = input('Digite sua senha: ')
    
    if usuarioLogin == usuario and usuarioSenha == senha:
        print('Você esta logado!!!')
        break
    else:
        print('Você errou tente novamente!!!')
