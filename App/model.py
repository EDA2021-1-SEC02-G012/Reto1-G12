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
from DISClib.Algorithms.Sorting import shellsort as sa
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
    catalog = {'videos': None,
               'categories': None,
               }

    catalog['video'] = lt.newList()
    catalog['categories'] = lt.newList('SINGLE_LINKED', cmpfunction=None)
    catalog["channels"] = lt.newList("SINGLE_LINKED", cmpfunction=compare_channel_titles)
    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['video'], video)
    categories = video['category'].split(",")
    # Se obtienen los datos del requerimiento (title, channel_title, 
    # trending_date, country, views, likes, dislikes).
    """
    for video in videos: 

        title = video['title'].split(",")
        channel_title = video['channel_title'].split(",")
        trending_date = video['trending_date'].split(",")
        country = video['country'].split(",")
        country = video['country'].split(",")
        views = video['views'].split(",")
        likes = video['likes'].split(",")
        dislikes = video['dislikes'].split(",")
    """
    for video_name in categories:
        addVideoCategories(catalog, video._namestrip(), video)

def addVideoCategories(catalog, name, video):
    categories = catalog['categories']
    poscategory = lt.isPresent(categories, name)
    if poscategory > 0:
        category = lt.getElement(categories, poscategory)
    else:
        category = newCategories(name)
        lt.addLast(categories, category)
    lt.addLast(category['category'], video)


def addCategory(catalog, category):
    """
    Adiciona una categoría a la lista de categorías
    """
    c = newCategory(category['name'], category['id'])
    lt.addLast(catalog['category'], c)


# Funciones para creacion de datos

def newCategories(name,id):
    """
    Esta estructura almancena las categorías utilizados para marcar libros.
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


def compare_channel_titles(channel_title_name, channel):
    if (channel_title_name.lower() in channel['name'].lower()):
        return 0
    return -1


def compare_likes(video1, video2):
    return (float(video1['likes']) > float(video2['likes']))


def compare_categories(name, categories):
    return (name == video['category'])


# Funciones de ordenamiento
"""
def sortBooks(catalog):
    sa.sort(catalog['books'], compareratings)
"""


# Funciones de ordenamiento
