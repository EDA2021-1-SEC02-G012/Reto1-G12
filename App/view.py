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

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

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
        " más likes en un país con un tag específico.")
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
    print("2- Lista tipo LINKED_LIST")
    operating = True

    while operating:
        list_type = int(input(
            'Seleccione el tipo de representación de la lista en memoria: '))

        if list_type == 1:
            adt = 'ARRAY_LIST'
            operating = False
            break
        elif list_type == 2:
            adt = 'LINKED_LIST'
            operating = False
            break
        else:
            print("Ingrese un número válido.")

    return adt


def sort_type() -> str:
    print("\n1- Ordenamiento tipo insertionsort")
    print("2- Ordenamiento tipo selectionsort")
    print("3- Ordenamiento tipo shellsort")
    print("4- Ordenamiento tipo mergesort")
    print("5- Ordenamiento tipo quicksort")

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
        elif t == 4:
            sort_type_str = "ms"
            operating = False
            break
        elif t == 5:
            sort_type_str = "qs"
            operating = False
            break

        else:
            print("Ingrese un número válido.")

    return sort_type_str


def printResults(ord_videos, sample):
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
                'Dislikes: ' + str(video.get('dislikes')) + ", " +
                'Fecha de publicación: ' + str(video.get('dislikes')))
            i += 1


def printResultsv2(ord_videos, sample):
    printlist = []
    i = 1
    while len(printlist) <= (sample - 1):
        element = lt.getElement(ord_videos, i)
        title = str(element.get('title'))
        if title not in printlist:
            printlist.append(title)
            print("\n")
            print(
                'Título: ' + str(element.get('title')) + ", " +
                'Nombre del canal: ' + str(element.get('channel_title'))
                + ", " + 'Visitas: ' + str(element.get('views')) + ", " +
                'Likes: ' + str(element.get('likes')) + ", " +
                'Dislikes: ' + str(element.get('dislikes')) + ", " +
                'Tags: ' + str(element.get('tags')))
        i += 1


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        x = 'ARRAY_LIST'
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
        print('Países cargados: ' + str(lt.size(catalog['country'])))
        lista = ''
        for i in range(0, lt.size(catalog['country'])):
            element = lt.getElement(catalog['country'], i)
            pais = str(element.get('country_name'))
            if i < (lt.size(catalog['country'])-1):
                lista += (pais + ", ")
            else:
                lista += pais
        print(lista)

    elif int(inputs[0]) == 2:
        pais = input("Ingrese el país de referencia: ")
        categoria = int(input('Ingrese la categoría de referencia: '))
        n = int(input("Ingrese el número de videos que desea imprimir: "))

        result1 = controller.getVideosByCategoryAndCountry(
            catalog['country'], categoria, pais)

        result = controller.sortVideos(
            result1, lt.size(result1), 'ms', 'cmpVideosByViews')

        print(
            "Para la muestra de",
            lt.size(catalog['country']),
            "elementos, el tiempo (mseg) es:",
            str(result[0]))

        printResults(result[1], n)

    elif int(inputs[0]) == 3:
        pais = input("Ingrese el país de referencia: ")
        lista = controller.getVideosByCountry(catalog['country'], pais)
        result = controller.sortVideos(
            lista, lt.size(lista), 'ms', 'comparetitles')[1]
        dias_tendencia = controller.getMostTrendingDays(result)
        print(dias_tendencia)

    elif int(inputs[0]) == 4:
        categoria = int(input('Ingrese la categoría de referencia: '))
        result1 = controller.getVideosByCategory(
            catalog['video'], categoria)
        result = controller.sortVideos(
            result1, lt.size(result1), 'ms', 'comparetitles')[1]

        video_tendencia = controller.getMostTrendingDays(result)
        print(video_tendencia)

    elif int(inputs[0]) == 5:
        pais = input("Ingrese el país de referencia: ")
        tag = input('Ingrese el tag de referencia: ')
        n = int(input("Ingrese el número de videos que desea imprimir: "))

        result = controller.getVideosByCountryAndTag(
            catalog['country'], tag, pais)

        print(
            "Para la muestra de",
            lt.size(catalog['country']),
            "elementos, el tiempo (mseg) es:",
            str(result[0]))

        printResultsv2(result[1], n)

    else:
        sys.exit(0)
sys.exit(0)
