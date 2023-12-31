def cadastrar(nome_user, senha_user):
    """Função responsável por adicionar um novo usuário ao txt"""
    with open('cadastros.txt', encoding='UTF-8', mode='a') as arquivo:
        arquivo.write(f"{dict(nome = nome_user, senha = senha_user)}\n")           


def entrar(nome_user, senha_user):
    """Função responsável por acessar a conta que já tenha no txt"""
    with open('cadastros.txt', encoding='UTF-8', mode='r') as arquivo:
        for user in arquivo.readlines():
            if nome_user in user and senha_user in user:
                return True
            else:
                return False
