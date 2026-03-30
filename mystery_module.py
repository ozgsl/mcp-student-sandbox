import math


def find_roots(a, b, c):
    """Return the real roots of the quadratic equation ax^2 + bx + c = 0."""
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None

    positive_root = (-b + math.sqrt(discriminant)) / (2 * a)
    negative_root = (-b - math.sqrt(discriminant)) / (2 * a)
    return positive_root, negative_root
