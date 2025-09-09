class Pessoa:
    def __init__(self, cpf , nome , sobrenome , email, telefone):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.sobrenome = sobrenome


    def exibir_dados_pessoais(self):
        print('===dados pessoais===')
        print(f' cpf : {self.nome}')
        print(f'nome: {self.nome}')
        print(f'email: {self.email}')
        print(f'telefone: {self.telefone}')
        print(f'sobrenome: {self.sobrenome}')
