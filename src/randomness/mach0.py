# coding: utf-8

import random


def weighted_random_generator(weights, size, start=None, end=None, **kwargs):  # noqa: E501
    '''Generate an array of weighted random numbers

    This is pure python, so it might be slower depending on the size attr.

    params:
        weights (list): Should be a list of weights.
        start (int): The start of the range to include.
        end (int): The end of the ranage to include.

    returns:
        (list): A list of random numbers based off the weights and matching
                the size attr.

    '''
    results = []

    start = start or 0
    end = end or size

    bean_counter = {
        i: 0
        for i in range(0, size)
    }

    while len(results) < size:
        rand_num = int(random.random() * end) + 1  # nosec

        if bean_counter[rand_num] < weights[rand_num - 1]:
            bean_counter[rand_num] += 1
            results.append(rand_num)

    return results
