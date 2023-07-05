from Veiculo import Veiculo
from Carro import Carro
from Drone import Drone
from No import No



class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def addCarro(self, carro):
        if self.primeiro == None:
            self.primeiro = No(carro)
            self.ultimo = self.primeiro
        else:
            self.ultimo.proximo = No(carro)
            self.ultimo = No(carro)
        
    def imprimirCarro(self):
        if self.primeiro == None:
            print("A Fila de Carros está vazia!")
        else:
            aux = self.primeiro
            while aux :
                aux.veiculo.imprimirCarro()
                aux = aux.proximo
            
    def removerCarro(self):
        aux = self.primeiro
        if self.primeiro == None:
            print("A Fila de Carros está Vazia!")  
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
        if aux is not None: 
            aux.proximo = None 
        return aux
    
    def addDrone(self, drone):
        if self.primeiro == None:
            self.primeiro = No(drone)
            self.ultimo = self.primeiro
        else:
            self.ultimo.proximo = No(drone)
            self.ultimo = No(drone)
        
    def imprimirDrone(self):
        if self.primeiro == None:
            print("A Fila de Drones está Vazia!")
        else:
            aux = self.primeiro
            while aux :
                aux.veiculo.imprimirDrone()
                aux = aux.proximo
         
    def removerDrone(self):
        aux = self.primeiro
        if self.primeiro == None:
            print("A Fila de Drones está Vazia!")  
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo 
        if aux is not None: 
            aux.proximo = None 
        return aux
    
    