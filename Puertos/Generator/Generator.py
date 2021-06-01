import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from Nucleo.Clases.libros import libros
from faker import Faker
import random

from pymongo import MongoClient


"""
Atributos de libros:
    - titulo
    - autor
    - anoLanzamiento
    - categoria
    - editorial
    - idioma
    - numPaginas
    - descripcion
"""

cliente = MongoClient()