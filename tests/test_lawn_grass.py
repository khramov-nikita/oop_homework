import pytest

from src.product import LawnGrass


def test_grass_1_init(grass_1: LawnGrass) -> None:
    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500.0
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_grass_2_init(grass_2: LawnGrass) -> None:
    assert grass_2.name == "Газонная трава 2"
    assert grass_2.description == "Выносливая трава"
    assert grass_2.price == 450.0
    assert grass_2.quantity == 15
    assert grass_2.country == "США"
    assert grass_2.germination_period == "5 дней"
    assert grass_2.color == "Темно-зеленый"


def test_add(grass_1: LawnGrass, grass_2: LawnGrass) -> None:
    assert grass_1 + grass_2 == 16750.0


def test_add_wrong_type(grass_1: LawnGrass) -> None:
    with pytest.raises(TypeError) as exc_info:
        result = grass_1 + 123
