def crearObjetoJSON():
    titulo = input("Titulo: ")
    descripcion = input("Descripcion: ")
    director = input("Director: ")
    genero = input("Genero: ")
    clasificacion = input("Clasificacion: ")
    idiomas = input("Idiomas: ")
    fechaEstreno = input("Fecha de Estreno: ")
    duracionMinutos = input("Duracion en Minutos: ")
    paisOrigen = input("Pais de Origen: ")

    objetoJSON = {
        "titulo":           titulo,
        "descripcion":      descripcion,
        "director":         director,
        "genero":           genero,
        "clasificacion":    clasificacion,
        "idiomas":          idiomas,
        "fechaEstreno":     fechaEstreno,
        "duracionMinutos":  duracionMinutos,
        "paisOrigen":       paisOrigen
    }
    return objetoJSON

def actualizacionObjetoJSON():
    print("Opciones de actualizacion")
    print("1. Modificar el registro completo")
    print("2. Modificar ciertos valores")

    opcion = input("Ingrese una opcion (1 o 2): ")
    if opcion == "1":
        return crearObjetoJSON()
    elif opcion == "2":
        llave = input("Ingrese el indice a buscar: ")
        valor = input("Ingrese el valor a sustituir: ")
        objetoJSON = {llave: valor}
        return objetoJSON
    else:
        return None