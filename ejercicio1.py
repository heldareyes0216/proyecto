cantidad = int(input("¿cuantas personas desea ingresar? "))

for i in range(cantidad):
    print(f"ingresaste {cantidad} persona ")

nombre = input("¿cual es su nommbre? ")    

#validacion edad 
while True:
    try:
        edad = int(input("ingrese su edad "))
        if edad >= 15:
            print("puede seguir adelante ")
            break

        else:
            print("para participar debe ser mayor o tener 15 años")
            break
    except:
        print("error: debe ingresar un numero valido ")

#validacion de conocimientos  
while True:
    try:
        conocimientos = input("¿tiene conocimientos basicos de computcion (si/no)?")
        if conocimientos == "si":
            print("puede seguir adelante ")
            break

        elif conocimientos == "no":
            print("no puede hacer parte del taller ")
            break 

        else:
            print("debe ingresar solo 'si' o 'no' ")

    except:
        print("ha ocurrido  un error ")
    


#conditions 
if edad < 15 or conocimientos == "no":
    print("no cumple los requisitos para partcipar en el taller ")

else:
    print("felicidades puede hacer parter del taller ") 

    print("su proceso ha finalizado. ") 
        



