import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from abc import ABC, abstractmethod
from Nucleo.Clases.libros import libros

class Bibliotecario(ABC):
    @abstractmethod
    def guardarLibro(self,libro:libros) -> str:
        pass

    @abstractmethod
    def buscarLibroXNombre(self,nombre:str) -> libros:
        pass

    @abstractmethod
    def buscarLibrosXAutor(self,autor:str) -> libros:
        pass

    @abstractmethod
    def buscarLibrosXAno(self,fecha:int) -> libros:
        pass

    @abstractmethod
    def buscarLibrosXEditorial(self,editorial:str) -> libros:
        pass

    @abstractmethod
    def buscarLibrosXIdioma(self,idioma:str) -> libros:
        pass