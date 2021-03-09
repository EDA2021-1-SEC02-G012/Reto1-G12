﻿"""
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
from DISClib.Algorithms.Sorting import insertionsort as iss
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import shellsort as sa
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
    todos los videos, adicionalmente, crea una lista vacia para los categorias.
    """
    catalog = {'video': None,
               'country': None,
               'category': None
               }

    catalog['video'] = lt.newList(list_type, comparevideoid)
    catalog['country'] = lt.newList(list_type, comparecountries)
    catalog['category'] = lt.newList(list_type)
    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['video'], video)

    countries = video['country'].split(",")
    for video_name in countries:
        addVideoCountry(catalog, video_name.strip(), video)


def addVideoCountry(catalog, country_name, video):
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
    Adiciona una categoría a la lista de categorías
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
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    category = {'name': '', 'c_id': ''}
    category['name'] = name
    category['c_id'] = c_id
    return category


# Funciones de consulta

def getVideosByCountryAndTag(catalog, tag, country):
    sublist = getVideosByCountry(catalog, country)
    sublist2 = getVideosByTag(sublist, tag)
    return sublist2


def getVideosByCategoryAndCountry(catalog, category, country):
    sublist = getVideosByCountry(catalog, country)
    sublist2 = getVideosByCategory(sublist, category)
    return sublist2


def getVideosByCountry(catalog, country):
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
    lista = lt.newList('ARRAY_LIST', cmpVideosByViews)
    titles = lt.newList('ARRAY_LIST')
    i = 1

    while i <= lt.size(videos):
        c_tags = lt.getElement(videos, i).get('tags')'
        lt.addLast(titles, (str(lt.getElement(videos, i).get('title'))))
        if tag in c_tags and lt.isPresent(titles, str(lt.getElement(videos, i).get('title'))) != 0:
            element = lt.getElement(videos, i)
            lt.addLast(lista, element)

        i += 1

    return lista


def VideoMasTrendingCategoria(catalog, categoria):
    sublist = getVideosByCategory(catalog, categoria)
    sorted_list = sortVideos(sublist, lt.size(sublist), "ms", comparevideotitle )
    VideoMasTrending = getMostTrendingDaysByTitle(sorted_list)
    return VideoMasTrending


def getMostTrendingDaysByTitle(videos):
    repetitions = lt.newList('ARRAY_LIST')
    titles = lt.newList('ARRAY_LIST')
    positions = lt.newList('ARRAY_LIST')

    i = 1
    j = 1
    k = 1
    pos = 1
    repetition = 1

    while i <= lt.size(videos):
        video_title = lt.getElement(videos, i).get('title')

        if lt.isPresent(title, video_title) == 0:
            lt.addLast(titles, video_title)
            lt.addLast(positions, i)
            lt.addLast(repetitions, repetition)
            j += 1
            repetition = 1
        else:
            repetition += 1

        i += 1

    while k <= lt.size(repetitions):
        mayor = lt.getElement(repetitions, k)
        k += 1
        if mayor < lt.getElement(repetitions, k):
            mayor = lt.getElement(repetitions, k)
            pos = k

    video_title_max_pos = lt.getElement(positions, k-1)
    video_title_max = lt.getElement(videos, video_title_max_pos)

    return video_title_max


# Funciones utilizadas para comparar elementos dentro de una lista


def comparevideoid(videoid, video):
    return (videoid == video['video_id'])


def comparevideotitle(video_title, videos):
    if (video_title.lower() in videos['title'].lower()):
        return True
    return False


def cmpVideosByCategory(category1, category2):
    return (float(category1['category_id']) > float(category2['category_id']))


def comparecountries(country_name, countries):
    if (country_name.lower() in countries['country_name'].lower()):
        return 0
    return -1


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
    # Podemos remover los ifs
    sub_list = lt.subList(catalog, 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()

    if cmp == 'cmpVideosByViews':
        if sort_type == "iss":
            sorted_list = iss.sort(sub_list, cmpVideosByViews)
        elif sort_type == "ss":
            sorted_list = ss.sort(sub_list, cmpVideosByViews)
        elif sort_type == "sa":
            sorted_list = sa.sort(sub_list, cmpVideosByViews)
        elif sort_type == "ms":
            sorted_list = ms.sort(sub_list, cmpVideosByViews)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, cmpVideosByViews)

    elif cmp == "cmpVideosByCategory":
        if sort_type == "iss":
            sorted_list = iss.sort(sub_list, cmpVideosByCategory)
        elif sort_type == "ss":
            sorted_list = ss.sort(sub_list, cmpVideosByCategory)
        elif sort_type == "sa":
            sorted_list = sa.sort(sub_list, cmpVideosByCategory)
        elif sort_type == "ms":
            sorted_list = ms.sort(sub_list, cmpVideosByCategory)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, cmpVideosByCategory)

    elif cmp == "comparevideoid":
        if sort_type == "iss":
            sorted_list = iss.sort(sub_list, comparevideoid)
        elif sort_type == "ss":
            sorted_list = ss.sort(sub_list, comparevideoid)
        elif sort_type == "sa":
            sorted_list = sa.sort(sub_list, comparevideoid)
        elif sort_type == "ms":
            sorted_list = ms.sort(sub_list, comparevideoid)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, comparevideoid)

    elif cmp == "comparevideotitle":
        if sort_type == "iss":
            sorted_list = iss.sort(sub_list, comparevideotitle)
        elif sort_type == "ss":
            sorted_list = ss.sort(sub_list, comparevideotitle)
        elif sort_type == "sa":
            sorted_list = sa.sort(sub_list, comparevideotitle)
        elif sort_type == "ms":
            sorted_list = ms.sort(sub_list, comparevideotitle)
        elif sort_type == "qs":
            sorted_list = qs.sort(sub_list, comparevideotitle)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
