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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
