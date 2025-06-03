from pizza.menu import menu
from pizza.crear_pizza import crear_pizza
from pizza.limpiar import limpiar
from pizza.seleccionar_masa import seleccionar_masa
from pizza.seleccionar_salsa import seleccionar_salsa


def main():

    ## Crear diccionaio con los elementos de la pizza
    pizza = crear_pizza()
    cont = 0

    while True:
        ## Configuracion para dar mensaje de bienvenida solo al iniciar
        if cont == 0:
            cont += 1
            limpiar()
            print("BIENVENIDO A PIZZAJUT\nArma tu pizza a gusto!!!")

        ## Imprimir Menú
        menu()

        opcion = input("\nQue deseas hacer?\nIngresa el número de tu elección: ")

        ## Opcion 1: Seleccion ded masa
        if opcion == "1":
            limpiar()
            masa = seleccionar_masa()
            if masa != None:
                pizza["Masa"] = masa
            limpiar()
            
        ## Opcion 2: seleccion de salsa
        elif opcion == "2":
            limpiar()
            salsa = seleccionar_salsa()
            if salsa != None:
                pizza["Salsa"] = salsa

        ## Opcion 3: 
        elif opcion == "3":
            print("3")

        elif opcion == "4":
            print("4")

        elif opcion == "5":
            print("5")
        elif opcion == "6":
            exit()
        else:
            limpiar()
            print("\nOpción no válida, intenta de nuevo por favor.\n")



if __name__ == "__main__":
    main()