class libros:
    def __init__(self, titulo:str, autor: str, añoLanzamiento:int, categoria:str, editorial: str, idioma: str, numPaginas: int,  descripcion:str):
        self.titulo = titulo
        self.autor = autor
        self.añoLanzamiento = añoLanzamiento
        self.categoria = categoria
        self.editorial = editorial
        self.idioma = idioma
        self.numPaginas = numPaginas
        self.descripcion = descripcion
    
    def getTitulo(self):
        return self.titulo
    def getAutor(self):
        return self.autor
    def getAñoLanzamiento(self):
        return self.añoLanzamiento
    def getCategoria(self):
        return self.categoria
    def getEditorial(self):
        return self.editorial
    def getIdioma(self):
        return self.idioma
    def getNumPaginas(self):
        return self.numPaginas
    def getDescripcion(self):
        return self.descripcion
            
    def __str__(self) -> str:
        self.cadena = "Título:\n\t{}\n".format(self.titulo)
        self.cadena += "Autor:\n\t{}\n".format(self.autor)
        self.cadena += "Año de lanzamiento:\n\t{}\n".format(self.añoLanzamiento)
        self.cadena += "Categoría:\n\t{}\n".format(self.categoia)
        self.cadena += "Editorial:\n\t{}\n".format(self.editorial)
        self.cadena += "Idioma:\n\t{}\n".format(self.idioma)
        self.cadena += "Número de páginas:\n\t{}\n".format(self.numPaginas)
        self.cadena += "Descripción:\n\t{}\n".format(self.descripcion)
        return self.cadena  
