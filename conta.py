
class Conta:
    def __init__(self, numero:int, titular:str):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    def depositar(self,valor:float):
        self.__saldo += valor

    def retirar(self, valor:float):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            print('Saldo insuficiente!!')
            return False
    
    def getSaldo(self):
        return self.__saldo


