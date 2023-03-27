from Conexion import coleccion
from bson import *

def consultarRegistros(id: None):
    if id is None:
        registros = coleccion.find()
        for registro in registros:
            print(registro)
    else:
        query = {"_id": ObjectId(id)}
        registro = coleccion.find_one(query)
        print(registro)

def crearRegistro(objetoJSON):
    resultado = coleccion.insert_one(objetoJSON)
    print(resultado.inserted_id)

def actualizarRegistro(id, objetoJSON):
    query = {"_id": ObjectId(id)}
    valoresNuevos = {"$set": objetoJSON}
    resultado = coleccion.update_one(query, valoresNuevos)
    print(resultado.modified_count)

def eliminarRegistro(id):
    query = {"_id": ObjectId(id)}
    print(query)
    resultado = coleccion.delete_one(query)
    print(resultado.deleted_count)