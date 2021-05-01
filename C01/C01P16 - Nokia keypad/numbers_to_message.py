from utills import Keyboard


def numbers_to_message(pressed_sequence):
    keyboard = Keyboard()
    msg = []
    count_pressing = 1
    is_next_capitalized = False

    for index, number in enumerate(pressed_sequence):
        if number == -1:
            continue
        if number == 1:
            is_next_capitalized = True
            continue

        btn = keyboard.BUTTONS[number]

        if index != len(pressed_sequence) - 1 and number == pressed_sequence[index + 1]:
            count_pressing += 1
            if count_pressing > btn.loop_len:
                count_pressing = 1
            continue

        letter = keyboard.find_char_by_count_pressing_button(number, count_pressing)
        if is_next_capitalized:
            letter = letter.upper()
            is_next_capitalized = False
        msg.append(letter)
        count_pressing = 1

    return ''.join(msg)
