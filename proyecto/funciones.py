from os import system
import shutil
import pathlib 

def pedir_eleccion():
    while True:


        eleccion = (input("""Elija lo que desea hacer a continuacion:
                         
-----------------[1] Leer Receta
-----------------[2] Crear Receta
-----------------[3] Crear Categoria
-----------------[4] Eliminar Receta
-----------------[5] Eliminar Categoria
-----------------[6] Finalizar Programa
                             
----------------- Su eleccion: """))
        
        if eleccion in ["1","2","3","4","5","6"]:
            break
        else:
            eleccion = (input("""\nPorfavor elija una opcion valida
                             
Elija lo que desea hacer a continuacion:
                             
-----------------[1] Leer Receta
-----------------[2] Crear Receta
-----------------[3] Crear Categoria
-----------------[4] Eliminar Receta
-----------------[5] Eliminar Categoria
-----------------[6] Finalizar Programa
                             
----------------- Su eleccion: """))

       
    system("cls")
            
    return int(eleccion)



def lista_categorias():
    lista = []
    ruta = pathlib.Path("proyecto 6/proyecto/categorias")
    for item in ruta.iterdir():
        lista.append(item.name)
    return lista


def eleccion_categorias(lista):
    
    while True:
        eleccion = input(f"Las categorias disponibles son las siguientes {lista}, ¿cual deseas abrir?: ")
        if eleccion in lista:
            system("cls")
            return eleccion
            
        system("cls")

def lista_recetas(categoria):
    lista_nombres = []
    lista_direcciones = []
    ruta = pathlib.Path("proyecto 6/proyecto/categorias") / categoria

    for item in ruta.iterdir():
        lista_nombres.append(item.stem)
        lista_direcciones.append(item)

    return lista_nombres, lista_direcciones


def eleccion_receta(lista_direcciones,lista_nombres):
    while True:
        eleccion = input(f"Las recetas disponibles son las siguientes {lista_nombres}: ")
        if eleccion in lista_nombres:
            system("cls")
            return lista_direcciones[lista_nombres.index(eleccion)]
        system("cls")


def crear_receta(categoria):    

    ruta = pathlib.Path("proyecto 6/proyecto/categorias") / categoria
    nombre_receta = input("¿Cuál va a ser el nombre de la nueva receta?")

    nuevo_archivo = ruta / f"{nombre_receta}.txt"
    system("cls")
    if nuevo_archivo.exists():
        print("⚠️ Ya existe una receta con ese nombre.")
        return
    else:
        receta = input("Ingrese la receta a continuación:\n")
        nuevo_archivo.write_text(receta, encoding="utf-8")
        print(f"✅ Receta '{nombre_receta}' guardada en la categoría '{categoria}'.")

def crear_categoria():
    nombre = input("Ingrese el nombre de la nueva categoria: ")
    ruta = (pathlib.Path("proyecto 6/proyecto/categorias") / nombre)
    system("cls")
    if ruta.exists():
        print("⚠️ La categoría ya existe.")
    else:
        ruta.mkdir()
        print(f"✅ Categoría '{nombre}' creada correctamente.")


def eliminar_receta(ruta):
    pathlib.Path(ruta).unlink()

def eliminar_categoria(ruta):
    shutil.rmtree(ruta)


    