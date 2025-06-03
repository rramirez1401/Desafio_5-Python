from pizza.limpiar import limpiar

def eliminar_ingredientes(ingre_actual:list) -> list:

    while True:
        ## Imprimir menú de ingredientes actuales
        print("Selecciona el ingrediente que quieras eliminar de tu pizza:\n")
        for idx, ingrediente in enumerate(ingre_actual):
            print(f"{idx + 1}. {ingrediente}")
        print(f"{len(ingre_actual) + 1}. Volver al menú \n")
        

        eleccion = input()
        
        ## Procesamiento de la elección
        try:
            eleccion = int(eleccion)
            if eleccion in range(1, (len(ingre_actual) + 2)):
                if eleccion in range(1, (len(ingre_actual) + 1)):
                    eleccion -= 1
                    del ingre_actual[eleccion]
                    limpiar()
                    continue
                    
                elif eleccion == (len(ingre_actual) + 1):
                    if len(ingre_actual) >= 1:
                        return ingre_actual
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

    pass