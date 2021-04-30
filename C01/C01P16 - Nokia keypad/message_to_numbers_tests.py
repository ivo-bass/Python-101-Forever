from unittest import TestCase, main
from message_to_numbers import message_to_numbers


class TestMessageToNumbers(TestCase):
    def test_1(self):
        actual = message_to_numbers("abc")
        expected = [2, -1, 2, 2, -1, 2, 2, 2]
        self.assertEqual(expected, actual)

    def test_2(self):
        actual = message_to_numbers("a")
        expected = [2]
        self.assertEqual(expected, actual)

    def test_3(self):
        actual = message_to_numbers("Ivo e Panda")
        expected = [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
        self.assertEqual(expected, actual)

    def test_4(self):
        actual = message_to_numbers("aabbcc")
        expected = [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
