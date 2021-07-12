def verificar(dato):
    while dato == "":
        print("Error")
        dato = input("Ingrese el dato nuevamente: ")
    return dato


def convertir(valor):
    while valor.isdecimal() == False:
        print("Error")
        valor = input("Ingrese valor nuevamente: ")
    return valor

alumnos = {}


while True:
    print("Ingrese el número de la operación que desea ejecutar:")
    print("1 - Añadir un alumno a la lista.")
    print("2 - Ver la lista de alumnos.")
    print("3 - Ver la cantidad de cursos de un alumno.")
    print("4 - Salir.")
   
    opcion = input(">>> ")
    
    if opcion == "1":
        #ingreso del alumno
        nombre_alumno = input("Ingrese el nombre del alumno: ")

        nombre_alumno = verificar(nombre_alumno)
        # Es condición que la cantidad de cursos sea un número entero.
        
        cursos = input("Ingrese la cantidad de cursos: ")
        
        cursos = convertir(cursos)
       
        alumnos[nombre_alumno] = cursos
        print("Has ingresado el alumno correctamente.")
    elif opcion == "2":
        print("Los alumnos:")  
         
        for nombre in alumnos:
            cursos = alumnos[nombre]
            
            print(nombre + " - " + str(cursos) + " cursos")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print(nombre +" tiene "+ str(alumnos[nombre])+" cursos.")
        else:
            print("Ese alumno no tiene cursos asignados")
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        # Forzar el bucle a que termine.
        break
    else:
        print("La opción ingresada no es correcta, vuelva a intentarlo.")
