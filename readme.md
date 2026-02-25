# Calculadora en Python

## Descripción

Este proyecto consiste en el desarrollo de una calculadora interactiva en Python que permite realizar múltiples operaciones matemáticas desde la terminal.

La aplicación fue desarrollada aplicando conceptos fundamentales de programación como:

- Funciones
- Condicionales
- Ciclos
- Manejo de errores
- Validación de datos

## Funcionalidades

La calculadora permite realizar las siguientes operaciones:

- Suma  
- Resta  
- Multiplicación  
- División (con validación de división por cero)  
- Potencia  
- Raíz cuadrada (con validación de números negativos)  
- Porcentaje  
- Módulo  
- Promedio  

Además:

- Permanece activa hasta que el usuario decida salir.
- Maneja errores si el usuario ingresa datos no numéricos.


## Conceptos Aplicados

- 'def' para crear funciones.
- 'return' para devolver resultados.
- 'while True' para mantener el programa en ejecución.
- 'if / elif / else' para el control de flujo.
- 'try / except' para el manejo de errores.
- 'float()' para convertir texto en números.


## Explicación del Proceso del Código

1. Se definen funciones independientes para cada operación matemática.
2. Cada función recibe parámetros y devuelve un resultado usando 'return'.
3. Se utiliza un ciclo 'while True' para que la calculadora funcione continuamente.
4. Se muestra un menú de opciones al usuario.
5. El usuario selecciona una opción mediante 'input()'.
6. Se utiliza 'if / elif' para determinar qué operación ejecutar.
7. Se usa 'try / except' para evitar que el programa se detenga si el usuario ingresa valores inválidos.
8. El programa finaliza cuando el usuario selecciona la opción "0".