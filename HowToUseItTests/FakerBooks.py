import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from Nucleo.Clases.libros import libros
from faker import Faker
import random

"""
Atributos de libros:
titulo
autor
anoLanzamiento
categoria
editorial
idioma
numPaginas
descripcion
"""

categorias=['electronica', 'filosofia', 'juvenil', 'Ciencia ficcion']
idiomas=['espanol','ingles','frances','italiano']

fake = Faker()
titulo = fake.sentence(nb_words=5)
autor = fake.name()
anoLanzamiento = fake.year()
categoria = fake.sentence(nb_words=1, ext_word_list=categorias)
editorial = fake.sentence(nb_words=2)
idioma = fake.sentence(nb_words=1, ext_word_list=idiomas)
numPaginas = random.randint(300,600)
descripcion = fake.sentence(nb_words=100)
x = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
print(x)