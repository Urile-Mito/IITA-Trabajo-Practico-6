import json

datos_escuela = {'Alumnos':[{
            'Nombre': 'Juan',
            'Apellido': 'Perez',
            'Fecha de nacimiento': '01/01/2005',
            'DNI': '12345678',
            'Tutor': 'María Rodríguez',
            'Notas': [8, 7, 9],
            'Faltas': 2,
            'Amonestaciones': 1
        },
        {
            'Nombre': 'Ana',
            'Apellido': 'Gomez',
            'Fecha de nacimiento': '05/03/2006',
            'DNI': '87654321',
            'Tutor': 'Luis Fernandez',
            'Notas': [9, 9, 8],
            'Faltas': 0,
            'Amonestaciones': 0
        },{
            'Nombre': 'María',
            'Apellido': 'García',
            'Fecha de nacimiento': '03/07/2004',
            'DNI': '23456789',
            'Tutor': 'Pedro Martínez',
            'Notas': [7, 6, 8],
            'Faltas': 1,
            'Amonestaciones': 0
        },
        {
            'Nombre': 'Carlos',
            'Apellido': 'López',
            'Fecha de nacimiento': '12/11/2005',
            'DNI': '34567890',
            'Tutor': 'Ana Rodríguez',
            'Notas': [8, 9, 7],
            'Faltas': 0,
            'Amonestaciones': 2
        },
        {
            'Nombre': 'Lucía',
            'Apellido': 'Fernández',
            'Fecha de nacimiento': '05/05/2006',
           'DNI': '45678901',
            'Tutor': 'Juan Pérez',
            'Notas': [9, 9, 8],
            'Faltas': 3,
            'Amonestaciones': 1
        }]}

def agregar_alumno(datos_alumnos):
    alumno = {}
    alumno['Nombre'] = input("Ingrese el nombre del alumno: ")
    alumno['Apellido'] = input("Ingrese el apellido del alumno: ")
    alumno['Fecha de nacimiento'] = input("Ingrese la fecha de nacimiento del alumno: ")
    alumno['DNI'] = input("Ingrese el DNI del alumno: ")
    alumno['Tutor'] = input("Ingrese el nombre y apellido del tutor del alumno: ")
    alumno['Notas'] = []
    alumno['Faltas'] = 0
    alumno['Amonestaciones'] = 0
    datos_alumnos['Alumnos'].append(alumno)
    print("Alumno agregado correctamente.")

def mostrar_datos_alumno(alumno):
    print("\nDatos del alumno:")
    for key, value in alumno.items():
        print(f"{key}: {value}")

def mostrar_datos_todos_alumnos(datos_alumnos):
    print("\n--- Datos de todos los alumnos ---")
    for i, alumno in enumerate(datos_alumnos['Alumnos'], 1):
        print(f"Alumno {i}:")
        mostrar_datos_alumno(alumno)

def modificar_datos_alumno(datos_alumnos, dni):
    for alumno in datos_alumnos['Alumnos']:
        if alumno['DNI'] == dni:
            print("\nModificar datos de este alumno:")
            mostrar_datos_alumno(alumno)
            opcion = input("¿Qué dato desea modificar? (Nombre, Apellido, Fecha de nacimiento, DNI, Tutor): ")
            if opcion in alumno:
                nuevo_valor = input(f"Ingrese el nuevo valor para '{opcion}': ")
                alumno[opcion] = nuevo_valor
                print("Datos actualizados correctamente.")
                break
            else:
                print("Dato no válido.")
    else:
        print("No se encontró ningún alumno con ese DNI.")

def expulsar_alumno(datos_alumnos, dni):
    for alumno in datos_alumnos['Alumnos']:
        if alumno['DNI'] == dni:
            datos_alumnos['Alumnos'].remove(alumno)
            print("Alumno expulsado correctamente.")
            break
    else:
        print("No se encontró ningún alumno con ese DNI.")

def programa_escuela(datos_alumnos):
    while True:
        print("\n--- Programa de gestión de escuela ---")
        print("a) Agregar alumno")
        print("b) Mostrar datos de alumno")
        print("c) Mostrar datos de todos los alumnos")
        print("d) Modificar datos de alumno")
        print("e) Expulsar alumno")
        print("f) Salir")
        opcion = input("Ingrese la letra de la opción que desea (o 'f' para salir): ")

        if opcion == 'f':
            print("Saliendo del programa...")
            break

        elif opcion == 'a':
            agregar_alumno(datos_alumnos)

        elif opcion == 'b':
            dni = input("Ingrese el DNI del alumno del que desea ver los datos: ")
            for alumno in datos_alumnos['Alumnos']:
                if alumno['DNI'] == dni:
                    mostrar_datos_alumno(alumno)
                    break
            else:
                print("No se encontró ningún alumno con ese DNI.")

        elif opcion == 'c':
            mostrar_datos_todos_alumnos(datos_alumnos)

        elif opcion == 'd':
            dni = input("Ingrese el DNI del alumno al que desea modificar los datos: ")
            modificar_datos_alumno(datos_alumnos, dni)

        elif opcion == 'e':
            dni = input("Ingrese el DNI del alumno que desea expulsar: ")
            expulsar_alumno(datos_alumnos, dni)

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

programa_escuela(datos_escuela)
