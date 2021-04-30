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


def check_for_capital_letter(numbers, letter):
    if letter.isupper():
        numbers.append(1)
    return letter.lower()


def check_for_duplicate_index(numbers, button_number):
    if numbers and button_number == numbers[-1]:
        numbers.append(-1)


def find_button_and_char_indices(letter):
    btn_i = [KEYBOARD.index(btn_chars) for btn_chars in KEYBOARD if letter in btn_chars][-1]
    char_i = KEYBOARD[btn_i].index(letter)
    times_pressed = char_i + 1
    return btn_i, times_pressed


def message_to_numbers(message):
    numbers = []
    for letter in message:
        letter = check_for_capital_letter(numbers, letter)
        btn_number, times_pressed = find_button_and_char_indices(letter)
        check_for_duplicate_index(numbers, btn_number)
        numbers += [btn_number] * times_pressed
    return numbers
