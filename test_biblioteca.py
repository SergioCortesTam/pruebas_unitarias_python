import pytest
from biblioteca import Libro, Biblioteca

def test_libro_inicializacion():
    libro = Libro("Diseño de Interfaces 2ºDAM", "Ofelia", 2020)
    assert libro.titulo == "Diseño de Interfaces 2ºDAM"
    assert libro.autor == "Ofelia"
    assert libro.anio == 2020
    assert libro.prestado == False

def test_libro_prestado():
    libro = Libro("Judo", "Sergio Cortes", 2019)
    libro.prestado = True
    assert libro.prestado == True

def test_biblioteca_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Futbol", "Carlos", 2018)
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1

def test_biblioteca_eliminar_libro():
    biblioteca = Biblioteca()
    libro1 = Libro("Diseño Interfaces", "Ofelia", 2020)
    libro2 = Libro("Programacion Multimedia", "Alfonso", 2019)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.eliminar_libro("Diseño Interfaces")
    assert len(biblioteca.libros) == 1

def test_biblioteca_buscar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Tenis", "Sergio Cortes", 2018)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.buscar_libro("Tenis")
    assert resultado.titulo == "Tenis"

def test_biblioteca_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("DI", "Ofelia", 2020)
    libro2 = Libro("GitHub", "Carlos", 2019)
    libro3 = Libro("AcesoDatos", "Alfonso", 2018)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    resultado = biblioteca.listar_libros()
    assert len(resultado) == 3

def test_biblioteca_prestar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Tenis de Mesa", "Sergio Cortes", 2019)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.prestar_libro("Tenis de Mesa")
    assert resultado == "Has pedido prestado el libro 'Tenis de Mesa'."

def test_biblioteca_devolver_libro():
    biblioteca = Biblioteca()
    libro = Libro("PSP", "Alfonso", 2018)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("PSP")
    resultado = biblioteca.devolver_libro("PSP")
    assert resultado == "Has devuelto el libro 'PSP'."
