# coding: utf-8


import random


def random_generator(samples, size):
    return [random.randrange(1, size + 1) for _ in range(0, size)]
