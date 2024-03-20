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

    return [
        int(random.random() * end) + 1
        for _ in range(0, size)
    ]


def weighted_random_generator(samples, size, start=None, end=None, **kwargs):
    random_nums = random_generator(
        size=size,
        start=start,
        end=end,
        **kwargs,
    )

    results = {
        i: 0
        for i in INDEX_MAP
    }

    for random_num in random_nums:
        results[random_num] += 1

    for index, value in results.items():
        __import__('pdb').set_trace()
        pass


if __name__ == '__main__':
    weighted_random_generator(
        samples=[1, 2, 3],
        size=100,
        start=1,
        end=3,
    )
