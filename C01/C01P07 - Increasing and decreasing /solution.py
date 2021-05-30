from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns):
    if len(ns) <= 1:
        return Monotonicity.NONE

    increasing = True
    decreasing = True
    for i in range(len(ns) - 1):
        a = ns[i]
        b = ns[i + 1]
        increasing = increasing and a < b
        decreasing = decreasing and a > b

    if increasing:
        return Monotonicity.INCREASING
    if decreasing:
        return Monotonicity.DECREASING
    return Monotonicity.NONE


print(increasing_or_decreasing([1, 2, 3]))
print(increasing_or_decreasing([1, 2, 3, 4, 5]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([5, 6, -10]) == Monotonicity.NONE)
print(increasing_or_decreasing([1, 1, 1, 1]) == Monotonicity.NONE)
print(increasing_or_decreasing([9, 8, 7, 6]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([]) == Monotonicity.NONE)
print(increasing_or_decreasing([1]) == Monotonicity.NONE)
print(increasing_or_decreasing([1, 100]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([1, 100, 100]) == Monotonicity.NONE)
print(increasing_or_decreasing([100, 1]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([100, 1, 1]) == Monotonicity.NONE)
print(increasing_or_decreasing([100, 1, 2]) == Monotonicity.NONE)
