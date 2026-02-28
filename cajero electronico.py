def cajero_automatico():
    saldo = 0
    clave = "1234"
    movimientos = []
    print("==== bienvenidos al cajero ==== ")


    while True:
        print("\n--- menu pricipal ---")
        print("1. retiro rapido ")
        print("2. retiro ")
        print("3. consulta saldo ")
        print("4. tranferencia" )
        print("5. gestion de clave")
        print("6. consulta movimientos ")
        print("7. otras operaciones ")
        print("0. salir ")

        option = int(input("seleccione una opcion: "))

        if option == "1":
           monto = 100 
           if saldo >= monto:
              saldo -= monto
              movimientos.append(f"retiro rapido: -${monto}")
              print(f"retiro valido exitoso. Nuevo saldo: -${monto}")

           else:
              print("fondos insuficientes. ")


        elif option == "2":
            try:
                monto = float(input("ingrese monto retirar:" ))
                if monto <= 0:
                   print("monto invalido. ")
                elif monto > saldo:
                    print("fondos insuficientes. ")
                else:
                    saldo -= monto
                    movimientos.append(f"retiro: -${monto}")
                    print(f"retiro exitoso. Nuevo saldo ${saldo}")
            except ValueError:
                print("ingrese un numeor valido. ")

                               

        elif option == "3":
            print(f"saldo actual: ${saldo}")


        elif option == "4":
            try:
                cuenta_destino = int(input("ingrese numero cuenta de destino"))
                monto = float(input("ingrese monto a transferir: "))
                if monto <= 0:
                    print("fondos insuficientes. ")
                else: 
                    saldo -= monto 
                    movimientos.append(f"transferencia a {cuenta_destino}: -${monto}")
                    print(f"transferencia exitosa. Nuevo saldo: ${saldo}")
            except ValueError:
                print("ingrese un numero valido. ")
                        







 




     




 
        
