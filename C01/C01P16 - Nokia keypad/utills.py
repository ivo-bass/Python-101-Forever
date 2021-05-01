class Char:
    def __init__(self, symbol: str, button: int, times_pressed: int):
        self.symbol = symbol
        self.button = button
        self.times_pressed = times_pressed


class Button:
    def __init__(self, *chars):
        self.chars = chars
        self.loop_len = len(self.chars)


class Keyboard:
    CHARS = {
        ' ': Char(' ', 0, 1),
        'a': Char('a', 2, 1),
        'b': Char('b', 2, 2),
        'c': Char('c', 2, 3),
        'd': Char('d', 3, 1),
        'e': Char('e', 3, 2),
        'f': Char('f', 3, 3),
        'g': Char('g', 4, 1),
        'h': Char('h', 4, 2),
        'i': Char('i', 4, 3),
        'j': Char('j', 5, 1),
        'k': Char('k', 5, 2),
        'l': Char('l', 5, 3),
        'm': Char('m', 6, 1),
        'n': Char('n', 6, 2),
        'o': Char('o', 6, 3),
        'p': Char('p', 7, 1),
        'q': Char('q', 7, 2),
        'r': Char('r', 7, 3),
        's': Char('s', 7, 4),
        't': Char('t', 8, 1),
        'u': Char('u', 8, 2),
        'v': Char('v', 8, 3),
        'w': Char('w', 9, 1),
        'x': Char('x', 9, 2),
        'y': Char('y', 9, 3),
        'z': Char('z', 9, 4),
    }

    BUTTONS = {
        0: Button(CHARS[' ']),
        2: Button(CHARS['a'], CHARS['b'], CHARS['c']),
        3: Button(CHARS['d'], CHARS['e'], CHARS['f']),
        4: Button(CHARS['g'], CHARS['h'], CHARS['i']),
        5: Button(CHARS['j'], CHARS['k'], CHARS['l']),
        6: Button(CHARS['m'], CHARS['n'], CHARS['o']),
        7: Button(CHARS['p'], CHARS['q'], CHARS['r'], CHARS['s']),
        8: Button(CHARS['t'], CHARS['u'], CHARS['v']),
        9: Button(CHARS['w'], CHARS['x'], CHARS['y'], CHARS['z']),
    }

    def find_char_by_count_pressing_button(self, number, count):
        for sequence in self.BUTTONS.values():
            for char in sequence.chars:
                if char.button == number and char.times_pressed == count:
                    return char.symbol
