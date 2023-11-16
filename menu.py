from typing import Dict, Tuple, List


class Menu:
    """
    Pizzeria's menu
    """
    @staticmethod
    def menu() -> Dict[str, Tuple[str, Tuple[str, str], List[str]]]:
        """
        Get the menu of the pizzeria.

        Returns:
        - recipes: A dictionary containing the pizza names as keys
        And their information as values.
        The value is a tuple containing
        The pizza image, available sizes, and ingredients.
        """
        recipes = {
            "Margherita": (
                "🧀",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "tomatoes"],
            ),
            "Pepperoni": (
                "🍕",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "pepperoni"],
            ),
            "Hawaiian": (
                "🍍",
                ("L", "XL"),
                ["tomato sauce", "mozzarella", "chicken", "pineapple"],
            ),
        }
        return recipes
