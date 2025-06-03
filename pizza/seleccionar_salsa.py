from pizza.limpiar import limpiar

def seleccionar_salsa() -> str:
    ## Listado de masas disponibles. Es posible agregar mas si es necesario
    salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]

    while True:
        ## Imprimir menú de salsas
        print("Selecciona una salsa para tu pizza:\n")
        for idx, salsa in enumerate(salsas):
            print(f"{idx + 1}. {salsa}")
        print(f"{len(salsas) + 1}. Volver al menú \n")
        eleccion = input()

        ## Procesamiento de la elección
        try:
            eleccion = int(eleccion)
            if eleccion in range(1, (len(salsas) + 2)):
                if eleccion in range(1, (len(salsas) + 1)):
                    eleccion = salsas[eleccion - 1]
                    return eleccion
                elif eleccion == (len(salsas) + 1):
                    return
            else:
                limpiar()
                input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
                limpiar()
        except ValueError: 
            limpiar()
            input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
            limpiar()



