from pizza.menu import menu
from pizza.crear_pizza import crear_pizza
from pizza.limpiar import limpiar
from pizza.seleccionar_masa import seleccionar_masa
from pizza.seleccionar_salsa import seleccionar_salsa
from pizza.agregar_ingredientes import agregar_ingredientes
from pizza.eliminar_ingredientes import eliminar_ingredientes
from pizza.mostrar_pizza import mostrar_pizza

def main():

    ## Crear diccionaio con los elementos de la pizza
    pizza = crear_pizza()
    cont = 0

    while True:
        ## Configuracion para dar mensaje de bienvenida solo al iniciar
        if cont == 0:
            cont += 1
            limpiar()
            print("BIENVENIDO A PIZZAJUT\nArma tu pizza a gusto!!!\n(De forma predefinida la pizza viene con masa tradicional y salsa de tomate)")

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
            limpiar()

        ## Opcion 3: Agregar Ingredientes
        elif opcion == "3":
            limpiar()
            ingre = agregar_ingredientes(pizza["Ingredientes"])
            if ingre != None:
                pizza["Ingredientes"] = ingre
            limpiar()

        ## Opcion 4: Eliminar ingredientes
        elif opcion == "4":
            limpiar()
            if len(pizza["Ingredientes"]) >= 1:
                ingre_actual = eliminar_ingredientes(pizza["Ingredientes"])
                if ingre_actual is None:
                    ingre_actual = []
                pizza["Ingredientes"] = ingre_actual
            else:
                limpiar()
                input("Aún no has agregado ingredientes\nEnter para continuar...")
            limpiar()

        ## Opcion 5: Mostrar la pizza
        elif opcion == "5":
            limpiar()
            mostrar_pizza(pizza)
            limpiar()

        ## Opcion 6: Salir
        elif opcion == "6":
            limpiar()
            print("Vuelve Pronto\n")
            exit()
        else:
            limpiar()
            print("\nOpción no válida, intenta de nuevo por favor.\n")



if __name__ == "__main__":
    main()