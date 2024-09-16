from src.category import Category
from src.product import Product


def test_category_init(product_1: Product, product_2: Product, product_3: Product, product_4: Product) -> None:
    category_1 = Category("Смартфоны",
                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для "
                          "удобства жизни", [product_1, product_2, product_3])
    assert category_1.name == "Смартфоны"
    assert category_1.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                      "функций для удобства жизни")
    assert category_1.category_count == 1
    assert category_1.product_count == 3
    category_2 = Category("Телевизоры",
                          "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и "
                          "помощником",
                          [product_4])
    assert category_2.name == "Телевизоры"
    assert category_2.description == ("Современный телевизор, который позволяет наслаждаться просмотром, станет вашим "
                                      "другом и помощником")
    assert category_1.category_count == 2
    assert category_2.category_count == 2
    assert category_2.product_count == 1
