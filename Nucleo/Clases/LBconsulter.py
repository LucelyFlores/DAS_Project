from pymongo import MongoClient
from abc import ABC, abstractmethod
from libros import *


class LBConsulter(ABC):

    @abstractmethod
    def getTitulo(self, titulo:str) -> libros:
        pass

    @abstractmethod
    def getAuthor(self, autor:str) -> libros:
        pass


    @abstractmethod
    def getAñoLanzamiento(self, añoLanzamiento:int) -> libros:
        pass

    @abstractmethod
    def getCategoria(self,categoria:str) -> libros:
        pass

