from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas

    def getPortas(self):
        return self.__portas
    
    def imprimirCarro(self):
        super().imprimir()
        print("Portas: ", str(self.__portas))