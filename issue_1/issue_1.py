LETTER_TO_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': ' '
}


def encode(message):
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    Примеры:
    >>> encode('SOS') # doctest: +ELLIPSIS
    '... --- ...'

    >>> encode('HLWRLD')
    '.... .-.. .-- .-. .-.. -..'

    >>> encode(-1)
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable

    >>> encode('')
    ''

    >>> encode('ДЗ')
    Traceback (most recent call last):
    KeyError: 'Д'
    """

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)