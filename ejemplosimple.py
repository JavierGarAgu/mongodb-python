from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")  # cliente de mongodb
db = client["rancho"]  # base de datos. Si no existe, se crea automáticamente


coleccion = db["ejemplo1"]  # Coleccion. si no existe, se crea automáticamente


nuevo_documento = {"nombre": "Vaca", "edad": 3,
                   "peso": 450}  # creamos el documento
# Guardamos el id de la creación
resultado = coleccion.insert_one(nuevo_documento)


print(f"Conexión exitosa. Documento insertado con ID: {resultado.inserted_id}")


for doc in coleccion.find():  # Mostramos todos los documentos de la coleccion
    print(doc)
