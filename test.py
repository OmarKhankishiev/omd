import pytest
from pizza import delivery_func, bake, pickup, Margherita, Pepperoni, Hawaiian


class TestPizza:

    def test_size(self):
        """
        Test pizza's size
        """
        with pytest.raises(ValueError):
            Pepperoni('XXL')

    def test_diff_pizza(self):
        """
        Test different/same pizzas
        """

        assert Margherita() != Pepperoni()
        assert Pepperoni() == Pepperoni()
        assert Pepperoni('L') != Pepperoni('XL')

    def test_margherita(self):
        """S
        Test Margherita pizza
        """
        margherita = Margherita()
        assert margherita.receipt == [
            'tomato sauce',
            'mozzarella',
            'tomatoes',
        ]

    def test_pepperoni(self):
        """
        Test Pepperoni pizza
        """
        pepperoni = Pepperoni()
        assert pepperoni.receipt == [
            'tomato sauce',
            'mozzarella',
            'pepperoni',
        ]

    def test_hawaiian(self):
        """
        Test Hawaiian pizza
        """
        hawaiian = Hawaiian()
        assert hawaiian.receipt == [
            'tomato sauce',
            'mozzarella',
            'chicken',
            'pineapple'
        ]


class TestDecorators:

    def test_bake(self, capsys):
        """
        Test bake
        """
        pizza = Pepperoni()
        bake(pizza)
        got = capsys.readouterr()
        assert 'Заказ Pepperoni приготовлен' in got.out

    def test_delivery_func(self, capsys):
        """
        Test delivery
        """
        delivery_func('Pepperoni')
        got = capsys.readouterr()
        assert 'Доставлена пицца Pepperoni' in got.out

    def test_pickup(self, capsys):
        """
        Test pickup
        """
        pickup('Pepperoni')
        got = capsys.readouterr()
        assert 'Забрали пиццу Pepperoni' in got.out
