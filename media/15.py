DOTS = "⠠⠉⠓⠥⠝⠛⠀⠠⠓⠊⠥⠀⠠⠇⠁⠍"

SHAPES = {
    "a": (1,), "b": (1, 2), "c": (1, 4), "d": (1, 4, 5), "e": (1, 5),
    "f": (1, 2, 4), "g": (1, 2, 4, 5), "h": (1, 2, 5), "i": (2, 4),
    "j": (2, 4, 5), "k": (1, 3), "l": (1, 2, 3), "m": (1, 3, 4),
    "n": (1, 3, 4, 5), "o": (1, 3, 5), "p": (1, 2, 3, 4), "q": (1, 2, 3, 4, 5),
    "r": (1, 2, 3, 5), "s": (2, 3, 4), "t": (2, 3, 4, 5), "u": (1, 3, 6),
    "v": (1, 2, 3, 6), "w": (2, 4, 5, 6), "x": (1, 3, 4, 6),
    "y": (1, 3, 4, 5, 6), "z": (1, 3, 5, 6),
}

DOT = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32}

CELLS = {
    chr(0x2800 + sum(DOT[dot] for dot in shape)): letter
    for letter, shape in SHAPES.items()
}

CAPITAL = chr(0x2800 + DOT[6])
BLANK = chr(0x2800)


def read(dots):
    letters = []
    capital = False

    for cell in dots:
        if cell == CAPITAL:
            capital = True
        elif cell == BLANK:
            letters.append(" ")
            capital = False
        else:
            letter = CELLS.get(cell, "?")
            letters.append(letter.upper() if capital else letter)
            capital = False

    return "".join(letters).strip()


print(DOTS)
print(read(DOTS))
