from typing import Any

import pytest

from src.product import Product


def test_product_1_init(product_1: Product) -> None:
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_2_init(product_2: Product) -> None:
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_product_3_init(product_3: Product) -> None:
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14


def test_product_4_init(product_4: Product) -> None:
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7


def test_product_price(capsys: Any, product_1: Product) -> None:
    product_1.price = 0
    captured_1 = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured_1.out
    assert product_1.price == 180000.0
    product_1.price = -20000
    captured_2 = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured_2.out
    assert product_1.price == 180000.0
    product_1.price = 200000
    assert product_1.price == 200000


def test_new_product() -> None:
    product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str(capsys: Any, product_1: Product) -> None:
    print(product_1)
    captured = capsys.readouterr()
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in captured.out


def test_product_add(product_1: Product, product_2: Product) -> None:
    assert product_1 + product_2 == 2580000.0
    with pytest.raises(TypeError) as exc_info:
        result = product_1 + 1


def test_mro_product(capsys: Any) -> None:
    print(Product.__mro__)
    captured = capsys.readouterr()
    assert (
        "(<class 'src.product.Product'>, <class 'src.product.MixinInfo'>, <class 'src.product.BaseProduct'>, "
        "<class 'abc.ABC'>, <class 'object'>)\n"
    ) in captured


def test_product_zero_quantity() -> None:
    with pytest.raises(ValueError) as exc_info:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_product_negative_quantity() -> None:
    with pytest.raises(ValueError) as exc_info:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, -1)
