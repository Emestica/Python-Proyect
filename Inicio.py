from Operaciones import *
from Funciones import *

bandera = True

while bandera:
    print("Menu")
    print("1. Guardar el registro de una pelicula")
    print("2. Actualizar el registro de una pelicula")
    print("3. Eliminar el registro de una pelicula")
    print("4. Consultar todas peliculas")
    print("5. Consultar peliculas por fecha de emision")
    print("6. Consultar peliculas por titulo")
    print("7. Salir")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        objetoJSON = crearObjetoJSON()
        crearRegistro(objetoJSON)
    elif opcion == "2":
        id = input("Ingrese el valor del ID: ")
        objetoJSON = actualizacionObjetoJSON()
        if objetoJSON is not None:
            actualizarRegistro(id, objetoJSON)
    elif opcion == "3":
        id = input("Ingrese el valor del ID: ")
        eliminarRegistro(id)
    elif opcion == "4":
        consultarRegistros(None)
    elif opcion == "5":
        print("Funcionalidad En Mantenimiento :D")
    elif opcion == "6":
        print("Funcionalidad En Mantenimiento :D")
    elif opcion == "7":
        bandera=False