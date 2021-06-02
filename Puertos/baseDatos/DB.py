import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from pymongo import MongoClient
from Nucleo.Clases.libros import libros
from Interfaces.interfacedb import Bibliotecario


class BibliotecarioEx(Bibliotecario):
    ### ATENCION AQUI: poner el puerto de tu base de mongo
    mongo_client = MongoClient(host="localhost",port=27017)
    db = mongo_client["project"]
    col = db["libros"]
    
    def guardarLibro(self, libro: libros):
        titulo = libro.getTitulo()
        autor = libro.getAutor()
        añoLanzamiento = libro.getAnoLanzamiento()
        categoria = libro.getCategoria()
        editorial = libro.getEditorial()
        idioma = libro.getIdioma()
        numPaginas = libro.getNumPaginas()
        descripcion = libro.getDescripcion()
        dicc = {
            "Titulo" : titulo,
            "Autor" : autor,
            "Año Lanzamiento" : añoLanzamiento,
            "Categoria" : categoria,
            "Editorial" : editorial,
            "Idioma" : idioma,
            "Nummero de Paginas" : numPaginas,
            "Descripcion" : descripcion
        }

        self.col.insert_one(dicc)

    def checkIfExist(self, libro: libros):
        if self.col.count_documents({"Titulo":libro.getTitulo()}, limit = 1) != 0:
            return True
        else:
            return False
        