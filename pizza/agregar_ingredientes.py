from pizza.limpiar import limpiar


def agregar_ingredientes(seleccion_ingre) -> list:
    ## Listado de ingredientes disponibles. Es posible agregar mas si es necesario
    ingre_dispo = ["Tomate", "Champiñones", "Aceitunas", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]


    while True:
        ## Imprimir menú de ingredientes
        print("Selecciona los ingredientes para tu pizza (No se pueden repetir):\n")
        for idx, ingrediente in enumerate(ingre_dispo):
            print(f"{idx + 1}. {ingrediente}")
        print(f"{len(ingre_dispo) + 1}. Volver al menú \n")
        
        print(f"Tus ingredientes: {seleccion_ingre}")

        eleccion = input()
        
        ## Procesamiento de la elección
        try:
            eleccion = int(eleccion)
            if eleccion in range(1, (len(ingre_dispo) + 2)):
                if eleccion in range(1, (len(ingre_dispo) + 1)):
                    eleccion = ingre_dispo[eleccion - 1]
                    if eleccion in seleccion_ingre:
                        limpiar()
                        input(f"Ya agregaste {eleccion}, no se pueden repetir los ingredientes\nEnter para continuar... ")
                    else:
                        seleccion_ingre.append(eleccion)
                    limpiar()
                    
                elif eleccion == (len(ingre_dispo) + 1):
                    if len(seleccion_ingre) >= 1:
                        return seleccion_ingre
                    else:
                        return
            else:
                limpiar()
                input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
                limpiar()
        except ValueError: 
            limpiar()
            input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
            limpiar()




