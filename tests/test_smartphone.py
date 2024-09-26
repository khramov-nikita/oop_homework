from typing import Any

import pytest

from src.product import Smartphone


def test_smartphone_1_init(smartphone_1: Smartphone) -> None:
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_smartphone_2_init(smartphone_2: Smartphone) -> None:
    assert smartphone_2.name == "Iphone 15"
    assert smartphone_2.description == "512GB, Gray space"
    assert smartphone_2.price == 210000.0
    assert smartphone_2.quantity == 8
    assert smartphone_2.efficiency == 98.2
    assert smartphone_2.model == "15"
    assert smartphone_2.memory == 512
    assert smartphone_2.color == "Gray space"


def test_smartphone_3_init(smartphone_3: Smartphone) -> None:
    assert smartphone_3.name == "Xiaomi Redmi Note 11"
    assert smartphone_3.description == "1024GB, Синий"
    assert smartphone_3.price == 31000.0
    assert smartphone_3.quantity == 14
    assert smartphone_3.efficiency == 90.3
    assert smartphone_3.model == "Note 11"
    assert smartphone_3.memory == 1024
    assert smartphone_3.color == "Синий"


def test_add(smartphone_1: Smartphone, smartphone_2: Smartphone) -> None:
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_add_wrong_type(smartphone_1: Smartphone) -> None:
    with pytest.raises(TypeError) as exc_info:
        result = smartphone_1 + 123


def test_mro_smartphone(capsys: Any) -> None:
    print(Smartphone.__mro__)
    captured = capsys.readouterr()
    assert ("(<class 'src.product.Smartphone'>, <class 'src.product.Product'>, <class 'src.product.MixinInfo'>, "
            "<class 'src.product.BaseProduct'>, <class 'abc.ABC'>, <class 'object'>)\n") in captured
