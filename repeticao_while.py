cardapio = [
    'frango a kiev',
    'filet',
    'bolinho de bacalho',
    'batata frita',
    'camarão',
    'costela ao molho barbecue']

item = cardapio.pop(0)

while item != 'camarão':
    print(f'Esse item não é camarão!! Isso é {item}, Cadê o Camarão?!')
    item = cardapio.pop(0)