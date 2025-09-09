class ContaBancaria:
    def __init__(self, agencia, tipo_conta, saldo,num_conta, pessoa):
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.num_conta = num_conta
        self.saldo =saldo
        self.pessoa = pessoa

    def exibir_dados(self):
        print(f'ficha conta bancaria: agencia: {self.agencia}, tipo de conta: {self.tipo_conta} numero da conta: {self.num_conta} seu saldo: {self.saldo} pessoa: {self.pessoa}.')

    def exibir_saldo(self):
        print(f'saldo: {self.saldo}')

    def exibir_dados_pessoais(self):
        self.pessoa.exibir_dados_pessoais()
