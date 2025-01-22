from pymongo import MongoClient  # El cliente de MongoDB
from bson.objectid import ObjectId # para tratar los id de los BSON


# obtener base de datos desde la ip de mi server de mongodb en proxmox


def obtener_bd():
    host = "10.6.6.104" #cambiar a localhost o a vuestra ip
    puerto = "27017"
    base_de_datos = "rancho"
    cliente = MongoClient("mongodb://{}:{}".format(host, puerto))
    return cliente[base_de_datos]


# insertar nuevo animal


def insertar(animal):
    base_de_datos = obtener_bd()
    animales = base_de_datos.rancho
    return animales.insert_one(animal).inserted_id


# obtener los animales


def obtener():
    base_de_datos = obtener_bd()
    for x in base_de_datos.rancho.find({}, {"_id": 1, "nombre": 1, "especie": 1}):
        print(x)


# actualizar nombre de un animal por id


def actualizar(id, nombre):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.rancho.update_one(
        {
            '_id': ObjectId(id)
        },
        {
            '$set': {
                "nombre": nombre
            }
        })
    return resultado.modified_count


# eliminar un animal por id


def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.rancho.delete_one(
        {
            '_id': ObjectId(id)
        })
    return resultado.deleted_count


# Menu


menu = """RANCHO
1 - Dar de alta animal
2 - Ver nombre y especie de todos los animales
3 - Actualizar nombre de animal
4 - Eliminar
5 - Salir
"""


eleccion = None


# Mientras la eleccion no sea 5 se seguira repitiendo


while eleccion != 5:
    print(menu)
    eleccion = int(input("Elige: "))
    # Insertar
# Insertar
    if eleccion == 1:
        print("Insertar")
        nombre = input("Nombre del animal: ")
        especie = input("Especie del animal: ")

        # Crear el diccionario del animal
        animal = {
            "nombre": nombre,
            "especie": especie,
        }

        # Pedir más campos opcionales
        while True:
            continuar = input(
                "¿Quieres añadir más campos? (si/no): ").strip().lower()
            if continuar == "no":
                break
            elif continuar == "si":
                nombre_campo = input("Nombre del campo: ").strip()
                valor_campo = input(f"Valor del campo '{
                                    nombre_campo}': ").strip()
                animal[nombre_campo] = valor_campo
            else:
                print("Por favor, responde 'si' o 'no'.")

        # insertar el animal en MongoDB
        id = insertar(animal)
        print("El id del animal insertado es:", id)
    # Listar animal
    elif eleccion == 2:
        print(obtener())
    # actualizar animal
    elif eleccion == 3:
        print("Actualizar")
        id = input("Dime el id: ")
        nombre = input("Nuevo nombre del animal: ")
        animales_actualizados = actualizar(id, nombre)
        print("Número de animales actualizados: ", animales_actualizados)
    # Eliminar animal
    elif eleccion == 4:
        print("Eliminar")
        id = input("Dime el id: ")
        animales_eliminados = eliminar(id)
        print("Número de animales eliminados: ", animales_eliminados)
    # Salir
    elif eleccion == 5:
        print("Adios")
    # Opción incorrecta
    else:
        print("Opción incorrecta")
