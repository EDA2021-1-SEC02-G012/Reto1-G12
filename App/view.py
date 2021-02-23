"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("\n_______________________________________________________________")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print(
        "2- Conocer cuáles son los n videos con más views que son "
        + " tendencia en un país, dada una categoría específica."
        )
    print(
        "3- Conocer cuál es el video que más días ha sido" +
        " trending para un país específico.")
    print(
        "4- Cuál es el video que más días ha sido" +
        " trending para una categoría específica.")
    print(
        "5- Conocer cuáles son los n videos diferentes con" +
        "más likes en un país con un tag específico.")
    print("0- Salir")


def initCatalog(list_type):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(list_type)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


def listType() -> str:
    print("\n1- Lista tipo ARRAY_LIST")
    print("2- Lista tipo SINGLE_LINKED")
    operating = True

    while operating:
        list_type = int(input(
            'Seleccione el tipo de representación de la lista en memoria: '))

        if list_type == 1:
            adt = 'ARRAY_LIST'
            operating = False
            break
        elif list_type == 2:
            adt = 'SINGLE_LINKED'
            operating = False
            break
        else:
            print("Ingrese un número válido.")

    return adt


def sort_type() -> str:
    print("\n1- Ordenamiento tipo insertionsort")
    print("2- Ordenamiento tipo selectionsort")
    print("3- Ordenamiento tipo shellsort")

    operating = True
    while operating:
        t = int(input(
            'Seleccione el tipo de ordenamiento: '))

        if t == 1:
            sort_type_str = "iss"
            operating = False
            break
        elif t == 2:
            sort_type_str = "ss"
            operating = False
            break
        elif t == 3:
            sort_type_str = "sa"
            operating = False
            break
        else:
            print("Ingrese un número válido.")

    return sort_type_str


def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i = 1
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print(
                'Título: ' + str(video.get('title')) + ", " +
                'Nombre del canal: ' + str(video.get('channel_title')) + ", " +
                'Fue tendencia el día: ' + str(video.get('trending_date'))
                + ", " + 'Visitas: ' + str(video.get('views')) + ", " +
                'Likes: ' + str(video.get('likes')) + ", " +
                'Dislikes: ' + str(video.get('dislikes')))
            i += 1


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        x = listType()
        print("\nCargando información de los archivos ....")
        catalog = initCatalog(x)
        loadData(catalog)

        first = lt.firstElement(catalog['video'])
        primervideo = {
            'Título: ': str(first.get('title')),
            'Nombre del canal: ': str(first.get('channel_title')),
            'Fue tendencia el día: ': str(first.get('trending_date')),
            'Visitas: ': str(first.get('views')),
            'Likes: ': str(first.get('likes')),
            'Dislikes: ': str(first.get('dislikes'))}

        print('\nVideos cargados: ' + str(lt.size(catalog['video'])))
        print('\nDatos del primer video: ')
        for i in primervideo.keys():
            print(str(i) + str(primervideo.get(i)))
        print('\nCategorías cargadas: ' + str(lt.size(catalog['category'])))

    elif int(inputs[0]) == 2:
        size = input("Indique tamaño de la muestra: ")
        sort_type_str = sort_type()
        result = controller.sortVideos(catalog, int(size), sort_type_str)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printResults(result[1])

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
