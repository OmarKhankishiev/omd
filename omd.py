def step1():
    print(
        'Утка-мяляр 🦆 решила выпить и зайти в бар.'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print(f'Выберите: {"/".join(options)}')
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка-маляр взяла зонтик и отправилась в бар.'
        'На улице было ясно.'
        'А где дождь?!'
    )


def step2_no_umbrella():
    print(
        'Утка-мяляр решила не брать зонтик и отправилась в бар.'
        'На улице было ясно.'
        'Балдеж.'
    )


if __name__ == '__main__':
    step1()
