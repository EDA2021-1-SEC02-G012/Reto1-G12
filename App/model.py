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
# from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los categorias.
    """
    catalog = {'video': None,
               'categories': None,
               'country': None
               }

    catalog['video'] = lt.newList()
    catalog['categories'] = lt.newList('SINGLE_LINKED')
    catalog['country'] = lt.newList('SINGLE_LINKED')
    catalog['c_id'] = lt.newList('SINGLE_LINKED')
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
    lt.addLast(catalog['c_id'], c)


# Funciones para creacion de datos

def newCountry(country_name):
    """
    Crea una nueva estructura para modelar los videos de
    a partir de los paises title, channel_title, trending_date, country, views, likes, dislikes
    "title": "", "channel_title": "", "trending_date": "", "views": 0, "likes": 0, "dislikes": 0
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

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
"""
def sortBooks(catalog):
    sa.sort(catalog['books'], compareratings)
"""


# Funciones de ordenamiento
