import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from Puertos.Generator.Generator import GeneradorEx
from Puertos.baseDatos.DB import BibliotecarioEx

"""
Aqui se podra modificar cuantos libros se buscan generar
Usar generarUno cuando se trate de pruebas
"""

muchos = GeneradorEx().generarMuchos(100)
guardar = BibliotecarioEx().guardarMuchosLibros(muchos)