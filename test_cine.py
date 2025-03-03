import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("SergioFilm", 10, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para SergioFilm. Total: $40"
    assert pelicula.asientos_disponibles == 5

def test_compra_insuficiente():
    pelicula = Pelicula("CarlosFilm", 3, 10)
    resultado = pelicula.vender_entradas(4)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula.asientos_disponibles == 3

def test_compra_cero_entradas():
    pelicula = Pelicula("OfeliaFilm", 10, 5)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para OfeliaFilm. Total: $0"
    assert pelicula.asientos_disponibles == 10
