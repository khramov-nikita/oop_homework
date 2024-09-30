from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """
    Базовый класс для продуктов
    """

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    def price(self) -> None:
        pass


class MixinInfo:
    """
    Класс миксин, который выводит в консоль информацию о том, от какого класса и с какими параметрами был создан объект
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(MixinInfo, BaseProduct):
    """
    Класс описывающий продукт в магазине, содержит название, описание, цену и количество
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        elif quantity < 0:
            raise ValueError("Товар с отрицательным количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

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
