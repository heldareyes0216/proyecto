
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

print("\n === RESULATDOS ===")
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