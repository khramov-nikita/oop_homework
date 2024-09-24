class Product:
    """
    Класс описывающий продукт в магазине, содержит название, описание, цену и количество
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        try:
            result = self.quantity * self.price + other.quantity * other.price
        except TypeError as e:
            raise f'{e}, can not add two non Product objects'
        else:
            return result

    @property
    def to_dict(self):
        return {"name": self.name, "description": self.description, "price": self.__price, "quantity": self.quantity}

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0.0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, kwargs: dict):
        return cls(**kwargs)

