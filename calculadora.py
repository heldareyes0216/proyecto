def sumar(a , b):
    return a + b 

def restar(a , b):
    return a - b 

def multiplicar(a , b):
    return a * b 

def dividir(a , b):
    if b == 0:
     return "error: no se puede dividir entre 0"
    return a / b 

def potencia(a , b):
   return a ** b 

def raiz_cuadrada(a):
   if a < 0: 
    return "error: no se puede sacar raiza cuadrada de un numero negativo"
   return a ** 0.5 

def porcentaje(a , b):
   return (a * b) / 100 

def modulo(a , b):
   if b == 0:
      return "error: no se puede dvidir entre 0"
   return a % b 

def promedio(a , b):
   return (a + b) / 2 

while True:
 print("calculadora en python")
 print("1. sumar")
 print("2. restar")
 print("3. multiplicar")
 print("4. dividir")
 print("5. potencia")
 print("6. raiz cuadrada")
 print("7. porcentaje")
 print("8. modulo")
 print("9. promedio")
 print("0. salir")

 option = input("elegir una opcion del 1-9: ")

 if option == "0":
   print("gracias por usar la calculadora")
   break
 
 try:

    if option == "6":
       a = float(input("ingrese el numero: "))
       print("resultado", raiz_cuadrada(a))

    elif option in ["1","2","3","4","5","7","8","9"]:
       a = float(input("ingrese el primer numero: "))
       b = float(input("ingrese el segundo numero: "))

    if option == "1":
      print("resultado" , sumar(a , b))
    elif option == "2":
     print("resultado" , restar(a , b))
    elif option == "3":
     print("resultado" , multiplicar(a , b))
    elif option == "4":
     print("resultado", dividir(a , b))
    elif option == "5":
     print("resultado" , potencia(a , b))
    elif option == "6":
     print("resultado" , raiz_cuadrada(a))
    elif option == "7":
     print("resultado" , porcentaje(a , b)) 
    elif option == "8":
     print("resultado", modulo(a , b))
    elif option == "9":
     print("resultado", promedio(a, b))

    else:
     print("opcion no valida") 

 except: 
  print("error: debes ingresar numeros validos ")
     
       
   
   

           