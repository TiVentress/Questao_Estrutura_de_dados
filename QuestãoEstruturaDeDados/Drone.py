from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtd_helices):
        super().__init__(marca, modelo)
        self._qtd_helices = qtd_helices

    def getHelices(self):
        return self._qtd_helices

    def imprimirDrone(self):
        super().imprimir()
        print("Quantidade de Hélices: ", self._qtd_helices)