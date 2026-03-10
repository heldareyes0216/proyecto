
import os 

nota1 = "desarrollo_software"
nota2 = "habilidades_socioemocionales"
nota3 = "ingles" 

while True:

  os.system("clear")


#validación de modulo(solo numeros)
  while True:
    try:
      modulo = int(input("ingrese el número del modulo: "))
      break
    except ValueError:
          print("Error: ingrese un numero valido.")

  while True:
      nombre = input("ingrese su nombre: ")
      if nombre.isalpha():
        break
      else:
          print("Error: el nombre solo debe tener letras.")


#validación del frente
      def perdir_nota(frente):
          while True:
              try:
                nota = float(input(f"ingrese nota del frente {frente}: "))
                if 0 <= nota <= 100:
                    return nota 
                else:
                    print("error: la nota debe estar entre o - 100.")
              except ValueError:
                print("Error: ingrese un numero valido.") 
                continue   

#pedir las tres notas en un solo bloque 
  nota1 = perdir_nota(1)
  nota2 = perdir_nota(2)
  nota3 = perdir_nota(3)

#sacar el promedio
  promedio = (nota1 * 0.6) + (nota2 * 0.2) + (nota3 * 0.2)

#resultado de notas 
  if promedio <= 49:
   calificacion = "Reprobado"

  elif promedio <= 70: 
   calificacion = "Regular"   

  else:
   calificacion = "excelente"


#resultado 
  print("promedio final:", promedio) 
  print("Calificación:", calificacion)

#alerta
  if nota1 < 50:
      print("Alerta:debe reforzar el frente técnico principal.")

#ver si aprobó o no
  if promedio < 50:
   estado = "No aprobó"
  else:
   estado = "Aprobado" 

#resumen del coder 
  print("\n===== RESUME DEL MODULO =====")
  print("Nombre:", nombre)
  print("Módulo:", modulo)
  print("Nota frente 1:", nota1)
  print("Nota frente 2:", nota2)
  print("Nota frente 3:", nota3)
  print("Promedio:", promedio)
  print("Calificación:", calificacion)
  print("Estado:", estado)    
    
 # Preguntar si quiere registrar otro
  continuar =  input("¿Desea ingresar otro coder? (si/no): ")
  if continuar.lower() == "no":
    break 
