import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from Nucleo.Clases.libros import libros
from faker import Faker
import random
from Puertos.baseDatos.DB import BibliotecarioEx
from Interfaces.interfaceGen import Generador


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
class GeneradorEx(Generador):
    def generarUno(self):
        fake = Faker()
        categorias=['electronica', 'filosofia', 'juvenil', 'Ciencia ficcion']
        idiomas=['espanol','ingles','frances','italiano']
        titulo = fake.sentence(nb_words=5)
        autor = fake.name()
        anoLanzamiento = fake.year()
        categoria = fake.sentence(nb_words=1, ext_word_list=categorias)
        editorial = fake.sentence(nb_words=2)
        idioma = fake.sentence(nb_words=1, ext_word_list=idiomas)
        numPaginas = random.randint(300,600)
        descripcion = fake.sentence(nb_words=100)
        return libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)

    def generarMuchos(self,cantidad:int):
        muchos=[]
        fake = Faker()
        for i in range(1,cantidad):
            categorias=['electronica', 'filosofia', 'juvenil', 'Ciencia ficcion']
            idiomas=['espanol','ingles','frances','italiano']
            titulo = fake.sentence(nb_words=5)
            autor = fake.name()
            anoLanzamiento = fake.year()
            categoria = fake.sentence(nb_words=1, ext_word_list=categorias)
            editorial = fake.sentence(nb_words=2)
            idioma = fake.sentence(nb_words=1, ext_word_list=idiomas)
            numPaginas = random.randint(300,600)
            descripcion = fake.sentence(nb_words=100)
            x = libros(titulo,autor,anoLanzamiento,categoria,editorial,idioma,numPaginas,descripcion)
            muchos.append(x)
        return muchos