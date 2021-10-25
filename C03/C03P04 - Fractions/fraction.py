from math import gcd, lcm


class Fraction:
    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.
        If denominator = 0, raise ValueError.
        """
        if denominator == 0:
            raise ValueError
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """
        Returns the string representation of self.
        """
        if self.numerator == 0:
            return "0"
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        self.__validate_type(other)
        self_gcd = gcd(self.numerator, self.denominator)
        other_gcd = gcd(other.numerator, other.denominator)
        return (self.numerator // self_gcd == other.numerator // other_gcd
                and
                self.denominator // self_gcd == other.denominator // other_gcd
                )

    def __lt__(self, other):
        """
        Returns if self < other
        """
        self.__validate_type(other)
        new_denominator = lcm(self.denominator, other.denominator)
        a_x = new_denominator // self.denominator
        b_x = new_denominator // other.denominator
        return self.numerator * a_x < other.numerator * b_x

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        self.__validate_type(other)
        new_denominator = lcm(self.denominator, other.denominator)
        a_x = new_denominator // self.denominator
        b_x = new_denominator // other.denominator
        a_num = self.numerator * a_x
        b_num = other.numerator * b_x
        return Fraction(a_num + b_num, new_denominator)

    def __sub__(self, other):
        """
        Returns new Fraction, that's the substraction of self and other.
        """
        self.__validate_type(other)
        new_denominator = lcm(self.denominator, other.denominator)
        a_x = new_denominator // self.denominator
        b_x = new_denominator // other.denominator
        a_num = self.numerator * a_x
        b_num = other.numerator * b_x
        return Fraction(a_num - b_num, new_denominator)

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        self.__validate_type(other)
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        if self.numerator == 0:
            return Fraction(self.numerator, self.denominator)
        self_gcd = gcd(self.numerator, self.denominator)
        return Fraction(
            self.numerator // self_gcd,
            self.denominator // self_gcd
        )

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        return (
            gcd(self.numerator, self.denominator) == 1
            or self.numerator == 0
        )

    def __validate_type(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"{other} is not of type Fraction")
