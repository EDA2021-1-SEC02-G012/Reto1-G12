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
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=None)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    videos = lt.addLast(catalog['video'], video)

    # Se obtienen los datos del requerimiento (title, channel_title, 
    # trending_date, country, views, likes, dislikes).
    title = video['title'].split(",")
    channel_title = video['channel_title'].split(",")
    trending_date = video['trending_date'].split(",")
    country = video['country'].split(",")
    country = video['country'].split(",")
    views = video['views'].split(",")
    likes = video['likes'].split(",")
    dislikes = video['dislikes'].split(",")


def addVideoTitle(catalog, title, video):
    titles = catalog['title']
    postitle = lt.isPresent(title, )
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['books'], book)


# Funciones para creacion de datos

def newTitle():
    pass


def newCategory():
    pass


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
""" 
def compareauthors(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1
"""
# Funciones de ordenamiento
