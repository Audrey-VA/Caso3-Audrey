
import pytest
from calculadora import sumar, restar, multiplicar, dividir


def test_suma():
    assert sumar(10, 5) == 15


def test_resta():
    assert restar(10, 5) == 5


def test_multiplicacion():
    assert multiplicar(10, 5) == 50


def test_division():
    assert dividir(10, 5) == 2.0


def test_division_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
