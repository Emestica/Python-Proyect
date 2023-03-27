import pymongo

cliente =pymongo.MongoClient("mongodb://localhost:27017/")
db = cliente["parcial"]
coleccion = db["peliculas"]