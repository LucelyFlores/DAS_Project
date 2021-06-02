import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)


from abc import ABC, abstractclassmethod, abstractmethod
from Nucleo.Clases.libros import libros

class Bibliotecario(ABC):
    #listo
    @abstractmethod
    def guardarlibro(self, libro:libros) -> str:
        pass
    #listo
    @abstractmethod
    def checkIfExist(self, libro:libros):
        pass

    #Pendientes
    @abstractmethod
    def guardarMuchosLibros(self, listaLibros:list(libros)) -> str:
        pass
    @abstractmethod
    def libroPorTitulo(self, titulo:str) -> libros:
        pass
    @abstractmethod
    def librosPorAutor(self, autor:str) -> list(libros):
        pass
    @abstractmethod
    def librosPorAno(self,ano:int) -> list(libros):
        pass
    @abstractmethod
    def librosPorIdioma(self,idioma:str) -> list(libros):
        pass
    @abstractmethod
    def librosPorEditorial(self,editorial:str) -> list(libros):
        pass