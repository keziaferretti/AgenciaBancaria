from conta import Conta

class AgenciaBancaria:
    def __init__(self, codigo:int):
        self.__codigo = codigo
        self.__contas = []
        
    def addContas(self, objConta):
        self.__contas.append(objConta)
    
    def getConta(self, numero:int):
        for conta in self.__contas:
            if conta.getNumero() == numero:
                return conta
        return None
    

    