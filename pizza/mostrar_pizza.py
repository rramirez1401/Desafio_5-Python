from pizza.limpiar import limpiar


def mostrar_pizza(pizza:dict):
    print("Tu pizza contiene lo siguiente:\n")
    for k, v in pizza.items():
        if k == "Ingredientes":
            if len(v) == 0:
                print(f"{k}: No has agregado ingredientes!")
            else:
                ingre = ", ".join(v)
                print(f"{k}: {ingre}")
        else:    
            print(f"{k}: {v}")
    

    tiempo = 20 + ((len(pizza["Ingredientes"])) * 2)

    print(f"\nTu pizza estaría lista en {tiempo} minutos\n")

    eleccion = input("1. Confimar el pedido\n2. Volver al menú principal\n")

    if eleccion == "1":
        limpiar()
        print(f"""
Tu pedido estará listo en {tiempo} minutos.
Te esperamos.
Muchas gracias por preferirnos!!!

""")
        exit()

    elif eleccion == "2":
        return
    
    else: 
        limpiar()
        input("Opción inválida. Intenta de nuevo por favor...\nPulsa Enter para continuar")
        limpiar()
