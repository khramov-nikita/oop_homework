from typing import Any
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Базовый класс для продуктов
    """

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class Product(ABC):
    """
    Класс описывающий продукт в магазине, содержит название, описание, цену и количество
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if isinstance(other, self.__class__) and isinstance(self, other.__class__):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError

    # @property
    # def to_dict(self) -> dict:
    #     return {"name": self.name, "description": self.description, "price": self.__price, "quantity": self.quantity}

    @property
    def price(self) -> float:
        """
        Геттер для атрибута 'price'
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для атрибута 'price'
        """
        if new_price <= 0.0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, kwargs: dict) -> Any:
        """
        Метод создаёт новый продукт из словаря
        """
        return cls(**kwargs)


class Smartphone(Product):
    """
    Класс описывает смартфоны
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс описывает газонную траву
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
