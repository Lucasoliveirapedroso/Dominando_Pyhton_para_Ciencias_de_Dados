contatos = {
    'Lucas0@gmail.com': {'nome': 'Lucas0', 'telefone': '1111-1111'},
    'Lucas2@gmail.com': {'nome': 'Lucas1', 'telefone': '1111-2222'},
    'Lucas3@gmail.com': {'nome': 'Lucas2', 'telefone': '1111-3333'},
    'Lucas4@gmail.com': {'nome': 'Lucas3', 'telefone': '1111-4444'}
}

for chave in contatos:
    print(chave, contatos[chave])


#metodo correto 

for contato, valor in contatos.items():
    print(contato, valor)