import math


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def is_prime(number):
    if number <= 1 or int(number) != number:
        print("The number isn't prime")
    else:
        if (2 ** number - 2) % number == 0:  # Theorem of Euler
            print("The number is prime")
        else:
            print("The number isn't prime")


def sqrt(x, n):
    return x ** (1/n)


def calc_surface_parallelogram(a, b, angle=90):
    return a * b * math.sin(angle * math.pi / 180) / 2


def calc_discriminate(a, b, c):
    discriminate = b ** 2 - 4 * a * c
    return discriminate


def get_roots(a, b, c):
    discriminate = calc_discriminate(a, b, c)
    if discriminate >= 0:
        x_1 = (-b + sqrt(discriminate, 2)) / 2 * a
        x_2 = (-b - sqrt(discriminate, 2)) / 2 * a
        if x_1 == int(x_1) and x_2 == int(x_2):
            return int(x_1), int(x_2)
        elif x_1 == int(x_1) and x_2 != int(x_2):
            return int(x_1), x_2
        elif x_1 != int(x_1) and x_2 == int(x_2):
            return x_1, int(x_2)
        else:
            return x_1, x_2
    else:
        return None, None