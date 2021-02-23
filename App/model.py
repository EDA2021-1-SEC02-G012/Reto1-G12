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
from DISClib.Algorithms.Sorting import insertionsort as iss
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import shellsort as sa
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

    catalog['video'] = lt.newList(list_type)
    catalog['country'] = lt.newList(list_type)
    catalog['category'] = lt.newList(list_type)
    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['video'], video)
    '''
    countries = video['country'].split(",")
    for video_name in countries:
        addVideoCountry(catalog, video_name.strip(), video)'''


'''
def addVideoCountry(catalog, country_name, video):
    countries = catalog['country']
    poscountry = lt.isPresent(countries, country_name)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(country_name)
        lt.addLast(countries, country)
    lt.addLast(country['video'], video)'''


def addCategory(catalog, categories):
    """
    Adiciona una categoría a la lista de categorías
    """
    c = newCategory(categories['name'], categories['id'])
    lt.addLast(catalog['category'], c)


# Funciones para creacion de datos

'''
def newCountry(country_name):
    """
    Crea una nueva estructura para modelar los videos de
    a partir de los paises title, channel_title, trending_date, country, views,
    likes, dislikes"title": "", "channel_title": "", "trending_date": "",
    "views": 0, "likes": 0, "dislikes": 0
    """
    country = {'country_name': "", "video": None}
    country['country_name'] = country_name
    country['video'] = lt.newList('ARRAY_LIST')
    return country
    '''


def newCategory(name, c_id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    category = {'name': '', 'c_id': ''}
    category['name'] = name
    category['c_id'] = c_id
    return category


# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista


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


def sortVideos(catalog, size, sort_type):
    sub_list = lt.subList(catalog['video'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if sort_type == "iss":
        sorted_list = iss.sort(sub_list, cmpVideosByViews)
    elif sort_type == "ss":
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
    elif sort_type == "sa":
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
