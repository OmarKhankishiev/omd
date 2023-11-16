import random
import time
from typing import Dict, List


class Pizza:
    """
    A base class for representing a pizza.
    """
    ingredients: List[str] = []
    img: str = ''

    def __init__(self, size: str = 'L'):
        """
        Initialize the Pizza.

        Parameters:
        - size: The size of the pizza. Default is 'L'.

        Raises:
        - ValueError: If size is not 'L' or 'XL'.

        Returns:
        None
        """
        if size not in ['L', 'XL']:
            raise ValueError('Доступны только рамеры "L" и "XL"')
        self.name = self.__class__.__name__
        self.size = size
        self.receipt = self.__class__.receipt
        self.img = self.__class__.img

    def __eq__(self, different) -> bool:
        """
        Compare the Pizza with another object.

        Parameters:
        - different: The object to compare with.

        Returns:
        - bool: True if the pizzas are equal, False otherwise.
        """
        if not isinstance(different, Pizza):
            return NotImplemented
        return (
            self.name == different.name and
            sorted(self.receipt) == sorted(different.receipt)
            and self.size == different.size
        )

    def get_receipt(self) -> Dict[str, List[str]]:
        """
        Get the receipt of the pizza.

        Returns:
        - receipt: A dictionary containing the pizza name and its ingredients.
        """
        return {self.name: self.receipt}


class Margherita(Pizza):
    """
    A class representing a Margherita pizza.
    """
    receipt = ["tomato sauce", "mozzarella", "tomatoes"]
    img = "🧀"


class Pepperoni(Pizza):
    """
    A class representing a Pepperoni pizza.
    """
    receipt = ["tomato sauce", "mozzarella", "pepperoni"]
    img = "🍕"


class Hawaiian(Pizza):
    """
    A class representing a Hawaiian pizza.
    """
    receipt = ["tomato sauce", "mozzarella", "chicken", "pineapple"]
    img = "🍍"


def log(message_struc: str):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start_point = time.time()
            result = function(*args, **kwargs)
            end_point = time.time()
            duration = end_point - start_point
            message = f"{message_struc} {duration:.0f} c!"
            print(message)
            return result

        return wrapper

    return decorator


@log('♨️ Готовка заняла')
def bake(pizza: Pizza):
    """Готовит пиццу"""
    time.sleep(random.randint(1, 10))
    pizza_name, receipt = list(pizza.get_receipt().items())[0]
    print(
        f'Заказ {pizza_name} приготовлен\nиз: {", ".join(receipt)}'
    )


@log('🚀 Доставка заняла')
def delivery_func(pizza: str):
    """Доставляет пиццу"""
    time.sleep(random.randint(1, 10))
    print(f'Доставлена пицца {pizza}')


@log('🏰 Доставили за')
def pickup(pizza: str):
    """Самовывоз"""
    time.sleep(random.randint(1, 10))
    print(f'Забрали пиццу {pizza}')
