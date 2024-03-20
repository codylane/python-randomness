# coding: utf-8


import random


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
    size += 1
    end = end or size

    return [
        random.randrange(start, end + 1, **kwargs)
        for _ in range(0, size - 1)
    ]
