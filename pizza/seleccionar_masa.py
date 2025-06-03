from pizza.limpiar import limpiar

def seleccionar_masa() -> str:
    ## Listado de masas disponibles. Es posible agregar mas si es necesario
    base = ["Masa tradicional", "Masa delgada", "Masa con bordes de queso"]

    while True:
        ## Imprimir menú de masas
        print("Selecciona la masa para tu pizza:\n")
        for idx, masa in enumerate(base):
            print(f"{idx + 1}. {masa}")
        print(f"{len(base) + 1}. Volver al menú \n")
        eleccion = input()

        ## Procesamiento de la elección
        try:
            eleccion = int(eleccion)
            if eleccion in range(1, (len(base) + 2)):
                if eleccion in range(1, (len(base) + 1)):
                    eleccion = base[eleccion - 1]
                    return eleccion
                elif eleccion == (len(base) + 1):
                    return
            else:
                limpiar()
                input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
                limpiar()
        except ValueError: 
            limpiar()
            input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
            limpiar()



