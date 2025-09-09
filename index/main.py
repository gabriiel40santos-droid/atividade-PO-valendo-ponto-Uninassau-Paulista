from index import ContaBancaria
from pessoa import Pessoa


cliente = Pessoa('14798969427','bielzao', 'augusto', 'b.A@teste.com', '81989458636' )

conta = ContaBancaria ('banco itau','credito', '837', '10000', cliente)
conta.exibir_saldo()
conta.exibir_dados()
conta.exibir_dados_pessoais()          



