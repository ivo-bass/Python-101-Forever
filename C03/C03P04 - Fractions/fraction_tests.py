from math import exp
import unittest
from unittest import result

from fraction import Fraction


class DummyFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


class FractionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.numerator = 1
        self.denominator = 2
        self.a = Fraction(self.numerator, self.denominator)
        self.b = Fraction(self.numerator, self.denominator)
        return super().setUp()

    def test_init(self):
        with self.subTest("Valid values"):
            fraction = Fraction(1, 2)
            self.assertEqual(1, fraction.numerator)
            self.assertEqual(2, fraction.denominator)

        with self.subTest("Zero denominator"):
            with self.assertRaises(ValueError):
                Fraction(1, 0)

    def test_string_method(self):
        self.assertEqual(f"{self.numerator}/{self.denominator}", str(self.a))

    def test_repr_method(self):
        self.assertEqual(
            f"Fraction({self.numerator}, {self.denominator})", repr(self.a))

    def test_equality(self):
        with self.subTest("Valid values"):
            c = Fraction(3, 5)
            self.assertEqual(self.a, self.a)

            self.assertEqual(self.a, self.b)
            self.assertEqual(self.b, self.a)

            self.assertNotEqual(self.a, c)
            self.assertNotEqual(c, self.a)

        with self.subTest("Fractions not simplified"):
            c = Fraction(2, 4)

            self.assertEqual(self.a, c)
            self.assertEqual(c, self.a)

        with self.subTest("Different fractions with 0 numerator"):
            c = Fraction(0, 1)
            d = Fraction(0, 2)
            self.assertEqual(c, d)
            self.assertEqual(d, c)

        with self.subTest("Dummy fraction"):
            c = DummyFraction(1, 2)
            with self.assertRaises(TypeError):
                self.a == DummyFraction(1, 2)

    def test_ordering(self):
        with self.subTest("Same denominator"):
            b = Fraction(3, 2)
            self.assertTrue(self.a < b)
            self.assertTrue(b > self.a)
            self.assertFalse(self.a == b)

        with self.subTest("Different denominator"):
            b = Fraction(3, 5)
            self.assertTrue(self.a < b)
            self.assertTrue(b > self.a)
            self.assertFalse(self.a == b)

        with self.subTest("With zero and negative"):
            b = Fraction(0, 5)
            c = Fraction(-1, 2)
            self.assertTrue(b < self.a)
            self.assertTrue(c < self.a)
            self.assertTrue(c < b)

        with self.subTest("Dummy fraction"):
            c = DummyFraction(1, 2)
            with self.assertRaises(TypeError):
                self.a < DummyFraction(1, 2)

        with self.subTest("Sorting"):
            a = Fraction(1, 4)
            b = Fraction(3, 5)
            initial = [b, a]
            expected = [a, b]
            result = sorted(initial)
            self.assertEqual(expected, result)

    def test_addition(self):
        with self.subTest("With same denominator"):
            expected = Fraction(2, 2)
            self.assertEqual(expected, self.a + self.b)
            self.assertEqual(expected, self.b + self.a)

        with self.subTest("With different denominator"):
            b = Fraction(3, 5)
            expected = Fraction(11, 10)
            self.assertEqual(expected, self.a + b)
            self.assertEqual(expected, b + self.a)

        with self.subTest("With negative fraction"):
            b = Fraction(-1, 2)
            expected = Fraction(0, 2)
            self.assertEqual(expected, self.a + b)
            self.assertEqual(expected, b + self.a)

        with self.subTest("With zero"):
            b = Fraction(0, 2)
            expected = Fraction(1, 2)
            self.assertEqual(expected, self.a + b)
            self.assertEqual(expected, b + self.a)

        with self.subTest("Dummy fraction"):
            with self.assertRaises(TypeError):
                self.a + DummyFraction(1, 2)

    def test_substraction(self):
        with self.subTest("With same denominator"):
            expected = Fraction(0, 2)
            self.assertEqual(expected, self.a - self.b)
            expected = Fraction(0, 2)
            self.assertEqual(expected, self.b - self.a)

        with self.subTest("With different denominator"):
            b = Fraction(3, 5)
            expected = Fraction(-1, 10)
            self.assertEqual(expected, self.a - b)
            expected = Fraction(1, 10)
            self.assertEqual(expected, b - self.a)

        with self.subTest("With negative fraction"):
            b = Fraction(-1, 2)
            expected = Fraction(2, 2)
            self.assertEqual(expected, self.a - b)
            expected = Fraction(-2, 2)
            self.assertEqual(expected, b - self.a)

        with self.subTest("With zero"):
            b = Fraction(0, 5)
            expected = Fraction(5, 10)
            self.assertEqual(expected, self.a - b)
            expected = Fraction(-5, 10)
            self.assertEqual(expected, b - self.a)

        with self.subTest("Dummy fraction"):
            with self.assertRaises(TypeError):
                self.a - DummyFraction(1, 2)

    def test_multiplication(self):
        with self.subTest("with_same_fractions"):
            expected = Fraction(1, 4)
            self.assertEqual(expected, self.a * self.b)
            self.assertEqual(expected, self.b * self.a)

        with self.subTest("with_diff_fractions"):
            b = Fraction(3, 5)
            expected = Fraction(3, 10)
            self.assertEqual(expected, self.a * b)
            self.assertEqual(expected, b * self.a)

        with self.subTest("with_one_negative_fraction"):
            b = Fraction(-3, 5)
            expected = Fraction(-3, 10)
            self.assertEqual(expected, self.a * b)
            self.assertEqual(expected, b * self.a)

        with self.subTest("with_two_negative_fractions"):
            a, b = Fraction(-1, 2), Fraction(-3, 5)
            expected = Fraction(3, 10)
            self.assertEqual(expected, a * b)
            self.assertEqual(expected, b * a)

        with self.subTest("Dummy fraction"):
            with self.assertRaises(TypeError):
                self.a * DummyFraction(1, 2)

    def test_simplify(self):
        with self.subTest("with_simple_fraction"):
            self.assertEqual("1/2", str(self.a.simplify()))

        with self.subTest("with_complex_fraction"):
            fr = Fraction(2, 4)
            self.assertEqual("1/2", str(fr.simplify()))
            self.assertEqual("2/4", str(fr))

        with self.subTest("simplify_zero"):
            c = self.a - self.b
            self.assertEqual("0", str(c.simplify()))

    def test_is_simplified(self):
        with self.subTest("when_is_simplified"):
            a = Fraction(1, 2)
            self.assertTrue(a.is_simplified())

        with self.subTest("when is not simplified"):
            b = Fraction(2, 4)
            self.assertFalse(b.is_simplified())

        with self.subTest("test_is_simplified_after_simplification"):
            fr = Fraction(3, 15)
            self.assertTrue(fr.simplify().is_simplified())

        with self.subTest("test_is_simplified_zero"):
            c = Fraction(0, 2)
            self.assertTrue(c.is_simplified())


if __name__ == "__main__":
    unittest.main()
