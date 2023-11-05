import pytest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (
            int(b) for b in bin_format.format(1 << len(seen_categories))
        )
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_math():
    assert fit_transform('Python class') == [('Python class', [1])]


@pytest.mark.parametrize(
    'what, result',
    [
        (
            ['Math', 'Python', 'ML', 'Algo', 'Python'],
            [
                ('Math', [0, 0, 0, 1]),
                ('Python', [0, 0, 1, 0]),
                ('ML', [0, 1, 0, 0]),
                ('Algo', [1, 0, 0, 0]),
                ('Python', [0, 0, 1, 0]),
            ],
        ),
        ('Extra subject', [('Extra subject', [1])]),
    ],
)
def test_subjects(what, result):
    assert fit_transform(what) == result


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_extra():
    assert fit_transform('Python class') == [('Python class', [1])]


if __name__ == '__main__':
    pass