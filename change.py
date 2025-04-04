def change():
    expense = 23.75
    money = 100
    pesos = (money - expense)
    centavos = (float(pesos)-int(pesos))*100
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")
    print("\nVuelto\n")
    print("Pesos:")
    print(int(pesos))
    print("Centavos:")
    print(int(centavos))
change()
