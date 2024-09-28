from typing import Any

from src.product import Product


class Category:
    """
    Класс описывающий категорию товаров, содержит название категории, описание категории и список продуктов
    """

    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: None | list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, *args: Product) -> None:
        """
        Метод добавляет продукты в категорию
        """
        for arg in args:
            if issubclass(arg.__class__, Product):
                self.__products.append(arg)
            else:
                raise TypeError
            Category.product_count += len(args)

    @property
    def products(self) -> str:
        """
        Метод возвращает список продуктов в категории в виде строки
        """
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return "".join(result)

    @property
    def products_list(self) -> Any:
        """
        Метод возвращает список продуктов в категории в виде списка
        """
        return self.__products
