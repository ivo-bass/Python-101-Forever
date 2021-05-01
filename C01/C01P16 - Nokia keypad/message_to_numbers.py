from utills import Keyboard


def check_for_capital_letter(numbers, letter):
    if letter.isupper():
        numbers.append(1)
        letter = letter.lower()
    return letter


def check_for_duplicate_number(numbers, button_number):
    if numbers and button_number == numbers[-1]:
        numbers.append(-1)


def message_to_numbers(message):
    keyboard = Keyboard()
    numbers = []
    for letter in message:
        letter = check_for_capital_letter(numbers, letter)
        number = keyboard.CHARS[letter].button
        times_pressed = keyboard.CHARS[letter].times_pressed
        check_for_duplicate_number(numbers, number)
        numbers += [number] * times_pressed
    return numbers
