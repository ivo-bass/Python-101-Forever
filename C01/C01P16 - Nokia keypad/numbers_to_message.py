# Using indices as button numbers
KEYBOARD = (
    ' ',     # 0
    '',      # 1
    'abc',   # 2
    'def',   # 3
    'ghi',   # 4
    'jkl',   # 5
    'mno',   # 6
    'pqrs',  # 7
    'tuv',   # 8
    'wxyz',  # 9
)


def numbers_to_message(pressed_sequence):
    msg = []
    times_pressed = 1
    is_next_capitalized = False

    for index, button in enumerate(pressed_sequence):

        if button == -1:
            continue

        if button == 1:
            is_next_capitalized = True
            continue

        if not index == len(pressed_sequence) - 1 \
                and button == pressed_sequence[index + 1]:
            times_pressed += 1
            continue

        letters_in_button = len(KEYBOARD[button])
        letter_index = (times_pressed + letters_in_button - 1) % letters_in_button
        letter = KEYBOARD[button][letter_index]

        if is_next_capitalized:
            letter = letter.upper()
            is_next_capitalized = False

        msg.append(letter)
        times_pressed = 1

    return ''.join(msg)
