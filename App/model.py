"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog(list_type):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, los videos por país
    y adicionalmente, crea una lista vacia para los categorias.
    """
    catalog = {'video': None,
               'country': None,
               'category': None
               }

    catalog['video'] = lt.newList(list_type, comparevideoid)
    catalog['country'] = lt.newList(list_type, comparecountries)
    catalog['category'] = lt.newList(list_type)
    return catalog


# Funciones para agregar información al catalogo


def addVideo(catalog, video):
    '''
    Adiciona los videos a la lista de videos
    '''
    lt.addLast(catalog['video'], video)

    countries = video['country'].split(",")
    for video_name in countries:
        addVideoCountry(catalog, video_name.strip(), video)


def addVideoCountry(catalog, country_name, video):
    '''
    Adiciona los videos a la lista de países, ordenándolos por país
    '''
    countries = catalog['country']
    poscountry = lt.isPresent(countries, country_name)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(country_name)
        lt.addLast(countries, country)
    lt.addLast(country['video'], video)


def addCategory(catalog, categories):
    """
    Adiciona las categorías a la lista de categorías
    """
    c = newCategory(categories['name'], categories['id'])
    lt.addLast(catalog['category'], c)


# Funciones para creacion de datos


def newCountry(country_name):
    """
    Crea una nueva estructura para modelar los videos de
    a partir de los paises
    """
    country = {'country_name': "", "video": None}
    country['country_name'] = country_name
    country['video'] = lt.newList('ARRAY_LIST')
    return country


def newCategory(name, c_id):
    """
    Esta estructura almancena las categorías utilizadas para marcar videos.
    """
    category = {'name': '', 'c_id': ''}
    category['name'] = name
    category['c_id'] = c_id
    return category


# Funciones de consulta

def getVideosByCategoryAndCountry(catalog, category, country):
    """
    Devuelve una lista de los videos.
    Args:
    catalog: Catálogo de información
    category: Categoría específica
    country: País específico
    """
    sublist = getVideosByCountry(catalog, country)
    sublist2 = getVideosByCategory(sublist, category)
    return sublist2


def getVideosByCountryAndTag(catalog, tag, country):
    """
    Devuelve una lista de los videos.
    Args:
    catalog: Catálogo de información
    tag: Tag específico
    country: País específico
    """
    sublist = getVideosByCountry(catalog, country)
    sublist2 = getVideosByTag(sublist, tag)
    sorted_list = sortVideos(
        sublist2, int(lt.size(sublist2)), 'ms', 'comparelikes')
    return sorted_list


def getVideosByCountry(catalog, country):
    """
    Devuelve una lista de los videos.
    Args:
    catalog: Catálogo de información
    country: País específico
    """
    operating = True
    i = 1
    while operating and i <= lt.size(catalog):
        pais = lt.getElement(catalog, i)
        nombre_pais = pais.get('country_name')
        if nombre_pais == country:
            operating = False
        else:
            i += 1

    return pais['video']


def getVideosByCategory(videos, category):
    """
    Devuelve una lista de los videos.
    Args:
    catalog: Catálogo de información
    category: Categoría específica
    """
    lista = lt.newList('ARRAY_LIST', cmpVideosByViews)
    i = 1
    while i <= lt.size(videos):
        c_id = int(lt.getElement(videos, i).get('category_id'))
        if category == c_id:
            element = lt.getElement(videos, i)
            lt.addLast(lista, element)
        i += 1

    return lista


def getVideosByTag(videos, tag):
    """
    Devuelve una lista de los videos.
    Args:
    catalog: Catálogo de información
    tag: Tag específico
    """
    lista = lt.newList('ARRAY_LIST')
    i = 1

    while i <= lt.size(videos):
        c_tags = lt.getElement(videos, i).get('tags')
        tagpresence = tag in c_tags

        if tagpresence:
            element = lt.getElement(videos, i)
            lt.addLast(lista, element)

        i += 1

    return lista


def VideoMasTrendingCategoria(catalog, categoria):
    """
    Devuelve una lista de los videos.
    Args:
    catalog: Catálogo de información
    categoria: Categoría específica
    """
    sublist = getVideosByCategory(catalog, categoria)
    sorted_list = sortVideos(
        sublist, lt.size(sublist), "ms", "cmpVideosByViews")[1]
    VideoMasTrending = getMostTrendingDaysByTitle(sorted_list)
    return VideoMasTrending


def getMostTrendingDaysByTitle(videos):
    """
    Devuelve una lista de los videos.
    Args:
    videos: Catálogo de información
    """
    elemento = lt.firstElement(videos)
    mayor_titulo = None
    mayor = 0
    i = 0

    for video in lt.iterator(videos):
        if video['video_id'] == elemento['video_id']:
            i += 1
        else:
            if i > mayor:
                mayor_titulo = elemento
                mayor = i
            i = 1
            elemento = video

    if i > mayor:
        mayor_titulo = elemento
        mayor = i
    return (mayor_titulo, mayor)


# Funciones utilizadas para comparar elementos dentro de una lista

def comparevideoid(videoid, video):
    """
    Devuelve verdadero (True) si el ID de video1 es igual al del video2
    Args:
    video1: informacion del primer video que incluye su valor 'ID'
    video2: informacion del segundo video que incluye su valor 'ID'
    """
    return (videoid == video['video_id'])


def cmpVideosByCategory(category1, category2):
    """
    Devuelve verdadero (True) si la 'categoría' de video1 es menor que la
    del video2
    Args:
    video1: informacion del primer video que incluye su valor 'category'
    video2: informacion del segundo video que incluye su valor 'category'
    """
    return (float(category1['category_id']) > float(category2['category_id']))


def comparecountries(country_name, countries):
    """
    Devuelve verdadero (0) si el video se encuentra en el catálogo
    Args:
    country_name: país específico
    countries: catálogo de información
    """
    if (country_name.lower() in countries['country_name'].lower()):
        return 0
    return -1


def comparelikes(video1, video2):
    """
    Devuelve verdadero (True) si los 'likes' del video1 son menores que los
    del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (float(video1['likes'])) > (float(video2['likes']))


def comparetitles(video1, video2):
    """
    Devuelve verdadero (True) si el 'title' de video1 es menor que la
    del video2 (Comparación alfanumérica)
    Args:
    video1: informacion del primer video que incluye su valor 'title'
    video2: informacion del segundo video que incluye su valor 'title'
    """
    return (video1['title']) > (video2['title'])


def cmpVideosByViews(video1, video2) -> bool:
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los
    del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) > float(video2['views']))


# Funciones de ordenamiento


def sortVideos(catalog, size, sort_type, cmp):
    """
    Organiza los videos del catálogo de acuerdo al parámetro establecido
    Args:
    catalog: catálogo de información
    size: tamaño de la muestra
    sort_type: tipo de sorting. Puede ser 'ms': mergesort o 'qs': quicksort.
    cmp: parámetro de comparación
    """
    sub_list = lt.subList(catalog, 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()

    if cmp == 'cmpVideosByViews':
        if sort_type == "ms":
            sorted_list = ms.sort(sub_list, cmpVideosByViews)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, cmpVideosByViews)

    if cmp == 'comparetitles':
        if sort_type == "ms":
            sorted_list = ms.sort(sub_list, comparetitles)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, comparetitles)

    if cmp == 'comparelikes':
        if sort_type == "ms":
            sorted_list = ms.sort(sub_list, comparelikes)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, comparelikes)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
