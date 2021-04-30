from unittest import TestCase, main

from numbers_to_message import numbers_to_message


class TestNumbersToMessage(TestCase):
    def test_1(self):
        actual = numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
        expected = "abc"
        self.assertEqual(expected, actual)

    def test_2(self):
        actual = numbers_to_message([2, 2, 2, 2])
        expected = "a"
        self.assertEqual(expected, actual)

    def test_3(self):
        actual = numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
        expected = "Ivo e Panda"
        self.assertEqual(expected, actual)

    def test__with_empty_sequence__should_return_empty_string(self):
        actual = numbers_to_message([])
        expected = ""
        self.assertEqual(expected, actual)

    def test__with_only_special_buttons__should_return_empty_string(self):
        actual = numbers_to_message([1, -1, 1, -1])
        expected = ""
        self.assertEqual(expected, actual)

    def test__with_2_time_gaps__should_add_next_letter(self):
        actual = numbers_to_message([2, -1, -1, 2])
        expected = "aa"
        self.assertEqual(expected, actual)

    def test__with_2_spaces__should_add_1_space(self):
        actual = numbers_to_message([2, 0, 0, 2])
        expected = "a a"
        self.assertEqual(expected, actual)

    def test__with_capitalize_before_space__should_not_capitalize_next_letter(self):
        actual = numbers_to_message([2, 1, 0, 2])
        expected = "a a"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
