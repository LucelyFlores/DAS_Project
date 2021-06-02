import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)


from abc import ABC, abstractclassmethod, abstractmethod
from Nucleo.Clases.libros import libros

class Generador(ABC):
    @abstractmethod
    def generarUno(self) -> libros:
        pass
    @abstractmethod
    def generarMuchos(self, cantidad:int) ->  list:
        pass