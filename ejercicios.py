
#heladeria 

vainilla = 0 
chocolate = 0
fresa = 0 

for i in range(5):

    sabor = input("Ingrese el sabor que prefiere: ").lower()

    if sabor == "vainilla":
       vainilla += 1
       print("pedido tomado.")

    
    elif sabor == "chocolate":
        chocolate += 1
        print("pedido tomado")

    elif sabor == "fresa":
        fresa += 1
        print("pedido tomado")
    
    else:
        print("Eliga un sabor disponible.")    

print("\n === RESULTADOS ===")
print("vainilla", vainilla)
print("chocolate", chocolate)
print("fresa", fresa)

#gimnasio
edad = int(input("\n ingrese su edad: "))

if edad < 13:
    print("no puede ingresar.")

elif 13 <= edad <= 17:
    print("Pertenece: clase juvenil.")

elif 18 <= edad <= 59:
    print("Pertenece: clase general.")

else:
    print("Pertenece: clase senior.")


#cafetería
café = 4000
té = 3500
jugo = 5000

while True:
    print("=== MENÚ ===")
    print("1. Café $4000")
    print("2. Té $3500")
    print("3. Jugo $5000")

    option = int(input("Seleccione una opción: "))
    cantidad = int(input("¿Cuantos desea?: "))
    
    if option == 1:
        total_pedido = café * cantidad
        print(f"Pedido tomado. Total: {total_pedido}")

    elif option == 2:
        total_pedido = té * cantidad
        print(f"Pedido tomado. Total: {total_pedido}")

    elif option == 3: 
        total_pedido = jugo * cantidad 
        print(f"Pedido tomado. Total: {total_pedido}")

#cine
    edad = int(input("¿Cual es tu edad?: "))

    if edad < 12:
       precio = 8000

    elif 12 <= edad <= 59:
       precio = 12000

    else:
       precio = 9000        
    
    print(f"Total a pagar: {precio}")

#tienda de mascotas 

    mascota = input("¿Qué tipo de mascota tiene?: ").lower()

    if mascota == "perro":
       print("Se recomienda comida balanceada para perros.")

    elif mascota == "gato":
       print("Se recomienda comida para gatos.")

    elif mascota == "conejo":
       print("Se recomienda heno, verduras o comida especial.")    

#parqueadero

    horas = int(input("¿Cuantas horas estuvo en el parqueadero?:"))
    if horas == 1:
        total = 5000

    else:
        total = 5000 + (horas - 1) * 3000

    print(f"Total a pagar: {total}")


#peluquería

    hora = int(input("Ingrese la hora de llegada (0 a 23): "))

    if 6 <= hora <= 11:
        print("El cliente llegó en la mañana")

    elif 12 <= hora <= 17:
        print("El cliente llegó en la tarde")

    elif 18 <= hora <= 22:
        print("El cliente llegó en la noche")
    
    else:
       print("Fuera de horario") 

#tienda deportiva
    contador = 0

    for i in range(6):

       precio = int(input("ingrese el precio del producto: "))
    
       if precio > 100000:
          contador += 1

    print(f"Cantidad de productos que valen mas 100000: {contador}")

#spa

    servicio = input("¿qué servicio desea?: ").lower()

    if servicio == "masaje":
        print("servicio confirmado.")

    elif servicio == "facial":
        print("servicio confirmado.")

    elif servicio == "manicure":
        print("servicio confirmado.")

    else:
        print("no se encuentra disponible") 


#academia de baile 
    asistencia  = int(input("¿cuantas veces asististe a clases este mes?: "))

    if asistencia < 5:
       print("asitencia baja.")

    elif 5 <= asistencia <= 8:
        print("asistencia media.")

    else:
        print("asistencia alta.")  

#heladeria varios clientes
    cono = 3000
    vaso = 4000
    banana_split = 9000

    total_vendido = 0
    cliente = 0

    cont_cono = 0
    cont_vaso = 0
    cont_banana = 0

    while True:
        print("\n=== MENÚ ===")
        print("1. cono $3000")
        print("2. vaso $4000")
        print("3. banana split $9000")

        option = int(input("sleccione una opcion: "))
        cantidad = int(input("que cantidad desea: "))
   

        if option == 1:
           total = cono * cantidad 
           cont_cono =+ cantidad

        elif option == 2:
            total = vaso * cantidad
            cont_vaso =+ cantidad

        elif option == 3:
            total = banana_split * cantidad
            cont_banana =+ cantidad 

        else:
            print("producto no valido")
            continue

        print("Total a pagar:", total)

        total_vendido += total

        cliente += 1

        continuar = input("¿desea ingresar otro cliente (si/no)?: ")
        if continuar.lower() == "no":
           break 

    print("\n=== RESUMEN DEL DÍA ===")
    print("Total vendido:", total_vendido)
    print("Clientes atendidos:", cliente)

    if cont_cono > cont_vaso and cont_cono > cont_banana:
        print("El producto más pedido fue: Cono")
    elif cont_vaso > cont_cono and cont_vaso > cont_banana:
        print("El producto más pedido fue: Vaso")
    else:
        print("El producto más pedido fue: Banana Split") 

#Gimansio rendimiento semanal
    bajo = 0
    medio = 0 
    alto =  0

    for i in range(5):

      cliente = input("Ingrese su nombre: ")

      dias_asistidos = int(input("Ingrese numero de dias asitidos en la semana: "))

      minutos = int(input("Ingrese el promedio de minuto snetrenados a la semana: "))

      if dias_asistidos < 3:
        bajo += 1
        print(cliente, "Bajo compromiso")


      elif 3 <= dias_asistidos <= 4:
        medio += 1
        print(cliente, "Compromiso medio")

      elif 5 <= dias_asistidos:
        alto += 1
        print(cliente, "compromiso alto")

    print("\n === RESULTADOS ===")
    print("Bajo compromiso: ", bajo)
    print("Compromiso medio: ", medio)
    print("Compromiso bajo: ", bajo)  

#cafeteria descuento
    total_dia = 0

    while True:
        print("\n=== CLIENTE NUEVO ===")
        inicio = input("presione 'enter' si desea continuar o escriba 'salir' si desa salir ").lower()
        if inicio == "salir":
           break

        option = ""
    

        while option != "salir":
            print("\n=== MENÚ ===")
            print("1. cafe $4000")
            print("2. capuchino $7000")
            print("3. pastel $6000")
            print("si desea salir digite 'salir'.")

            option = input("Seleccione una opción: ").lower()

            if option == "salir":
               break

            if option == "1":
               precio = 4000
               producto = "cafe"

            elif option == "2":
                precio = 7000
                producto = "capuchino"

            elif option == "3":
                precio = 6000
                producto = "pastel"
   
            else:
                print("Error: ingrese un valor valido")
                continue

            cantidad = int(input("cantidad deseada: "))
            subtotal = precio * cantidad
            total_cliente += subtotal

            print(f"\nsubtotal actual: {total_cliente}")

        if total_cliente > 20000:
           total_cliente *= 0.9
           print("se le aplicó un descuento del 10%")  

        print(f"\ntotal cliente: {total_cliente}")

        total_dia += total_cliente

    
    print("\n===RESUMEN DEL DIA===")
    print(f"\nTOTAL DEL DIA: {total_dia}")   

#cine control sala 
    niños = 0
    adultos = 0 
    adulto_mayor = 0
    cont_ingresos = 0 
    capacidad = 10


    while cont_ingresos < capacidad:
        seguir = input("¿desea ingresar?(si/no): ").lower()

        if seguir == "no":
            break

        edad = int(input("Edad del cliente: "))


        if edad < 18:
            niños += 1
            print("Pertenece al grupo de niños")

        elif 18 <= edad <= 59:
            adultos += 1
            print("Pertenece al grupo de adultos")

        else:
            adulto_mayor += 1
            print("pertenece al grupo de adultos mayores")

        cont_ingresos += 1

        
    print("\n===RESUMEN DEL DIA===")
    print("Personas ingresadas", cont_ingresos)
    print("Total niños", niños)
    print("Total adultos", adultos)
    print("Total adultos mayores", adulto_mayor)

    if cont_ingresos == capacidad:
        print("se llenó")
    else:
        print("no se llenó") 

#tienda de mascostas ventas 
    alimento = 0
    juguete = 0
    accesorio = 0
    cont_categoria = []

    total_alimento = 0
    total_juguete = 0
    total_accesorio = 0

    for i in range(3):

        categoria = input("¿que desea llevar?: ").lower()
        valor_compra = float(input("¿cuanto da su compra?: "))

        if categoria == "alimento":
            alimento += 1 
            total_alimento += valor_compra
            
        elif categoria == "jueguete":
            juguete += 1
            total_juguete += valor_compra
            
        elif categoria == "accesorio":
            accesorio += 1
            total_accesorio += valor_compra
            
        else:
            print("Seleccione una categoria disponible.")

    print("\n=== RESUMEN ===")
    print("ventas por categorias: ", total_alimento)
    print("ventas por categorias: ", total_accesorio)
    print("ventas por categorias: ", total_juguete)

    if total_juguete > total_alimento and total_juguete > total_accesorio:
        print("categoria juguete generó mas dinero")
        
    elif total_alimento > total_accesorio and total_alimento > total_accesorio:
        print("categoria alimento generó mas dinero")

    else:
        print("categoria accesorio generó mas dinero") 


#peluqueria agenda
    total_dia = 0
    cont_corte =  0
    cont_cepillado = 0
    cont_tintura = 0
    cliente_corte =0
    cliente_cepillado = 0
    cliente_tintura = 0

    for i in range(5):

        cliente = input("ingrese su nombre: ")
        servicio = input("ingrese el servcio solicitado(corte, cepillado, tintura): ")
        valor = float(input("ingrese el valor pagado: "))

        if servicio == "corte":
            total_dia += valor
            cont_corte += 1
            cliente_corte += 1

        elif servicio == "cepillado":
            total_dia += valor
            cont_cepillado += 1
            cliente_cepillado += 1

        elif servicio == "tintura":
            total_dia += valor
            cont_tintura += 1
            cliente_tintura += 1

    print("\n=== Resumen ====")
    print("Total del dia:", total_dia)
    print("Cantidad de clientes por corte:", cliente_corte )        
    print("Cantidad de clientes por cepillado:", cliente_cepillado )
    print("Cantidad de clientes por tintura:", cliente_tintura )       

    if cont_tintura > cont_cepillado and cont_tintura > cont_corte:
            print("Servicio mas solicitado: 'tintura' ")
    elif cont_cepillado > cont_corte and cont_cepillado > cont_tintura:
            print("sericio mas solicitado: 'cepillado' ")
    else:
            print("\nservicio mas solicitado: 'corte' ")        