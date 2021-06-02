from abc import ABC, abstractmethod
from pymongo import MongoClient
import random
from Nucleo.Clases.libros import libros as libro

class Bibliotecario(ABC):
    #listo
    @abstractmethod
    def guardarlibro(self, libro:libros):
        pass
    #listo
    @abstractmethod
    def checkIfExist(self, libro:libros):
        pass