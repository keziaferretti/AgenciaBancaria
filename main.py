from conta import Conta
from agenciaBancaria import AgenciaBancaria

agencia = AgenciaBancaria(798)

#bjetos Conta
conta1 = Conta(1, "Kézia Ferretti")
conta2 = Conta(2, "Bruno Alves")

#adicionar
agencia.addContas(conta1)
agencia.addContas(conta2)

#deposito
conta1.depositar(300)
conta2.depositar(500)
#saque
conta1.retirar(200)
conta2.retirar(50)

print(agencia.listarContas())
