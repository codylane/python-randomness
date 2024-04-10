# coding: utf-8

import random


INDEX_MAP = {
    1: 'A',
    2: 'B',
    3: 'C',
}


def random_generator(size, start=None, end=None, **kwargs):
    '''Generates a list of random numbers

    params:
        size (int)  - Required
                    - The number of total items the generator should perform
                      calculations.
        start (int) - Optional - The start of the range. Defaults to `1`
        end (int)   - Optional -The end of the range. Defaults to `size + 1`
        kwargs (dict): To be passed to random.randrange

    returns:
        (list) - Of random numbers

    '''
    start = start or 1
    end = end or (size + 1)

    results = [
        int(random.random() * end) + 1
        for _ in range(0, size)
    ]

    return results


def weighted_random_generator(weights, size, start=None, end=None, **kwargs):  # noqa: E501
    '''Generate an array of weighted random numbers

    This is pure python, so it might be slower depending on the size attr.

    params:
        weights (list): Should be a list of weights.
        start (int): The start of the range to include.
        end (int): The end of the ranage to include.
        **kwargs (dict): A dict of additional key value pairs that can be passed
                         to `random_generator`.

    returns:
        (list): A list of random numbers based off the weights and matching
                the size attr.

    '''
    results = []

    start = start or 0
    end = end or size

    bean_counter = {
        i: 0
        for i in INDEX_MAP
    }

    while len(results) < size:
        rand_num = int(random.random() * end) + 1

        if bean_counter[rand_num] < weights[rand_num - 1]:
            bean_counter[rand_num] += 1
            results.append(rand_num)

    return results
