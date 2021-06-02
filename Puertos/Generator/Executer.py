import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from Puertos.Generator.Generator import GeneradorEx
from Puertos.baseDatos.DB import BibliotecarioEx

"""
Aqui se podra modificar cuantos libros se buscan generar
Usar generarUno cuando se trate de pruebas
"""

uno = GeneradorEx().generarUno()
print(uno)
guardar = BibliotecarioEx().guardarLibro(uno)
#muchos = generar.generarMuchos(100)