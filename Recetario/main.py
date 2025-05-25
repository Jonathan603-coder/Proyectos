from funciones import *
from os import system
import pathlib

nombre_usuario = input("Ingrese su nommbre: ")

system("cls")

print(f"!Bienvenido/a a su recetario personal {nombre_usuario}, recuerde que el repertorio de recetas se encuentra en la carpeta \"categorias\"\n")
while True:
    eleccion_usuario = pedir_eleccion()
    if eleccion_usuario == 6:
        system("cls")
        break

    elif eleccion_usuario == 1:
        categorias = lista_categorias()

        categoria_elegida = eleccion_categorias(categorias)

        nombres_recetas,direccion_recetas = lista_recetas(categoria_elegida)

        receta_elegida = eleccion_receta(direccion_recetas,nombres_recetas)

        

        contenido = receta_elegida.read_text(encoding="utf-8")

        print(f"""

{contenido}

""")
        

    elif eleccion_usuario == 2:
        categorias = lista_categorias()
        categoria_elegida = eleccion_categorias(categorias)
        crear_receta(categoria_elegida)



    elif eleccion_usuario == 3:
        crear_categoria()        




    elif eleccion_usuario == 4:
        categorias = lista_categorias()

        categoria_elegida = eleccion_categorias(categorias)

        nombres_recetas,direccion_recetas = lista_recetas(categoria_elegida)

        receta_elegida = eleccion_receta(direccion_recetas,nombres_recetas)

        eliminar_receta(receta_elegida)

        
    
    else:
        categorias = lista_categorias()
        categoria_elegida = eleccion_categorias(categorias)
        eliminar_categoria(categoria_elegida)



print(f"!Espero nos veamos pronto otra vez {nombre_usuario}¡")

