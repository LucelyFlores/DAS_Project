from pymongo import MongoClient
from Core.Clases import libros as libro

class MHRecorderGuardador(MHRecorder):
    ### ATENCION AQUI: poner el puerto de tu base de mongo
    mongo_client = MongoClient(host="localhost",port=27017)
    db = mongo_client["project"]
    col = db["libros"]

    def guardarlibro(self, libros: libro):
        titulo = libros.getTitulo()
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
        if self.col.count_documents({"Titulo":libro.getTitulo()}, limit = 1) != 0:
            return True
        else:
            return False

    