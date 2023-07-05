from Veiculo import Veiculo
from Carro import Carro
from Drone import Drone
from Fila import Fila


def menu():
    fila = Fila()
    while True:
        escolha = input(
            """
            ===========================
                       MENU
            ===========================
            1- Adicionar Carro
            2- Adicionar Drone
            3- Remover Carro
            4- Remover Drone
            5- Imprimir Fila de Carros
            6- Imprimir Fila de Drones
            7- Sair
            escolha uma das opções: """
        )
        if escolha == "1":
            print(" ")
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            portas = input("Digite a quantidade de portas do carro: ")
            carro = Carro(marca, modelo, portas)
            fila.addCarro(carro)
            print("------------------------")
            print("Carro adicionado à fila.")
        elif escolha == "2":
            print(" ")
            marca = input("Digite a marca do drone: ")
            modelo = input("Digite o modelo do drone: ")
            qtd_helices = input("Digite a quantidade de hélices do drone: ")
            drone = Drone(marca, modelo, qtd_helices)
            fila.addDrone(drone)
            print("------------------------")
            print("Drone adicionado à fila.")
        elif escolha == "3":
            print(" ")
            fila.removerCarro()
            print("O primeiro carro da fila foi removido!")
        elif escolha == "4":
            print(" ")
            fila.removerDrone()
            print("O primeiro drone da fila foi removido!")
        elif escolha == "5":
            print(" ")
            fila.imprimirCarro()
        elif escolha == "6":
            print(" ")
            fila.imprimirDrone()
        elif escolha == "7":
            print(" ")
            print("Obrigado(a) por utilizar o software!")
            break
        else:
            print(" ")
            print("Opção inválida! Digite uma das opções do menu")