import click
from pizza import delivery_func, bake, pickup, Margherita, Pepperoni, Hawaiian
from menu import Menu


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza')
@click.argument('size')
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza = pizza.capitalize()
    try:
        order_pizza = {
            'Margherita': Margherita(size),
            'Pepperoni': Pepperoni(size),
            'Hawaiian': Hawaiian(size)
        }[pizza]

        if delivery:
            print(
                f'Делаем пиццу {order_pizza.__class__.__name__} с доставкой',
                f'Размера {order_pizza.size}')
            bake(order_pizza)
            delivery_func(pizza)
        else:
            print(
                f'Делаем пиццу {order_pizza.__class__.__name__} на самовывоз',
                f'Размера {order_pizza.size}')
            bake(order_pizza)
            pickup(pizza)
    except KeyError:
        print(f'К сожалению, пиццы {pizza} нет в наличии')


@cli.command
def menu():
    """Выводит меню"""
    for name, (img, size, receipt) in Menu.menu().items():
        print(
            f'{name} {img} sizes({size[0]}, {size[1]}): '
            f'{", ".join(receipt)}'
        )


if __name__ == '__main__':
    cli()
