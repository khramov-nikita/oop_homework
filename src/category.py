from src.product import Product


class Category:
    """
    Класс описывающий категорию товаров, содержит название категории, описание категории и список продуктов
    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: None | list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, *args: Product):
        for arg in args:
            self.__products.append(arg)
        Category.product_count += len(args)

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return "".join(result)

    @property
    def products_list(self):
        return self.__products

